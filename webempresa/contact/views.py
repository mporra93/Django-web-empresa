from django.shortcuts import render, redirect
from django.urls import reverse

from django.core.mail import EmailMessage

from .forms import ContactForm



# Create your views here.
def contact(request):
    # print('TIPO DE PETICION: {}'.format(request.method))
    
    contact_form = ContactForm()
    
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            #Enviamos correo y redireccionamos 
            email = EmailMessage(
                "La Cafferiera: Nuevo Mensaje de contacto",
                "De {name} <{}>\n\n{}".format(name, email, content),
                'do_not_reply@inbox.mailtrap.io',
                ["matias.ie@gmail.com",],
                reply_to=[email]
            )
            try:
                email.send()
                return redirect(reverse('contact')+"?ok")
            except:
                return redirect(reverse('contact')+"?fail")

    return render(request, "contact/contact.html", {'form':contact_form})
