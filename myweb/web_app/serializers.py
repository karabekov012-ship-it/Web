from rest_framework import serializers
from .models import (UserProfile, Follow, Post,
                     PostContent, PostLike, Comment,
                     CommentLike,)
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'bio']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user

class UserLoginSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }



class UserProfileListSerializer(serializers.ModelSerializer):
    get_count_post = serializers.SerializerMethodField
    get_count_following = serializers.SerializerMethodField
    get_count_followers = serializers.SerializerMethodField

    class Meta:
        model = UserProfile
        fields = ['id', 'user_image', 'get_count_following' , 'get_count_followers', 'get_count_post', 'is_official']

    def get_count_post(self, obj):
        return obj.post.count()

    def get_count_following(self):
        return self.following.count()

    def get_count_followers(self):
        return self.followers.count()


class UserProfileDetailSerializer(serializers.ModelSerializer):
    get_count_post = serializers.SerializerMethodField
    get_count_following = serializers.SerializerMethodField
    get_count_followers = serializers.SerializerMethodField

    class Meta:
        model = UserProfile
        fields = ['id', 'user_image', 'get_count_following' , 'get_count_followers', 'get_count_post', 'is_official', 'bio', 'date_registered']

    def get_count_post(self, obj):
        return obj.post.count()

    def get_count_following(self):
        return self.following.count()

    def get_count_followers(self):
        return self.followers.count()

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']


class FollowListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = '__all__'

class FollowDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = '__all__'


class PostContentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostContent
        fields = ['id',  'content']

class PostListSerializer(serializers.ModelSerializer):
    first_name = UserProfileReviewSerializer(read_only=True)
    last_name = UserProfileReviewSerializer(read_only=True)
    content = PostContentListSerializer(many=True)
    get_count_like = serializers.SerializerMethodField


    class Meta:
        model = Post
        fields = ['id', 'first_name', 'last_name', 'content', 'get_count_like', 'hashtag', 'description', 'created_date']

    def get_count_like(self):
        return self.like.count()



class CommentListSerializer(serializers.ModelSerializer):
    first_name = UserProfileReviewSerializer(read_only=True)
    last_name = UserProfileReviewSerializer(read_only=True)
    get_count_likes = serializers.SerializerMethodField

    class Meta:
        model = Comment
        fields = ['id', 'first_name', 'last_name', 'text', 'parent', 'created_date', 'get_count_likes']

    def get_count_likes(self):
        return self.likes.count()

class PostDetailSerializer(serializers.ModelSerializer):
    first_name = UserProfileReviewSerializer(read_only=True)
    last_name = UserProfileReviewSerializer(read_only=True)
    content = PostContentListSerializer(many=True)
    get_count_like = serializers.SerializerMethodField
    comment = CommentListSerializer(many=True)


    class Meta:
        model = Post
        fields = ['id', 'first_name', 'last_name', 'content', 'get_count_like', 'hashtag', 'description', 'created_date', 'comment']

    def get_count_like(self):
        return self.like.count()


class PostContentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostContent
        fields = '__all__'


class PostLikeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = '__all__'

class PostLikeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = '__all__'


class CommentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class CommentLikeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentLike
        fields = '__all__'

class CommentLikeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentLike
        fields = '__all__'