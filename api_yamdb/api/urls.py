from django.urls import include, path
from rest_framework import routers


from api.views import (
    ReviewsViewSet,
    CommentsViewSet,
    GenreViewSet,
    signup_cust
    # APISignupCust
)

app_name = "api"

router = routers.DefaultRouter(trailing_slash=True)

router.register(
    r"titles/(?P<title_id>\d+)/reviews", ReviewsViewSet, basename="reviews"
)
router.register(
    r"titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments",
    CommentsViewSet, basename="comments"
)
router.register(r"genres", GenreViewSet, basename="genre")

urlpatterns = [
    path("v1/", include(router.urls)),
    path('v1/auth/signup/', signup_cust, name='signup_cust')

]
