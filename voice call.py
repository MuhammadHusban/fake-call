import messagebird

#create instance of messagebird.Client using API key
client = messagebird.Client('SgWOZDnxzhQgqooiL2JdjvYCn')

try:
    msg = client.voice_message_create('+3151045416', 'Hey you, a little bird told me you wanted a call!', { 'voice' : 'male' })
    print(msg.__dict__)

except messagebird.client.ErrorException as e:
    for error in e.errors:
        print(error)