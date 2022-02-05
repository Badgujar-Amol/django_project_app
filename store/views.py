from django.shortcuts import render

def signin(request):
    context = {}
    return render(request,'store/signin.html',context)

def ecom(request):
    context = {}
    return render(request,'store/ecom.html',context)

def card(request):
    context = {}
    return render(request,'store/card.html',context)

