from twilio.rest import TwilioRestClient

account_sid = "" # Your Account SID from www.twilio.com/console
auth_token  = ""  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Fantastic Beasts and where to find them, catch it in IMAX 3D - 19 Nov",
    to="+",    # Replace with your phone number
    from_="+") # Replace with your Twilio number

print(message.sid)
