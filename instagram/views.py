from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Post, Tag
from .forms import PostForm

from django.contrib import messages

from django.contrib.auth import get_user_model

from django.db.models import Q

@login_required
def index(request):
  post_list = Post.objects.all()\
        .filter(
          Q(author=request.user) |
          Q(author__in=request.user.following_set.all())
        )

  suggested_user_list = get_user_model().objects.exclude(pk=request.user.pk)\
  .exclude(pk__in=request.user.following_set.all())[:3]

  return render(request, "instagram/index.html", {
    'post_list': post_list,
    "suggested_user_list": suggested_user_list,
  })

@login_required
def post_new(request):
  if request.method == 'POST':
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
      post = form.save(commit=False)
      post.author = request.user
      post.save()

      # manytomany field 는 pk 값을 무조건 필요로 하기 때문에 세이브 다음에 아래 로직이 실행
      post.tag_set.add(*post.extract_tag_list()) # * 붙인 거 기억

      messages.success(request, "포스팅을 저장했습니다.")
      return redirect(post) # TODO: get_absolute_url 활용

  else:
    form = PostForm()
  return render(request, "instagram/post_form.html", {
    "form": form,
  })


def post_detail(request, pk):
  post = get_object_or_404(Post, pk=pk)
  return render(request, "instagram/post_detail.html", {
    "post": post,
  })

def user_page(request, username):
  page_user = get_object_or_404(get_user_model(), username=username, is_active=True)

  post_list = Post.objects.filter(author=page_user)
  post_list_count = post_list.count()

  if request.user.is_authenticated:
    is_follow = request.user.following_set.filter(pk=page_user.pk).exists()
  else:
    is_follow = False

  return render(request, "instagram/user_page.html", {
    "page_user": page_user,
    "post_list": post_list,
    "post_list_count": post_list_count,
    "is_follow": is_follow,
  })