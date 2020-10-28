from django import forms
from .models import User

from django.contrib.auth.forms import (
  UserCreationForm,
  PasswordChangeForm as AuthPasswordChangeForm
)


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

  
class ProfileForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['avatar', 'first_name', 'last_name', 'website_url', 'bio', 'phone_number', 'gender']

class PasswordChangeForm(AuthPasswordChangeForm):
  def clean_new_password2(self):
    old_password = self.cleaned_data.get('old_password')
    new_password2 = super().clean_new_password2()
    if old_password == new_password2:
      raise forms.ValidationError("새로운 암호는 기존 암호와 다르게 입력해주세요.")
    return new_password2