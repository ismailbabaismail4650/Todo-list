from django.urls import path
from. import views
from .views import TaskList, TaskDetail,TaskCreate,TaskUpdate, TaskDelete, MyloginViews, Registerpage

urlpatterns = [
    path('login/',MyloginViews.as_view(), name="login"),
    path('logout/', views.Mylogout, name='logout'),
    path('register/',Registerpage.as_view(), name="register"),

    path('', TaskList.as_view(), name="tasks"),
    path('task/<int:pk>/',TaskDetail.as_view(), name="task"),
    path('create/',TaskCreate.as_view(), name="create"),
    path('update/<int:pk>/',TaskUpdate.as_view(), name="update"),
    path('delete/<int:pk>/',TaskDelete.as_view(), name="delete"),
]