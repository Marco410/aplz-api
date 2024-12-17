from django.db import models

# Create your models here.

class Order(models.Model):
    """
    Order model
    """
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()
    DeletedAt = models.DateTimeField(blank=True, null=True)
    date = models.TextField()
    status = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    loanId = models.IntegerField(blank=True, null=True)
    merchantId = models.IntegerField(blank=True, null=True)
    products = models.CharField(max_length=255, blank=True, null=True)
    branchId = models.IntegerField(blank=True, null=True)
    sellsAgentId = models.IntegerField(blank=True, null=True)
