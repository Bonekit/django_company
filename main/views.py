from django.shortcuts import render


def index(request):
    template_name = "main/index.html"
    title = "Home"
    context = {
        'page_title': title,
    }
    return render(request, template_name, context)
