from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.
def index(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        email =  EmailMessage(
            subject = form.cleaned_data['title'],
            message = form.cleaned_data['content'],
            from_email = 'contact@teenwolftoken.com',
            recipient_list=['contact@teenwolftoken.com'],
            reply_to = form.cleaned_data['contact_email'],
        )
        sent = email.send (fail_silently=False)
        return redirect('/')
    return render(request, 'index.html')