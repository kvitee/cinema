from django.db import models
from django.db.models import Q
from django.db.models.constraints import (
    CheckConstraint, UniqueConstraint
)


class Hall(models.Model):
    name = models.CharField(
        max_length=50
    )

    cost_factor = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        default=1.0
    )

    class Meta:
        db_table = "halls"
        constraints = [
            CheckConstraint(
                check=Q(cost_factor__gt=0),
                name="hall_cost_factor_positive"
            ),
            UniqueConstraint(
                fields=("name",),
                name="hall_unq"
            ),
        ]


class Seat(models.Model):
    hall = models.ForeignKey(
        to=Hall,
        on_delete=models.CASCADE
    )

    row_number = models.SmallIntegerField()
    seat_number = models.SmallIntegerField()

    cost_factor = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        default=1.0
    )

    class Meta:
        db_table = "seats"
        constraints = [
            CheckConstraint(
                check=Q(cost_factor__gt=0),
                name="seat_cost_factor_positive"
            ),
            UniqueConstraint(
                fields=("hall_id", "row_number", "seat_number"),
                name="seat_unq"
            ),
        ]
