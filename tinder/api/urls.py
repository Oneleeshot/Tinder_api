from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register('matches', views.MatchViewSet, basename='matches')
router.register('messages', views.MessageViewSet, basename='messages')
router.register('images', views.ImageViewSet, basename='images')
router.register('profiles', views.ProfileViewSet, basename='profiles')
router.register('users', views.UserViewSet, basename='users')
