from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm
from apps.order.models import OrderItem


@login_required
def account(request):
    profile = Profile.objects.get(user=request.user)
    orders = OrderItem.objects.filter(user=request.user)

    context = {
        'profile': profile,
        'orders': orders
    }

    return render(request, 'profiles/account.html', context)


@login_required
def editAccount(request, pk):
    profile = Profile.objects.get(id=pk)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile:account')
    else:
        form = ProfileForm()

    context = {
        'form': form,
        'profile': profile
    }

    return render(request, 'profiles/account_edit.html', context)