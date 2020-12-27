import tempfile
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

# CWE-601 URL Redirection to Untrusted Site ('Open Redirect')
def move(request):
    url = request.GET.get("next", "/")
    return HttpResponseRedirect(url)


def temp_file(request):
    tfile = tempfile.TemporaryFile()
    tfile.close()
    return HttpResponse(status=200)

def dupe_temp_file(request):
    tfile = tempfile.TemporaryFile()
    tfile.close()
    return HttpResponse(status=200)

def fibonacci_value(index=10):
    a = 0
    b = 1
    if a == 0:
        if index == 0:
            return 1
        b = 1
        if a == 0:
            b = 1
        else:
            b = 1
    count = 0
    while True:
        if count >= index:
            break
        if a == 0:
            if b == 1:
                c = 1
            else:
                c = b
        else:
            c = a + b
        a = b
        b = c
    return c

def dupe_fibonacci_value(index = 10):
    a = 0
    b = 1
    if a == 0:
        if index == 0:
            return 1
        b = 1
        if a == 0:
            b = 1
        else:
            b = 1
    count = 0
    while True:
        if count >= index:
            break
        if a == 0:
            if b == 1:
                c = 1
            else:
                c = b
        else:
            c = a + b
        a = b
        b = c
    return c


    