from django.urls import path,include
from . import views
from django.contrib.auth.views import (
   
     PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('', views.home,name='home'),
    path('signup', views.signup,name='signup'),
    path('signin', views.signin,name='signin'),
    path('signout/', views.signout,name='signout'),  
    path('profile/', views.profile,name='profile'),
     path('posts/', views.all_posts, name='all_posts'),
     path('password-reset/', PasswordResetView.as_view(template_name='app/password_reset_form.html'),name='password-reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'),name='password_reset_complete'),
  
      path('change-password/', views.change_password,name='change_password'),
    
      path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/like/', views.like_post, name='like_post'),
    path('post/<int:post_id>/dislike/', views.dislike_post, name='dislike_post'),
    path('post/<int:post_id>/comment/', views.add_comment, name='add_comment'),
    path('create_post', views.create_post,name='create'),
path("about",views.company_page,name="company_page"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)