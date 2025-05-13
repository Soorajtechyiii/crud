from django.db import models

class ProductDetails(models.Model):
    productname=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    quantity=models.IntegerField()
    price=models.FloatField()
    image=models.ImageField(upload_to='image/',null=True)


