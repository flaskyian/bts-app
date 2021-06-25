from django.urls import path
from . import views

app_name = "fanpage"

urlpatterns = [
    path("", views.PostListView.as_view(), name="list"),
    path("<uuid:public_id>", views.PostDetailView.as_view(), name="detail"),
    path("create", views.PostCreateView.as_view(), name="create"),
]