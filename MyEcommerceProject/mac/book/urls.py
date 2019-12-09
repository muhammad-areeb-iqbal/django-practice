from django.urls import path
from . import views
from django.views.generic import TemplateView
from .views import BookPageTemplateView, BookPageView, BookDetailView, BookListView, BookCreateView, BookUpdateView

urlpatterns = [
    #path('about/', TemplateView.as_view(template_name="book.html")),
    #path('about/', BookPageTemplateView.as_view()),
    #path('about/', BookPageView.as_view()),
    path('<int:pk>/', BookDetailView.as_view()),
    path('', BookListView.as_view()),
    path('add/', BookCreateView.as_view(success_url="/book/"), name='add-book'),
    path('edit/<int:pk>/', BookUpdateView.as_view(success_url="/book/"), name='edit-book'),
]