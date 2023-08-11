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

    def get_queryset(self):
        return TaskModel.objects.filter(is_completed=False)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update({"sec_title": "Incomplete Tasks"})
        return ctx


class CompletedTaskView(ListView):
    model = TaskModel
    template_name = "home.html"
    context_object_name = "tasks"
    ordering = ["taskTitle"]

    def get_queryset(self):
        return TaskModel.objects.filter(is_completed=True)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update({"sec_title": "Complete Tasks"})
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


class TaskDeleteView(DeleteView):
    model = TaskModel
    template_name = "confirm_delete.html"
    success_url = reverse_lazy("home")

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update({"sec_title": "Delete Task"})
        return ctx
