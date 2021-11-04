from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Board, Reply

# Register your models here.
admin.site.register(Board)
admin.site.register(Reply)