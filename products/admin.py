from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Product, Category, Review, UserAccount, UserRating

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(UserRating)

# Defined an inline admin descriptor for UserAccount which acts a bit like a singleton
class UserAccountInline(admin.StackedInline):
    model = UserAccount
    can_delete = False
    verbose_name_plural = "useraccounts"


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = [UserAccountInline]


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
