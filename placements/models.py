from django.contrib.auth.models import Permission, User
from django.db import models


class Company(models.Model):
    user = models.ForeignKey(User, default=1)
    company_name = models.CharField(max_length=20)
    company_description = models.CharField(max_length=250)
    company_type = models.CharField(max_length=10)
    depts = models.CharField(max_length=250)
    date_of_visit = models.CharField(max_length=250)
    package = models.FloatField()
    cgpa = models.FloatField()
    contact_1 = models.BigIntegerField()
    contact_2 = models.BigIntegerField()
    email_id = models.EmailField()
    bond = models.FloatField()
    rating = models.FloatField()
    website = models.URLField()
    company_logo = models.FileField()

    def __str__(self):
        return self.company_name

    def as_json(self):
        return dict(
            company_id=self.id,
            package=self.package,
            cgpa=self.cgpa,
            bond=self.bond,
            contact_1=self.contact_1,
            contact_2=self.contact_2,
            date_of_visit=self.date_of_visit,
            depts=self.depts.upper(),
            company_description=self.company_description,
            company_type = self.company_type,
            company_name = self.company_name,
            email_id=self.email_id,
            company_logo=self.company_logo.url,
            rating=self.rating,
            website=self.website,
            dept = self.depts)

    def as_jsonUser(self):
        return dict(
            company_id=self.id,
            package=self.package,
            cgpa=self.cgpa,
            bond=self.bond,
            date_of_visit=self.date_of_visit,
            depts=self.depts.upper(),
            company_description=self.company_description,
            company_type = self.company_type,
            company_name = self.company_name,
            company_logo=self.company_logo.url,
            rating=self.rating,
            website=self.website,
            dept = self.depts)


