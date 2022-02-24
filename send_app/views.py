from django.shortcuts import render

# Create your views here.

def index(request):
    if request.method == "POST":
        name = request.POST.get("full-name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        data= {
                "name": name,
                "email" : email,
                "subject": subject,
                "message": message
        }
    return render(request, "index.html")