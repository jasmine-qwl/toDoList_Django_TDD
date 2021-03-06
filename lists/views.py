from django.shortcuts import redirect, render
from lists.models import List
from lists.forms import ItemForm, ExistingListItemForm, NewListForm
from django.contrib.auth import get_user_model

User = get_user_model()

def home_page(request):
    return render(request, 'home.html', {'form': ItemForm()})

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    form = ExistingListItemForm(for_list=list_)
    if request.method == 'POST':
        form = ExistingListItemForm(for_list = list_, data = request.POST)
        if form.is_valid():
            form.save()
            return redirect(list_)
    return render(request, 'list.html', {'list': list_, 'form': form})

def new_list(request):
    form = NewListForm(data=request.POST)
    if form.is_valid():
        list_ = form.save(owner=request.user)
        return redirect(list_)
    return render(request, 'home.html', {'form': form})

def my_lists(request, email):
    owner = User.objects.get(email=email)
    return render(request, 'my_lists.html', {'owner': owner})

def share_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    sharee = request.POST['sharee']
    try:
        user_sharee = User.objects.get(email=sharee)
    except User.DoesNotExist:
        user_sharee = User.objects.create(email=sharee)
    list_.shared_with.add(user_sharee)
    return redirect(list_)

def delete_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    list_.delete()
    owner = list_.owner.email
    return redirect(f'/lists/users/{owner}/')
