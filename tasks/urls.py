from django.urls import path
from .views import TasksViews, TaskDetail, TaskCreateViews, TaskUpdateViews, TaskDeleteViews


urlpatterns = [
    path('', TasksViews.as_view(), name="tasks"),
    path('<int:pk>/', TaskDetail.as_view(), name="detail"),
    path('create/', TaskCreateViews.as_view(), name="create"),
    path('update/<int:pk>/', TaskUpdateViews.as_view(), name="update"),
    path('delete/<int:pk>/', TaskDeleteViews.as_view(), name="delete"),


]
