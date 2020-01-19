from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),


    url(r'^catalog/$', views.Catalog.as_view(), name='catalog'),
    url(r'^catalog/(?P<pk>\d+)$', views.CatalogDetail.as_view(), name='catalog_detail'),

    url(r'^goods/(?P<pk>\d+)$', views.GoodDetail.as_view(), name='good_detail'),



    # url(r'^goods/$', views.GoodListView.as_view(), name='goods'),
    # url(r'^goods/(?P<pk>\d+)$', views.GoodDetailView.as_view(), name='good-detail'),

    # url(r'^category/$', views.CatListView.as_view(), name='category'),
    # url(r'^category/(?P<pk>\d+)$', views.CatDetailView.as_view(), name='category-detail'),

    # url(r'^order/$', views.OrderListView.as_view(), name='order'),
    # url(r'^order/(?P<pk>\d+)$', views.OrderDetailView.as_view(), name='order-detail'),

    # url(r'^cat/$', views.CListView.as_view(), name='cat'),
    # url(r'^cat/(?P<pk>\d+)$', views.GDetailView.as_view(), name='detail'),

    # url(r'^cat/$', views.CatsListView.as_view(), name='categorys'),
]

