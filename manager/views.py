from django.shortcuts import redirect, render
from django.utils.safestring import mark_safe
from calendar import calendar
import datetime
now = datetime.datetime.now()

from .models import Lesson

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