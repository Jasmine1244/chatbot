import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import Word_tokenize
import random
nltk.download('punkt')
nltk.download('wordnet')
lemmmatizer=WordNetLemmatizer()
intents={
    'greeting':['hello','hi','hey'],
    'goodbye':['bye','goodbye','see you later'],
    'thanks':['thank you','thanks','appreciate it'],
}
responses={
    'greeting':['hi!,how are you?','hello!','hey'],
    'goodbye':['see you late!','bye','goodbye'],
    'thanks':['you\re welcome','no problem','any time']

}
def process_input(input_text):
    tokens=Word_tokenize(input_text)
    tokens=[lemmmatizer.lemmatize(tokens)for tokens in tokens]
    return tokens
def determine_intent(tokens):
    for token in token:
        for intent, keywords in intents.items():
         if token.lower() in keywords:
            return intents
    return None
def generate_response(intent):
   return random
def chatbot():
   print('chatbot:hi! i am here to help you. ')
   while Ture:
      user_input= input ('you: ')
      tokens= process_input(user_input)
      intent= determine_intent(tokens)
      if intent :
         response = generate_response(intent)
         print('chatbot:',response)
      else: 
         print('chatbot: sorry, i did not understand that.')    
        