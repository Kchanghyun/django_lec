from django.contrib import admin
from .models import MainContent
from .models import Notice

admin.site.register(MainContent)


# Register your models here.
@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')  # 관리자 패널에서 표시할 필드
    search_fields = ('title',)  # 제목으로 검색 가능
    ordering = ('-created_at',)  # 작성일 기준 내림차순 정렬
