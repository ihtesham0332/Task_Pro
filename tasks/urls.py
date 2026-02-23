from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='list'), # type: ignore
    path('update_task/<str:pk>/', views.updateTask, name='update_task'),
    path('delete_task/<str:pk>/', views.deleteTask, name='delete_task'),
    path('complete_task/<str:pk>/', views.completeTask, name='complete_task'), 
    path('undo_task/<str:pk>/', views.undoTask, name='undo_task'),
    path('privacy/', views.privacyPolicy, name='privacy'),
    path('terms/', views.termsOfService, name='terms'), # <-- New!
    path('support/', views.support, name='support'),    # <-- New!
    path('logout/', views.logoutUser, name='logout'),
]