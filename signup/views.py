from django.shortcuts import render, redirect
from django.db import connection

def signup_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')

        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO signup_userss (email, phone_number) VALUES (%s, %s)", [email, phone_number])

        return redirect('success')
    
    return render(request, 'signup/signup.html')

def success_view(request):
    return render(request, 'signup/success.html')
