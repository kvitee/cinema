from django.db import models
from django.db.models import Q
from django.db.models.constraints import (
    CheckConstraint, UniqueConstraint
)


class Movie(models.Model):
    title = models.CharField(
        max_length=100
    )

    summary = models.CharField(
        max_length=1000
    )

    release_date = models.DateField()

    production_country = models.CharField(
        max_length=50
    )

    director = models.CharField(
        max_length=50
    )

    duration = models.DurationField()

    age_restriction = models.SmallIntegerField()

    class Meta:
        db_table = "movies"
        constraints = [
            CheckConstraint(
                check=Q(age_restriction__gt=0),
                name="age_restriction_positive"
            ),
            UniqueConstraint(
                fields=("title",),
                name="movie_unq"
            ),
        ]
