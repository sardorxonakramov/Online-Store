from django.db.models.query import QuerySet
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, ListView, DeleteView
from django.contrib.auth import get_user_model


from .forms import UserRegistrationForm
from app_main.models import Cart


User = get_user_model()


class UserLogin(LoginView):
    template_name = 'login.html'
    extra_context = {
        'footer_fixed': True,
    }

    def get_success_url(self):
        return self.request.POST.get('next')
    
    def dispatch(self, request, *args, **kwargs):
        if request.method == 'GET' and request.user.is_authenticated:
            return redirect('home')
        
        return super().dispatch(request, *args, **kwargs)
    

class UserRegistration(CreateView):
    template_name = 'registration.html'
    model = User
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')
    extra_context = {
        'footer_fixed': True,
    }

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'GET' and request.user.is_authenticated:
            return redirect('home')
        
        return super().dispatch(request, *args, **kwargs)


def user_logout(request):
    logout(request)
    return redirect('home')


class CartView(ListView):
    template_name = 'cart.html'
    context_object_name = 'cart_products'
    extra_context = {
        'footer_fixed': True
    }
    
    def get_queryset(self):
        return self.request.user.cart_set.all()


class CartProductDeleteView(DeleteView):
    model = Cart
    success_url = reverse_lazy('cart')
    pk_url_kwarg = 'cart_product_id'
    