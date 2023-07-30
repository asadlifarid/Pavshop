# this python module has been designed for app URLs. That is called informally URLconf;
from django.urls import path, re_path, include

from authentication.views import login_page, logout_page, success_page, register_page, profiles, activate, UserLoginView, RegisterView, UserLogoutView, ProfileView
from django.contrib.auth import views as auth_views



urlpatterns = [
    # path('login/', login_page, name='login_page'),
    path('login/', UserLoginView.as_view(), name='login_page'),
    # path('logout/', logout_page, name='logout_page'),
    path('logout/', UserLogoutView.as_view(), name='logout_page'),

    # path('register/', register_page, name='register_page'),
    path('register/', RegisterView.as_view(), name='register_page'),

    path('register/success_page/',success_page, name='success_page'),
    # path('profile/', profiles, name='profiles'),
    path('profile/', ProfileView.as_view(), name='profiles'),

    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,33})/$',
        activate, name='activate'),
    path('social-auth/', include('social_django.urls', namespace="social")),


    path('password-reset/', 
        auth_views.PasswordResetView.as_view(template_name='passwords/password_reset.html', 
        html_email_template_name='passwords/password_reset_email.html'), name='password_reset'),

    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='passwords/password_reset_done.html'), name='password_reset_done'),

    
    path('password-reset-confirm/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name='passwords/password_reset_confirm.html'), 
        name='password_reset_confirm'),

    path('password-reset-complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name='passwords/password_reset_complete.html'),
        name='password_reset_complete'),

    path('password-change/', 
        auth_views.PasswordChangeView.as_view(template_name='passwords/password_change_form.html'), 
        name='password_change')
    
    
]

