from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    password1 = models.CharField(("password"), max_length=128)

class AuctionListing(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE, related_name="apovezano")
    slika = models.ImageField(upload_to='images',blank= True)
    naslov = models.CharField(max_length=24)
    opis = models.CharField(max_length=240)
    cena = models.IntegerField()
    datum = models.DateTimeField()
    Kategorije = (
        ('Tehnika', 'Tehnika'),
        ('Kuca', 'Kuca'),
        ('Odeca', 'Odeca'),
    )

    follower = models.ManyToManyField(User)

    kategorija= models.CharField(max_length=15, choices=Kategorije)
    krajb = models.BooleanField()
    krajbiddinga = models.BooleanField()

    def __str__(self):
        return f"{self.kategorija},{self.slika},{self.naslov},{self.opis},{self.cena},{self.datum}"



class Komentar(models.Model):
    klisting = models.ForeignKey(AuctionListing, on_delete=models.CASCADE, related_name="klistings")
    user =  models.ForeignKey(User, on_delete=models.CASCADE, related_name="kpovezano")
    komentar = models.CharField(max_length= 240)

class Bids(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE, related_name="bpovezano")
    bids = models.IntegerField()
    product = models.ForeignKey(AuctionListing,on_delete=models.CASCADE, related_name="bpovezano")
    class Meta:
         get_latest_by = 'bids'

class Following(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cfollower")
    post =  models.ForeignKey(AuctionListing,on_delete=models.CASCADE, related_name="wpost")



