from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from accounts import forms
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy


# Create your views here.

@login_required
def open_profile(request):
    return render(request, 'authenticate/profile.html')


def signup(request):
    form = forms.UserForm()
    if request.method == 'POST':
        form = forms.UserForm(request.POST)

        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('index')

    return render(request, 'screens/authenticate/signup.html', {'form': form})


class UserUpdateView(UpdateView):
    model = User
    fields = ('first_name', 'last_name')
    template_name = 'screens/authenticate/profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user
