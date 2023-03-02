from django.shortcuts import render
from twilio.rest import Client
from app.settings import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN
from django.http import HttpResponse

# Create your views here.
order_details = {
    'remetente': 'Priscila Postol Petrentchuck',
    'assunto': 'Exclusão de usuario',
    'data': '20 de Janeiro de 2023',
    'hora': '10:26'
}

def send_notification(request):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    if request.method == 'POST':
         
        user_whatsapp_number = request.POST['user_number']

        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body='Tem um novo chamado no suporte de *{}* com o assunto *{}* na data de *{}* e na hora *{}*'.format(
                order_details['remetente'], order_details['assunto'], order_details['data'],
                order_details['hora']),
            to='whatsapp:+{}'.format(user_whatsapp_number)
        )

        print(user_whatsapp_number)
        print(message.sid)
        return HttpResponse('Great! Expect a message...')

    return render(request, 'phone.html')