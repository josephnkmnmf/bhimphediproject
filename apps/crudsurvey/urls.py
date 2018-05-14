from django.conf.urls import url
from apps.crudsurvey.views import SurveCreate, SurveList, SurveDelete, SurveUpdate, SurveShow, search, auth_view, logout, loggedin, invalid_login
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^new/', SurveCreate.as_view(), name='Surve_create'),
    url(r'^list', SurveList.as_view(), name='Surve_list'),
    url(r'^delete/(?P<pk>\w+)/$', SurveDelete.as_view(), name='Surve_eliminate'),
    url(r'^edit/(?P<pk>\w+)/$', SurveUpdate.as_view(), name='Surve_edit'),
    url(r'^show/(?P<pk>\w+)/$', SurveShow.as_view(), name='Surve_show'),
    url(r'^search/$', search, name='Surve_search'),

    # user auth urls
    url(r'^login/$', login, {'template_name':'crudsurvey/login.html'}, name='Login'),
    url(r'^auth/$', auth_view),
    url(r'^logout/$', logout, name='User_logout'),
    url(r'^loggedin/$', loggedin),
    url(r'^invalid/$', invalid_login),

]
