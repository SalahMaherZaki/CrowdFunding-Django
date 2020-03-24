from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("HomePage.urls")),
    path('projects/', include("projects.urls")),
    path('profile/', include("user.urls")),
	# ---- Login with Facebook -----
    path('accounts/' , include("allauth.urls")),
    path('fblogin/',TemplateView.as_view(template_name='login.html'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
