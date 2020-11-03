from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import include, path

from django.views.generic import RedirectView

from django.contrib.auth.decorators import login_required

from django_pydenticon.views import image as pydenticon_image

# @login_required
# def root(request):
#     return render(request, "root.html")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('instagram/', include('instagram.urls')),
    path('', RedirectView.as_view(pattern_name='instagram:index'), name='root'),
    path('accounts/', include('accounts.urls')),
    path('identicon/image/<path:data>', pydenticon_image, name='pydenticon_image'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
    
    urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)