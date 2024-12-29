from django.shortcuts import render


def main_page(request):
    return render(request, 'main.html')

def poems_page(request):
    return render(request, 'poems.html')


def letters_page(request):
    return render(request, 'letters.html')

def map_page(request):
    return render(request, 'map.html')