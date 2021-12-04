from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from .forms import UserUpdateForm, ProfileUpdateForm
from homepage.models import Post,Comment
# Create your views here.

# Update it here
@login_required
def profile(request):
    images = Post.objects.all()
    post = Post.objects.filter(author=request.user).order_by('-date_posted')
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('homepage:index')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'images': images,
        'posts' : post
    }

    return render(request, 'profile.html', context)