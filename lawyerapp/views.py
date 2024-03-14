from django.shortcuts import render, redirect
from lawyerapp.models import Lawyer
from lawyerapp.forms import LawyerForm
from clientapp.models import Book_lawyer, Feedback

# Create your views here.


def lawyer_is_login(request):
    if request.session.__contains__("email"):
        return True
    else:
        return False


def lawyer_home(request):
    return render(request, "lawyer_home.html", {})


def lawyer_details(request):
    email = request.session["email"]
    lawyer = Lawyer.objects.get(email=email)
    print(email)
    return render(request, "lawyer_details.html", {"lawyer": lawyer})


def lawyer_change_password(request):
    if lawyer_is_login(request):
        if request.method == "POST":
            email = request.session["email"]
            password = request.POST["password"]
            newpassword = request.POST["newpassword"]
            try:
                user = Lawyer.objects.get(email=email, password=password)
                user.password = newpassword
                user.save()
                msg = 'password update successfully'
                return render(request, "lawyer_login.html", {"msg": msg})
            except:
                msg = 'invalid data'
                return render(request, "lawyer_change_password.html", {"msg": msg})
        return render(request, "lawyer_change_password.html", {})
    else:
        return render(request, "lawyer_login.html", {})


def lawyer_edit(request, email):
    lawyer = Lawyer.objects.get(email=email)
    return render(request, "lawyer_update.html", {"lawyer": lawyer})


def lawyer_update(request):
    if request.method == 'POST':
        email = request.POST["email"]
        lawyers = Lawyer.objects.get(email=email)
        form = LawyerForm(request.POST,request.FILES, instance=lawyers)
        print(form.errors)
        if form.is_valid():
            form.save()
        return render(request, 'lawyer_home.html', {"msg": "updated"})
    return render(request, 'lawyer_update.html', {})


def lawyer_delete(request, email):
    lawyer = Lawyer.objects.get(email=email)
    lawyer.delete()
    return redirect("/lawyer_registration")


def view_booking(request, email):
    lawyer = Book_lawyer.objects.filter(lawyer_id=email)
    return render(request, "view_booking.html", {"lawyer": lawyer})


def booking_approve(request, book_id):
    approve = Book_lawyer.objects.get(id=book_id)
    approve.status = 1
    approve.save()
    return redirect('/lawyer_details')


def booking_reject(request, book_id):
    reject = Book_lawyer.objects.get(id=book_id)
    reject.status = 2
    reject.save()
    return redirect('/lawyer_details')


def client_feedback(request):
    email = request.session["email"]
    feedback = Feedback.objects.filter(lawyer_id=email)
    return render(request, "client_feedback.html", {"feedback": feedback})


def lawyer_logout(request):
    if request.session.has_key('email'):
        del request.session['email']
    return render(request, "lawyer_login.html.", {"msg": ""})
