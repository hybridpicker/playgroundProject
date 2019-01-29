from django.shortcuts import render, redirect

from song.models import Song
from band.models import Member
from band.models import Info
from contact.forms import ContactForm
from contact.email import contact_mail

# Create your views here.


def view_404(request):
    # make a redirect to homepage
    return redirect('/')


def home (request):
    songs = Song.objects
    members = Member.objects
    infos = Info.objects
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            name = request.POST['name']
            subject = str('Anfrage: ' + name)
            now = datetime.datetime.now()
            today = now.date()
            try:
                contact_mail(from_email, subject, message)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            render(request, 'home.html', {'songs':songs, 'members':members,
                                                'infos':infos, 'form': form})
    return render(request, 'home.html', {'songs':songs, 'members':members,
                                        'infos':infos, 'form': form})

def impressum (request):
    return render(request, 'impressum.html',)
