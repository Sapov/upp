# posts/views.py
from django.views.generic import ListView, CreateView
from .models import Post
from django.urls import reverse_lazy  # новый

from .forms import PostForm  # новый


class HomePageView(ListView):
    model = Post
    template_name = 'home.html'


class CreatePostView(CreateView):  # новый
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('home')


import os

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Post


def index(request):
    product = Post.objects.all()
    return render(request, "test.html", {"post": post})


# изменение данных в БД
def edit(request, id):
    try:
        product = Post.objects.get(id=id)

        if request.method == "POST":
            product.name = request.POST.get("name")
            product.quantity = request.POST.get("quantity")
            product.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"product": product})
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Клиент не найден</h2>")


# удаление данных из БД

# def delete(request, id):
#     try:
#         product = Product.objects.get(id=id)
#         product.delete()
#         return HttpResponseRedirect("/")
#     except Product.DoesNotExist:
#         return HttpResponseNotFound("<h2>Клиент не найден</h2>")

def delete(request, id):
    try:
        product = Product.objects.get(id=id)
        product.delete()
        return HttpResponseRedirect("/")
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Клиент не найден</h2>")


def create(request):
    if request.method == "POST":
        product = Post()
        product.title = request.POST.get('title')
        product.quantity = request.POST.get('quantity')
        # product.order =
        # product.material
        # product.width = 344
        # product.length = 444
        # product.resolution = 300
        # product.color_model =
        # product.size = 1000
        # product.price = 5000
        # product.path_file
        # product.created_at
        # product.updated_at
        product.save()

        return HttpResponseRedirect("/")



# изменение данных в БД
def calk(request, id):
    try:
        product = Product.objects.get(id=id)

        if request.method == "POST":

            product.name = request.POST.get("name")
            product.quantity = request.POST.get("quantity")
            product.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"product": product})
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Клиент не найден</h2>")
