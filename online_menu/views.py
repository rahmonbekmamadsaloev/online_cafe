from django.shortcuts import render ,redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout



def all_list_views (request):
   dish = Dish.objects.all()
   return render (request, 'home.html', context={"data":dish})



def register(request):
   if request.method == 'GET':
        return render(request, 'register.html')
     
   elif request.method == 'POST':
      name = request.POST.get('name')
      surname = request.POST.get('surname')
      username = request.POST.get('username')
      email = request.POST.get('email')
      password = request.POST.get('password')
      confirmPassword = request.POST.get('confirmPassword')

      if not username or not password or not confirmPassword or not email:
            return HttpResponse('ALL FIELDS ARE REQUIRED !!!')

      if password != confirmPassword:
            return HttpResponse("Passwords don't match!")

      if User.objects.filter(username=username).exists():
            return HttpResponse("Username already taken!")

      user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=name,
            last_name=surname
        )
      return redirect ('login')
   
   
def login_view(request):
    if request.method == 'GET':
        return render (request, 'login.html')
    
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect ('all_list_views')
        else:
            return HttpResponse('Invalid username or password')
         
         
      

def logout_view (request):
    logout(request)
    return redirect ('login')
 
 
 

def order_view(request):
    if not request.user.is_authenticated:
        return HttpResponse('Вы должны быть авторизованы, чтобы сделать заказ!')
     
    if request.method == 'GET':
        return render(request, 'order.html')

   
    if not request.user.is_authenticated:
        return HttpResponse('Вы должны быть авторизованы, чтобы сделать заказ!')

    if request.method == 'POST':
        name = request.POST.get('name')
        des = request.POST.get('des')
        day = request.POST.get('day')
        adres = request.POST.get('adres')

        if not name or not adres:
            return HttpResponse('ALL FIELDS ARE REQUIRED !!!')

        Order.objects.create(
            name=request.user,
            des=des,
            created_add=day,
            adres=adres
        )

        return HttpResponse('Заказ принят')

