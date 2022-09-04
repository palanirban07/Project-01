from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from app.models import Profile,Logger
from app.forms.profile_form import ProfileForm

def register_user(request):
    if request.method == "POST":
        data = request.POST
        profile = Profile()
        user = User()
        forms = ProfileForm(data)
        if forms.is_valid():
            profile.name = data.get('name')
            profile.email = data.get('email')
            profile.mobile = data.get('mobile')
           
            user.username = data.get('email')
            user.set_password(data.get("password"))
            user.save()
           
            profile.user_id = user.id
            profile.save()
            return redirect('home')
        else:
            print('error',forms.errors.as_data())
           
    return render(request, 'pages/register.html')