from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Rest_Articles
from .forms import RestArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView


def rest_home(request):

    search_query = request.POST.get('search_query')
    if request.method == 'POST' and search_query:
        print(search_query)
        rest_list = Rest_Articles.objects.filter(
            food__icontains = search_query
        )
    else:
        rest_list = Rest_Articles.objects.all()
    print(rest_list)
    return render(request,'rest/rest_home.html',{'rest': rest_list})




class RestDetailView(DetailView):
    model = Rest_Articles
    template_name = 'rest/details_view.html'
    context_object_name = 'rest'


class RestUpdateView(UpdateView):
    model = Rest_Articles
    template_name = 'rest/create.html'

    form_class = RestArticlesForm


class RestDeleteView(DeleteView):
    model = Rest_Articles
    success_url = '/rest/'
    template_name = 'rest/rest-delete.html'


def create(request):
    error = ''
    if request.method == 'POST':
        form = RestArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rest_home')
        else:
            error = 'Форма была неверной'

    form = RestArticlesForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'rest/create.html', data)
