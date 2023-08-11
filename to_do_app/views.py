from typing import Any, Dict
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from to_do_app.forms import TaskForm
from to_do_app.models import TaskModel


class HomeView(ListView):
    model = TaskModel
    template_name = "home.html"
    context_object_name = "tasks"
    ordering = ["taskTitle"]

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update({"sec_title": "Home"})
        return ctx


class TaskFormView(CreateView):
    model = TaskModel
    template_name = "task_form.html"
    form_class = TaskForm
    success_url = reverse_lazy("home")

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update({"sec_title": "Add Task"})
        return ctx


class TaskUpdateView(UpdateView):
    model = TaskModel
    template_name = "task_form.html"
    form_class = TaskForm
    success_url = reverse_lazy("home")

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update({"sec_title": "Edit Task"})
        return ctx
