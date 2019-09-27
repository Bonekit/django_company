from django.db import models
from django.utils import timezone
from django.urls import reverse


class Company(models.Model):
    id = models.BigAutoField(verbose_name='ID', primary_key=True)
    brand = models.CharField(verbose_name='Brand', unique=True, max_length=200)
    city = models.CharField(verbose_name='City', max_length=200)
    street = models.CharField(verbose_name='Street', max_length=200)
    account_number = models.CharField(verbose_name='Account Number', max_length=200, unique=True)
    image_logo = models.ImageField(upload_to='companies', blank=True)
    created_at = models.DateTimeField(verbose_name='Created At', editable=False)
    updated_at = models.DateTimeField(verbose_name='Updated At', editable=False)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def get_absolute_url(self):
        return reverse('company:company-detail', kwargs={'pk': self.id})

    def save(self, *args, **kwargs):
        """ On Save, update timestamps """
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(Company, self).save(*args, **kwargs)

    def __str__(self):
        return self.brand
