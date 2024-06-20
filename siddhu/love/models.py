from django.db import models

class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=20)
    alternate_no = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255)
    company_name = models.CharField(max_length=100)
    model_no = models.CharField(max_length=50)
    physical_condition = models.CharField(max_length=100)
    estimated_price = models.DecimalField(max_digits=10, decimal_places=2)
    imei_1 = models.CharField(max_length=100)
    imei_2 = models.CharField(max_length=100, unique=True)
    date = models.DateField()


    def __str__(self):
        return self.customer_name 