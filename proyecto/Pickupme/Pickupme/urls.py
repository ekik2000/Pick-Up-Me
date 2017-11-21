from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^pickupme/', include('Home.urls')),
    url(r'^login/', include('Login.urls')),
    url(r'^Register/', include('Register.urls')),

]
