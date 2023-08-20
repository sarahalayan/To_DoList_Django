from django.shortcuts import render
from django.views.generic import DeleteView,UpdateView,ListView, CreateView
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Task

# Create your views here.

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'to_do/index.html', {'tasks': tasks})

class TaskListView(UserPassesTestMixin,ListView):
    model = Task
    template_name = 'to_do/my_todo_list.html'
    context_object_name = 'list'
    ordering = ['created_at']

    def test_func(self):
        return self.request.user.is_authenticated  
        
    def get_queryset(self):
        # Filter the queryset to show only tasks belonging to the logged-in user
        return Task.objects.filter(user=self.request.user)


class TaskDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Task
    template_name='to_do/deletetask.html'
    success_url=reverse_lazy('todo-list')

    def test_func(self):
        task = self.get_object()  # Get the task instance
        return self.request.user == task.user  # Check if the user is the owner of the task

class TaskCreateView(LoginRequiredMixin,CreateView):
    model = Task
    template_name = 'to_do/addtask.html'
    fields = ['title', 'details','deadline','important']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskModifyView(UserPassesTestMixin,LoginRequiredMixin,UpdateView):
    model = Task
    template_name= 'to_do/edittask.html'
    fields = ['title', 'details','important','deadline','completed']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        task= self.get_object()
        if self.request.user == task.user:
            return True
        return False
    
class TaskUpdateView(UserPassesTestMixin,LoginRequiredMixin,UpdateView):
    model = Task
    template_name='to_do/updatetask.html'
    fields = ['completed']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        task= self.get_object()
        if self.request.user == task.user:
            return True
        return False

