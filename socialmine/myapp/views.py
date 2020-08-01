from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User

from .models import user
# Create your views here.
def login(request):
    return render(request,'login.html')

def sign(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        male = request.POST.get('male')
        gender = "M"
        if(male == 'off'):
            gender="F"
        dob = request.POST.get('dob')
        password = request.POST.get('pass')
        obj = user.objects.all()
        if (not (len(user.objects.filter(name=name))==1 and len(user.objects.filter(email=email))==1)):
            u = User.objects.create_user(uname, email,password)
            u.save()
            NewUser = user(name= name, uname=uname,email=email,dob=dob,password =password,gender=gender)
            NewUser.save()
            return HttpResponse("<script>alert('account created successfully')</script>")
        return HttpResponse("<script>alert('account already exists Please try different details')</script>")
        

            

