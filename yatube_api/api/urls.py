from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from api.views import CommentViewSet, GroupViewSet, PostViewSet

appname = 'api'
router = DefaultRouter()

router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet,
                basename='comments')

urlpatterns = [
    path('api/v1/api-token-auth/', views.obtain_auth_token),
    path('api/v1/', include(router.urls)),
]
