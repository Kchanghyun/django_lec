from django.shortcuts import get_object_or_404, render
from mysite.models import MainContent, Product
from mysite.models import Notice
from datetime import timedelta
from django.utils import timezone

# Create your views here.


def mainpage(request):
    return render(request, 'pages/mainpage.html')


def company(request):
    return render(request, 'pages/company_info.html')


def product(request):
    return render(request, 'pages/product_category.html')


def support(request):
    # return render(request, 'pages/community.html')
    community_content_list = Notice.objects.filter(category='공지사항').order_by('-created_at')
    context = {
        'page_title': '공지사항',
        'community_content_list': community_content_list
    }
    return render(request, 'pages/community.html', context)


def faq(request):
    # return render(request, 'pages/community.html')
    community_content_list = Notice.objects.filter(category='Q&A')
    context = {
        'page_title': 'Q&A',
        'community_content_list': community_content_list
    }
    return render(request, 'pages/community.html', context)



def products(request):
    return render(request, 'pages/products.html')


def detail(request, product_id):
    product_list = get_object_or_404(Product, pk=product_id)
    context = {'product_list': product_list}
    return render(request, 'mysite/content_detail.html', context)


def sup_detail(request, notice_id):
    notice_list = get_object_or_404(Notice, pk=notice_id)
    context = {'notice_list': notice_list}
    return render(request, 'pages/community_detail.html', context)


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


def new(request):
    now = timezone.now()
    ten_days_ago = now - timedelta(days=10)
    products = Product.objects.filter(pub_date__gte=ten_days_ago)
    return render(request, 'pages/products.html', {'products': products})