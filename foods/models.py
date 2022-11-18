from django.db import models
from django.utils.translation import gettext as _


class Food(models.Model):
    FOOD_TYPE = [
        ("breakfast" , "صبحانه"),
        ("drinks" , "نوشیدنی"),
        ("dinner", "شام"),
        ("lunch" , "نهار"),
    ]
    name = models.CharField(max_length=100)
    description = models.CharField(_("توضیحات") , max_length=50)
    rate = models.IntegerField(_("امتیاز"))
    price = models.IntegerField()
    time = models.IntegerField(_("زمان لازم"))
    pub_date = models.DateTimeField(_("تاریخ انتشار"),auto_now_add=True)
    photo = models.ImageField(upload_to='foods/')
    type = models.CharField(_("نوع غذا") , max_length=10 , choices=FOOD_TYPE , default="dinner")

    def __str__(self):
        return self.name