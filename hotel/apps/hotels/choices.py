from django.db import models


class BookingStatus(models.IntegerChoices):
    DECLINED = 1, "Declined"
    APPROVED = 2, "Approved"
    CANCELED = 3, "Canceled"
    IN_PROCESS = 4, "In process"
