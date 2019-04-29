from django import forms
from django.core.mail import send_mail
import logging


logger =logging.getLogger(__name__)


class ContactForm(forms.Form):
   from_email = forms.EmailField(required=True)
   subject = forms.CharField(required=True)
   message = forms.CharField(widget=forms.Textarea, required=True)

   def send_mail(self):
      logger.info("Sending email to customer service")
      message = "From: {0}\n{1}".format(
         self.cleaned_data["name"],
         self.cleaned_data["message"]
      )
      send_mail(
         "Site message",
         message,
         "f8abrahan@gmail.com",
         ["cortes.abrahan@yahoo.com.mx"],
         fail_silently=False,
      )