from django.contrib.auth.models import User
from django.db import models


class Customer(models.Model):
    user = models.OneToOneField(User, null=True ,on_delete=models.CASCADE)
    cname = models.CharField(max_length=10)
    caddr = models.CharField(max_length=50)
    cemail = models.EmailField()
    cphone = models.CharField(max_length=12)

    def __str__(self):
        return self.cname

seller_choices = (
    ('Flipkart','Flipkart'),
    ('Amazon','Amazon'),
    ('Ebay','Ebay'),
    ('Ajio','Ajio')
)

class AllOrder(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    batch_no = models.IntegerField()
    qty = models.IntegerField()
    price = models.FloatField()
    seller = models.CharField(max_length=20, choices=seller_choices)

    def __str__(self):
        return self.name
