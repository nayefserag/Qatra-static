from .views import * 
from django.urls import path ,include 
from django.contrib.auth import views
from django.views.generic import TemplateView



from django.contrib.auth.views import (
    LogoutView, 
    LoginView,
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns = [
    path('Home/', home , name = 'home'),
    path('login/', loginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='Sginin/logout.html'), name='logout'),
    path('SignUpBB/',Sginup),
    

    ##
    path('accounts/', include('allauth.urls') ,name='accounts'),
    path('auth/', include('social_django.urls', namespace='social')),
    ##

    path('password-reset/', views.PasswordResetView.as_view(template_name='Reset/password_reset_form.html'), name='password_reset'),
    path('password-reset/done/', views.PasswordResetDoneView.as_view(template_name='Reset/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(template_name='Reset/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', views.PasswordResetCompleteView.as_view(template_name='Reset/password_reset_complete.html'), name='password_reset_complete'),
]   



