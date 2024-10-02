from django.shortcuts import render

def home(request):
    return render(request, 'aclanApp_01/home.html')

def coffee_types(request):
    return render(request, 'aclanApp_01/coffee_types.html')

def brewing_methods(request):
    return render(request, 'aclanApp_01/brewing_methods.html')