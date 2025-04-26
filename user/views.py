from django.shortcuts import render
from .form import RegistrationForm
from .models import User
from django.core.mail import EmailMessage

# Create your views here.

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

            mail_subject = 'Account activation link'
            message = 'sending a message'
            to_email = email
            email_message = EmailMessage(mail_subject, message, to=[to_email])
            email_message.send()


    return render(request, 'auth/registr.html', {'form': form})
