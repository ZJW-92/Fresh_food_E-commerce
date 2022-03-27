from django.db import models

from df_user.models import UserInfo
from df_goods.models import GoodsInfo

class CartInfo(models.Model):

    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name="User")
    goods = models.ForeignKey(GoodsInfo, on_delete=models.CASCADE, verbose_name="Commodity")
    count = models.IntegerField(verbose_name="", default=0)  # check number of unit of goods

    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.uname + 'cart'
