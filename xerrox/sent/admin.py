from django.contrib import admin
from .models import Query, Results

# Register your models here.

admin.site.register(Query),
admin.site.register(Results)
