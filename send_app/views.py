import imp
from django.shortcuts import render
from django.core.mail import send_mail
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
        #message1 = f'new message: {message} from:{email}'
        message1 = '''
        new message: {}

        from: {}
        '''.format(data['message'], data['email'])
        
        send_mail(data['subject'], message1, '', ['example@gmail.com']) # here in "example@gmail.com" you have to put the email where you want to send the email
    return render(request, "index.html")