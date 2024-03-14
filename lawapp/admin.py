from django.contrib import admin
from clientapp.models import *
from lawapp.models import Contact
from lawyerapp.models import *

# Register your models here.
admin.site.register(Client)
admin.site.register(Lawyer)
admin.site.register(Contact)