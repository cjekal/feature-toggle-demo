from django.urls import path
from apis import views

urlpatterns = [
    path('payments/', views.payment_list),
    path('payments/<int:pk>/', views.payment_detail),
]
