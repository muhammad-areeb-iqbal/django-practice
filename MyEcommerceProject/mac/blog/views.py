from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import PostModel
from .forms import PostModelForm
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    # if request.user.is_authenticated:
    #     print("Logged in User")
    # else:
    #     print("Non login user")
    #     raise 404

    q = request.GET.get("q", None)
    if q == None:
        post_list = PostModel.objects.all()
        q = ""
    else:
        post_list = PostModel.objects.filter(
            Q(title__icontains=q) |
            Q(content__icontains=q)
        )
    context = {"post_list": post_list, "q": q}
    return render(request, "blog/index.html", context)


def detail(request, id=None):
    # try:
    #     qs = PostModel.objects.get(id= id)
    # except:
    #     raise Http404
    qs = get_object_or_404(PostModel, id=id)
    content = {"list": qs}
    return render(request, "blog/detail.html", content)


@login_required(login_url='/admin/')
def post_create_view(request):
    # if request.method == 'POST':
    #     form = PostModelForm(request.POST)
    #     if form.is_valid():
    #         try:
    #             form.save()
    #             return redirect("/blog")
    #         except:
    #             print("ddddddddd")
    # else:
    #     form = PostModelForm

    form = PostModelForm(request.POST or None)
    try:
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            messages.success(request, 'Post added successfully.')
            return redirect("/blog/")
    except:
        pass
    content = {"form": form}
    return render(request, "blog/create.html", content)


@login_required(login_url='/admin/')
def post_edit_view(request, id=None):
    post = get_object_or_404(PostModel, id=id)
    form = PostModelForm(request.POST or None, instance=post)
    try:
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            messages.success(request, 'Post updated successfully.')
            return redirect("/blog/edit/" + str(id))
    except:
        pass
    content = {"form": form, "post": post}
    return render(request, "blog/edit.html", content)


@login_required(login_url='/admin/')
def destroy(request, id):
    post = get_object_or_404(PostModel, id=id)
    post.delete()
    messages.success(request, 'Post deleted successfully.')
    return redirect("/blog")
