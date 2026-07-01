from django.db import models
from django.contrib.auth.models import User


class Dealer(models.Model):
    name = models.CharField(max_length=200)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    image = models.URLField(default='https://images.unsplash.com/photo-1492144534655-ae79c964c9d7?auto=format&fit=crop&w=800&q=80')

    def __str__(self):
        return self.name


class Review(models.Model):
    dealer = models.ForeignKey(Dealer, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=5)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.dealer.name}'
