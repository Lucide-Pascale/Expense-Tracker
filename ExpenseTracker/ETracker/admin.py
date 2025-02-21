from django.contrib import admin
from ETracker import models

admin.site.register(models.Category),
admin.site.register(models.Expense)

# Register your models here.
