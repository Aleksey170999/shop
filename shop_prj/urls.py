from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('customers/', include('customers.urls')),
    path('products/', include('products.urls')),
    path('', RedirectView.as_view(url=reverse_lazy('home-page'), permanent=False)),
    path('cart/', include('cart.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

