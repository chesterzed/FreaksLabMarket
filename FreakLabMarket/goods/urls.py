from django.urls import path
from goods import views

app_name = 'goods'
urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('search/', views.product, name='search'),
    path('product/<slug:slug>', views.product, name='product'),
]