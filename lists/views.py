from django.shortcuts import redirect, render
from lists.models import List
from lists.forms import ItemForm, ExistingListItemForm
from django.views.generic import FormView, CreateView, DetailView
from django.contrib.auth import get_user_model

User = get_user_model()

class HomePageView(FormView):
    template_name = 'home.html'
    form_class = ItemForm

class ViewAndAddToList(DetailView, CreateView):
    model = List
    template_name = 'list.html'
    form_class = ExistingListItemForm

    def get_form(self):
        self.object = self.get_object()
        return self.form_class(for_list=self.object, data=self.request.POST)

class NewListView(CreateView):
    form_class = ItemForm
    template_name = 'home.html'

    def form_valid(self, form):
        list_ = List.objects.create()
        form.save(for_list=list_)
        return redirect(list_)

def my_lists(request, email):
    owner = User.objects.get(email=email)
    return render(request, 'my_lists.html', {'owner': owner})
