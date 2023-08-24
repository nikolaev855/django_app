from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post

class HomePage(ListView):
    https_method_names = ["get"]
    template_name = 'feed/homepage.html'
    model = Post
    context_object_name = 'posts'
    queryset = Post.objects.all().order_by('-id')[0:30]

class PostDetailView(DetailView):
    https_method_names = ["get"]
    template_name = "feed/detail.html"
    model = Post
    context_object_name = "post"

class CreateNewPost(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "feed/create.html"
    fields = ['text']
  
    def form_valid(self, form):
        obj = form.save(commit=False())
        return super().form_valid(form)
