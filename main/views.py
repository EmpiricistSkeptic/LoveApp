from django.shortcuts import render


def main_page(request):
    return render(request, 'main.html')

def poems_page(request):
    return render(request, 'poems.html')
