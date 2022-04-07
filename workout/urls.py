from django.urls import path
from . import views

app_name = 'workout'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post/', views.CreateWorkoutView.as_view(), name='post'),
    path('post_done/', views.PostSuccessView.as_view(), name='post_done'),
    path('user_list/<int:user>', views.UserView.as_view(), name='user_list'),
    path('detail/<int:pk>/', views.DetailView.as_view(), name='workout_detail'),
    path('comment/create/<int:pk>/', views.Comment.as_view(), name='comment'),
    path('mypage/', views.MypageView.as_view(), name='mypage'),
    path('workout/<int:pk>/delete/', views.WorkoutDeleteView.as_view(), name='delete'),
    path('workout/<int:pk>/update/', views.WorkoutUpdateView.as_view(), name='update'),
    path('data/', views.data_screen, name='data'),
    path('data/plot', views.get_place_svg, name='img_plot'),
]