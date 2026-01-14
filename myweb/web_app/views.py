from django.core.serializers import serialize
from .models import (UserProfile, Follow, Post,
                     PostContent, PostLike, Comment, CommentLike,)
from .serializers import (UserProfileSerializer, UserProfileListSerializer, UserProfileDetailSerializer,
                          FollowListSerializer, FollowDetailSerializer, UserProfileReviewSerializer,
                          PostListSerializer, PostDetailSerializer, UserLoginSerializer,
                          PostContentListSerializer, PostContentDetailSerializer,
                          PostLikeListSerializer, PostLikeDetailSerializer, CommentListSerializer,
                          CommentDetailSerializer, UserSerializer, CommentLikeListSerializer, CommentLikeDetailSerializer)
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class LoginView(TokenObtainPairView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({"detail": "Неверные учетные данные"}, status=status.HTTP_401_UNAUTHORIZED)

        user = serializer.validated_data
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)

class UserProfileListViewSet(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileListSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)

class UserProfileDetailViewSet(generics.RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileDetailSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)

class UserProfileReviewViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileReviewSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)


class FollowListAPIView(generics.ListAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowListSerializer

class FollowDetailAPIView(generics.RetrieveAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowDetailSerializer


class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer


class PostContentListAPIView(generics.ListAPIView):
    queryset = PostContent.objects.all()
    serializer_class = PostContentListSerializer

class PostContentDetailAPIView(generics.RetrieveAPIView):
    queryset = PostContent.objects.all()
    serializer_class = PostContentDetailSerializer


class PostLikeListAPIView(generics.ListAPIView):
    queryset = PostLike.objects.all()
    serializer_class = PostLikeListSerializer

class PostLikeDetailAPIView(generics.RetrieveAPIView):
    queryset = PostLike.objects.all()
    serializer_class = PostLikeDetailSerializer


class CommentListAPIView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer

class CommentDetailAPIView(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer


class CommentLikeListAPIView(generics.ListAPIView):
    queryset = CommentLike.objects.all()
    serializer_class = CommentLikeListSerializer

class CommentLikeDetailAPIView(generics.RetrieveAPIView):
    queryset = CommentLike.objects.all()
    serializer_class = CommentLikeDetailSerializer













