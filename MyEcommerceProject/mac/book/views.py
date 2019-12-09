from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import View
from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView
from .models import Book
from django.db.models import Q
from django.contrib import messages

# Create your views here.
class BookPageTemplateView(TemplateView):

    template_name = "book.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = "data"
        return context

class BookPageView(View):

    template_name = 'book.html'

    def get(self, request, *args, **kwargs):
        print("GET REQUEST")
        context = {"data":"New Data"}
        return render(request, self.template_name, context)

class BookDetailView(DetailView):
    model = Book

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #     context['book_list'] = Book.objects.all()
    #     return context

class BookListView(ListView):
    model = Book
    context_object_name = 'book_list'

class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        title =  form.cleaned_data['title']
        qs = Book.objects.filter( Q(title__icontains=title)).count()
        if qs > 0:
            messages.error(self.request,"Title already exists")
            return super(BookCreateView, self).form_invalid(form)
        messages.success(self.request, "Book added succesfully")
        return super(BookCreateView, self).form_valid(form)

class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'description']