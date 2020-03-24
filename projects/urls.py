from django.urls import path , include
from . import views


urlpatterns = [
    path('', views.listProjects , name= "projects" ),
    path('charge', views.charge , name= "charge" ),
    path('<project_id>', views.singleProject , name= "singleProject" ),
    path('<project_id>/<success>', views.singleProject , name= "singleProject" ),
    # path('<int:id>',views.singleProject,name='selectProject'),
    path('report/',views.reportProject,name='reportProject'),
    path('tag/<tag_name>', views.tagProjects , name= "tags" ),
]
