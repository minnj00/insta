from django.shortcuts import render, redirect
from .models import Post 
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    posts = Post.objects.all().order_by('-id')
    comment_form = CommentForm()
    context = {
        'posts': posts,
        'comment_form': comment_form
    }
    return render(request, 'index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:index')
    else:
        form = PostForm()
        
    context = {
        'form': form
    }

    return render(request, 'form.html', context)
@login_required
def comment_create(request, post_id):
    comment_form = CommentForm(request.POST)

    if comment_form.is_valid():
        comment = comment_form.save(commit=False) 

        # 로그인 유지 정보 넣기
        comment.user = request.user

        # post_id를 기준으로 찾은 post(두번째방법도 존재, 전에했던 방법 참고)
        post = Post.objects.get(id=post_id)
        comment.post = post
        comment.save()

        return redirect('posts:index')

@login_required
def like(request, post_id):

    # 좋아요 버튼을 누른 유저
    user = request.user
    post = Post.objects.get(id=post_id)
    
    # 좋아요버튼을 이미 누른 경우
    # if user in post.like_users.all(): # post를 좋아요 누른 모든 유저목록 중에 지금 로그인 한 user가 있다면
    if post in user.like_posts.all():
        post.like_users.remove(user)
        # user.like_posts.remove(post)
    # 아직 좋아요버튼을 안누른 경우
    else:
        post.like_users.add(user)
        # user.like_posts.add(post)
    return redirect('posts:index')

