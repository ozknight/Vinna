from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Company(models.Model):
    user = models.ForeignKey(User)
    company_name = models.CharField(max_length=100)
    company_address = models.CharField(max_length=255)
    company_country = models.CharField(max_length=100)
    company_province = models.CharField(max_length=100)
    company_postal_code = models.SmallIntegerField(default=6000)
    company_email = models.EmailField()
    company_website = models.URLField(null=True, blank=True)
    company_contact_person = models.CharField(max_length=255)
    valid = models.BooleanField(default=False)
    def is_approved(self):
        return self.valid
    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
