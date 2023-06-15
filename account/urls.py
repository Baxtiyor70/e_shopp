from django.urls import path
from .views import RegisterApiView, LoginStartView, LoginEndView

urlpatterns = [
    path('register/', RegisterApiView.as_view()),
    path('login_start/', LoginStartView.as_view()),
    path('login_end/', LoginEndView.as_view())

]
