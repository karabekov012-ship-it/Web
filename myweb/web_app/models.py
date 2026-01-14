from django.db import models
from django.contrib.auth.models import AbstractUser
#from django.core.validators import MinValueValidator, MaxValueValidator

class UserProfile(AbstractUser):
    bio = models.TextField(null=True, blank=True)
    user_image = models.ImageField(null=True, blank=True)
    is_official = models.BooleanField(default=False)
    user_link = models.URLField(null=True, blank=True)
    date_registered = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name}-{self.last_name}'

    def get_count_post(self):
        return self.post.count()

    def get_count_following(self):
        return self.following.count()

    def get_count_followers(self):
        return self.followers.count()

class Follow(models.Model):
    following = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='following')
    follower = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='followers')
    create_date = models.DateField(auto_now_add=True)


class Post(models.Model):
    description = models.TextField(null=True, blank=True)
    hashtag = models.CharField(max_length=100, null=True, blank=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='post', null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)

    def get_count_like(self):
        return self.like.count()



class PostContent(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='content')
    content = models.FileField()


class PostLike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='like')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        unique_together = ('user', 'post')



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)

    def get_count_likes(self):
        return self.likes.count()


class CommentLike(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        unique_together = ('user', 'comment')

class Chat(models.Model):
    person = models.ManyToManyField(UserProfile)
    created_date = models.DateField(auto_now_add=True)

class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='author')
    text = models.TextField()
    image = models.ImageField(upload_to='images', null=True, blank=True)
    video = models.FileField(upload_to='videos', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)