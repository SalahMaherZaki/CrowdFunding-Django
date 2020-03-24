from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.show_profile),
    path('edit/', views.edit_profile),
    path('delete/<int:id>', views.delete_profile),
    path('my_projects/<int:id>', views.my_projects),
    # path('edit_project/<int:id>', views.edit_project),
    path('delete_project/<int:id>', views.delete_project)

]
