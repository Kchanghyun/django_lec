from django.shortcuts import render

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
