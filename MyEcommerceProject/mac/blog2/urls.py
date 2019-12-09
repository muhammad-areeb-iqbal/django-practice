from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="blog2Index"),
    # path("detail/<int:id>", views.detail, name="detail"),
    # path("create/", views.post_create_view, name="create"),
    # path("edit/<int:id>", views.post_edit_view, name="edit"),
    # path("delete/<int:id>", views.destroy, name="delete"),
]