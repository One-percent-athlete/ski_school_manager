from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Lesson

class SignUpForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('username', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control w-full p-2 bg-gray-50 rounded border border-gray-300 focus:ring-3 focus:ring-blue-300'
		self.fields['username'].widget.attrs['placeholder'] = '账号名'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<ul class="form-text text-muted small"><li>不可以使用记号以及空格</li><li>150文字以下</li></ul>'

		self.fields['password1'].widget.attrs['class'] = 'form-control w-full p-2 bg-gray-50 rounded border border-gray-300 focus:ring-3 focus:ring-blue-300'
		self.fields['password1'].widget.attrs['placeholder'] = '密码'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>不可以和账号相同</li><li>8文字以上</li><li>不可使用数字</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control w-full p-2 bg-gray-50 rounded border border-gray-300 focus:ring-3 focus:ring-blue-300'
		self.fields['password2'].widget.attrs['placeholder'] = '確認密码'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<ul class="form-text text-muted small"><li>再度パスワード入力</li></ul>'
		
class UserProfileForm(forms.ModelForm):
	COLORS = [
        ('#808080', '灰色'),
        ('#ff6961', '赤色'),
        ('#ffb480', '橙色'),
        ('#f8f38d', '黄色'),
        ('#42d6a4', '緑色'),
        ('#08cad1', '水色'),
        ('#59adf6', '青色'),
        ('#9d94ff', '紫色'),
        ('#c780e8', '桃色'),
    ]
	TYPE = [
        ('管理', '管理'),
        ('教练', '教练'),
        ('其他', '其他'),
    ]
	SKI = [
        ('双板无极', '双板无极'),
        ('双板1级', '双板1级'),
        ('双板2级', '双板2级'),
        ('双板3级', '双板3级'),
        ('双板4级', '双板4级'),
    ]
	SNOWBOARD = [
        ('单板无极', '单板无极'),
        ('单板1级', '单板1级'),
        ('单板2级', '单板2级'),
        ('单板3级', '单板3级'),
        ('单板4级', '单板4级'),
    ]
	SKI_SYSTEM = [
        ('加拿大', '加拿大'),
        ('新西兰', '新西兰'),
        ('澳洲', '澳洲'),
        ('日本', '日本'),
        ('其他', '其他'),
        ('无', '无'),
    ]
	SNOWBOARD_SYSTEM = [
        ('加拿大', '加拿大'),
        ('新西兰', '新西兰'),
        ('澳洲', '澳洲'),
        ('日本', '日本'),
        ('其他', '其他'),
        ('无', '无'),
    ]
   
	fullname = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control w-1/5 mb-4 p-2 bg-gray-50 rounded border border-gray-300 focus:ring-3 focus:ring-blue-300', 'placeholder':'姓名'}))
	color = forms.ChoiceField(label="日历表示色", choices=COLORS, widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
	birthday = forms.DateField(label='生日', widget=forms.DateInput(attrs={'type': 'date', 'class':'form-control mb-4 p-2 bg-gray-50 rounded border border-gray-300 focus:ring-3 focus:ring-blue-300'}))
	phone = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control w-1/5 mb-4 p-2 bg-gray-50 rounded border border-gray-300 focus:ring-3 focus:ring-blue-300', 'placeholder':'電話号码: 07012345678'}))
	email = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control w-1/5 mb-4 p-2 bg-gray-50 rounded border border-gray-300 focus:ring-3 focus:ring-blue-300', 'placeholder':'电子邮箱: 1234@gmail'}))
	wechat = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control w-1/5 mb-4 p-2 bg-gray-50 rounded border border-gray-300 focus:ring-3 focus:ring-blue-300', 'placeholder':'微信: 1234'}))
	whatsapp = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control w-1/5 mb-4 p-2 bg-gray-50 rounded border border-gray-300 focus:ring-3 focus:ring-blue-300', 'placeholder':'Whatsapp: 1234'}))
	line = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control w-1/5 mb-4 p-2 bg-gray-50 rounded border border-gray-300 focus:ring-3 focus:ring-blue-300', 'placeholder':'LINE: 1234'}))
	ski_system = forms.ChoiceField(label="双板体系", choices=SKI_SYSTEM, widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
	ski = forms.ChoiceField(label="双板级别", choices=SKI, widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
	snowboard_system = forms.ChoiceField(label="单板体系", choices=SNOWBOARD_SYSTEM, widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
	snowboard = forms.ChoiceField(label="单板级别", choices=SNOWBOARD, widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
	accommodation = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control w-1/5 mb-4 p-2 bg-gray-50 rounded border border-gray-300 focus:ring-3 focus:ring-blue-300', 'placeholder':'宿舍'}))
	commission = forms.DecimalField(label="", max_digits=10, decimal_places=2, widget=forms.TextInput(attrs={'class':'form-control w-1/5 mb-4 p-2 bg-gray-50 rounded border border-gray-300 focus:ring-3 focus:ring-blue-300', 'placeholder':'提成'}))
	note = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control w-1/5 mb-4 p-2 bg-gray-50 rounded border border-gray-300 focus:ring-3 focus:ring-blue-300', 'placeholder':'注意事項'}))
	contract_type = forms.ChoiceField(label="职务", choices=TYPE, widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
	is_active = forms.BooleanField(label="現役中", required=False)

	class Meta:
		model = Profile
		fields = ('fullname', 'color', 'birthday', 'phone', 'email', 'wechat', 'whatsapp', 'line', 'ski_system', 'ski', 'snowboard_system', 'snowboard', 'accommodation', 'commission', 'note', 'contract_type', 'is_active')

class LessonForm(forms.ModelForm):
	
	PAYMENT_TYPES = [
        ('現金','現金'),
        ('刷卡', '刷卡'),
        ('電子支付', '電子支付'),
        ('未支付', '未支付'),
    ]
	
	PLACE = [
        ('比洛夫', '比洛夫'),
        ('花园', '花园'),
        ('安努', '安努'),
        ('莫伊哇', '莫伊哇'),
        ('留寿都', '留寿都'),
        ('喜乐乐', '喜乐乐'),
    ]
	
	LESSON_TYPE = [
        ('初学', '初学'),
        ('初级', '初级'),
        ('中级', '中级'),
        ('上级', '上级'),
        ('导滑', '导滑'),
    ]

	lesson_number = forms.IntegerField(label="课次", widget=forms.TextInput(attrs={'class':'form-control mb-4 p-2 bg-gray-50 rounded border border-gray-300 focus:ring-3 focus:ring-blue-300', 'placeholder': '课次'}))
	instructors = forms.ModelMultipleChoiceField(label="教练", queryset=Profile.objects.all(), widget=forms.CheckboxSelectMultiple)
	client = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control mb-4 p-2 bg-gray-50 rounded border border-gray-300 focus:ring-3 focus:ring-blue-300', 'placeholder': '客人名'}))
	lesson_type = forms.ChoiceField(label="课程类型", choices=LESSON_TYPE, widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
	address = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control mb-4 p-2 bg-gray-50 rounded border border-gray-300 focus:ring-3 focus:ring-blue-300', 'placeholder': '酒店名'}))
	place = forms.ChoiceField(label="雪场", choices=PLACE, widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
	note = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={'class':'form-control mb-4 p-2 bg-gray-50 rounded border border-gray-300 focus:ring-3 focus:ring-blue-300', "placeholder": "連絡事項"}))
	finished = forms.BooleanField(label="完了", required=False)
	start_date = forms.DateField(label='開始日', widget=forms.DateInput(attrs={'type': 'date', 'class':'form-control mb-4 p-2 bg-gray-50 rounded border border-gray-300 focus:ring-3 focus:ring-blue-300'}))
	end_date = forms.DateField(label='終了日', widget=forms.DateInput(attrs={'type': 'date', 'class':'form-control mb-4 p-2 bg-gray-50 rounded border border-gray-300 focus:ring-3 focus:ring-blue-300'}))
	payment_type = forms.ChoiceField(label="支付方式", choices=PAYMENT_TYPES, widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
	payment_amount = forms.ChoiceField(label="支付总额", widget=forms.TextInput(attrs={'class':'form-control mb-4 p-2 bg-gray-50 rounded border border-gray-300 focus:ring-3 focus:ring-blue-300', 'placeholder': '支付总额'}))
	payment_date = forms.DateField(label='支付日', widget=forms.DateInput(attrs={'type': 'date', 'class':'form-control mb-4 p-2 bg-gray-50 rounded border border-gray-300 focus:ring-3 focus:ring-blue-300'}))
	class Meta:
		model = Lesson
		fields = ('lesson_number', 'instructors', 'client', 'lesson_type', 'address', 'place', 'note', 'finished', 'start_date', 'end_date', 'payment_type', 'payment_amount', 'payment_date')
		labels = {
			'instructors': '',
		}
