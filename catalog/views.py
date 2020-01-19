from django.shortcuts import render
from .models import Good, Maincategory, Category, People, Order
from django.views.generic import ListView, DetailView


#~~~~~~~~~~~~~~~~~  КАТАЛОГ  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Catalog(ListView):
    model = Good
    template_name = "base_catalog.html"

    @staticmethod
    def all_goods():
        return Good.objects.all()

    @staticmethod
    def all_maincat():
        return Maincategory.objects.all()


    @staticmethod
    def all_category():
        return Category.objects.all()



#~~~~~~~~~~~~~~~~~  SUB КАТАЛОГ  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



class CatalogDetail(DetailView):
    model = Category
    template_name = "base_catalog_detail.html"

    @staticmethod
    def all_goods():
        return Good.objects.all()

    @staticmethod
    def all_maincat():
        return Maincategory.objects.all()


    @staticmethod
    def all_category():
        return Category.objects.all()



#~~~~~~~~~~~~~~~~~  КАРТОЧКА ТОВАРА  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



class GoodDetail(DetailView):
    model = Good
    template_name = "base_detail.html"

    @staticmethod
    def all_goods():
        return Good.objects.all()

    @staticmethod
    def all_maincat():
        return Maincategory.objects.all()


    @staticmethod
    def all_category():
        return Category.objects.all()
























class GoodListView(ListView):
    model = Good
    template_name = "good_list.html"

class GoodDetailView(DetailView):
    model = Good
    template_name = "good_detail.html"

  
    @staticmethod
    def all_orders():
        return Order.objects.all()

    @staticmethod
    def all_peoples():
        return People.objects.all()





class CatListView(ListView):
    model = Category
    template_name = "cat_list.html"


    @staticmethod
    def all_goods():
        return Good.objects.all()

    @staticmethod
    def all_orders():
        return Order.objects.all()

    @staticmethod
    def all_peoples():
        return People.objects.all()





class CatDetailView(DetailView):
    model = Category
    template_name = "cat_detail.html"
    

    @staticmethod
    def all_goods():
        return Good.objects.all()

    @staticmethod
    def all_orders():
        return Order.objects.all()

    @staticmethod
    def all_peoples():
        return People.objects.all()




class OrderListView(ListView):
    model = Order
    template_name = "order_list.html"


    @staticmethod
    def all_goods():
        return Good.objects.all()

    @staticmethod
    def all_orders():
        return Order.objects.all()

    @staticmethod
    def all_peoples():
        return People.objects.all()





class OrderDetailView(DetailView):
    model = Order
    template_name = "order_detail.html"
    

    # @staticmethod
    # def all_goods():
    #     return Good.objects.all()

    @staticmethod
    def all_goods():
        return Good.objects.all()

    @staticmethod
    def all_orders():
        return Order.objects.all()

    @staticmethod
    def all_peoples():
        return People.objects.all()

    






# class CatsListView(ListView):
#     model = Category
#     template_name = "shop.html"

#     def get_context_data(self, **kwargs):
#         context = super(CatsListView, self).get_context_data(**kwargs)
#         context['goods'] = Good.objects.all()
#         return context


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



class CListView(ListView):
    model = Good
    template_name = "catalog/c_list.html"

class GDetailView(DetailView):
    model = Good
    template_name = "catalog/detail.html"


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class IndexView(ListView):
    model = Good
    template_name = "catalog/index.html"