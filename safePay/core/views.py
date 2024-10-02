from django.shortcuts import render 

def index(request):
    return render(request, 'core/landing_page.html')

def about_us(request):
    return render(request, 'core/about_us.html')


def contact_us(request):
    return render(request, 'core/contact_us.html')