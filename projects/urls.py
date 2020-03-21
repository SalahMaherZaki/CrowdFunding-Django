from django.urls import path , include
from . import views


urlpatterns = [
    path('', views.listProjects , name= "projects" ),
    path('<int:id>',views.selectProject,name='selectProject'),
    path('report/',views.reportProject,name='reportProject'),
    path('tag/<tag_name>', views.tagProjects , name= "tags" ),
]
