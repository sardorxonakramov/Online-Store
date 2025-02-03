from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views


urlpatterns = [
    path('login/', views.UserLogin.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('registration/', views.UserRegistration.as_view(), name='registration'),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('cart-product-delete/<int:cart_product_id>/', views.CartProductDeleteView.as_view(), name='cart_product_delete'),
]
