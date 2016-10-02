from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import ParallelCorpus


class IndexView(generic.ListView):
    template_name = "corpus/index.html"
    context_object_name = "corpora"

    def get_queryset(self):
        return ParallelCorpus.objects.all()


class DetailView(generic.DetailView):
    model = ParallelCorpus
    template_name = "corpus/corpus_index.html"


