"""lawfirm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from lawapp import views
from lawyerapp import views as l
from clientapp import views as c
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # main urls
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path('attorney/', views.attorney, name="attorney"),
    path('client_registration/', views.client_registration, name="client_registration"),
    path('client_reg/', views.client_reg, name="client_reg"),
    path('client_login/', views.client_login, name="client_login"),
    path('lawyer_registration/', views.lawyer_registration, name="lawyer_registration"),
    path('lawyer_reg/', views.lawyer_reg, name="lawyer_reg"),
    path('lawyer_login/', views.lawyer_login, name="lawyer_login"),

    # client
    path('client_home/', c.client_home, name="client_home"),
    path('client_details/', c.client_details, name="client_details"),
    path('client_change_password/', c.client_change_password, name="client_change_password"),
    path('client_logout/', c.client_logout, name="client_logout"),
    path('client_edit/<str:email>', c.client_edit, name="client_edit"),
    path('client_delete/<str:email>', c.client_delete, name="client_delete"),
    path('client_update/', c.client_update, name="client_update"),
    path('book_lawyer/<str:pk>', c.book_lawyer, name="book_lawyer"),
    path('client_lawyers/', c.client_lawyers, name="client_lawyers"),
    path('booked/', c.booked, name="booked"),
    path('feedback/<int:id>', c.feedback, name="feedback"),

    # lawyer
    path('lawyer_home/', l.lawyer_home, name="lawyer_home"),
    path('lawyer_details/', l.lawyer_details, name="lawyer_details"),
    path('lawyer_change_password/', l.lawyer_change_password, name="lawyer_change_password"),
    path('lawyer_logout/', l.lawyer_logout, name="lawyer_logout"),
    path('lawyer_edit/<str:email>',l.lawyer_edit, name="lawyer_edit"),
    path('lawyer_delete/<str:email>', l.lawyer_delete, name="lawyer_delete"),
    path('lawyer_update/', l.lawyer_update, name="lawyer_update"),
    path('view_booking/<str:email>', l.view_booking, name="view_booking"),
    path('booking_approve/<str:book_id>', l.booking_approve, name="booking_approve"),
    path('booking_reject/<str:book_id>', l.booking_reject, name="booking_reject"),
    path('client_feedback/', l.client_feedback, name="client_feedback"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
