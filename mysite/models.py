from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class MainContent(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')


class Notice(models.Model):
    title = models.CharField(max_length=200) # 공지사항 제목
    content = models.TextField()  # 공지사항 내용
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 작성자
    content_list = models.ForeignKey(MainContent, on_delete=models.CASCADE)  # 제목
    content = models.TextField()  # 작성 내용
    create_date = models.DateTimeField(auto_now_add=True)  # 작성 날짜
    modify_date = models.DateTimeField(auto_now=True)  # 수정 날짜

# models.ForeignKey('self', on_delete=models.CASCADE) <- 자신과 다대일 관계인 객체를 만듦
# MainContent에는 여러 개의 Comment가 달릴 수 있는데, MainContent를 삭제하면 관련된 Comment도 삭제한다는 의미
# create_date에는 auto_now_add=True로 최초 시간을 저장하고 댓글을 수정하면 modify_date에서 auto_now=True로 수정 시간을 저장
