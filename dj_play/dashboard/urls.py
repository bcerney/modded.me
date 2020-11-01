from django.urls import include, path, re_path

from . import views


app_name = "dashboard"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    re_path(r"^verify/(?P<uuid>[a-z0-9\-]+)/", views.verify, name="verify"),
    path("dashboard/", views.DashboardView.as_view(), name="dashboard"),
    path("dashboard/send-daily-snapshot", views.DailySnapshotView.as_view(), name="send-daily-snapshot"),
    # sprint
    path("sprints/<int:pk>/", views.SprintDetailView.as_view(), name="sprint-detail"),
    # virtues
    path("virtues/<int:pk>/", views.VirtueDetailView.as_view(), name="virtue-detail"),
    path(
        "virtues/topic/<int:pk>/", views.TopicDetailView.as_view(), name="topic-detail"
    ),
    path("virtues/task/<int:pk>/", views.TaskDetailView.as_view(), name="task-detail"),
    path("virtues/add-virtue/", views.VirtueCreateView.as_view(), name="add-virtue"),
    path("virtues/add-topic/", views.TopicCreateView.as_view(), name="add-topic"),
    path("virtues/add-task/", views.TaskCreateView.as_view(), name="add-task"),
    path(
        "virtues/task/<int:pk>/complete-task",
        views.CompleteTaskView.as_view(),
        name="complete-task",
    ),
]
