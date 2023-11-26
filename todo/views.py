from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import TodoForm
from .models import Todo


def home(request):
    list = Todo.objects.order_by('-date')
    return render(request, 'home.html', {'list': list})


def category(request, url):
    list = Todo.objects.filter(complite__exact=url)
    return render(request, 'home.html', {'list': list})


def add(request):
    list = Todo.objects.order_by("-date")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = TodoForm()
    return render(request, 'add.html', {"form": form, "list": list})


def update(request, id):
    todo = get_object_or_404(Todo, id=id)
    form = TodoForm(instance=todo)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('home')

    form = TodoForm()
    return render(request, 'update.html', {"form": form, "todo": todo})


def delete(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.delete()
    return redirect("home")


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))


def logout_user(request):
    logout(request)
    return redirect('login')
