from django.conf.urls import url,include
from rest_framework import routers
from django.urls import path
from .views import StudentOperation


router = routers.DefaultRouter()
#router.register(r'v2', FlipVendorCrud)
router.register(r'v1', StudentOperation)

urlpatterns=router.urls

