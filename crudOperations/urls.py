from django.urls import include, path
from .views import GameCreate, GameDetail, GameUpdate, GameDelete, GameList

urlpatterns = [
    path('create/',GameCreate.as_view(),name='create-game'),
    path('list',GameList.as_view(),name='list-game'),
    path('<int:pk>/',GameDetail.as_view(),name='retrieve-game'),
    path('update/<int:pk>/',GameUpdate.as_view(),name='update_game'),
    path('delete/<int:pk>/',GameDelete.as_view(),name='delete_game'),
]
