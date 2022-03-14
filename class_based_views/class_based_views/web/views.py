from django.urls import reverse_lazy
from django.views import generic as views
from .forms import TodoCreateForm, TodoUpdateForm

from .models import Todo, Category


class HomePageListView(views.ListView):
    model = Todo
    context_object_name = 'todos'
    template_name = 'list_todos.html'

    def get_ordering(self):
        return '-category', 'title', 'description'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['message'] = 'Hello to everybody!'
        return context


class TodoDetailView(views.DetailView):
    model = Todo
    template_name = 'todo_details.html'


class TodoCreateView(views.CreateView):
    model = Todo
    template_name = 'todo_create.html'
    form_class = TodoCreateForm

    success_url = reverse_lazy('cbv index')


class TodoUpdateView(views.UpdateView):
    template_name = 'todo_update.html'
    model = Todo
    form_class = TodoUpdateForm

    success_url = reverse_lazy('cbv index')


class TodoDeleteView(views.DeleteView):
    model = Todo
    template_name = 'todo_delete.html'
    success_url = reverse_lazy('cbv index')
