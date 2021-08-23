from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views
from .forms import *
urlpatterns = [
     path('', views.student_login_view, name='login'),
    path('signup/', views.student_signup_view, name='signup'),
    path('profile/', views.profile_view),
    path('logout/', views.user_logout, name="logout"),
    path('delete_view/<int:id>/',views.delete_view, name="deleteUser"),
    path('visitProfile/', views.user_profile, name='visitProfile'),
    path('viewResume/<int:id>/', views.resume_view, name='resumeView'),
    path('updateProfile/<int:id>/', views.update_profile, name="updateProfile"),
    path('changePassword/', views.change_password, name="changePassword"),
    path('updateEmail/', views.update_email, name="updateEmail"),
    path('password-Reset/', auth_views.PasswordResetView.as_view(template_name='password_Reset.html', form_class=MyPasswordResetForm), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
