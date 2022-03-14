from django.urls import path
from .views import HomePageListView, TodoDetailView, TodoCreateView, TodoUpdateView, TodoDeleteView

urlpatterns = [
    path('', HomePageListView.as_view(), name='cbv index'),

    path('todo/cbv/<int:pk>', TodoDetailView.as_view(), name='todo details'),
    path('todo/create/', TodoCreateView.as_view(), name='todo create'),
    path('todo/update/<int:pk>/', TodoUpdateView.as_view(), name='todo update'),
    path('todo/delete/<int:pk>/', TodoDeleteView.as_view(), name='todo delete'),
]
