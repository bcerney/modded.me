from django.db import models


class MannaProfile(models.Model):
    journals = models.ForeignKey(Journal, related_name="manna_profile", on_delete=models.CASCADE)
    quotes = models.ForeignKey(Journal, related_name="manna_profile", on_delete=models.CASCADE)


class Journal(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, blank=False)
    entries = models.ForeignKey(
        JournalEntry, related_name="journal", on_delete=models.CASCADE
    )

    def get_absolute_url(self):
        return reverse("manna:journal-detail", args=[self.id])

    class Meta:
        ordering = ["created"]


class JournalEntry(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    journal = models.ForeignKey(
        Journal, related_name="entries", on_delete=models.CASCADE
    )
    text = models.TextField()

    def __str__(self):
        return f'{self.created} - {self.text}'

    def get_absolute_url(self):
        return reverse("manna:journal-entry-detail", args=[self.id])

    class Meta:
        ordering = ["created"]

# TODO: need for inheritance here? need to consider meditation use cases
# class MeditationJournalEntry(models.Model):
#     created = models.DateTimeField(auto_now_add=True)
#     journal = models.ForeignKey(
#         Journal, related_name="entries", on_delete=models.CASCADE
#     )
#     text = models.TextField()

#     def __str__(self):
#         return f'{self.created} - {self.text}'

#     def get_absolute_url(self):
#         return reverse("manna:journal-entry-detail", args=[self.id])

#     class Meta:
#         ordering = ["created"]
