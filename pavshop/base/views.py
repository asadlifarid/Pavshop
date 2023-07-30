from django.conf import settings
from django.http import HttpResponseRedirect, request
from django.shortcuts import render, redirect

from django.core.exceptions import ValidationError


from .models import Contact, Team, Sponsor, Newsletter
from .forms import ContactForm, NewsletterForm
from products.models import *
from base.models import AbstractModel

# Additional features for languages(en-az)
from django.urls import reverse_lazy   # dil deyisimi ucun, REDIRECT edende az->en etmesin, az->az etsin meselen

# Additional features for error/ success messages
from django.contrib import messages

from django.core.mail import send_mail
from blogs.models import Story

from datetime import datetime, date



# Genereic Views imports here
from django.views.generic import CreateView, TemplateView, ListView, View
from django.views.generic.detail import SingleObjectMixin


from django.utils.translation import gettext_lazy as _  



# Create your views here.
def base_page(request):
    # products = Product.objects.annotate(Count("reviews"))
    # rate_list = []

    # for i in products:
    #     if float(i.average_rating()) >= 3:
    #         rate_list.append(i)

    # print(rate_list)

    # context = {
    #     'products' : products,
    #     'rate_list' : rate_list
    # }

    return render(request, "base.html")



# class NewsletterView(CreateView):
#     # model = Newsletter
#     form_class = NewsletterForm
#     # success_url = reverse_lazy('thanks_page')


#     def form_valid(self):
#         return super().form_valid(form)


#     def form_invalid(self, form):
#         # messages.add_message(self.request, messages.ERROR, _('ERROR'))
#         return self.render_to_response(self.get_context_data(form=form))








def contact_page(request):
    form = ContactForm()

    if request.method == 'POST':
        print('POST olunud')
        form = ContactForm(data=request.POST)
        print('form sent')
        if form.is_valid():
            print('form valid')
            form.save()
            messages.add_message(request, messages.SUCCESS, 'SUCCESS')
            # eger cari oldugumuz sehife az dilinde ise, redirect verdikde dil deyisimi olmasin deye reverse_lazy() istifade olunur

            send_mail(
                subject=f"First of all, thank you for contacting us, {request.user.username}.", 
                message=f"\n\nHelp is on the way! Our team of Customer Care specialists is already working on your request and we will be back in the shortes time possible ( but no lates than 24 hours! ).\n\n\nIf your issue is urgent, please don't hesitate to contact us via our web chat. We really appreciate your patience, and we're working to improve your experience with us.\n\n\n\n\nGood day!", 
                from_email=settings.EMAIL_HOST_USER, 
                recipient_list=["parvanayva@gmail.com", "pyva0055@gmail.com"], 
                fail_silently=False,
            )
            return redirect(reverse_lazy('thanks_page'))  # redirect(reverse_lazy) imkan verir ki, redirect verdikde bele dil deyisimi olmasin;
            


    context = {
        'form' : form
    }


    # print(context)
    
    return render(request, 'contact.html', context)
    


# Contact 1 form generate etdiyi ucun CreateView istifade edirik
class ContactView(CreateView):   # inherit alir CreateView'dan
    # model = Contact
    # fields = '__all__'
    form_class = ContactForm  # bizim yaratdigimiz form olsun deyirik, ozu generate etdiyi yox
    template_name = 'contact.html'
    success_url = reverse_lazy('thanks_page')

    
    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, _('SUCCESS'))
        send_mail(
                subject=f"First of all, thank you for contacting us, {self.request.user.username}.", 
                message=f"\n\nHelp is on the way! Our team of Customer Care specialists is already working on your request and we will be back in the shortes time possible ( but no lates than 24 hours! ).\n\n\nIf your issue is urgent, please don't hesitate to contact us via our web chat. We really appreciate your patience, and we're working to improve your experience with us.\n\n\n\n\nGood day!", 
                from_email=settings.EMAIL_HOST_USER, 
                recipient_list=["parvanayva@gmail.com", "pyva0055@gmail.com"], 
                fail_silently=False,
            ),
        send_mail(
            subject=self.request.POST.get('subject').split(),
            message=f"Contact details:\n{Contact.objects.filter(created_at__month = datetime.today().month).last()}\n\n\nMessage detail: {self.request.POST.get('message')}",
            from_email=self.request.user.email,
            recipient_list=['parvanayva@gmail.com']
            
        
        )

        return super().form_valid(form)

    
    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, _('ERROR'))
        return self.render_to_response(self.get_context_data(form=form))








def thanks_page(request):
    return render(request, 'thanks-contact.html')



def about_us_page(request):
    teams = Team.objects.all()
    sponsors = Sponsor.objects.all()

    context = {
        'teams' : teams,
        'sponsors' : sponsors,
    }
    
    return render(request, 'about-us.html', context)



class AboutView(TemplateView):
    template_name = 'about-us.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["teams"] = Team.objects.all()
        context["sponsors"] = Sponsor.objects.all()
        context["top_rated"] = Product.objects.annotate(Count("reviews"))
        context["rate_list"] = [i for i in context["top_rated"] if float(i.average_rating()) >= 3][:3]
        return context
    





def home(request):
    products = Product.objects.all()[:8]
    all_products = Product.objects.filter(money__gte=100).all()


    context = {
        'products' : products,
        'all_products' : all_products,
    }

    return render(request, 'index.html', context)



class HomeView(TemplateView):
    template_name = 'index.html'



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.all()[:8]
        context["all_products"] = Product.objects.filter(money__gte=100).all()
        # products = Product.objects.annotate(Count("reviews"))
        context["top_rated"] = Product.objects.annotate(Count("reviews"))
        context["rate_list"] = [i for i in context["top_rated"] if float(i.average_rating()) >= 3][:3]

        return context


    # rate_list = []

    # for i in products:
    #     if float(i.average_rating()) >= 3:
    #         rate_list.append(i)

    # print(rate_list)

    # context = {
    #     'products' : products,
    #     'rate_list' : rate_list
    # }
     

