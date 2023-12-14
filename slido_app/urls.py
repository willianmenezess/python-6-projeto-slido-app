from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from slido_app.views import (
    index,
    register_visitor,
    create_visitor,
    create_question,
    QuestionViewSet,
)

router = routers.DefaultRouter()

router.register("questions", QuestionViewSet)

urlpatterns = [
    path("", index, name="homepage"),
    path("login/", register_visitor, name="login"),
    path("visitor/new", create_visitor, name="create_visitor"),
    path("question/new", create_question, name="create_question"),
    path("api/", include(router.urls)),
    path(
        "api/token/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path(
        "api/token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),
    path(
        "api/token/verify/",
        TokenVerifyView.as_view(),
        name="token_verify",
    ),
]
