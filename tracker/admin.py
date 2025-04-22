from django.contrib import admin
from .models import Category,Transaction


# Register models
admin.site.register(Transaction)
admin.site.register(Category)


