from .forms import LoginForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View

class LoginView(View):
    form_class = LoginForm
    template_name = 'accounts/login.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, { 'form': form })

    def post(self, request):
        form = self.form_class(None, request.POST)

        if form.is_valid():
            print('valid working')
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('movies.dashboard')
                else:
                    return HttpResponse("Inactive user.")

        return render(request, self.template_name, { 'form': form })

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('accounts.login')

class RegisterView(View):
    form_class = LoginForm
    template_name = 'accounts/register.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, { 'form': form })

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            # create obj from form, don't save yet.
            user = form.save(commit=False)
            # cleaned (formatted) data, hash password, and save
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User object if credentials are correct
            user = authenticate(username=username, password=password)

            # Check if in database
            if user is not None:
                # Account is okay
                if user.is_active:
                    login(request, user)
                    return redirect('movies.dashboard')

        return render(request, self.template_name, { 'form': form })
