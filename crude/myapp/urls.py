from django.urls import path
from .import views

urlpatterns = [
    path('',views.product,name='product'),
    path('add_details',views.add_details,name='add_details'),
    path('edit/<int:pk>',views.edit,name='edit'),
    path('edit_details/<int:p>',views.edit_details,name='edit_details'),
    path('show',views.show,name='show'),
    path('delete/<int:pk>',views.delete,name='delete'),
]
