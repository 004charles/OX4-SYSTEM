from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [

    path('', include('website.urls')),

    # Admin Django
    path('admin/', admin.site.urls),

    # Painel interno
    path('painel/', include('admin_painel.urls')),
    path('api/v1/usuarios/', include('usuarios.urls')),    
    path('api/v1/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # web site
    path('ox4transporte/', include('website.urls')),

    # app user

    path('app/', include('front_user.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
