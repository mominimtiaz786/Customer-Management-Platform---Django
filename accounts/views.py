from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    
    total_orders = orders.count()
    orders_delievered = orders.filter(status="Delieverd").count()
    orders_pending = orders.filter(status="Pending").count()

    context = {'orders':orders[:5],'customers':customers,'total_orders':total_orders, 'orders_delievered':orders_delievered, 'orders_pending':orders_pending}
    return render(request,'accounts/dashboard.html', context)

def product(request):
    all_products = Product.objects.all()
    context = {'products':all_products}
    return render(request,'accounts/products.html',context)

def customer(request):
    return render(request,'accounts/customer.html')