from django.shortcuts import render


def about(request):
    """Страница описания проекта."""
    template_name = 'pages/about.html'
    return render(request, template_name, {})


def rules(request):
    """Страница с правилами проекта."""
    template_name = 'pages/rules.html'
    return render(request, template_name, {})
