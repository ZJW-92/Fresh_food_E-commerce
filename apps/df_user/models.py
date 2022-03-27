from django.db import models

from datetime import datetime

from df_goods.models import GoodsInfo


class UserInfo(models.Model):

    uname = models.CharField(max_length=20, verbose_name="user", unique=True)
    upwd = models.CharField(max_length=40, verbose_name="password", blank=False)
    uemail = models.EmailField(verbose_name="email", unique=True)
    ushou = models.CharField(max_length=20, default="", verbose_name="delivery address")
    uaddress = models.CharField(max_length=100, default="", verbose_name="address")
    uyoubian = models.CharField(max_length=6, default="", verbose_name="postcode")
    uphone = models.CharField(max_length=11, default="", verbose_name="tel")

    class Meta:
        verbose_name = "user information"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.uname


class GoodsBrowser(models.Model):

    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name="user ID")
    good = models.ForeignKey(GoodsInfo, on_delete=models.CASCADE, verbose_name="goods ID")
    browser_time = models.DateTimeField(default=datetime.now, verbose_name="browse time")

    class Meta:
        verbose_name = "browse item"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{0}browse list {1}".format(self.user.uname, self.good.gtitle)
