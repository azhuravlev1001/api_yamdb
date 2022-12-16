from rest_framework.routers import DefaultRouter
from .views import ReviewViewSet, CommentViewSet, TitleViewSet


router = DefaultRouter()
router.register(r'titles', TitleViewSet)
router.register(
    r'titles/(?P<title_id>\d+)/reviews', ReviewViewSet,
    basename='reviews'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments', CommentViewSet,
    basename='comments'
)