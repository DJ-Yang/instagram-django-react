from django import forms
from .models import User

from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['email'].required = True

  class Meta(UserCreationForm.Meta):
    model = User # 직접 만든 앱의 유저모델로 변경, 기존 속성은 auth.User를 따름
    fields = ['username', 'email', 'first_name', 'last_name']

  def clean_email(self):
    email = self.cleaned_data.get('email')
    if email:
      qs = User.objects.filter(email=email)
      if qs.exists():
        raise forms.ValidationError("이미 등록된 이메일 주소입니다.")
    return email

  