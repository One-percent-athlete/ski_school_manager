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
		self.fields['password2'].widget.attrs['placeholder'] = '確認パスワード'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<ul class="form-text text-muted small"><li>再度パスワード入力</li></ul>'
		
class UserProfileForm(forms.ModelForm):
	CHOICE = [
       	('其他', '其他'),
        ('教练', '教练'),
        ('管理', '管理'),]
	
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

	fullname = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control w-1/5 mb-4 p-2 bg-gray-50 rounded border border-gray-300 focus:ring-3 focus:ring-blue-300', 'placeholder':'お名前スペースなし'}))
	phone = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control w-1/5 mb-4 p-2 bg-gray-50 rounded border border-gray-300 focus:ring-3 focus:ring-blue-300', 'placeholder':'携帯電話番号: 07012345678'}))
	note = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control w-1/5 mb-4 p-2 bg-gray-50 rounded border border-gray-300 focus:ring-3 focus:ring-blue-300', 'placeholder':'注意事項'}))
	contract_type = forms.ChoiceField(label="雇用形態", choices=CHOICE, widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
	is_active = forms.BooleanField(label="現役中", required=False)
	color = forms.ChoiceField(label="カレンダー表示色", choices=COLORS, widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))

	class Meta:
		model = Profile
		fields = ('fullname', 'phone', 'note', 'contract_type', 'is_active')

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

	attendees = forms.ModelMultipleChoiceField(label="同行者", queryset=Profile.objects.all(), widget=forms.CheckboxSelectMultiple)
	name = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control mb-4 p-2 bg-gray-50 rounded border border-gray-300 focus:ring-3 focus:ring-blue-300', 'placeholder': '現場名'}))
	address = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control mb-4 p-2 bg-gray-50 rounded border border-gray-300 focus:ring-3 focus:ring-blue-300', 'placeholder': '場所'}))
	job_description = forms.CharField(label="",required=False, widget=forms.TextInput(attrs={'class':'form-control mb-4 p-2 bg-gray-50 rounded border border-gray-300 focus:ring-3 focus:ring-blue-300', "placeholder": "作業内容"}))
	note = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={'class':'form-control mb-4 p-2 bg-gray-50 rounded border border-gray-300 focus:ring-3 focus:ring-blue-300', "placeholder": "連絡事項"}))
	finished = forms.BooleanField(label="完了", required=False)
	start_date = forms.DateField(label='作業開始日', widget=forms.DateInput(attrs={'type': 'date', 'class':'form-control mb-4 p-2 bg-gray-50 rounded border border-gray-300 focus:ring-3 focus:ring-blue-300'}))
	end_date = forms.DateField(label='作業終了日', widget=forms.DateInput(attrs={'type': 'date', 'class':'form-control mb-4 p-2 bg-gray-50 rounded border border-gray-300 focus:ring-3 focus:ring-blue-300'}))
	payment_type = forms.ChoiceField(label="支付方式", choices=PAYMENT_TYPES, widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
	place = forms.ChoiceField(label="カレンダー表示色", choices=PLACE, widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))

	class Meta:
		model = Lesson
		fields = ('attendees', 'name', 'client', 'address', 'job_description','note', 'finished', 'start_date', 'end_date', 'color')
		labels = {
			'head_person':'職長',
			'attendees': '同行者',
		}