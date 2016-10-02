from django.contrib import admin

from .models import ParallelCorpus, ParallelSentence

# Register your models here.

class ParallelSentenceInline(admin.TabularInline):
    model = ParallelSentence
    extra = 1


class ParallelCorpusAdmin(admin.ModelAdmin):
    inlines = [ParallelSentenceInline]

admin.site.register(ParallelCorpus, ParallelCorpusAdmin)
