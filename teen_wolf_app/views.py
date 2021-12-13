from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.
def index(request):
    if request.method == 'POST':
        email =  EmailMessage(
        subject = request.POST['name'],
        message = request.POST['message'],
        from_email = request.POST['email'],
        reply_to = request.POST['email'],
        )
        sent = email.send (subject, message, from_email, ['contact@teenwolftoken.com'], fail_silently=False)
    return render(request, 'index.html')