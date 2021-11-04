from django.urls import path
from . import views

app_name = "board"
urlpatterns = [
    path('', views.index, name="index"),
    path('create', views.create, name="create"),
    path('detail/<bpk>', views.detail, name="detail"),
    path('delete/<bpk>', views.delete, name="delete"),
    path('modify/<bpk>', views.modify, name="modify"),
    path('addup/<bpk>', views.addup, name="addup"),
    path('removeup/<bpk>', views.removeup, name="removeup")
]