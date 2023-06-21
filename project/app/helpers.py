from django.core.mail import send_mail
from django.conf import settings
import uuid
def send_forget_password_mail(email,token):
    
    subject="link for password change"
    message=f'click on link to reset password  http://127.0.0.1:8000/forget_password/{token}/'
    email_form=settings.EMAIL_HOST_USER
    recipent_list=[email]
    send_mail(subject,message,email_form, recipent_list)
    return True