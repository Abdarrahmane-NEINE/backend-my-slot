from django.urls import re_path

from ApiMySlot import views

from django.conf.urls.static import static
from django.conf import settings


# from django.urls import path
# initial case
# from . import views
# urlpatterns = [
#     path('', views.index, name='index'),
# ]

urlpatterns = [
    # import views  APIs
    re_path(r'^availabilitie$',views.availabilitieApi),
    re_path(r'^availabilitie/([0-9]+)$',views.availabilitieApi),

    re_path(r'^reservation$',views.reservationApi),
    re_path(r'^reservation/([0-9]+)$',views.reservationApi),

    re_path(r'^test$',views.testApi),
    re_path(r'^test/([0-9]+)$',views.testApi),

    re_path(r'^reservation/savefile',views.SaveFile)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT )