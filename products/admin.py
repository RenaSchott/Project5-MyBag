from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Product, Category, Review, UserAccount, UserRating


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'price',
        'material',
        'description',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'product',
        'author',
        'content',
        'created_on',
    )

    ordering = ('product', 'created_on',)


class UserRatingAdmin(admin.ModelAdmin):
    list_display = (
        'review',
        'rating',
        'author',
    )

    ordering = ('review',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(UserRating, UserRatingAdmin)
admin.site.register(UserAccount)

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
