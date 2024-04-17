from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import SignInForm
from django.shortcuts import render
def main(request):
    return render(request, 'index.html'

    )
def signin_view(request):
    if request.method == 'POST':



        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)


            return HttpResponseRedirect(reverse('main:main'))



    return render(request, 'login.html' )
# Create your views here.
