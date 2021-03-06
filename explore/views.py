from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from explore.models import CommunicationPost, CommunicationComment
from accounts.models import Profile
from explore.models import CommunicationPost
from .forms import PostForm
from my_profile.models import Post
from explore.forms import CommentForm
from django.contrib import messages
from accounts.models import User


def post_list(request):
    post = CommunicationPost.objects.all()
    randuser = Post.objects.order_by('?')
    return render(request, "explore/post_list.html", {
        'post_list': post,
        'rand_list': randuser,
    })


def post_detail(request, id):
    post = get_object_or_404(CommunicationPost, id=id)
    form = CommentForm

    return render(request, 'explore/post_detail.html', {
        'post': post,
        'form': form,
    })


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save()
            return redirect('/explore/')
    else:
        form = PostForm()
    return render(request, 'explore/post_form.html', {
        'form': form,
    })


def post_edit(request, id):
    post = get_object_or_404(CommunicationPost, id=id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            post = form.save()
            return redirect('explore:post_detail', id=id)
    else:
        form = PostForm(instance=post)
    return render(request, 'explore/post_form.html', {
        'form': form,
    })


def post_delete(request, id):
    post = get_object_or_404(CommunicationPost, id=id)

    if request.method == 'POST':
        post.delete()
        return redirect('/explore/', request.user)


@login_required
def my_communication_list(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    post_list = user.communicationpost_set.all()

    return render(request, 'explore/my_communication_list.html', {
        'post_list': post_list,
        'username': username,
    })


def whats_new(request):
    all_profile = Profile.objects.all()  #모든 프로필

    return render(request, 'explore/whatsnew_test.html', {
        'profile_list': all_profile,
    })


@login_required
def comment_new(request, post_id):
    post = get_object_or_404(CommunicationPost, id=post_id)

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('explore:post_detail', post.id)
    else:
        form = CommentForm()
    return render(request, 'explore/comment_form.html', {
            'form': form,
        })


@login_required
def comment_edit(request, post_id, id):
    comment = get_object_or_404(CommunicationComment, id=id)
    if comment.author != request.user:
        return redirect(comment.post)

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            comment = form.save()
            return redirect(comment.post)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'explore/comment_form.html', {
            'form': form,
        })


@login_required
def comment_delete(request, post_id, id):
    comment = get_object_or_404(CommunicationComment, id=id)
    if comment.author != request.user:
        return redirect(comment.post)

    if request.method == 'POST':
        comment.delete()
        return redirect(comment.post)

    return render(request, 'explore/comment_confirm_delete.html', {
        'comment': comment,
    })

def insider_user(request):
    insa = Profile.objects.filter(all_follows__gt=5).order_by(['-follows'])[:7] #order_by 추가해야함
    return print(insa)

def random_user(request):
    randuser = Post.objects.order_by('?')[:7]
    return print(randuser)
