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
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  photo = models.ImageField(upload_to="instagram/%Y/%m/%d")
  caption = models.CharField(max_length=500)
  tag_set = models.ManyToManyField('Tag', blank=True)
  location = models.CharField(max_length=100)

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
      return reverse("instagram:post_detial", kwargs={"pk": self.pk})
  

class Tag(models.Model):
  name = models.CharField(max_length=50, unique=True)

  def __str__(self):
    return self.name