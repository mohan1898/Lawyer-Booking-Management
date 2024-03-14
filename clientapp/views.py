from django.shortcuts import render, redirect
from clientapp.models import Client, Book_lawyer
from clientapp.forms import ClientForm, Book_lawyerForm,  FeedbackForm
from lawyerapp.models import Lawyer


# Create your views here.


def client_is_login(request):
    if request.session.__contains__("email"):
        return True
    else:
        return False


def client_home(request):
    return render(request, "client_home.html", {})


def client_details(request):
    email = request.session["email"]
    client = Client.objects.get(email=email)
    print(email)
    return render(request, "client_details.html", {"client": client})


def client_change_password(request):
    if client_is_login(request):
        if request.method == "POST":
            email = request.session["email"]
            password = request.POST["password"]
            newpassword = request.POST["newpassword"]
            try:
                user = Client.objects.get(email=email, password=password)
                user.password = newpassword
                user.save()
                msg = 'password update successfully'
                return render(request, "client_login.html", {"msg": msg})
            except:
                msg = 'invalid data'
                return render(request, "client_change_password.html", {"msg": msg})
        return render(request, "client_change_password.html", {})
    else:
        return render(request, "client_login.html", {})


def client_edit(request, email):
    client = Client.objects.get(email=email)
    return render(request, "client_update.html", {"client": client})


def client_update(request):
    if request.method == 'POST':
        email = request.POST["email"]
        client = Client.objects.get(email=email)
        form = ClientForm(request.POST, instance=client)
        print(form.errors)
        if form.is_valid():
            form.save()
        return render(request, 'client_home.html', {"msg": "updated"})
    return render(request, 'client_update.html', {})


def client_delete(request, email):
    client = Client.objects.get(email=email)
    client.delete()
    return redirect("/client_registration")


def client_lawyers(request):
    lawyers = Lawyer.objects.all()
    return render(request, "client_lawyers.html", {"lawyers": lawyers})


def book_lawyer(request, pk):
    email = request.session["email"]
    client = Client.objects.get(email=email)
    lawyer = Lawyer.objects.get(pk=pk)
    if request.method == 'POST':
        form = Book_lawyerForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "book_lawyers.html", {"client": client.email, "lawyer": lawyer.email})
    return render(request, "book_Lawyers.html", {"client": client.email, "lawyer": lawyer.email})


def booked(request):
    email = request.session["email"]
    client = Client.objects.get(email=email)
    form = Book_lawyer.objects.filter(client_id=client.email)
    return render(request, "booked.html", {"forms": form, "client": client})


def feedback(request, id):
    email = request.session['email']
    client = Client.objects.get(email=email)
    book = Book_lawyer.objects.get(id=id)
    if request.method == "POST":
        booked = FeedbackForm(request.POST)
        print(booked.errors)
        if booked.is_valid():
            booked.save()
        return render(request, "feedback.html", {"msg": "thanks for your feedback", "booked": booked, 'customer': client, "client": book.client_id, "book": book.lawyer_id})
    return render(request, "feedback.html", {"client": book.client_id,  'customer': client, "book": book.lawyer_id})


def client_logout(request):
    if request.session.has_key('email'):
        del request.session['email']
    return render(request, "client_login.html.", {"msg": ""})

