from django.db import models
from django.urls import reverse


class People(models.Model):
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('people-detail', args=[str(self.id)])



class Maincategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('Maincategory', args=[str(self.id)])




class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category-detail', args=[str(self.id)])



class Good(models.Model):
    name = models.CharField(max_length=200)
    decs = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])




class Order(models.Model):
    name = models.CharField(max_length=200)
    good = models.ManyToManyField(Good)
    people = models.ForeignKey(People, on_delete=models.SET_NULL, null=True)
    
            

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('order-detail', args=[str(self.id)])
