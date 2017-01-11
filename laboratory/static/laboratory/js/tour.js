/**
 * Created by jaquer on 09/01/17.
 */
console.log('tour');
var tour = new Tour({
    steps: [
        {
            element: "#brand_id",
            title: "Hello!",
            content: "Welcome to Organilab, the simple laboratory organizer. Let's take a look of the main features of this system",
            placement: 'bottom'
        },
        {
            element: '#index_labview_id',
            title: 'Laboratory',
            content: "The laboratory view is Organilab's main feature because it offers a general view of the structure of the laboratory for its management",
            placement: "bottom"
        },
        {
            element: '#index_manage_id',
            title: 'Management',
            content: "In the management views you can find everything you need to control the components of the laboratory, from rooms to objects.",
            placement: "bottom"
        },
        {
            element: '#index_report_id',
            title: 'Reports',
            content: "If you need a full inventory of the whole laboratory or an specific component, this is the place to do it",
            placement: "bottom"
        },
        {
            element: '#select_id',
            title: 'Select laboratory',
            content: 'You can have access to multiple laboratories, select the one you want to manage by clicking this link',
            placement: 'bottom'
        },
        {
            element: '#labview_id',
            title: 'Laboratory view',
            content: 'In this view you can manage most of the components related to the lab, including its rooms, furniture and objects',
            placement: 'bottom'
        },
        {
            element: '#management_id',
            title: 'Management views',
            content: 'This views manage the different objects handled by the Organilab system for the current laboratory',
            placement: 'bottom'
        },
        {
            element: '#reports_id',
            title: 'Reports',
            content: 'Here you can see and retrieve the reports generated by the different components handled and saved in the Organilab system',
            placement: 'bottom'
        },
        {
            element: '#reservation_list_id',
            title: 'My reservations',
            content: 'In this view you can check out all the reservations related to you and their current status.',
            placement: 'bottom'
        },
        {
            element: '#reservation_admin_id',
            title: 'Reservation administration',
            content: 'Here you create and finish a given reservation registered in the Organilab system',
            placement: 'bottom'
        },
        {
            element: '#feedback_id',
            title: 'Help us!',
            content: "If you have an issue testing or using Organilab, let us know. We'll be eager to help you",
            placement: 'bottom'
        }
    ]
});

tour.init(true);