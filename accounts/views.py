from .forms import UserForm, UserProfileForm
from django.shortcuts import render

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            #.set_password hashes the password
            user.set_password(user.password)
            user.save()
            registered = True

        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'accounts/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )
