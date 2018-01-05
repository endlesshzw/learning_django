from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('topic', views.topics, name='topics'),
    path('topic/<int:topic_id>', views.topic, name='topic'),
    path('new_topic', views.new_topic, name='new_topic'),
    path('new_entry/<int:topic_id>', views.new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry'),
    path('save_info/', views.save_info, name='save_info'),
]

app_name = 'learning_logs'