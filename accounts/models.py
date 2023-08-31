from django.db import models
from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField

# Create your models here.

class User(AbstractUser):
    profile_image = ResizedImageField(
        size=[500, 500],
        crop=['middle', 'center'],
        upload_to='profile',
    )
    # post_set 자동생성
    # like_posts 자동생성 (related_to 로 이름 정해줌)
    following = models.ManyToManyField('self', related_name='followers', symmetrical=False)
    # 선생님은 followings 라고 하셨음.
    #followers = 라는 컬럼이 자동 생성
