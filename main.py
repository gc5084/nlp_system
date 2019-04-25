from dialog_manager import dialog_manager
from speech import speech_recognition_client, text_to_speech_client

EXAMPLE_SENTENCES = ['Hi, what is the price of the bitcoin ?',
                     'Give me the price of the bitcoin',
                     'price of the bitcoin',
                     'Show me the price of the Bitcoin',
                     'List me the price of the Euro',
                     'Display the high for the Ripple',
                     'List me the low of the Ripple',
                     'What was the price for the Euro last week  ?']

# Initialize information
recognizer = speech_recognition_client.SpeechRecognizer()
synthesizer = text_to_speech_client.SpeechSynthesizer()
dialog_manager = dialog_manager.DialogManager()

# Start the dialogue
#synthesizer.talk("Hello, My Name is Ana and I will be your Stock Assistant. " + START_CONVERSATION)
#name = recognizer.listen()
#synthesizer.talk("Hello, " + name + " please tell me your request")

conversation_active = True

while conversation_active:
    print("Speak!")
    text = EXAMPLE_SENTENCES[7]#recognizer.listen()
    text_lowercase = text.lower()
    if text_lowercase is None:
        synthesizer.talk("Sorry I couldn\'t understand you, please repeat.")

    print("Text recognized " + text_lowercase)
    dialog_manager.process_input(text_lowercase)
    current_state = dialog_manager.get_state()

    synthesizer.talk(text_lowercase)
