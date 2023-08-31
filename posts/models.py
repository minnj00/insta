from django.db import models
from django_resized import ResizedImageField
from django.conf import settings

# Create your models here.

class Post(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # 생성된 시간설정
    updated_at = models.DateTimeField(auto_now=True) # 수정된 시간설정
    # image = models.ImageField(upload_to='image/%Y/%m') # 사진 저장을 위해서는 pip install pillow 할 것, 
    # upload_to 부분이 바뀌었을 떄 db에서 관리하는게 아니여서 makemigrations를 안했는데도 될 수 있음 근데 혹시 모르니깐 makemigrations 꼭 할 것 
    image = ResizedImageField(
        size=[500,500],
        crop=['middle', 'center'],
        upload_to='image/%Y/%m',
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # user_id 가 자동생성

class Comment(models.Model):
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)