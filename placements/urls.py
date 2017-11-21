from django.conf.urls import url
from . import views

app_name = 'placements'

urlpatterns = [
    url(r'^addCompany/$', views.addCompany, name='addCompany'),
    url(r'^companyDetail/$', views.companyDetail, name='companyDetail'),
    url(r'^addCompanyDetails/$', views.addCompanyDetails, name='addCompanyDetails'),
    url(r'^getCompanies/$', views.getCompanies, name='getCompanies'),
]