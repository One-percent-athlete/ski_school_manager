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
        ('管理', '管理'),
        ('教练', '教练'),
        ('其他', '其他'),
    )
    SKI = (
        ('双板无极', '双板无极'),
        ('双板1级', '双板1级'),
        ('双板2级', '双板2级'),
        ('双板3级', '双板3级'),
        ('双板4级', '双板4级'),
    )
    SNOWBOARD = (
        ('单板无极', '单板无极'),
        ('单板1级', '单板1级'),
        ('单板2级', '单板2级'),
        ('单板3级', '单板3级'),
        ('单板4级', '单板4级'),
    )
    SKI_SYSTEM = (
        ('加拿大', '加拿大'),
        ('新西兰', '新西兰'),
        ('澳洲', '澳洲'),
        ('日本', '日本'),
        ('其他', '其他'),
        ('无', '无'),
    )
    SNOWBOARD_SYSTEM = (
        ('加拿大', '加拿大'),
        ('新西兰', '新西兰'),
        ('澳洲', '澳洲'),
        ('日本', '日本'),
        ('其他', '其他'),
        ('无', '无'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField("生年月日", blank=True, null=True)
    color = models.CharField("教练色", max_length=30, choices=COLORS)
    contract_type = models.CharField("职务", max_length=50, choices=TYPE, default='教练')
    fullname = models.CharField("姓名", max_length=20, blank=True)
    phone = models.CharField("電話", max_length=20, blank=True)
    email = models.CharField("邮箱", max_length=50, blank=True)
    wechat = models.CharField("微信", max_length=20, blank=True)
    whatsapp = models.CharField("Whatsapp", max_length=20, blank=True)
    line = models.CharField("LINE", max_length=20, blank=True)
    ski_system = models.CharField("双板体系", max_length=50, choices=SKI_SYSTEM, default='加拿大')
    snowboard_system = models.CharField("单板体系", max_length=50, choices=SNOWBOARD_SYSTEM, default='加拿大')
    ski = models.CharField("级别", max_length=50, choices=SKI, default='双板1级')
    snowboard = models.CharField("级别", max_length=50, choices=SNOWBOARD, default='单板1级')
    accommodation = models.CharField("宿舍", max_length=20, blank=True)
    commission = models.DecimalField("提成", max_digits=10, decimal_places=2, default=0.00)
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
    PAYMENT_TYPES = (
        ('現金','現金'),
        ('刷卡', '刷卡'),
        ('電子支付', '電子支付'),
        ('未支付', '未支付'),
        )
    PLACE = (
        ('比洛夫', '比洛夫'),
        ('花园', '花园'),
        ('安努', '安努'),
        ('莫伊哇', '莫伊哇'),
        ('留寿都', '留寿都'),
        ('喜乐乐', '喜乐乐'),
        ('其他', '其他'),
    )
    instructors = models.ManyToManyField(Profile, related_name="instructors", blank=False)
    lesson_number = models.IntegerField("课次", blank=False, null=True, default=0)
    lesson_type = models.CharField("课程类型", max_length=50, blank=True, null=True)
    client = models.CharField("客人姓名", max_length=255)
    address = models.CharField("酒店", max_length=255)
    level = models.CharField("级别", max_length=255)
    place = models.CharField("雪场", max_length=50, choices=PLACE, default='比洛夫')
    payment_type = models.CharField("付款方式", max_length=50, choices=PAYMENT_TYPES, default='未支付')
    payment_amount = models.DecimalField("付款金額", max_digits=10, decimal_places=2, blank=True, null=True)
    payment_date = models.DateTimeField("付款日", blank=True, null=True)
    note = models.CharField("備考", max_length=255, blank=True, null=True)
    start_date = models.DateTimeField("開始日")
    end_date = models.DateTimeField("終了日")
    finished = models.BooleanField("終了", default=False)
    date_created = models.DateTimeField("作成日", auto_now_add=True)

    def __str__(self):
        return f"{self.instructors} - {self.client}"
    
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
        return f"{self.content} - {self.author} - {self.date_created}"