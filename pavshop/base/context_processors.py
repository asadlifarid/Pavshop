# context processors are used to objects global

from base.forms import NewsletterForm
from base.models import Newsletter
from django.shortcuts import redirect


# from django.views.generic import CreateView


def newsletter_context(request):
   
    form = NewsletterForm()  # burda da deyirik ki, form'u bos gotur evvelden
    print('newsletter2222222222222')
    if request.method == 'POST':
        form = NewsletterForm(data=request.POST)
        print('newsletter11111')
        # print('form is here')
        if form.is_valid():
            print('form is valid')
            form.save()
            form = NewsletterForm()  # formu save etdikden sonra formu sifirla; eks halda tekrar emailler gonderir; ve bir nuans olaraq, sheifeni refresh edende win + R ile deyil, brauzerde linke basib Enter etmek lazim, ki tekrar gondermesin
   
            
            
    return {
        'letterform' : form
    }


