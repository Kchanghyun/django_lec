from django.db import models

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
