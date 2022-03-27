from datetime import datetime

from django.db import models
from tinymce.models import HTMLField

class TypeInfo(models.Model):
    # commodity category information
    isDelete = models.BooleanField(default=False)
    ttitle = models.CharField(max_length=20, verbose_name="category")

    class Meta:
        verbose_name = "category"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.ttitle


class GoodsInfo(models.Model):
    # detail information
    isDelete = models.BooleanField(default=False)
    gtitle = models.CharField(max_length=20, verbose_name="commodity name", unique=True)
    gpic = models.ImageField(verbose_name='commodity image', upload_to='df_goods/image/%Y/%m', null=True, blank=True)
    gprice = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="commodity price")
    gunit = models.CharField(max_length=20, default='500g', verbose_name="weight per unit")
    gclick = models.IntegerField(verbose_name="clicks", default=0, null=False)
    gjianjie = models.CharField(max_length=200, verbose_name="overview")
    gkucun = models.IntegerField(verbose_name="stock", default=0)
    gcontent = HTMLField(max_length=200, verbose_name="details")
    gtype = models.ForeignKey(TypeInfo, on_delete=models.CASCADE, verbose_name="category")


    class Meta:
        verbose_name = "commodity"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.gtitle
