from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView 
from django.http import HttpResponseRedirect
from django.urls import reverse

from wiki.forms import PageForm
from wiki.models import Page


class PageListView(ListView):
    """ Renders a list of all Pages. """
    model = Page

    def get(self, request):
        """ GET a list of Pages. """
        pages = self.get_queryset().all()
        return render(request, 'list.html', {
          
          'pages': pages
        })

class PageDetailView(DetailView):
    """ Renders a specific page based on it's slug."""
    model = Page

    def get(self, request, slug):
        """ Returns a specific wiki page by slug. """
        page = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'page.html', {
          'page': page
        })

class PageNew(CreateView):
    model = Page

    def get(self, request):
      """ Prints the form """
      page_form = PageForm()
      return render(request, 'add_page.html', {
        'page_form': page_form
      })

    def post(self, request):
      """processes the form and adds a wiki """
      form = PageForm(request.POST)
      form.instance.author = self.request.user
      print(form)
      if form.is_valid():
        page = form.save()
        return HttpResponseRedirect(reverse('wiki-details-page', args=[page.slug] ))
      else:
        print("CRI__________________________-")

