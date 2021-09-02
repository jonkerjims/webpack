from django.db import models


# Create your models here.
class classify(models.Model):
    class_name = models.CharField(max_length=30,default='添加分类')
    tag = models.CharField(max_length=500,default='介绍网站')
    is_delete = models.IntegerField(max_length=1,default=1)


class data(models.Model):
    class_name = models.CharField(max_length=30)
    title = models.CharField(max_length=100,default='暂无标题')
    site_addr = models.CharField(max_length=500)
    classify_id = models.IntegerField(max_length=500, default=0)
    is_delete = models.IntegerField(max_length=1, default=1)

