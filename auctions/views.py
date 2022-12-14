from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from . import forms

from .models import User, Auction, Bid


def index(request):
    return render(request, "auctions/index.html", {
        "auctions": Auction.objects.filter(is_active=True)
    })


def add_auction(request):
    if request.method != "POST":
        form = forms.AddAuction()
        return render(request, "auctions/add-auction.html", {
            "form": form,
        })

    # POST
    form = forms.AddAuction(request.POST, request.FILES)
    if form.is_valid():
        Auction(
            user_id=request.user,
            name=form.cleaned_data["name"],
            description=form.cleaned_data["description"],
            photo=form.files["photo"],
            starting_price=form.cleaned_data["price"],
            is_active = True,
        ).save()
    return HttpResponseRedirect(reverse("index"))


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
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
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def auction(request, auction_id):
    # Price block 
    bids = Bid.objects.filter(auction_id=auction_id).order_by('-price')
    auction = Auction.objects.get(pk=auction_id)
    price = bids.first().price if bids.exists() else auction.starting_price


    # if no bids, use starting price
    
    # if therere some use max value
    return render(request, "auctions/auction.html", {
        "auction": auction,
        "price": price,
    })