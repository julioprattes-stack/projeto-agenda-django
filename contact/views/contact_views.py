from django.shortcuts import render
from contact.models import ContactModel

def index_view(request):
    contact = ContactModel.objects \
    .all().filter(show=True).order_by('-id')[:10]

    return render(
        request,
        'contact/index.html',
        {'contacts': contact}
    )