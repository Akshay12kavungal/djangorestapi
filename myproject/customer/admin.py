from django.contrib import admin
from .models import Departments,Doctors,Booking,Contact,Profile

# Register your models here.
class DepartmentsAdmin(admin.ModelAdmin):
    list_display=('dep_name','dep_description')
admin.site.register(Departments,DepartmentsAdmin)


class DoctorAdmin(admin.ModelAdmin):
    list_display=('doc_name','doc_spec','dep_name','doc_name','dep_image')
admin.site.register(Doctors,DoctorAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display=('name','email','message')
admin.site.register(Contact,ContactAdmin)

class BookingAdmin(admin.ModelAdmin):
    list_display=('id','p_name','p_email','doc_name','booking_date','booked_on')
admin.site.register(Booking,BookingAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display=('user','first_name','last_name','phone_number','email','profile_pic')

admin.site.register(Profile,ProfileAdmin)

