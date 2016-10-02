from django.db import models


class ParallelCorpus(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class ParallelSentence(models.Model):
    src = models.TextField()
    tgt = models.TextField()
    parallel_corpus = models.ForeignKey(ParallelCorpus, on_delete=models.CASCADE)

    def __str__(self):
        return self.src + " ⇔  " + self.tgt

class AlignmentModel(models.Model):
    log = models.TextField()


class Alignment(models.Model):
    alignment = models.TextField()
    parallel_sentence = models.ForeignKey(ParallelCorpus, on_delete=models.CASCADE)
    alignment_model = models.ForeignKey(AlignmentModel, on_delete=models.CASCADE)


