from django.conf import settings
from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from blogs.models import *

from django.db.models import Count

# from django.core.exceptions import ValidationError


from social_django.models import UserSocialAuth


from django.contrib.auth import get_user_model

User = get_user_model()


# activation
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from authentication.tokens import account_activation_token



from django.utils.http import urlsafe_base64_decode
from authentication.tokens import account_activation_token
from django.utils.encoding import force_str


from django.core.mail import EmailMultiAlternatives


# Generic Views import'lar
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordChangeView
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin



# Create your views here.
def login_page(request):
    next_page = request.GET.get('next', reverse_lazy('login_page'))
    form = LoginForm()
    if request.method =='POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(request=request, username = form.cleaned_data['username'], password = form.cleaned_data['password'])
            if not user:
                messages.add_message(request, messages.ERROR, "User not found")
                """ redirect'mizi root'a gore teyin edirik; root'da next deyisen varsa, onun qarsiligini qaytarsin, value yeni, yoxdursa, reverse_lazy icindeki deyere qaytarsin, yeni login-page  """
                return redirect(next_page)  
            login(request, user)
            return redirect(reverse_lazy('profiles'))   # sonra redirect'i deyis, product sehifeye gonder
    context = {
        'loginform':form
    }
    return render(request, 'login.html', context=context)




class UserLoginView(LoginView):
    template_name = 'login.html'
    form_class = LoginForm
   
    

    # success_url = reverse_lazy('profiles')
    

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "User not found!  Password or Username is wrong")
        return redirect('login_page')
    
    
    def get_default_redirect_url(self):
        """Return the default redirect URL."""
        if self.next_page:
            return resolve_url('profiles')
        else:
            return resolve_url(settings.LOGIN_REDIRECT_URL)
    
  
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["next_page"] = self.request.GET.get('next', reverse_lazy('login_page'))
    #     return context
    

    
    # def form_valid(self, form):
    #     user = authenticate(self.request==self.request, username = form.cleaned_data['username'], password = form.cleaned_data['password'])
    #     if not user:
    #         messages.add_message(request, messages.ERROR, "User not found")
    #         return redirect(next_page)  
    #     login(self.request, user)
    #     return redirect(reverse_lazy('profiles'))
    


 



# Create your views here.
def logout_page(request):
    logout(request)
    return redirect('login_page')


# Generic LogOut View
class UserLogoutView(SuccessMessageMixin, LogoutView):
    def get(self, request):
        logout(request)
        success_message = "You're logged out!"
        return redirect('login_page')




# Create your views here.
def success_page(request):
    return render(request, 'success_page.html')





# Create your views here.
def register_page(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(data = request.POST, files=request.FILES)
        if form.is_valid():
            user = form.save(commit=False)

            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            # return redirect('home')

            # messages.add_message(request, messages.SUCCESS, 'SUCCESS')
            return redirect('success_page')
        
    context = {
        'form' : form
    }

    return render(request, 'register.html', context=context)




# Generic Register View
class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    # success_url = reverse_lazy('success_page')


   
    def form_valid(self, form):
        user = form.save(commit=False)
        # user.is_active = False
        # user.save()
        # form.instance.username = self.request.user

        current_site = get_current_site(self.request)
        subject = 'Activate Your Pavshop Account'
        message = render_to_string('account_activation_email.html', {
            'user': self.request.user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        mail = EmailMultiAlternatives(subject=subject, body=message, from_email=settings.EMAIL_HOST_USER, to=[user.email, ])
        mail.content_subtype = 'html'
        mail.send()

        return redirect(reverse_lazy("success_page"))









# Create your views here.
@login_required(login_url='login_page')
def profiles(request):
    
    # google_logins = UserSocialAuth.objects.select_related('user').filter(provider="google-oauth2")
    # print(google_logins)
    # for google_login in google_logins:
    #     print(google_login.user.id, google_login.user.email)

    storys = Story.objects.filter(author = request.user.id)
    storys_count = storys.count()

    context = {
        'storys' : storys,
        'storys_count' : storys_count
    }
    return render(request, 'user-profile.html', context=context)



# Generic Profil View
class ProfileView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'user-profile.html'
    context_object_name = 'storys'
    # success_url = reverse_lazy('profile')
    # success_message = "Success! You are'logged in your profile!"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["storys"] = Story.objects.filter(author = self.request.user.id)
        context["storys_count"] = context["storys"].count
        return context
    




# Generic Passwords Views
class PasswordResetView(SuccessMessageMixin, PasswordResetView):
    template_name = "password_reset.html"
    email_template_name = "password_reset_email.html"
    subject_template_name = "password_reset_subject"
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('home')




class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'passwords/password_change_form.html'
    success_message = 'Sucessfully Changed Your Password'
    success_url = reverse_lazy('login_page')







def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('login_page')
    else:
        return render(request, 'account_activation_invalid.html')