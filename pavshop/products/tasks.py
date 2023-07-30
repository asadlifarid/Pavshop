import time
from celery import shared_task
from base.models import Newsletter
from products.models import Product
from django.db.models import Count
from datetime import datetime

from django.contrib.auth import get_user_model, authenticate

User = get_user_model()

from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings



@shared_task
def export_data():
    print('Process Start')
    time.sleep(10)
    print('Process End')



@shared_task
def send_email_to_subs():
    email_lists = Newsletter.objects.values_list('email', flat=True)
    # productss = Product.objects.all()
    top_rated = Product.objects.annotate(Count("reviews"))
    product_emails = [i for i in top_rated if float(i.average_rating()) >= 3][:3]
    message = render_to_string('email-subscribers.html', {
            'product_emails' : product_emails,
            # 'productss' : productss
        })
    subject = 'Top rated Products for You'
    mail = EmailMultiAlternatives(subject=subject, body=message, from_email=settings.EMAIL_HOST_USER, to=email_lists)
    mail.content_subtype = 'html'
    mail.send(fail_silently=False)




@shared_task
def send_email_to_users():
    users = User.objects.all()
    top_rated = Product.objects.annotate(Count("reviews"))
    product_emails = [i for i in top_rated if float(i.average_rating()) >= 3][:5]
    # notify_users = []
    # for i in users:
    #     if i.last_login.month <= datetime.today().month:
    #         notify_users.append(i)
    notify_users = [i.email for i in users if i.last_login.month == datetime.today().month]
    message = render_to_string('email-subscribers.html', {
        'product_emails' : product_emails
    })
    subject = 'We observed that you do not visited to our website for 30 days. Top products for you!'
    mail = EmailMultiAlternatives(subject=subject, body=message, from_email=settings.EMAIL_HOST_USER, to=notify_users)
    mail.content_subtype = 'html'
    mail.send()
    

