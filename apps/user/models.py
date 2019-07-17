from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    """
    用户表
    """
    USER_GENDER_CHOICES = (
        (0, '女'),
        (1, '男'),
    )
    phone = models.CharField(max_length=32, db_index=True, blank=True,default="",verbose_name="手机号码",
                             help_text="手机号码" )
    sex = models.SmallIntegerField(choices=USER_GENDER_CHOICES, default=1, verbose_name="性别")
    avatar = models.CharField(max_length=50, default="", null=True, blank=True, verbose_name="头像")
    openid = models.CharField(max_length=64, db_index=True, verbose_name='openid')
