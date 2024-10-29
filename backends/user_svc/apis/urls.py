from django.urls import path
from apis import views

urlpatterns = [
    path('users/<int:pk>', views.UserProfileView.as_view()),
]
