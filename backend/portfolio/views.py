from django.shortcuts import render
from .models import ContactMessage


def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )

    return render(request, 'portfolio/index.html')
# Create your views here.
