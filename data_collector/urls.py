from django.conf.urls import url
from alchemansite.settings import MEDIA_ROOT, MEDIA_URL

from data_collector import views

from django.conf.urls.static import static
from django.conf import settings
#biar bisa safe photo


urlpatterns = [
    url(r'^department$',views.departmentApi),
    url(r'^department/([0-9]+)$',views.departmentApi),
    #can paham ieu cara nulis na, wkwkwk
    url(r'^employee$', views.employeeApi),
    url(r'^employee/([0-9]+)$',views.employeeApi),
    #udah mulai paham cara nulis url nya
    #jadi ini nanti si format http nya guys

    url(r'^employee/savefile', views.SaveFile)

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
