from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# tempalte -> string
from django.template.loader import render_to_string

# validator
from django.core.validators import RegexValidator

# 유저모델을 슬대는 get_user_model() 사용 하면 알아서 settings에 있는 AUTH_USER_MODEL을 참조해서 가져옴
class User(AbstractUser):
  class GenderChoices(models.TextChoices):
    MALE = "M", "남성"
    FEMALE = "F", "여성"

  website_url = models.URLField(blank=True)
  bio = models.TextField(blank=True)
  phone_number = models.CharField(max_length=13, blank=True, validators=[RegexValidator(r"^010-?[1-9]\d{3}-?\d{4}$")])
  gender = models.CharField(max_length=1, blank=True, choices=GenderChoices.choices)
  avatar = models.ImageField(blank=True, upload_to="accounts/profile/%Y/%m/%d",
                              help_text="24px * 24px 크기의 png/jpg 파일을 업로드해주세요.")

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