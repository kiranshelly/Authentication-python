
from twilio.rest import Client

ACCOUNT_SID = Your Number
AUTH_TOKEN = Your Number

c = Client(ACCOUNT_SID,AUTH_TOKEN)

m = c.messages.create(
    body="Twilio Here",
    from_= Your Twilio Number,
    to= Your NUmber
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

