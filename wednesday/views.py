from django.shortcuts import render
from datetime import datetime

# Create your views here.
def is_wednesday(request):
    today = datetime.today()
    weekday = today.strftime('%A')
    is_wednesday = weekday == 'Wednesday'
    
    context = {
        "today": today,
        "weekday": weekday,
        "is_wednesday": is_wednesday
    }
    
    return render(request, "wednesday/check.html", context)