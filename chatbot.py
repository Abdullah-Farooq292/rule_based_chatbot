#rule based chatbot

#dictianary for responses
responses = {
    'hello' : 'hi there!',
    'hey' : 'hello there!',
    'how are you?' : 'fine, how about you?',
    'what is your name?' : 'my name is decode, the decodelabs ai assistant!',
    'what do you do?' : 'im a rule based chatbot',
    'what is decodelabs?' : 'decodeLabs is a tech training company offering internships and industry projects across multiple domains!',
    'could you help me with something?' : 'ofcourse! what do you need help with?',
    'help' : 'what do you need help with?',
    'thank you' : 'you are welcome!',
    'thanks' : 'anytime!',
    'bye' : 'goodbye!',
    'goodbye' : 'bye, take care!'
}

#starting the chatbot
print("Decode: Hello! I am Decode, the DecodeLabs Assistant. Type 'exit' to quit.")

while True:
    raw_input = input('you: ')
    clean_input = raw_input.lower().strip()

    if clean_input == 'exit':
        print("Decode: Exiting......have a nice day!")
        break

    reply = responses.get(clean_input, "I'm not sure I understand. Could you rephrase that?")
    print("Decode: ", reply)