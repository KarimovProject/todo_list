from django.contrib import admin
from .models import TodoItem


# Register your models here.


from .models import *

admin.site.register(TodoItem)
