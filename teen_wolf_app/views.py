from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):
    if request.method == 'POST':
        subject = request.POST['name']
        message = request.POST['message']
        from_email = request.POST['email']
        reply_to = [from_email]
        send_mail(subject, message, from_email, ['contact@teenwolftoken.com'], fail_silently=False)
    return render(request, 'index.html')