from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SignupViewSet, CustomLoginView, LogoutView

router = DefaultRouter()
router.register(r'signup', SignupViewSet, basename='signup')

#urls to accounts management
urlpatterns = [
    path('', include(router.urls)),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]