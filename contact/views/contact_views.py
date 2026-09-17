from django.shortcuts import render, get_object_or_404
from django.http import Http404
from contact.models import ContactModel

def index_view(request):
    contact = ContactModel.objects \
    .all().filter(show=True).order_by('-id')[:10]

    return render(
        request,
        'contact/index.html',
        {'contact': contact}
    )


def contact_view(request, contact_id):
    # contact = ContactModel.objects \
    # .filter(id=contact_id).first()
    contact = get_object_or_404(
        ContactModel,
        id=contact_id,
        show=True
    )

    return render(
        request,
        'contact/contact.html',
        {'contact': contact}
    )