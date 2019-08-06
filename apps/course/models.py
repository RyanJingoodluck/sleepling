from django.db import models

from common.base.models import UUIDModel, RecordModel
from common.base.models import OrderingMeta


# Create your models here.


class DetailImage(UUIDModel):
    path = models.URLField(
        max_length=1024,
        blank=True,
        default="",
        verbose_name="详情图片链接",
        help_text="详情图片的链接"
    )

    class Meta(OrderingMeta):
        db_table = 'detail_image'
        verbose_name_plural = verbose_name = 'detail_image'


class Course(UUIDModel):
    name = models.CharField(
        db_index=True,
        max_length=128,
        verbose_name="课程名",
        help_text="课程名"
    )
    path = models.URLField(
        max_length=1024,
        blank=True,
        default="",
        verbose_name="课程语音链接",
        help_text="课程语音链接"
    )
    desc = models.CharField(
        max_length=1024,
        blank=True,
        default="",
        verbose_name="课程描述",
        help_text="课程描述"
    )
    # 时长单位是s
    duration = models.PositiveIntegerField(
        db_index=True,
        default=0,
        verbose_name="课程语音时长",
        help_text="课程语音时长"
    )

    class Meta(OrderingMeta):
        db_table = 'course'
        verbose_name_plural = verbose_name = 'course'

    def __str__(self):
        return "{}".format(self.name)


class CourseDetail(RecordModel):
    course = models.OneToOneField(
        to=Course,
        on_delete=models.CASCADE,
        verbose_name="课程",
        help_text="课程"
    )
    image = models.ForeignKey(
        to=DetailImage,
        on_delete=models.SET_DEFAULT,
        default='',
        verbose_name="图片",
        help_text="图片"
    )
    like_count = models.PositiveIntegerField(
        db_index=True,
        default=0,
        verbose_name="喜欢数",
        help_text="喜欢数"
    )
    like_count = models.PositiveIntegerField(
        db_index=True,
        default=0,
        verbose_name="课程语音时长",
        help_text="课程语音时长"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="课程价格",
        help_text="课程价格"
    )

    class Meta(OrderingMeta):
        db_table = 'course_detail'
        verbose_name_plural = verbose_name = 'course_detail'

    def __str__(self):
        return "{}详情".format(self.course.name)