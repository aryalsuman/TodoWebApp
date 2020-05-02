from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC61d15871cc83d172d898fc36561da08d'
auth_token = '54ec1b78c40d8f0e63b9ca4f47d5f423'
client = Client(account_sid, auth_token)


def Sendsms(messages):
    message = client.messages.create(
        body=messages,
        from_='+16156148527',
        to='+9779847494921'
    )
    return


# client = Client(account_sid, auth_token)
# message = client.messages.create(
#     body=messages,
#     from_='+16156148527',
#     to='+9779847494921'
# )
# print(message.sid)
