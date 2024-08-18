from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import MainContent, Comment, Product
from .models import Notice
from .forms import CommentForm

# Create your views here.


# localhost:8080/mysite 페이지 호출을 요청하면 urls.py에서 mysite 매핑을 확인하고
# views.py에서 index 함수를 호출해서 그 결과를 다시 브라우저에 출력하는 형태이다.

# URL 매핑 작업을 통해 브라우저에서 입력한 URL이 Django의 뷰(View)와 연결되도록 해야 한다.
# 프로젝트의 URL 설정 파일은 보통 urls.py 파일이다.

def index(request):
    content_list = MainContent.objects.order_by('-pub_date')
    context = {'content_list': content_list}
    return render(request, 'mysite/content_list.html', context)



# def notice_index(request):
#     community_content_list = Notice.objects.filter(category='공지사항').order_by('-created_at')
#     context = {'community_content_list': community_content_list}
#     return render(request, 'pages/community.html', context)

# def mouse(request):
#     products = Product.objects.filter(category='마우스')
#     return render(request, 'pages/products.html', {'products': products})

@login_required(login_url='accounts:login')
def comment_create(request, content_id):
    content_list = get_object_or_404(Product, pk=content_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.content_list = content_list
            comment.author = request.user
            comment.save()
            return redirect('detail', product_id=content_list.id)
    else:
        form = CommentForm()
        context = {'content_list': content_list, 'form': form}
        return render(request, 'mysite/content_detail.html', context)

@login_required(login_url='accounts:login')
def comment_update(request, comment_id):
    comment=get_object_or_404(Comment, pk=comment_id)

    if request.user != comment.author:  # 요청한 사람의 user가 댓글의 주인이 아니면 접근거부
        raise PermissionDenied

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('detail', product_id=comment.content_list.id)
    else:
        form = CommentForm(instance=comment)

    context = {'comment': comment, 'form':form}
    return render(request, 'mysite/comment_form.html', context)


@login_required(login_url='accounts:login')
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.user != comment.author:
        raise PermissionDenied
    else:
        comment.delete()
    return redirect('detail', product_id=comment.content_list.id)