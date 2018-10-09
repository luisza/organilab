from django.core.management.base import BaseCommand 
from django.contrib.auth.models import User , Group
from laboratory.models import OrganizationStructure, PrincipalTechnician, Laboratory
from constance import config
import random

"""
                    -------------------------
                    |          root         |         * = GROUP_STUDENT
                    -------------------------
                    /             |         \
                  dep1           dep2       dep3       GROUP_ADMIN
               /   \    \      /    \        |  \
            sch1     sch2  sch3    sch4   sch5   sch6  GROUP_LABORATORIST  
            /  \      |     |     / |       |      |
          lab1 lab2  lab3  lab4  /isch1    lab8   lab9        
                               lab5 / \ 
                                 lab6 lab7
"""

class Command(BaseCommand):
    
    def create_organization(self):
        """         -------------------------
                    |          root         |     * = GROUP_STUDENT
                    -------------------------
                    /             |         \
                  dep1           dep2       dep3  GROUP_ADMIN
               /   \    \      /    \        | 
            sch1  sch2  sch3  sch4*  sch5   sch6  GROUP_LABORATORIST
                               |
                              isch1               GROUP_ADMIN
        """
        
        self.root = OrganizationStructure.objects.create(
            name = "the university",
            group = Group.objects.get(pk=config.GROUP_ADMIN_PK)
        )
        self.dep1 = OrganizationStructure.objects.create(
            name = "departament 1",
            group = Group.objects.get(pk=config.GROUP_ADMIN_PK),
            parent = self.root
        )
        self.dep2 = OrganizationStructure.objects.create(
            name = "departament 2",
            group = Group.objects.get(pk=config.GROUP_ADMIN_PK),
            parent = self.root
        )

        self.dep3 = OrganizationStructure.objects.create(
            name = "departament 2",
            group = Group.objects.get(pk=config.GROUP_ADMIN_PK),
            parent = self.root
        )

        self.school1 = OrganizationStructure.objects.create(
            name = "School 1",
            group = Group.objects.get(pk=config.GROUP_LABORATORIST_PK),
            parent = self.dep1
        )
        self.school2 = OrganizationStructure.objects.create(
            name = "School 2",
            group = Group.objects.get(pk=config.GROUP_LABORATORIST_PK),
            parent = self.dep1
        )

        self.school3 = OrganizationStructure.objects.create(
            name = "School 3",
            group = Group.objects.get(pk=config.GROUP_LABORATORIST_PK),
            parent = self.dep1
        )
        self.school4 = OrganizationStructure.objects.create(
            name = "School 4",
            group = Group.objects.get(pk=config.GROUP_STUDENT_PK),
            parent = self.dep2
        )
        self.school5 = OrganizationStructure.objects.create(
            name = "School 5",
            group = Group.objects.get(pk=config.GROUP_LABORATORIST_PK),
            parent = self.dep2
        )
        self.school6 = OrganizationStructure.objects.create(
            name = "School 6",
            group = Group.objects.get(pk=config.GROUP_LABORATORIST_PK),
            parent = self.dep3
        )
        self.interschool = OrganizationStructure.objects.create(
            name = "Inter School 1",
            group = Group.objects.get(pk=config.GROUP_ADMIN_PK),
            parent = self.school4
        )
        
    def create_users(self):
        """
             uroot
             usch1_2_6
             usch4
             usch3_5
             uschi1
             usch6_i1
             udep1_2
             udep_3
        """

        self.uroot = User.objects.create_user("uroot", 
                                               "supervisor@organillab.org", 
                                               "admin12345")
        self.usch1_2_6 = User.objects.create_user("usch1_2_6", 
                                               "supervisor@organillab.org", 
                                               "admin12345")
        self.usch4 = User.objects.create_user("usch4", 
                                               "supervisor@organillab.org", 
                                               "admin12345")
        self.usch3_5 = User.objects.create_user("usch3_5", 
                                               "supervisor@organillab.org", 
                                               "admin12345")
        self.uschi1 = User.objects.create_user("uschi1", 
                                               "supervisor@organillab.org", 
                                               "admin12345")
        self.usch6_i1 = User.objects.create_user("usch6_i1", 
                                               "supervisor@organillab.org", 
                                               "admin12345")
        self.udep1_2 = User.objects.create_user("udep1_2", 
                                               "supervisor@organillab.org", 
                                               "admin12345")
        self.udep_3 = User.objects.create_user("udep_3", 
                                               "supervisor@organillab.org", 
                                               "admin12345")    
        
        self.lab_1 = User.objects.create_user("lab_1", 
                                               "supervisor@organillab.org", 
                                               "admin12345")          
        self.lab_2 = User.objects.create_user("lab_2", 
                                               "supervisor@organillab.org", 
                                               "admin12345")    
        self.lab_3 = User.objects.create_user("lab_3", 
                                               "supervisor@organillab.org", 
                                               "admin12345")    
        

        self.est_1 = User.objects.create_user("est_1", 
                                               "supervisor@organillab.org", 
                                               "admin12345")
        self.est_2 = User.objects.create_user("est_2", 
                                               "supervisor@organillab.org", 
                                               "admin12345")   
        self.est_3 = User.objects.create_user("est_3", 
                                               "supervisor@organillab.org", 
                                               "admin12345")   
        self.est_4 = User.objects.create_user("est_4", 
                                               "supervisor@organillab.org", 
                                               "admin12345")   

        gpa=Group.objects.get(pk=config.GROUP_ADMIN_PK)
        gpl = Group.objects.get(pk=config.GROUP_LABORATORIST_PK)
        gpe = Group.objects.get(pk=config.GROUP_STUDENT_PK)        
        
        
        self.uroot.groups.add(gpa)
        self.usch1_2_6.groups.add(gpl)
        self.usch4.groups.add(gpe)
        self.usch3_5.groups.add(gpl)
        self.uschi1.groups.add(gpa)
        self.usch6_i1.groups.add(gpl)
        self.udep1_2.groups.add(gpa)
        self.udep_3.groups.add(gpa)
        
        self.lab_1.groups.add(gpl)
        self.lab_2.groups.add(gpl)
        self.lab_3.groups.add(gpl)
        
        self.est_1.groups.add(gpe)
        self.est_2.groups.add(gpe)
        self.est_3.groups.add(gpe)
        self.est_4.groups.add(gpe)
        
    def create_principal_technicians(self):
        """
            uroot
            usch1_2_6
            usch4
            usch3_5
            uschi1
            usch6_i1
            udep1_2
            udep_3
        """
        pturoot=PrincipalTechnician.objects.create(
            name = "Ema Lopez",
            phone_number = "88-0000-0000",
            id_card = "8-1203-7890",
            email = "uroot@organilab.org",
            organization = self.root
            #assigned  FK a laboratory            

            )
        pturoot.credentials.add(self.uroot)
        
        for i, org, lab in [
               (1, self.school1, self.lab1),
               (2, self.school1, self.lab2),
               (3, self.school2, self.lab3),
               (4, self.school6, self.lab9)]:
            ptusch1_2_6=PrincipalTechnician.objects.create(
                name = "Juan perez "+str(i),
                phone_number = "88-0000-"+str(random.randint(1000, 9999)),
                id_card = "8-%d-7890"%(random.randint(1000, 9999)),
                email = "usch1_2_6@organilab.org",
                organization = org,
                assigned=lab           
            )
            ptusch1_2_6.credentials.add(self.usch1_2_6)        
        
        usch4=PrincipalTechnician.objects.create(
            name = "Jorge Madrigal",
            phone_number = "88-0000-"+str(random.randint(1000, 9999)),
            id_card = "8-%d-7890"%(random.randint(1000, 9999)),
            email = "usch4@organilab.org",
            organization = self.root,
            assigned=self.lab5            

            )
        usch4.credentials.add(self.usch4)

        for i, org, lab in [ (1, self.school3, self.lab4),
                             (2, self.school5, self.lab8) ]:
            usch3_5=PrincipalTechnician.objects.create(
                name = "Lola Cardenas "+str(i),
                phone_number = "88-0000-"+str(random.randint(1000, 9999)),
                id_card = "8-%d-7890"%(random.randint(1000, 9999)),
                email = "usch3_5@organilab.org",
                organization = org,
                assigned=lab,           
            )
            usch3_5.credentials.add(self.usch3_5)    

        uschi1=PrincipalTechnician.objects.create(
            name = "Marco atencio",
            phone_number = "88-0000-"+str(random.randint(1000, 9999)),
            id_card = "8-%d-7890"%(random.randint(1000, 9999)),
            email = "uschi1@organilab.org",
            organization = self.interschool,
            assigned = self.lab6

            )
        uschi1.credentials.add(self.uschi1)
        
        uschi1=PrincipalTechnician.objects.create(
            name = "Juan Carmona",
            phone_number = "88-0000-"+str(random.randint(1000, 9999)),
            id_card = "8-%d-7890"%(random.randint(1000, 9999)),
            email = "uschi1@organilab.org",
            organization = self.interschool,
            assigned=self.lab7           

            )
        uschi1.credentials.add(self.uschi1)
        
        
        for i, org, lab in [(1, self.school6, self.lab9), 
                            (2, self.interschool, self.lab6),
                            (3, self.interschool, self.lab7)
                            ]:
            usch6_i1=PrincipalTechnician.objects.create(
                name = "Keylor Vargas "+str(i),
                phone_number = "88-0000-"+str(random.randint(1000, 9999)),
                id_card = "8-%d-7890"%(random.randint(1000, 9999)),
                email = "usch6_i1@organilab.org",
                organization = org,
                assigned=lab           
            )
            usch6_i1.credentials.add(self.usch6_i1)  
            
        for i, org in enumerate([self.dep1, self.dep2 ]):
            udep1_2=PrincipalTechnician.objects.create(
                name = "Julio Volio "+str(i),
                phone_number = "88-0000-"+str(random.randint(1000, 9999)),
                id_card = "8-%d-7890"%(random.randint(1000, 9999)),
                email = "udep1_2@organilab.org",
                organization = org
                #assigned  FK a laboratory            
            )
            udep1_2.credentials.add(self.udep1_2)
            
        udep_3=PrincipalTechnician.objects.create(
            name = "Julia Obando",
            phone_number = "88-0120-0940",
            id_card = "8-4513-7890",
            email = "udep_3@organilab.org",
            organization = self.dep3
            #assigned  FK a laboratory            

            )
        udep_3.credentials.add(self.udep_3)


    def create_labs(self):
        """
            sch1     sch2  sch3    sch4   sch5   sch6   
            /  \      |     |     / |       |      |
          lab1 lab2  lab3  lab4  /isch1    lab8   lab9        
                               lab5 / \ 
                                 lab6 lab7
        """
        
        
        self.lab1 = Laboratory.objects.create(
                    name = "Laboratory 1",
                    phone_number = "88-0001-7890",
                    location = "N/D",
                    geolocation = '9.895804362670006,-84.1552734375',
                    organization = self.school1
                    )
        self.lab2 = Laboratory.objects.create(
                    name = "Laboratory 2",
                    phone_number = "88-0001-7890",
                    location = "N/D",
                    geolocation = '9.895804362670006,-84.1552734375',
                    organization = self.school1
                    )
        self.lab3 = Laboratory.objects.create(
                    name = "Laboratory 3",
                    phone_number = "88-0001-7890",
                    location = "N/D",
                    geolocation = '9.895804362670006,-84.1552734375',
                    organization = self.school2
                    )
        self.lab4 = Laboratory.objects.create(
                    name = "Laboratory 4",
                    phone_number = "88-0001-7890",
                    location = "N/D",
                    geolocation = '9.895804362670006,-84.1552734375',
                    organization = self.school3
                    )
        self.lab5 = Laboratory.objects.create(
                    name = "Laboratory 5",
                    phone_number = "88-0001-7890",
                    location = "N/D",
                    geolocation = '9.895804362670006,-84.1552734375',
                    organization = self.school4
                    )
        self.lab6 = Laboratory.objects.create(
                    name = "Laboratory 6",
                    phone_number = "88-0001-7890",
                    location = "N/D",
                    geolocation = '9.895804362670006,-84.1552734375',
                    organization = self.interschool
                    )
        self.lab7 = Laboratory.objects.create(
                    name = "Laboratory 7",
                    phone_number = "88-0001-7890",
                    location = "N/D",
                    geolocation = '9.895804362670006,-84.1552734375',
                    organization = self.interschool
                    )
        self.lab8 = Laboratory.objects.create(
                    name = "Laboratory 8",
                    phone_number = "88-0001-7890",
                    location = "N/D",
                    geolocation = '9.895804362670006,-84.1552734375',
                    organization = self.school5
                    )
        self.lab9 = Laboratory.objects.create(
                    name = "Laboratory 9",
                    phone_number = "88-0001-7890",
                    location = "N/D",
                    geolocation = '9.895804362670006,-84.1552734375',
                    organization = self.school6
                    )
        
        
        self.lab1.laboratorists.add(self.lab_1)
        self.lab2.laboratorists.add(self.lab_2)
        self.lab2.laboratorists.add(self.lab_3)
        self.lab3.laboratorists.add(self.lab_3)
        self.lab4.laboratorists.add(self.lab_2)
        self.lab5.laboratorists.add(self.lab_1)
        self.lab6.laboratorists.add(self.lab_1)
        self.lab7.laboratorists.add(self.lab_2)
        self.lab8.laboratorists.add(self.lab_3)
        self.lab9.laboratorists.add(self.lab_1)

        self.lab1.students.add(self.est_1)
        self.lab2.students.add(self.est_2)
        self.lab3.students.add(self.est_3)
        self.lab4.students.add(self.est_4)
        self.lab5.students.add(self.est_1)
        self.lab6.students.add(self.est_2)
        self.lab7.students.add(self.est_3)
        self.lab8.students.add(self.est_4)
        self.lab9.students.add(self.est_1)
        
        self.lab1.students.add(self.est_2)
        self.lab2.students.add(self.est_3)
        self.lab3.students.add(self.est_4)
        self.lab4.students.add(self.est_1)
        self.lab5.students.add(self.est_2)
        self.lab6.students.add(self.est_3)
        self.lab7.students.add(self.est_4)
        self.lab8.students.add(self.est_1)
        self.lab9.students.add(self.est_2)
        self.lab1.students.add(self.est_3)
        self.lab2.students.add(self.est_4)
        self.lab3.students.add(self.est_3)
        self.lab4.students.add(self.est_2)

    def handle(self, *args, **options):
        self.create_organization()
        self.create_users()
        self.create_labs()
        self.create_principal_technicians()
        
