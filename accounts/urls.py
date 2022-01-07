from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

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

    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='accounts/reset_password.html'),name="password_reset"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='accounts/reset_password_sent.html'),name="password_reset_done"),
    path('reset_password/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='accounts/reset_password_confirm'),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='accounts/reset_password_complete'),name="password_reset_complete"),
]