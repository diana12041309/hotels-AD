from django.shortcuts import render, redirect
from .form import RegistrationForm, UserLoginForm
from .models import User
from django.core.mail import EmailMessage, EmailMultiAlternatives
from .token import TokenGenerator
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.utils import timezone
from django.contrib.auth import login as auth_login, authenticate, logout

# Create your views here.

acc_active_token = TokenGenerator()

def registration(request):
    if request.method != 'POST':
        form = RegistrationForm()
    else:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            try:
                exist_user = User.objects.get(email=email)
                if not exist_user.is_active:
                    exist_user.delete()
                else:
                    return render(request, 'auth/registr.html', {'form': form, 'error': 'This user already exists'})
            except:
                pass

            user = form.save(commit=False)
            user.is_active = False
            user.save()

            domain = get_current_site(request)
            mail_subject = 'Account activation link'
            message = render_to_string('auth/acc_activate_email.html', {
                'user': user,
                'domain': domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': acc_active_token.make_token(user)
            })
            to_email = email
            email_message = EmailMultiAlternatives(mail_subject, message, to=[to_email])
            email_message.attach_alternative(message, "text/html")
            email_message.send()
            return render(request, 'auth/registr_email_message.html', {'email': to_email})

    return render(request, 'auth/registr.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk = uid)
    except:
        user = None

    if user is not None and acc_active_token.check_token(user, token):
        time_elapsed = timezone.now() - user.date_joined
        if time_elapsed.total_seconds() < 900:
            user.is_active = True
            user.save()
            return render(request, 'auth/success_activate.html')
    else:
        return render(request, 'auth/fail_activate.html')
    
def userLogin(request):
    if request.method != 'POST':
        form = UserLoginForm
    else:
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            print(user)
            if user is not None:
                auth_login(request, user)
                return redirect('hotel-list')
    return render(request, 'auth/login.html', {'form': form})

def userLogout(request):
    logout(request)
    return redirect('hotel-list')