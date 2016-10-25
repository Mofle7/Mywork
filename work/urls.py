from work import views
from django.conf.urls import url
urlspatterns = [
    url(r"^$",views.main ,name='main'),
    url(r"^support/$",views.support ,name='support'),
    url(r"^about/$", views.about_us, name='about_us'),
    url(r"^(?P<pk_id>\d+)/$",views.show_adv, name='show_adv'),
    url(r"^(?P<pk_id>\d+)/adv/add/$", views.add_adv, name='add_adv'),
    url(r"^(?P<pk_id>\d+)/adv/edit/$", views.edit_adv, name='edit_add'),
    url(r"^(?P<pk_id>\d+)/adv/del/$",views.del_adv, name='del_adv'),
    url(r"^(?P<pk_id>\d+)/$", views.show_profile, name='show_profile'),
    url(r"^(?P<pk_id>\d+)/profile/add/$", views.add_profile, name='add_profile'),
    url(r"^(?P<pk_id>\d+)/profile/edit/$", views.edit_profile, name='edit_profile'),
    url(r"^(?P<pk_id>\d+)/profile/del/$", views.del_profile, name='del_profile'),
    url(r"^search/$", views.search_page, name='search_page'),
    url(r"^forget_password/$", views.forget_password, name='forget_password'),

]