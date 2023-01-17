from rest_framework import routers
from django.urls import include, path
from api.views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet


router = routers.DefaultRouter()
router.register('v1/posts', PostViewSet, basename='posts')
router.register(
    r'v1/posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments'
)
router.register('v1/groups', GroupViewSet, basename='groups')
router.register('v1/follow', FollowViewSet, basename='followers')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
