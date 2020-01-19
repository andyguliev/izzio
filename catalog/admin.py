from django.contrib import admin
from django.contrib import admin
from .models import Maincategory, Category, Good, People, Order

admin.site.register(Good)
admin.site.register(Category)
admin.site.register(Maincategory)
admin.site.register(Order)
admin.site.register(People)




