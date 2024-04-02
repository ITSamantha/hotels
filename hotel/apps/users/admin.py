from django.contrib import admin

from apps.bookings.admin import BookingInline
from apps.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = [BookingInline]

    list_filter = ["sex"]

    search_fields = ["username", "first_name", "last_name", "email"]

    fieldsets = [
        (
            "Base Information",
            {
                "fields": ["username", "email", "first_name", "last_name", "date_joined", "sex", "birthday",
                           "mobile_phone", "is_active"],
            },
        )
    ]
