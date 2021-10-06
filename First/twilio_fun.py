
from twilio.rest import Client

ACCOUNT_SID = 'AC4e6b71910edc727de5a4b32e82ddd527'
AUTH_TOKEN = 'cc5d59a41783f8306f4e6125fb43f946'

c = Client(ACCOUNT_SID,AUTH_TOKEN)

m = c.messages.create(
    body="Twilio Here",
    from_= "+19363427869" ,
    to= "+917837040632"
)
print(m)

def send_sms(ACCOUNT_SID,AUTH_TOKEN,body,from_,to_):
    from twilio.rest import Client
    c = Client(ACCOUNT_SID,AUTH_TOKEN)

    m = c.messages.create(
        body=body,
        from_= from_ ,
        to = to_
    )

