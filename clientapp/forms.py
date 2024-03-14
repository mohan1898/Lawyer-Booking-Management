from django import forms
from clientapp.models import Client, Book_lawyer, Feedback


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = "__all__"


class Book_lawyerForm(forms.ModelForm):
    class Meta:
        model = Book_lawyer
        fields = ('client', 'lawyer', 'description', 'date', 'time')


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = "__all__"