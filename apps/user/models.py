from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    """
    用户表
    """
    phone = models.CharField(
        max_length=32,
        db_index=True,
        blank=True,
        default="",
        verbose_name="手机号码",
        help_text="手机号码"
    )
