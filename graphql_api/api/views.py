from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')


def category(request, pk):
    data={
        'pk':pk
    }
    return render(request, 'pages/ingrediant.html', data)

def ingredient(request):
    return render(request, 'pages/detail.html')