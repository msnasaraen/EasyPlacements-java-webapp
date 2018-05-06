from django.conf.urls import url
from . import views

app_name = 'placements'

urlpatterns = [
    url(r'^addCompany/$', views.addCompany, name='addCompany'),
    url(r'^companyDetail/$', views.companyDetail, name='companyDetail'),
    url(r'^usercompanyDetail/$', views.usercompanyDetail, name='usercompanyDetail'),
    url(r'^addCompanyDetails/$', views.addCompanyDetails, name='addCompanyDetails'),
    url(r'^getCompanies/$', views.getCompanies, name='getCompanies'),
    url(r'^getCompaniesUser/$', views.getCompaniesUser, name='getCompaniesUser'),
    url(r'^getElligibleCompaniesUser/$', views.getElligibleCompaniesUser, name='getElligibleCompaniesUser'),
    url(r'^approveUsers/$', views.approveUsers, name='approveUsers'),
    url(r'^approveAdmin/$', views.approveAdmin, name='approveAdmin'),
    url(r'^getUsersForApproval/$', views.getUsersForApproval, name='getUsersForApproval'),
    url(r'^getAdminForApproval/$', views.getAdminForApproval, name='getUsersForApproval'),
    url(r'^approvethisadmin/$', views.approvethisadmin, name='approvethisadmin'),
    url(r'^viewCompany/(?P<value>[0-9]+)/$', views.viewCompany, name='viewCompany'),
    url(r'^viewCompanyUser/(?P<value>[0-9]+)/$', views.viewCompanyUser, name='viewCompanyUser'),
    url(r'^updateCompany/(?P<value>[0-9]+)/$', views.updateCompany, name='updateCompany'),
    url(r'^deleteCompany/(?P<value>[0-9]+)/$', views.deleteCompany, name='deleteCompany'),
    url(r'^filterUser/$', views.filterUser, name='filterUser'),
    url(r'^filterAdmin/$', views.filterAdmin, name='filterAdmin'),

]