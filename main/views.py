from multiprocessing import context
from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, Http404, redirect
from django.views.generic import View

# Импорты для системы аутентификации
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

from .models import *

class Index(View):
    def get(self, request):

        things = Thing.objects.all()

        return render(request, "index.html", context={
            'things': things
        })

class Registration(View):
    def get(self, request):
        form = UserCreationForm()

        return render(request, 'registration/registration.html', context={
            'form': form,
        })

    def post(self, request):
        form = UserCreationForm(data=request.POST or None)

        if form.is_valid():
            u_name = form.cleaned_data.get('username')
            u_pass = form.cleaned_data.get('password2')

            form.save()

            user = authenticate(
                username=u_name,
                password=u_pass
            )

            # Логиним пользователя после успешной регистрации
            login(request, user)

            return redirect('index')

        return render(request, 'registration/registration.html', context={
            'form': form,
        })