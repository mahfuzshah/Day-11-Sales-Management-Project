from django.shortcuts import render
from SalesManagement.models import *

def addSalePage(request):
    if request.method=="POST":
        product_name=request.POST.get('product_name')
        category_name=request.POST.get('category')
        unit_price=request.POST.get('unit_price')
        quantity=request.POST.get('quantity')
        discount_percent=request.POST.get('discount_percent')
        tax_percent=request.POST.get('tax_percent')

        product=SaleModel(
            product_name=product_name,
            category=category_name,
            unit_price=unit_price,
            quantity=quantity,
            discount_percent=discount_percent,
            tax_percent=tax_percent,
        )
        product.save()

    sales=SaleModel.objects.all()
    context={
        'sales':sales
    }
    return render(request, 'add_sale.html', context)



def SaleList(request):

    sales=SaleModel.objects.all()
    for sale in sales:
        base_price = sale.unit_price * sale.quantity
        discount = base_price * (sale.discount_percent / 100)
        tax = base_price * (sale.tax_percent / 100)
        sale.total = base_price - discount + tax 

    context={
        'sales':sales
    }
    return render(request, 'sale_list.html', context)
