from django.db import models


class PostManager(models.Manager):
    queryset = None

    def get_queryset(self):
        if self.queryset is None:
            self.queryset = (
                super().get_queryset()
                .select_related('author',)
            )
        return self.queryset
