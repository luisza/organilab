# encoding: utf-8
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404


from laboratory.models import Laboratory
from laboratory.forms import UserCreate, UserSearchForm

from django.views.generic import FormView
from laboratory.views.djgeneric import ListView

from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User, Group

from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import render

from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class BaseAccessListLab(FormView, ListView):
    model = User
    template_name = 'laboratory/access_list.html'
    form_class = UserSearchForm
    user_create_form = UserCreate
    paginate_by = 30
    role = 0
    group = None
    search_user = None

    def post(self, request, *args, **kwargs):
        self.lab = kwargs['lab_pk']
        return super(BaseAccessListLab, self).post(request, *args, **kwargs)

    def get_queryset(self):
        if not self.search_user:
            return self.get_relationfield().all().order_by('pk')
        return self.get_relationfield().filter(pk__in=self.search_user).order_by('pk')

    def get_context_data(self, **kwargs):
        context = super(BaseAccessListLab, self).get_context_data(
            **kwargs)
        context.update(FormView.get_context_data(self, **kwargs))
        context['role'] = self.role
        context['user_create_form'] = self.user_create_form()
        return context

    def add_user_to_relation(self, user, relation, group_name):
        admin_group = Group.objects.get(name=group_name)
        user.groups.add(admin_group)
        if not relation.filter(id=user.pk).exists():
            relation.add(user)

    def remove_user_to_relation(self, user, relation, group_name):
        admin_group = Group.objects.get(name=group_name)
        relation.remove(user)
        # Fixme: Si el usuario no está asociado a ningún otro laboratorio
        # con el rol, entonces se deben quitar los permisos

    def form_valid(self, form):
        if form.cleaned_data['action'] == 'add':
            users = User.objects.filter(pk__in=form.cleaned_data['user'])
            relation_field = self.get_relationfield()
            for user in users:
                self.add_user_to_relation(user, relation_field,
                                          self.group)
            messages.info(self.request, "User added successfully")
            return redirect(self.get_success_url())
        elif form.cleaned_data['action'] == 'createuser':
            user_create_form = UserCreate(self.request.POST)
            if user_create_form.is_valid():
                user = user_create_form.save()
                self.add_user_to_relation(user, self.get_relationfield(),
                                          self.group)
                messages.info(self.request, _("User added successfully"))
                return redirect(self.get_success_url())
            else:
                self.object_list = self.get_queryset()
                context = self.get_context_data()
                context['user_create_form'] = user_create_form
                return render(self.request, self.template_name,
                              context)
        elif form.cleaned_data['action'] == 'rmuser':
            users = User.objects.filter(
                pk__in=self.request.POST.getlist('user'))
            relation_field = self.get_relationfield()
            for user in users:
                self.remove_user_to_relation(user, relation_field, self.group)
            messages.info(self.request, _("Users removed successfully"))
            return redirect(self.get_success_url())
        else:
            self.search_user = form.cleaned_data['user']
            kwargs = {'lab_pk': self.lab}
            return self.get(self.request, **kwargs)

    def get_success_url(self):
        return reverse(self.success_url,
                       kwargs={'lab_pk': self.lab})

    def get_relationfield(self):
        pass


class AccessListLabAdminsView(BaseAccessListLab):
    role = '#tab_lab_admins'
    group = 'laboratory_admin'
    success_url = 'laboratory:access_list_lab_admins'

    def get_relationfield(self):
        laboratory = get_object_or_404(Laboratory, pk=self.lab)
        return laboratory.lab_admins


class AccessListLaboratoritsView(BaseAccessListLab):
    role = '#tab_laboratorits'
    group = 'laboratory_professor'
    success_url = 'laboratory:access_list_laboratorits'

    def get_relationfield(self):
        laboratory = get_object_or_404(Laboratory, pk=self.lab)
        return laboratory.laboratorists


class AccessListStudentsView(BaseAccessListLab):
    role = '#tab_students'
    group = 'laboratory_student'
    success_url = 'laboratory:access_list_students'

    def get_relationfield(self):
        laboratory = get_object_or_404(Laboratory, pk=self.lab)
        return laboratory.students
