from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url( r'^login/$',auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    url(r'^logout/$', auth_views.LogoutView, name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),  # <--
    url(r'^admin/', admin.site.urls),
]
