"""Django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from Menu import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='Homepage'),
    path('product/', views.product, name='products'),
    path('productdetails/<str:pk>/', views.productA, name='product-details'),
    path('account/', views.account, name='Account'),
    path('cart/', views.cart, name='CartInfo'),
    path('register/', views.register, name='RegisterPage'),
    path('logout/', views.user_logout, name='LogOut'),
    path('checkout/', views.checkout, name='checkOut'),
    path('payment/', views.payment, name='payment'),
    path('add-item/', views.add_item, name='add_item'),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
