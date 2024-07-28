from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """
    Stores a single category
    """
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """
    Stores a product entry
    """
    category = models.ManyToManyField(Category)
    sku = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    material = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2,
                                 null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class UserAccount(models.Model):
    """
    Stores a single user profile
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField("person's user name", max_length=30)
    first_name = models.CharField("person's first name", max_length=30)
    last_name = models.CharField("person's last name", max_length=30)
    email = models.EmailField(max_length=254)
    image = models.ImageField(null=True, blank=True)
    is_allowed = models.BooleanField(null=True, blank=True, default=False)
    is_admin = models.BooleanField(null=True, blank=True, default=False)
    is_superadmin = models.BooleanField(null=True, blank=True, default=False)

    def __str__(self):
        return self.user_name


class Review(models.Model):
    """
    Stores a review for a specific product entry
    """
    name = models.CharField(max_length=254)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey(UserAccount, on_delete=models.RESTRICT,
                               related_name="author")

    def __str__(self):
        return self.review


class UserRating(models.Model):
    """
    Stores a rating for a specific product entry
    """
    author = models.ForeignKey(UserAccount, on_delete=models.RESTRICT)
    rating = {
        0: "0",
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5"
    }
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    help_text = "Please rate the product from  0 = horrible to 5 = fantastic."

    def __str__(self):
        return self.rating
