from django.contrib import admin
from . models import Subject, Mentor, Booking


admin.site.register(Subject)
admin.site.register(Mentor)
class BookingAdmin(admin.ModelAdmin):
    list_display=('id','s_name','s_phone','s_email','men_name','booking_date','booked_on')
admin.site.register(Booking,BookingAdmin)