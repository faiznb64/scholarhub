from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index, name='home' ),
    path('about/',views.about, name='about'),
    path('booking/',views.booking, name='booking'),
    path('mentor/',views.mentor, name='mentor'),
    path('contact/',views.contact, name='contact'),
    path('subject/',views.subject, name='subject'),

]
