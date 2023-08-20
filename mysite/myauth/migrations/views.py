from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth import authenticate

def my_login(request):
    if request.method == "GET":
        return render(request, 'myauth/login.html')
    username = request.POST('username')
    password = request.POST('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request,user)
        return redirect("main-page")
    return render(request, 'myauth/login.html', {"error":"пользовател не найден"})

