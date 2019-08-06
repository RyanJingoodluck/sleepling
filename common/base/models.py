import uuid

from django.db import models

from apps.user.models import User


class Meta:
    get_latest_by = 'created_at'
    ordering = ['-created_at']


class RecordModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间", help_text="更新时间")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间", help_text="创建时间")
    updater = models.ForeignKey(to=User, default=None, verbose_name="更新人", help_text="更新人",
                                on_delete=models.SET_DEFAULT)

    class Meta:
        abstract = True


class UUIDModel(RecordModel):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class OrderingMeta:
    get_latest_by = 'created_at'
    ordering = ['-created_at']
