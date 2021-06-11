
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm

# Create your views here.


def user_login(request):

    if request.method == 'POST':
        # POST IS THE BODY INFO OF A HTTP REQUEST POST
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Aunthenticated succesfully')

            else:
                return HttpResponse('Disable account')

        else:
            return HttpResponse('Invalid login')

    else:
        form = LoginForm()

    return render(request, 'account/login.html', {'form': form})
