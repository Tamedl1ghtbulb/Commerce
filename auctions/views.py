from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import datetime
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *

def index(request):
        sve = AuctionListing.objects.filter(krajbiddinga= False).values('kategorija').distinct()
        return render(request, "auctions/index.html",{
            "aukcija" : AuctionListing.objects.filter(krajbiddinga = False),
            "categories":sve,
            "end" : False,
        })

krajb= False
kbidder = False
def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("commerce:index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html",{
            'form': LoginForm()
        })


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("commerce:index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["password1"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("commerce:index"))
    else:
        return render(request, "auctions/register.html",{
            'form': RegisterForm(),
        })

@login_required(login_url= '/login')
def create(request):
    #Create a new listing based on passed POST data
    if request.method == "POST":
      #  print(request.data.get('slika'))
        post = AuctionForm(request.POST, request.FILES)
        if post.is_valid():
            post=post.cleaned_data
            ukupno = AuctionListing(krajbiddinga=False,krajb= False,kategorija=post["kategorija"],user=User.objects.get(username=request.user),cena=post["cena"],naslov=post["naslov"],opis=post["opis"], datum=datetime.datetime.today(), slika=request.FILES["slika"])
            ukupno.save()
        return HttpResponseRedirect(reverse("commerce:index"))
    #Present the user with the forms generated from Models to add a new listing
    else:
        return render(request, "auctions/create.html",{
            "forma": AuctionForm(),
        })

@login_required(login_url= '/login')
def listing(request,lol):
    listing = AuctionListing.objects.get(id=lol)
    if request.method == "POST":
        user = request.user
        if request.POST.get("dugme")=="Watchlist":
            if not AuctionListing.objects.filter(follower=user, id = listing.id):
                listing.follower.add(user)
            else:
                user.auctionlisting_set.remove(listing)
            return HttpResponseRedirect(reverse('commerce:listing', args=(lol,)))
        elif request.POST.get("kraj")== "End bidding":
            listing.krajbiddinga = True
            listing.save()
            return HttpResponseRedirect(reverse('commerce:listing', args=(lol,)))
    else:
        komentari = Komentar.objects.filter(klisting=lol)
        try:
            top_bid = Bids.objects.filter(user_id=request.user.id).latest('bids')
            top_bid_user = Bids.objects.filter(product_id=lol).latest('bids')
            if top_bid.bids==top_bid_user.bids:
                topbidder = True
            else:
                topbidder = False
        except:
            topbidder = False
        if User.objects.get(username=request.user) == listing.user:
            listing.krajb = True
            listing.save()
        else:
            listing.krajb = False
            listing.save()
        return render(request, "auctions/listing.html",{
            "listing": listing,
            "comment" : CommentForm(),
            "comments":komentari,
            "bid":Bid(),
            "owner" : listing.krajb,
            "krajbiddinga": listing.krajbiddinga,
            "topbidder": topbidder,
        })

def displayCategory(request):

    #Sort and display listings based on their category, also added logic if the listing has ended for Active listings and Archieve tabs

    if request.method == "POST":
        categoryFromForm = request.POST['category']
        end = request.POST['end']
        if categoryFromForm == 'All':
            activeListings = AuctionListing.objects.filter(krajbiddinga = end)
        else:
            activeListings = AuctionListing.objects.filter(kategorija=categoryFromForm, krajbiddinga = end)
        return render(request, "auctions/index.html", {
            "aukcija": activeListings,
            "categories":AuctionListing.objects.filter(krajbiddinga=end).values('kategorija').distinct(),
            'end':end
        })
    #Redirect to index if the user tries to GET the page. Prevents errors.
    else:
        return HttpResponseRedirect(reverse('commerce:index'))

@login_required(login_url= '/login')
def watchlist(request):
    listing= AuctionListing.objects.filter(follower = request.user)
    return render(request, "auctions/index.html", {
        "aukcija": listing,
        "watchlist": True
    })

@login_required(login_url= '/login')
def bids(request, id):
    if request.method == "POST":
        form = Bid(request.POST)
        if form.is_valid():
            user = request.user
            nbid = form.cleaned_data
            sve = AuctionListing.objects.get(id=id)
            if nbid['cena'] > sve.cena:
                sve1 = Bids(user = user,bids= nbid['cena'],product=sve)
                sve1.save()
                sve.cena = nbid['cena']
                sve.save()
                return HttpResponseRedirect(reverse('commerce:listing', args=(id,)))
            else:
                return HttpResponseRedirect(reverse('commerce:listing', args=(id,)))

    #Redirect to index if the user tries to GET the page. Prevents errors.
    else:
        return HttpResponseRedirect(reverse('commerce:index'))

@login_required(login_url= '/login')
def comments(request,id):
    if request.method == "POST":
        form = Komentar(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            sve = AuctionListing.objects.get(id=lol)
            user = User.objects.get(username=request.user)
            ncomment= Komentar(user = user,klisting = sve,komentar = ncomment["komentar"])
            ncomment.save()
            return HttpResponseRedirect(reverse('commerce:listing', args=(lol,)))

    #Redirect to index if the user tries to GET the page. Prevents errors.
    else:
        return HttpResponseRedirect(reverse('commerce:index'))


def archive(request):
    sve = AuctionListing.objects.filter(krajbiddinga= True).values('kategorija').distinct()
    return render(request, "auctions/index.html",{
            "aukcija" : AuctionListing.objects.filter(krajbiddinga = True),
            "categories":sve,
            "end" : True,
        })

@login_required(login_url= '/login')
def comment(request, postid):
    if request.method == "POST":
        comment = CommentForm(request.POST)
        if comment.is_valid():
            comment = comment.cleaned_data
            ncomment = Komentar(klisting = AuctionListing(id =postid), komentar = comment['komentar'], user=request.user )
            ncomment.save()
            return HttpResponseRedirect(reverse('commerce:listing', args=(postid,)))

    #Redirect to index if the user tries to GET the page. Prevents errors.
    else:
        return HttpResponseRedirect(reverse('commerce:index'))

@login_required(login_url= '/login')
def mylisting(request):
    listing= AuctionListing.objects.filter(user = request.user)
    return render(request, "auctions/index.html", {
        "aukcija": listing,
    })