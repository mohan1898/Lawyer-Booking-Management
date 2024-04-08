from django.shortcuts import render
from lawapp.models import Contact
from lawapp.forms import ContactForm
from clientapp.models import Client, Feedback
from clientapp.forms import ClientForm
from lawyerapp.models import Lawyer
from lawyerapp.forms import LawyerForm


# Create your views here.

def index(request):
    feedback = Feedback.objects.all()
    return render(request, "index.html", {"feedback": feedback})


def about(request):
    feedback = Feedback.objects.all()
    return render(request, "about.html", {"feedback": feedback})


def attorney(request):
    return render(request, "attorney.html", {})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            return render(request, "contact.html", {"msg": "message sent"})
    return render(request, "contact.html", {})


def client_registration(request):
    return render(request, "client_registration.html", {})


def client_reg(request):
    if request.method == 'POST':
        print("hi")
        email = request.POST['email']
        if Client.objects.filter(email=email).exists():
            print("email taken")
            return render(request, "client_registration.html", {"msg": "email already exists"})
        else:
            form = ClientForm(request.POST)
            print(form.errors)
            if form.is_valid():
                form.save()
                return render(request, "client_registration.html", {"msg": "inserted sucess", "form": form})
            else:
                return render(request, "client_registration.html", {})
    else:
        client = ClientForm()
        return render(request, "client_registration.html", {"msg": "", "form": client})


def client_login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        print(email, "", password)
        user = Client.objects.filter(email=email, password=password,)
        if user.exists():
            request.session['email'] = email
            return render(request, "client_home.html", {"msg": email})
        else:
            return render(request, "client_login.html", {"msg": "email or password is not exist"})
    return render(request, "client_login.html", {"msg": ""})


def lawyer_registration(request):
    return render(request, "lawyer_registration.html", {})


def lawyer_reg(request):
    if request.method == 'POST':
        print("hi")
        email = request.POST['email']
        if Lawyer.objects.filter(email=email).exists():
            print("email taken")
            return render(request, "lawyer_registration.html", {"msg": "email already exists"})
        else:
            form = LawyerForm(request.POST, request.FILES)
            print(form.errors)
            if form.is_valid():
                form.save()
                return render(request, "lawyer_registration.html", {"msg": "inserted sucess", "form": form})
            else:
                return render(request, "lawyer_registration.html", {})
    else:
        lawyer = LawyerForm()
        return render(request, "lawyer_registration.html", {"msg": "", "form": lawyer})


def lawyer_login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        print(email, "", password)
        user = Lawyer.objects.filter(email=email, password=password,)
        if user.exists():
            request.session['email'] = email
            return render(request, "lawyer_home.html", {"msg": email})
        else:
            return render(request, "lawyer_login.html", {"msg": "email or password is not exist"})
    return render(request, "lawyer_login.html", {"msg": ""})
