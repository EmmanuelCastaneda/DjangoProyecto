from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
urlpatterns = [
    path("",views.inicio),
    path('login/',views.login),
    path('inicioAdministrador/',views.inicioAdministrador),
    path('inicioTecnico/',views.inicioTecnico),
    path('inicioEmpleado/',views.inicioEmpleado),
    path('vistaSolicitud/',views.vistaSolicitud),
    path('registrarSolicitud/',views.registrarSolicitud),
    path('listarCasosParaAsignar/',views.listarCasos),
    path('listarCasosAsignados/',views.listarCasosTecnicos),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/uidb64/token/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('salir/',views.salir),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
