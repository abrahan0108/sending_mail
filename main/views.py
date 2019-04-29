from django.views.generic.edit import FormView
from main import forms
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
# Create your views here.


def sending_mail(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        send_mail('Subject', 'message', 'f8abrahan@gmail.com', [email], fail_silently=False)
        return HttpResponse('Mail Sent to' + email)

    return render(request, 'main/send_email.html')
