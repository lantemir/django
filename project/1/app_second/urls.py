from django.urls import path
from .views import home, index, about, login, todo_detail
from . import views as logic

# тут только "маршруты" - адрес страницы
urlpatterns = [
    path('', home, ""),
    path('home/', home, name="home"),
    path('login/', login, name="login"),
    path('index/', index, name="index"),
    path('about/', about, name="about"),

    # <str:todo_id>
    # <slug:todo_id>
    path('todo_detail/<int:todo_id>/', todo_detail, name="todo_detail"),
    path(route='todo_list/', view=logic.todo_list, name="todo_list"),
    path(route='todo_create/', view=logic.todo_create, name="todo_create"),







    #мой код Добавления списка todo
    path(route='my_todo_list_detail/<int:todo_id>', view=logic.my_todo_list_detail, name="my_todo_list_detail"),
    path(route='my_todo_list/', view=logic.my_todo_list, name="my_todo_list" ),

    path(route='my_todo_list_create/', view=logic.my_todo_list_create, name="my_todo_list_create")
    

    # path('todo_create/', idea_create, name='django_idea_create'),
    # path('todo_detail/<int:todo_id>/', idea_change, name='django_idea_change'),
    # path('todo_list/', idea_list, name='django_idea_list'),
]