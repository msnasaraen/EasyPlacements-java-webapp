from rest_framework import serializers
from .models import Company

class CarSerializer(serializers.ModelSerializer):

    company_logo = serializers.SerializerMethodField()

    class Meta:
        model = Company
        #fields = ('company_name', 'company_description', 'company_type', 'depts','date_of_visit','package','cgpa','contact_1','contact_2','email_id','bond','rating','website','company_logo')
        fields = '__all__'

    def get_company_logo(self, Company):
        request = self.context.get('request')
        photo_url = Company.company_logo.url
        return request.build_absolute_uri(photo_url)
