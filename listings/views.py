from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from listings.choices import state_choices, bedroom_choices, price_choices


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listing = paginator.get_page(page)
    context = {
        'listings':  paged_listing,

    }

    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing': listing,
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    listings = Listing.objects.order_by('-list_date')
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            listings = listings.filter(description__icontains=keywords)

    if 'city' in request.GET:
        keywords = request.GET['city']
        if keywords:
            listings = listings.filter(city__iexact=keywords)

    if 'state' in request.GET:
        keywords = request.GET['state']
        if keywords:
            listings = listings.filter(state__iexact=keywords)

    if 'bedrooms' in request.GET:
        keywords = request.GET['bedrooms']
        if keywords:
            listings = listings.filter(bedrooms__lte=keywords)

    if 'price' in request.GET:
        keywords = request.GET['price']
        if keywords:
            listings = listings.filter(Price__lte=keywords)
    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }

    return render(request, 'listings/search.html', context)
