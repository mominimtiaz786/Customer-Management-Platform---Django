from django.forms.models import inlineformset_factory
from django.shortcuts import redirect, render
from .models import *
from .forms import OrderForm, CreateUserForm, CustomerForm
from .filters import OrderFilter
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, admin_only, allowed_users


# Create your views here.

@login_required(login_url='login')
@admin_only
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    
    total_orders = orders.count()
    orders_delievered = orders.filter(status="Delieverd").count()
    orders_pending = orders.filter(status="Pending").count()

    context = {'orders':orders.order_by('-id')[:5],
    'customers':customers,'total_orders':total_orders, 'orders_delievered':orders_delievered, 'orders_pending':orders_pending}
    return render(request,'accounts/dashboard.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def product(request):
    all_products = Product.objects.all()
    context = {'products':all_products}
    return render(request,'accounts/products.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customer(request,id):
    customer = Customer.objects.get(id=id)
    customer_orders = customer.order_set.all()

    order_filter = OrderFilter(request.GET, queryset= customer_orders)
    customer_orders = order_filter.qs

    context = {'customer_orders':customer_orders, 'order_filter':order_filter,'customer':customer, 'order_count':customer_orders.count()}
    return render(request,'accounts/customer.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createOrder(request, id):
    customer = Customer.objects.get(id=id)
    #form = OrderForm(initial={'customer':customer})
    OrderFormSet = inlineformset_factory(Customer,Order, fields=('product','status'), extra=5)
    formset = OrderFormSet(queryset = Order.objects.none(),instance=customer)

    if request.method == 'POST':
        formset = OrderFormSet(request.POST,instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context = {'formset':formset}
    return render(request,'accounts/order_form.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
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

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteOrder(request, id):
    order = Order.objects.get(id=id)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        order.delete()
        return redirect('/')

    return render(request,'accounts/delete_order.html',{'order':order})

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='customer')
            user.groups.add(group)

            username = form.cleaned_data.get('username')
            customer = Customer.objects.create(user=user,email = user.email)
            customer.save()
            messages.success(request,"Account was created successfully for "+ username)
            return redirect('login')

    context = {'form':form}
    return render(request, 'accounts/register.html',context)

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'incorrect username or password')

    context = {}
    return render(request, 'accounts/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userPage(request):
    orders = request.user.customer.order_set.all()
    
    total_orders = orders.count()
    orders_delievered = orders.filter(status="Delieverd").count()
    orders_pending = orders.filter(status="Pending").count()

    context = {'orders':orders.order_by('-id'),
    'total_orders':total_orders, 'orders_delievered':orders_delievered, 'orders_pending':orders_pending}

    return render(request,'accounts/user_page.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def accountSettings(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)
    
    if request.method == "POST":
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('user-page')

    context = {'form':form,}
    return render(request,'accounts/account_settings.html',context)