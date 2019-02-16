from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.views import LoginView
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import Profile, User
from .forms import SignupForm
from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.templatetags.socialaccount import get_providers


LOGGED_IN_HOME = '/home/post_list'


def login_forbidden(function=None, redirect_field_name=None, redirect_to=LOGGED_IN_HOME):
    """
    Decorator for views that checks that the user is NOT logged in, redirecting
    to the homepage if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: not u.is_authenticated,
        login_url=redirect_to,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


@login_forbidden
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = SignupForm()
    return render(request, 'accounts/signup_form.html', {
        'form': form,
    })



@login_required
def profile(request, user_profile_id):
    user = get_object_or_404(User, pk=user_profile_id)
    profile = get_object_or_404(Profile, pk=user_profile_id)
    return render(request, 'accounts/profile.html', {'profile_user': user, 'request_user': request.user.id,'real_profile_user':profile})

@login_forbidden
def login(request):
    settings.LOGIN_REDIRECT_URL = '/accounts/error/'
    providers = []
    for provider in get_providers():

        try:
            provider.social_app = SocialApp.objects.get(provider=provider.id, sites=settings.SITE_ID)
        except SocialApp.DoesNotExist:
            provider.social_app = None
        providers.append(provider)
    return LoginView.as_view(
        template_name='accounts/login_form.html',
        extra_context={'providers': providers})(request)

@login_required
def follow_user(request, user_profile_id):
    #debug
    print(request.user.profile.id)
    print(user_profile_id)
    profile_to_follow = get_object_or_404(Profile, pk=user_profile_id)
    user_profile = request.user
    data = {}

    if int(user_profile_id) == request.user.profile.id:
        messages.warning(request, "You can not follow yourself")
    elif profile_to_follow.follows.filter(id=user_profile.id).exists():
        messages.warning(request, "You are already following this user.")
    else:
        profile_to_follow.follows.add(user_profile)
        messages.success(request, "You are now following {}".format(profile_to_follow.user))
    print(data)
    t = user_profile.followed_by.all()
    print(t)

    return redirect('accounts:profile', user_profile_id)

@login_required
def unfollow_user(request, user_profile_id):
    profile_to_follow = get_object_or_404(Profile, pk=user_profile_id)
    user_profile = request.user
    data = {}
    if profile_to_follow.follows.filter(id=user_profile.id).exists():
        profile_to_follow.follows.remove(user_profile)
        messages.success(request, "You are now unfollowing {}.".format(profile_to_follow.user))
    else:
        messages.warning(request, "You are not following this user")
    return redirect('accounts:profile', user_profile_id)


@login_required
def profile_redirect(request):
    return redirect('/home/post_list')

@login_required
def search(request):
    qs = User.objects.all()
    print(qs)
    q = request.GET.get('q', '')
    print(q)
    if q:
        qs = qs.filter(username__icontains=q)

        return render(request, 'accounts/search.html', {
            'user_result' : qs,
            'q' : q, })
