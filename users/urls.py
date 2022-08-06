'''Define the url model in learning_logs file'''

from django.urls import path,include
from . import views

app_name='users'

urlpatterns=[
    # The main page of login and logout
    path('',include('django.contrib.auth.urls')),
    path('register/',views.register,name='register'),
]
'''
    path('topics/',views.topics,name='topics'),
    path('topics/topic_<int:topic_id>/',views.topic,name='topic'),
    path('new_topics',views.new_topic,name='new_topic'),
    path('new_entry/<int:topic_id>/',views.new_entry,name='new_entry'),
    path('edit_entry/<int:entry_id>/',views.edit_entry,name='edit_entry'),
'''