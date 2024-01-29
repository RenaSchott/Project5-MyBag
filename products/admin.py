from django.contrib import admin
from .models import Product, Category, Review, UserAccount, UserRating

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(UserAccount)
admin.site.register(UserRating)
