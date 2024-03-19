from django.contrib import admin

# Register your models here.
from .models import Attendance,Category,Subcategory,CarModel, Booking,Type,Feedback,Customer,Mechanic,Blog,Payment,ItemPrice

admin.site.register(Customer)
admin.site.register(Attendance)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(CarModel)
admin.site.register(Booking)
admin.site.register(Type)
admin.site.register(Feedback)
admin.site.register(Mechanic)
admin.site.register(Blog)
admin.site.register(Payment)
admin.site.register(ItemPrice)