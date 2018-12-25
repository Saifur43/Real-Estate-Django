from django.shortcuts import redirect
from .models import Contacts


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']
        message = request.POST['message']

        contact = Contacts(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone,
                           user_id=user_id, message=message)
        contact.save(),
        return redirect('/listings/' + listing_id)
