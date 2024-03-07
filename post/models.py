from django.db import models
from django.contrib.auth.models import User


# class Post(models.Model):
#     post_title = models.CharField(max_length=150)
#     post_content = models.TextField(blank=True, null=True)  # TextField로 변경
#     post_img = models.ImageField(upload_to="posts/", blank=True, null=True)
#     post_manager = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.post_title
