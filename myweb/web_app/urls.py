from rest_framework import routers
from django.urls import path, include
from .views import (UserProfileViewSet, PostListAPIView, PostDetailAPIView, PostContentListAPIView,
                    PostContentDetailAPIView, PostLikeListAPIView, PostLikeDetailAPIView, CommentListAPIView,
                    CommentDetailAPIView, CommentLikeListAPIView, CommentLikeDetailAPIView, LogoutView,
                    UserProfileListViewSet, UserProfileDetailViewSet, RegisterView, LoginView)

router = routers.SimpleRouter()
router.register(r'user', UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('users/', UserProfileListViewSet.as_view(), name='user_list'),
    path('users/<int:pk>/', UserProfileDetailViewSet.as_view(), name='user_detail'),
    path('post/', PostListAPIView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailAPIView.as_view(), name='post_detail'),
    path('post_content/', PostContentListAPIView.as_view(), name='post_content_list'),
    path('post_content/<int:pk>/', PostContentDetailAPIView.as_view(), name='post_content_detail'),
    path('post_like/', PostLikeListAPIView.as_view(), name='post_like_list'),
    path('post_like/<int:pk>/', PostLikeDetailAPIView.as_view(), name='post_like_detail'),
    path('comment/', CommentListAPIView.as_view(), name='comment_list'),
    path('comment/<int:pk>/', CommentDetailAPIView.as_view(), name='comment_detail'),
    path('comment_like/', CommentLikeListAPIView.as_view(), name='comment_like_list'),
    path('comment_like/<int:pk>/', CommentLikeDetailAPIView.as_view(), name='comment_like_detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]