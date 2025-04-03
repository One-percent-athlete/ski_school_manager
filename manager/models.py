from datetime import date
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Profile(models.Model):
    CONTRACT_TYPES = (
        ('其他', '其他'),
        ('管理', '管理'),
        ('教练', '教练'),
    )
    TIXI = (
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
    contract_type = models.CharField("职务", max_length=50, choices=CONTRACT_TYPES, default='教练')
    fullname = models.CharField("姓名", max_length=20, blank=True)
    phone = models.CharField("電話", max_length=20, blank=True)
    email = models.CharField("邮箱", max_length=20, blank=True)
    weixin = models.CharField("微信", max_length=20, blank=True)
    whatsapp = models.CharField("Whatsapp", max_length=20, blank=True)
    line = models.CharField("LINE", max_length=20, blank=True)
    tixi = models.CharField("体系", max_length=50, choices=TIXI, default='加拿大')
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

class Notification(models.Model):
    author = models.ForeignKey(User, related_name="notification", on_delete=models.CASCADE)
    content = models.CharField("内容", max_length=500)
    date_created = models.DateTimeField("作成日", auto_now_add=True)
    
    def __str__(self):
        return f"{self.content} - {self.author} - {self.created_at}"