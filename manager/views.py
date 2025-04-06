from django.shortcuts import redirect, render
from django.utils.safestring import mark_safe
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import calendar
import datetime
now = datetime.datetime.now()

from .forms import SignUpForm, UserProfileForm
from .models import Lesson, Profile

def home(request):
    return render(request, 'home.html', {})

def schedule(request):
    if request.user.is_authenticated:
        genba_list = Lesson.objects.all().order_by('-date_created')
        genbas_today = []
        for genba in genba_list:
            date = datetime.datetime(now.year, now.month, now.day)
            start_date = datetime.datetime(genba.start_date.year, genba.start_date.month, genba.start_date.day)
            end_date = datetime.datetime(genba.end_date.year, genba.end_date.month, genba.end_date.day)
            if start_date <= date <= end_date:
                genbas_today.append(genba)
                if request.user.profile.contract_type == '下請け':
                    for genba in genbas_today:
                        if genba.head_person != request.user.profile or request.user.profile not in genba.attendees.all():
                            genbas_today.remove(genba)
    year = int(now.year)
    month = int(now.month)
    cal = calendar.HTMLCalendar().formatmonth(year, month)
    cal = cal.replace('<td ', '<td width="150" height="150" hover')
    cal = mark_safe(cal)
    if request.user.is_authenticated:
         context = {
            "genba_list": genba_list,
            "genbas_today":genbas_today,
            "year": year,
            "month": month,
            "cal": cal,
        }
         return render(request, "schedule.html", context=context)
    else:
        return redirect('login_user')
    
def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.profile:
                messages.success(request, (f"{user.profile} さん, お帰りなさい。"))
            else:
                messages.success(request, ("お帰りなさい。"))
            return redirect("home")
        else:
            messages.success(request, ("ユーザー名、またはパスワードが違います。再度お試しください。"))
            return redirect("login_user")
    else:
        return render(request, "authentication/login.html", {})  

@login_required(login_url='/login_user/')
def logout_user(request):
    logout(request)
    messages.success(request, ("ログアウトしました。"))
    return redirect("login_user")

@login_required(login_url='/login_user/')
def register_user(request):
    if request.user.is_superuser:
        form = SignUpForm()
        if request.method == "POST":
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password1"]
                user = authenticate(username=username, password=password)
                messages.success(request, ("プロフィールを入力してください。"))
                return redirect("update_profile", user.pk)
            else:
                messages.success(request, ("再度お試しください。"))
                return redirect("register_user")
        else:
            return render(request, "authentication/register_user.html", {
                "form": form
            })
    else:
        messages.success(request, ("ページは管理人のみがアクセスできます。"))
        return redirect("login_user")
    
@login_required(login_url='/login_user/')
def delete_user(request, user_id):
    if request.user.is_authenticated:
        current_user = Profile.objects.get(user__id=user_id)
        current_user.delete()
        messages.success(request, "プロフィールを削除しました。")
        return redirect("profile_list")
    else:
        messages.success(request, "ログインしてください。")
        return redirect("home")
    
@login_required(login_url='/login_user/')
def profile_list(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.all().order_by('-date_created')
        contract = request.user.profile.contract_type
        if request.method == "POST":
            keyword = request.POST['keyword']
            result_list = Profile.objects.filter(fullname__contains=keyword).order_by('-date_created')
            return render(request, "profile_search_list.html", {"result_list": result_list, "keyword": keyword})
        else:
            return render(request, "profile_list.html", { "profiles": profiles, "contract": contract })
    else:
        return redirect('login_user')

@login_required(login_url='/login_user/')
def update_profile(request, profile_id):
    if request.user.is_superuser:
        if request.user.is_authenticated:
            profile = Profile.objects.get(id=profile_id)
            form = UserProfileForm(request.POST or None, instance=profile)
            if form.is_valid():
                form.save()
                messages.success(request, "プロフィールを更新しました。")
                return redirect("profile_list")
            return render(request, "update_profile.html", {"form": form , "profile": profile })
        else:
            messages.success(request, "ログインしてください。")
            return redirect("login_user")
    else:
        messages.success(request, ("ページは管理人のみがアクセスできます。"))