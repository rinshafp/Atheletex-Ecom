from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from . models import Customer
# Create your views here.

def sign_out(request):
    logout(request)
    return redirect('home')

def show_account(request):
    context={}
    if request.POST and 'register' in request.POST:
        context['register']=True
        try:
           username=request.POST.get('username')
           password=request.POST.get('password')
           email=request.POST.get('email')
           address=request.POST.get('address')
           phone=request.POST.get('phone')
           # creates user account
           user=User.objects.create_user(
               username=username,
               password=password,
               email=email
           )
           #creates customer account
           customer=Customer.objects.create(
               name=username,
               user=user,
               phone=phone,
               address=address
           )
           success_message=" User Registered Successfully"
           messages.success(request,success_message)
        except Exception as e:
            error_message="invalid inputs or username"
            messages.error(request,error_message)
    # if request.POST and 'login' in request.POST:
    #     context['register']=False
    #     print(request.POST)
    #     username=request.POST.get['username']
    #     password=request.POST.get['password']
    #     print(username,password)
    #     user=authenticate(username=username,password=password)
    #     print(user)
    #     if user:
    #         login(request, user)
    #         return redirect('home')
    #     else:
    #         messages.error(request,'invalid user credentials')

    # return render(request,'account.html',context)

    if request.POST and 'login' in request.POST:
          context['register'] = False
          print("Form submitted:", request.POST)
    username = request.POST.get('username')
    password = request.POST.get('password')
    print("Credentials:", username, password)
    user = authenticate(username=username, password=password)
    print("Authenticated User:", user)
    if user:
        print("User authenticated successfully. Logging in...")
        login(request, user)
        return redirect('home')
    else:
        # print("Invalid credentials.")
        # messages.error(request, 'Invalid user credentials')

        print("Rendering account.html")
    return render(request, 'account.html', context)



