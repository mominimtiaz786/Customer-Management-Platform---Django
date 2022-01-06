from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('products/',views.product,name='products'),
    path('customer/<int:id>/',views.customer,name='customer'),
    path('create_order/<int:id>',views.createOrder,name='create_order'),
    path('update_order/<int:id>/',views.updateOrder,name='update_order'),
    path('delete_order/<int:id>/',views.deleteOrder, name='delete_order'),
    path('login/',views.loginPage,name='login'),
    path('register/',views.registerPage, name='register'),
    path('logout/',views.logoutUser,name='logout'),
    path('user/',views.userPage,name='user-page'),
    path('account/',views.accountSettings,name='account-settings'),
]