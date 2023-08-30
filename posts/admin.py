from django.contrib import admin
from .models import Post

# Register your models here.

# 관리자 페이지에서 Post 테이블을 관리할 수 있도록
admin.site.register(Post)