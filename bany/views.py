from django.shortcuts import render

def get_page1(request):
    return render(request, 'page1.html')
