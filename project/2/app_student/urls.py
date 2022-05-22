from django.urls import path
from . import views as logic

urlpatterns = [
        path(route='my_todo_list/', view=logic.my_todo_list, name="my_todo_list"),
]
