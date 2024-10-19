from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (ProfileViewSet, CommentViewSet, LikeViewSet,
                    RegisterView, PostViewSet, FollowerViewSet, 
                    NewsFeedView, home, profile, register, create_post)

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'likes', LikeViewSet)
router.register(r'posts', PostViewSet)
router.register(r'followers', FollowerViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('profile/', profile, name='profile'),
    path('register/', register, name='register'),
    path('create_post/', create_post, name='create_post'),
    path('newsfeed/', NewsFeedView.as_view(), name='newsfeed'),
    path('api/', include(router.urls)),
    path('api/register/', RegisterView.as_view(), name='api-register'),
]
