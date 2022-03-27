from django.db import models

from df_goods.models import GoodsInfo
from df_user.models import UserInfo

class OrderInfo(models.Model):  # big order
    oid = models.CharField(max_length=20, primary_key=True, verbose_name="big order")
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name="order user")
    odate = models.DateTimeField(auto_now=True, verbose_name="time")
    oIsPay = models.BooleanField(default=False, verbose_name="paid or not")
    ototal = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="total price")
    oaddress = models.CharField(max_length=150, verbose_name="delivery address")

    class Meta:
        verbose_name = "order"
        verbose_name_plural = verbose_name

    def __str__(self):

        return "{0}on order {1}".format(self.user.uname, self.odate)


class OrderDetailInfo(models.Model):

    goods = models.ForeignKey(GoodsInfo, on_delete=models.CASCADE, verbose_name="commodity")
    order = models.ForeignKey(OrderInfo, on_delete=models.CASCADE, verbose_name="order")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="commodity price")
    count = models.IntegerField(verbose_name="piece")

    class Meta:
        verbose_name = "details"
        verbose_name_plural = verbose_name

    def __str__(self):
        # return self.goods.gtitle + "(数量为" + str(self.count)  + ")"
        return "{0}(number is {1})".format(self.goods.gtitle, self.count)