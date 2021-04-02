from django.shortcuts import render


def index(request):
    context = {
        "message": "Hello World! added manual review"
    }
    return render(request, 'hello_world/index.html', context)
