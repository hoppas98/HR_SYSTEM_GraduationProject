from django.urls import path, include
from accounts import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('accounts/', include('allauth.urls'),),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    # path('accounts/login/', auth_views.LoginView.as_view(template_name='screens/authenticate/login.html'),
    #      name='accounts/login'),
    path('profile', views.UserUpdateView.as_view(), name='profile'),

]
