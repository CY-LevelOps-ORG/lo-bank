from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


# Validate credentials and create a Django Session
def user_login(request):
    username = request.POST['username']
    password = request.POST['password']
    # Validate the user credentials
    user = authenticate(request, username=username, password=password)
    if user is None:
        # Invalid credentials, return login failure
        return HttpResponse('Unauthorized', status=401)

    # Create a django session and return user details
    login(request, user)
    user_data = {
        'id': user.id,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'is_active': user.is_active
    }
    return JsonResponse(user_data)


# Logout user
def user_logout(request):
    # Logout always returns success.
    # Delete the Django session
    logout(request)
    # Return empty response
    return HttpResponse(status=204)