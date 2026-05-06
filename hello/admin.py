from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import ContactMessage, Product, Feedback

# registered product, feedback, and contact message models#
admin.site.register(Product)
admin.site.register(Feedback)
admin.site.register(ContactMessage)
