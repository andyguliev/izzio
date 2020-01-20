from django.db import models
from django.urls import reverse


class People(models.Model):
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('people-detail', args=[str(self.id)])








class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog_detail', args=[str(self.id)])




class Maincategory(models.Model):
    name = models.CharField(max_length=200)
    category = models.ManyToManyField(Category)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('maincategory', args=[str(self.id)])





class Good(models.Model):
    name = models.CharField(max_length=200)
    decs = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="image")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('good_detail', args=[str(self.id)])




class Order(models.Model):
    name = models.CharField(max_length=200)
    good = models.ManyToManyField(Good)
    people = models.ForeignKey(People, on_delete=models.SET_NULL, null=True)
    
            

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('order-detail', args=[str(self.id)])
