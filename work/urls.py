from work import views
from django.conf.urls import url
urlpatterns = [
    url(r"^$",views.main ,name='main'),
    url(r"^support/$",views.support ,name='support'),
    url(r"^about/$", views.about_us, name='about_us'),
    url(r"^adv/(?P<pk>\d+)/$",views.show_adv, name='show_adv'),
    url(r"^adv/(?P<pk>\d+)/add/$", views.add_adv, name='add_adv'),
    url(r"^adv(?P<pk>\d+)/edit/$", views.edit_adv, name='edit_adv'),
    url(r"^adv(?P<pk>\d+)/del/$",views.del_adv, name='del_adv'),
    url(r"^(?P<pk>\d+)/$", views.show_profile, name='show_profile'),
    url(r"^profile(?P<pk>\d+)/add/$", views.add_profile, name='add_profile'),
    url(r"^profile(?P<pk>\d+)/edit/$", views.edit_profile, name='edit_profile'),
    url(r"^profile(?P<pk>\d+)/del/$", views.del_profile, name='del_profile'),
    url(r"^search/$", views.search_page, name='search_page'),
    url(r"^forget_password/$", views.forget_password, name='forget_password'),

]
