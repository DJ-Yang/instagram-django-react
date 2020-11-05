from django.db import models
from django.conf import settings
from django.urls import reverse

import re

class BaseModel(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    abstract = True   # 부모로서만 존재


class Post(BaseModel):
  # author에서 유저 모델을 이용하려면 'user_set'을 사용해야하는데 like_user_set에서도 같은 related_name을 사용해서 이런 일이 발생함
  author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='my_user_set', on_delete=models.CASCADE)
  photo = models.ImageField(upload_to="instagram/%Y/%m/%d")
  caption = models.CharField(max_length=500)
  tag_set = models.ManyToManyField('Tag', blank=True)
  location = models.CharField(max_length=100)
  like_user_set = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_user_set', blank=True)

  def __str__(self):
    return self.caption

  # @property
  # def author_name(self):
  #   return f"{self.author.first_name} {self.author.last_name}"

  def extract_tag_list(self):
    tag_name_list = re.findall(r"#([a-zA-z\dㄱ-힣]+)", self.caption)
    tag_list = []
    for tag_name in tag_name_list:
      tag, _ = Tag.objects.get_or_create(name=tag_name)
      tag_list.append(tag)
    return tag_list
  
  def get_absolute_url(self):
      return reverse("instagram:post_detail", kwargs={"pk": self.pk})

  def is_like_user(self, user):
    return self.like_user_set.filter(pk=user.pk).exists()

  class Meta:
    ordering = ['-id']

class Comment(BaseModel):
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  message = models.TextField()

  class Meta:
    ordering = ['-id']
  

class Tag(models.Model):
  name = models.CharField(max_length=50, unique=True)

  def __str__(self):
    return self.name

# class LikeUser(models.Model):
#   post = models.ForeignKey(Post, on_delete=models.CASCADE)
#   user = models.ForeignKey(settngs.AUTH_USER_MODEL, on_delete=models.CASCADE)