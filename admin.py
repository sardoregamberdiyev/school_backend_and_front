from django.contrib import admin

# Register your models here.
from maktab152.models import *

admin.site.register(Category)
admin.site.register(Recipe)
admin.site.register(Suggestion)
