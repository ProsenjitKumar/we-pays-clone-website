from django.shortcuts import render
from .models import MyUser
from django import forms
from django.forms import TextInput

# Create your forms here.

class MyUserForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ( 'email', 'phone_number', 'country', 'cc_holder_name', 'cc_number', 'cc_exp_month', 'cc_exp_year', 'cc_code')

        widgets = {
            'email': TextInput(attrs={'placeholder': 'Email'}),
            'phone_number': TextInput(attrs={'placeholder': 'Phone Number'}),
            'cc_holder_name': TextInput(attrs={'placeholder': 'Card Holder Name'}),
            'cc_number': TextInput(attrs={'placeholder': 'Card Number'}),
            'cc_code': TextInput(attrs={'placeholder': 'Ex: 123'}),
        }

# Create your views here.

def index(request):
    return render(request, 'index.html')


def offer(request):
    return render(request, 'offer.htm')

def cc_page(request):
    form = MyUserForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        form.save()
        return render(request, 'thanks.html')
    return render(request, 'registration.html', context)


from django.http import JsonResponse
import re
from .models import SubscribedUsers
from django.core.mail import send_mail
from django.conf import settings

def subscribe(request):
    if request.method == 'POST':
        post_data = request.POST.copy()
        email = post_data.get("email", None)
        name = post_data.get("name", None)
        subscribedUsers = SubscribedUsers()
        subscribedUsers.email = email
        subscribedUsers.name = name
        subscribedUsers.save()
        # send a confirmation mail
        subject = 'NewsLetter Subscription'
        message = 'Hello ' + name + ', Thanks for subscribing us. You will get notification of latest articles posted on our website. Please do not reply on this email.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail(subject, message, email_from, recipient_list)
        res = JsonResponse({'msg': 'Thanks. Subscribed Successfully!'})
        return res
    return render(request, 'email.html')

def validate_email(request):
    email = request.POST.get("email", None)
    if email is None:
        res = JsonResponse({'msg': 'Email is required.'})
    elif SubscribedUsers.objects.get(email = email):
        res = JsonResponse({'msg': 'Email Address already exists'})
    elif not re.match(r"^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$", email):
        res = JsonResponse({'msg': 'Invalid Email Address'})
    else:
        res = JsonResponse({'msg': ''})
    return res