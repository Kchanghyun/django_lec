from django.contrib import admin
from .models import Notice
from .models import MainContent, Comment, Product
from django.utils.html import format_html


class MainContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'pub_date']
    search_fields = ['title']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['content_list', 'content', 'author', 'create_date', 'modify_date']
    search_fields = ['author']


admin.site.register(MainContent, MainContentAdmin)
admin.site.register(Comment, CommentAdmin)


# Register your models here.

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')  # 관리자 패널에서 표시할 필드
    search_fields = ('title',)  # 제목으로 검색 가능
    ordering = ('-created_at',)  # 작성일 기준 내림차순 정렬


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'image_tag', 'pub_date')

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="100" />'.format(obj.image.url))
        return 'No Image'

    image_tag.short_description = 'Image'
