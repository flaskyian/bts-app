from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.views import View
from django.urls import reverse_lazy

from . import models, forms

class PostListView(ListView):
    model = models.Post
    fields = "__all__"
    queryset = models.Post.objects.filter(active=True).order_by("-last_modified")

class PostDetailView(DetailView):
    model = models.Post
    
    def get_object(self, queryset=None):
        return self.model.objects.get(public_id=self.kwargs.get("public_id"))

class PostCreateView(CreateView):
    form_class = forms.PostForm
    template_name = "fanpage/post_form.html"
    success_url = reverse_lazy("fanpage:list")

