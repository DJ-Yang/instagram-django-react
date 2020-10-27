from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# tempalte -> string
from django.template.loader import render_to_string

# 유저모델을 슬대는 get_user_model() 사용 하면 알아서 settings에 있는 AUTH_USER_MODEL을 참조해서 가져옴
class User(AbstractUser):
  website_url = models.URLField(blank=True)
  bio = models.TextField(blank=True)

  # 메일 발송 함수
  # def send_welcome_email(self):
  #   subject = render_to_string("accounts/welcome_email_subject.txt", {
  #   "user": self,
  # })
  #   content = render_to_string("accounts/welcome_email_content.txt", {
  #   "user": self,
  # })
  #   sender_email = settings.WECOME_EMAIL
  #   send_mail(subject, content, sender_email, [self.email], fail_silently=False)

# class Profile(models.Model):
#   pass