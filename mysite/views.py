from django.shortcuts import get_object_or_404, render
from .models import MainContent
from .models import Notice

# Create your views here.


# localhost:8080/mysite 페이지 호출을 요청하면 urls.py에서 mysite 매핑을 확인하고
# views.py에서 index 함수를 호출해서 그 결과를 다시 브라우저에 출력하는 형태이다.

# URL 매핑 작업을 통해 브라우저에서 입력한 URL이 Django의 뷰(View)와 연결되도록 해야 한다.
# 프로젝트의 URL 설정 파일은 보통 urls.py 파일이다.

def index(request):
    content_list = MainContent.objects.order_by('-pub_date')
    context = {'content_list': content_list}
    return render(request, 'mysite/content_list.html', context)


def detail(request, content_id):
    content_list = get_object_or_404(MainContent, pk=content_id)
    context = {'content_list': content_list}
    return render(request, 'mysite/content_detail.html', context)


def notice_index(request):
    community_content_list = Notice.objects.order_by('-created_at')
    context = {'community_content_list': community_content_list}
    return render(request, 'pages/community.html', context)