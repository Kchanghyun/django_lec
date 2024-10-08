"""
URL configuration for my_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage),
    path('company/', views.company),
    path('mysite/product/', views.product),
    path('community/support', views.support, name='support'),
    path('community/faq', views.faq, name='faq'),
    path('mysite/product/new/', views.new, name='new'),
    path('mysite/product/head/', views.headsets, name='headsets'),
    path('mysite/product/notebook/', views.notebook, name='notebook'),
    path('mysite/product/keyboard/', views.keyboard, name='keyboard'),
    path('mysite/product/mouse/', views.mouse, name='mouse'),
    path('mysite/product/<int:product_id>/', views.detail, name='detail'),
    path('community/<int:notice_id>/', views.sup_detail, name='sup_detail'),
    # path('mysite/product/head/<int:product_id>/', views.product_detail, name='product_detail'),
]
