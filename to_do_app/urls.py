from django.urls import path
from to_do_app.views import HomeView, TaskFormView, TaskUpdateView


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("add-task/", TaskFormView.as_view(), name="add_task"),
    path("edit-task/<int:pk>", TaskUpdateView.as_view(), name="edit_task"),
]
