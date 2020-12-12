from django.contrib import admin
from django.views.generic.base import RedirectView
from django.urls import path, include
from django.conf.urls.static import static
from alcproject import settings

admin.site.site_header = "Pelatihan Online"
admin.site.site_title = "PO ALC Administration"
admin.site.index_title = "Administration | Pelatihan Online ALC Indonesia"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include('core.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
