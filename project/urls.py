from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('blogadmin/', admin.site.urls),
    path("", include('blog.urls'))
]

admin.site.index_title = 'Blog admin'
admin.site.site_header = 'Admin panel'
admin.site.site_title = 'Blog admin'
