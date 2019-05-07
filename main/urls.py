from django.urls import path
from django.views.generic import TemplateView
from main import views


urlpatterns = [
    path("",
         TemplateView.as_view(template_name="home.html"),
         name="home"),
    path("contact_us/",
         views.ContacUsView.as_view(),
         name="contact_us",
         ),
]