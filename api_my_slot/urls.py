from django.urls import re_path

from api_my_slot import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # import views  APIs
    re_path(r'^availabilitie$',views.availabilitie_api),
    re_path(r'^availabilitie/([0-9]+)$',views.availabilitie_api),

    re_path(r'^reservation$',views.reservation_api),
    re_path(r'^reservation/([0-9]+)$',views.reservation_api),

    re_path(r'^test$',views.handl_test_api),
    re_path(r'^test/([0-9]+)$',views.handl_test_api),

    re_path(r'^reservation/savefile',views.SaveFile)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT )