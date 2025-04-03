from datetime import date
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Profile(models.Model):
    COLORS = (
        ('#808080', '灰色'),
        ('#ff6961', '赤色'),
        ('#ffb480', '橙色'),
        ('#f8f38d', '黄色'),
        ('#42d6a4', '緑色'),
        ('#08cad1', '水色'),
        ('#59adf6', '青色'),
        ('#9d94ff', '紫色'),
        ('#c780e8', '桃色'),
    )
    TYPE = (
        ('其他', '其他'),
        ('管理', '管理'),
        ('教练', '教练'),
    )
    SYSTEM = (
        ('加拿大', '加拿大'),
        ('新西兰', '新西兰'),
        ('澳大利亚', '澳大利亚'),
        ('日本', '日本'),
        ('其他', '其他'),
    )
    LEVEL = (
        ('1级', '1级'),
        ('2级', '2级'),
        ('3级', '3级'),
        ('满级', '满级'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField("生年月日", blank=True, null=True)
    color = models.CharField("現場色", max_length=30, choices=COLORS)
    contract_type = models.CharField("职务", max_length=50, choices=TYPE, default='教练')
    fullname = models.CharField("姓名", max_length=20, blank=True)
    phone = models.CharField("電話", max_length=20, blank=True)
    email = models.CharField("邮箱", max_length=20, blank=True)
    weixin = models.CharField("微信", max_length=20, blank=True)
    whatsapp = models.CharField("Whatsapp", max_length=20, blank=True)
    line = models.CharField("LINE", max_length=20, blank=True)
    tixi = models.CharField("体系", max_length=50, choices=SYSTEM, default='加拿大')
    jibie = models.CharField("级别", max_length=50, choices=LEVEL, default='1级')
    sushe = models.CharField("宿舍", max_length=20, blank=True)
    note = models.CharField("備考", max_length=500, blank=True)
    is_active = models.BooleanField("現役中", default=True)
    date_created = models.DateTimeField("作成日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)

    def __str__(self):
        return f"{self.fullname}"
    

def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

post_save.connect(create_profile, sender=User)

class Lesson(models.Model):
    instructors = models.ManyToManyField(Profile, related_name="instructors", blank=False)
    name = models.CharField("", max_length=255)
    client = models.CharField("客人姓名", max_length=255)
    address = models.CharField("酒店", max_length=255)
    jibie = models.CharField("级别", max_length=255)
    job_description = models.CharField("内容", max_length=255, blank=True, null=True)
    note = models.CharField("備考", max_length=255, blank=True, null=True)
    start_date = models.DateTimeField("開始日")
    end_date = models.DateTimeField("終了日")
    finished = models.BooleanField("終了", default=False)
    date_created = models.DateTimeField("作成日", auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.client}"
    
    @property
    def Is_past(self):
        today = date.today()
        if self.end_date.date() < today:
            text = "Past"
        else:
            text = "Future"
        return text

class Notification(models.Model):
    author = models.ForeignKey(User, related_name="notification", on_delete=models.CASCADE)
    content = models.CharField("内容", max_length=500)
    date_created = models.DateTimeField("作成日", auto_now_add=True)
    
    def __str__(self):
        return f"{self.content} - {self.author} - {self.created_at}"