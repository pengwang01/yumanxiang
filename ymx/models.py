from django.db import models

# Create your models here.


class company(models.Model):
    company_name = models.CharField(max_length=500)
    company_description = models.CharField(max_length=5000, blank=True)
    company_primary_phone = models.CharField(max_length=100, blank=True)
    company_secondary_phone = models.CharField(max_length=100, blank=True)
    company_email = models.CharField(max_length=100, default='xxx@email.com', blank=True)
    company_address = models.CharField(max_length=500, blank=True)
    company_logo = models.FileField(blank=True)

    def __str__(self):
        return 'Company - ' + self.company_name