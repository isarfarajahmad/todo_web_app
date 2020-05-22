from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from . import models
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    todo_items = models.Todo.objects.all().order_by("-added_date")
    return render(request, 'main/index.html', { "todo_items": todo_items })

@csrf_exempt
def add_todo(request):
    current_date = timezone.now()
    content = request.POST["content"]
    created_obj = models.Todo.objects.create(added_date=current_date, text=content)
    length_of_todos = models.Todo.objects.all().count()
    return HttpResponseRedirect("/")


def delete_todo(request, todo_id):
    models.Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")
