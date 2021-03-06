from msilib.schema import RemoveIniFile
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator

from . import models
from . import utils

# тут только "логика" - функции для обработки и возврат данных

# class Todo:
#     def __init__(self, description, name="name1"):
#         self.description = description
#         self.name = name
#
# obj = Todo("sdomethi", "name2")
#
# obj.description
# obj.name

def index(request):
    return render(request, 'app_teacher/pages/index.html')


def home(request):
    # user_list = ['tom', 'jack', 'john', 'anna', 'sam']
    # page = Paginator(user_list, 2)
   
    # # print( page.num_pages())
    # print( page.page(2).object_list)

    
   
    return render(request, 'app_teacher/pages/home.html')


def about(request):
    return render(request, 'app_teacher/pages/about.html')


def origin_home(request):
    return render(request, 'app_teacher/pages/origin_home.html')


def todo_detail(request, todo_id):
    obj = models.Task.objects.get(id=todo_id)
    context = {
        "todo": obj
    }
    return render(request, 'app_teacher/pages/DetailTodo.html', context)


def todo_list(request):
    objects = models.Task.objects.all()
    count_object_on_one_page = 2
    current_page_from_request_parametr = request.GET.get('page')

    page_obj = utils.CustomPaginator.get_page(
        objs=objects,
        limit=count_object_on_one_page,
        current_page=current_page_from_request_parametr
    )
   



    context = {"list": None, "page": page_obj}
    return render(request, 'app_teacher/pages/todo_list.html', context)


def todo_create(request):
    if request.method == "POST":
        title1 = request.POST.get("title", "заголовок по умолчанию")
        description1 = request.POST.get("description", "описание по умолчанию")
        obj = models.Task.objects.create(
            title=title1,
            description=description1
        )
        obj.save()
    context = {}
    return render(request, 'app_teacher/pages/CreateTodo.html', context)


def todo_delete(request, todo_id):
    obj = models.Task.objects.get(id=todo_id)
    obj.delete()
    return redirect(reverse('todo_list', args=()))


def todo_update_status(request, todo_id):
    obj = models.Task.objects.get(id=todo_id)
    # obj.is_completed = not obj.is_completed
    if obj.is_completed:
        obj.is_completed = False
    else:
        obj.is_completed = True
    obj.save()
    return redirect(reverse('todo_list', args=()))


def todo_change_data(request, todo_id):
    obj = models.Task.objects.get(id=todo_id)

    if request.method == "POST":
        title1 = request.POST.get("title", "заголовок по умолчанию")
        description1 = request.POST.get("description", "описание по умолчанию")
        if obj.title != title1:
            obj.title = title1
        if obj.description != description1:
            obj.description = description1
        obj.save()
    context = {
        "todo": obj
    }
    return render(request, 'app_teacher/pages/ChangeTodo.html', context)


# class Todo:
#     def __init__(self, description, name="name1"):
#         self.description = description
#         self.name = name
#         self.value = 0

#     def counter(self, external_value):
#         self.value + external_value

#     @staticmethod
#     def count(value, extra):
#         return (value + extra) * 1000

# obj = Todo("spmthing", "name2")
# obj.description
# Todo.count()