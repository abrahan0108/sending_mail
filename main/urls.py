from django.urls import path
from django.views.generic import TemplateView
from .views import sending_mail


urlpatterns = [
    path("",
         TemplateView.as_view(template_name="home.html"),
         name="home"),
    path("send_email/",
         sending_mail),
]