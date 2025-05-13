from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name='укажите название тега',null=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='Укажите продукт', null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.product_name