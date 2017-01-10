from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required, login_required
from django.utils import timezone
from .models import Post, Comment
from .forms import PostForm, CommentForm

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'gestionBlog/post_list.html', {'posts':posts})
    
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'gestionBlog/post_detail.html', {'post':post})

@login_required
@permission_required('gestionBlog.add_post')
def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('gestionBlog.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'gestionBlog/post_edit.html', {'form':form})

@login_required
@permission_required('gestionBlog.edit_post')
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('gestionBlog.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'gestionBlog/post_edit.html', {'form':form})

@login_required
@permission_required('gestionBlog.delete_post')
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect("/", pk=post.pk)
    return render(request, 'gestionBlog/post_delete.html', {'post':post})
    
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('gestionBlog.views.post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'gestionBlog/add_comment_to_post.html', {'form':form})

@login_required
@permission_required('gestionBlog.delete_comment_to_post')
def delete_comment_to_post(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method=="POST":
        post_pk = comment.post.pk
        comment.delete()
        return redirect("/", pk=post_pk)
    return render(request, 'gestionBlog/comment_delete.html', {'comment':comment})
    
def show_home_after_login_logout(request):
    return redirect("/")
