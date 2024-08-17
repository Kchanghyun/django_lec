from django.shortcuts import get_object_or_404, render
from mysite.models import MainContent, Product
from mysite.models import Notice


# Create your views here.


def mainpage(request):
    return render(request, 'pages/mainpage.html')


def company(request):
    return render(request, 'pages/company_info.html')


def product(request):
    return render(request, 'pages/product_category.html')


def community(request):
    # return render(request, 'pages/community.html')
    community_content_list = Notice.objects.order_by('-created_at')
    context = {'community_content_list': community_content_list}
    return render(request, 'pages/community.html', context)


def products(request):
    return render(request, 'pages/products.html')


def detail(request, content_id):
    content_list = get_object_or_404(Product, pk=content_id)
    context = {'content_list': content_list}
    return render(request, 'mysite/content_detail.html', context)


def product_list(request):
    products = Product.objects.all()
    return render(request, 'pages/products.html', {'products': products})


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'pages/products.html', {'product': product})


def headsets(request):
    products = Product.objects.filter(category='헤드셋')
    return render(request, 'pages/products.html', {'products': products})


def notebook(request):
    products = Product.objects.filter(category='노트북')
    return render(request, 'pages/products.html', {'products': products})


def keyboard(request):
    products = Product.objects.filter(category='키보드')
    return render(request, 'pages/products.html', {'products': products})


def mouse(request):
    products = Product.objects.filter(category='마우스')
    return render(request, 'pages/products.html', {'products': products})