from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from tasks.models import Task
from django.shortcuts import render_to_response

def index(request):

  order = request.GET.get('order', 'desc')

  tasks = Task.objects.all()
  down=True
  up=False
  if(order == 'desc'):
    tasks = tasks.order_by('-date')
    up=True
    down=False
  elif(order == 'asc'):
    tasks = tasks.order_by('date')


  return render_to_response('list/index.html',{'tasks': tasks,'up':up,'down':down})
