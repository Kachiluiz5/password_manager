from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Password
from .forms import PasswordForm, UpdatePasswordForm
from django.contrib.auth.decorators import login_required

@login_required
def password_list(request):
    passwords = Password.objects.filter(owner=request.user)
    return render(request, 'manager/password_list.html', {'passwords': passwords})

@login_required
def generate_password(request):
    if request.method == 'POST':
        form = PasswordForm(request.POST)
        if form.is_valid():
            new_password = form.save(commit=False)
            new_password.owner = request.user
            new_password.generate()
            new_password.save()
            messages.success(request, 'Password generated successfully.')

            # Add the generated password to the context dictionary
            context = {
                'form': form,
                'generated_password': new_password.value,
            }

            # Return the render function with the updated context
            return render(request, 'manager/generate_password.html', context)
    else:
        form = PasswordForm()
        context = {
            'form': form,
        }
        return render(request, 'manager/generate_password.html', context)

@login_required
def delete_password(request, password_id):
    password = Password.objects.get(id=password_id)
    if password.owner == request.user:
        password.delete()
        messages.success(request, 'Password deleted successfully.')
    else:
        messages.error(request, 'You do not have permission to delete this password.')
    return redirect('manager:password_list')

@login_required
def update_password(request, password_id):
    password = Password.objects.get(id=password_id)
    if password.owner == request.user:
        if request.method == 'POST':
            form = UpdatePasswordForm(request.POST, instance=password)
            if form.is_valid():
                form.save()
                messages.success(request, 'Password updated successfully.')
                return redirect('manager:password_list')
        else:
            form = UpdatePasswordForm(instance=password)
        return render(request, 'manager/update_password.html', {'form': form})
    else:
        messages.error(request, 'You do not have permission to update this password.')
        return redirect('manager:password_list')