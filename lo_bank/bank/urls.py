from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# Register views with the router
router.register(r'accounts', views.BankAccountView)

urlpatterns = router.urls