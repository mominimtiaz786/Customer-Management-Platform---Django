from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from .forms import OrderForm
# Create your views here.

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    
    total_orders = orders.count()
    orders_delievered = orders.filter(status="Delieverd").count()
    orders_pending = orders.filter(status="Pending").count()

    context = {'orders':orders.order_by('-date'),#[:5],
    'customers':customers,'total_orders':total_orders, 'orders_delievered':orders_delievered, 'orders_pending':orders_pending}
    return render(request,'accounts/dashboard.html', context)

def product(request):
    all_products = Product.objects.all()
    context = {'products':all_products}
    return render(request,'accounts/products.html',context)

def customer(request,id):
    customer = Customer.objects.get(id=id)
    customer_orders = customer.order_set.all()
    context = {'customer_orders':customer_orders, 'customer':customer, 'order_count':customer_orders.count()}
    return render(request,'accounts/customer.html', context)

def createOrder(request):
    form = OrderForm
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request,'accounts/order_form.html',context)

def updateOrder(request,id):
    order = Order.objects.get(id=id)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request,'accounts/order_form.html',context)

def deleteOrder(request, id):
    order = Order.objects.get(id=id)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        order.delete()
        return redirect('/')

    return render(request,'accounts/delete_order.html',{'order':order})