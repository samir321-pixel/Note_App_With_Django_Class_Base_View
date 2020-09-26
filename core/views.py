from django.urls import reverse_lazy

from .models import Core
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView


# Create your views here.
class IndexView(ListView):
    model = Core
    template_name = 'core/index.html'
    context_object_name = 'index'


class SingleView(DetailView):
    model = Core
    template_name = 'core/single.html'
    context_object_name = 'post'


class PostView(ListView):
    model = Core
    template_name = 'core/posts.html'
    context_object_name = 'post_list'

class AddView(CreateView):
    model = Core
    template_name = 'core/add.html'
    fields='__all__'
    success_url = reverse_lazy('core:posts')

class EditView(UpdateView):
    model = Core
    template_name = 'core/edit.html'
    fields = '__all__'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('core:posts')

class Delete(DeleteView):
    model = Core
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('core:posts')
    template_name = 'core/confirm-delete.html'

