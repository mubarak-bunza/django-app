from django.shortcuts import render


def index(request):
    context = {
        "message": "Hello World! edited"
    }
    return render(request, 'hello_world/index.html', context)
