from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import render, redirect
from .models import article
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages


# @login_required
def home(request):
    today = timezone.now().date()
    context = {
            "date": today,
        }
    if request.method == "POST":
        subject = request.POST.get("email", "")
        message = request.POST.get("msg", "")
        picked_date = request.POST.get("date","")
        picked_time = request.POST.get("appointment","")
        subject = subject + " pour le " + str(picked_date) + " à " + str(picked_time)
        from_email = request.POST.get("email", "")
        if subject and message and from_email:
            try:
                send_mail(subject, message, from_email, ["thierry.fanahafa@gmail.com"])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return HttpResponseRedirect("/")
        else:
            return messages.warning(request,"Mail not sent")
        
        
      
    return render(request, 'home.html', context)


def about(request):
    today = timezone.now().date()
    context = {
            "date": today,
        }
    return render(request, 'about.html', context)

def products(request):
    today = timezone.now().date()
    context = {
            "objects": article.objects.filter(type="P")
        }
    return render(request, 'products.html', context)

def services(request):
    today = timezone.now().date()
    context = {
            "objects": article.objects.filter(type="S")
        }
    return render(request, 'services.html', context)