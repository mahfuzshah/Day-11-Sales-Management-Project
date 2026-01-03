
from django.contrib import admin
from django.urls import path
from SalesManagement.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', addSalePage, name='sale'),
    path('sale_list', SaleList, name='sale_list'),
]