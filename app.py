#from crypt import methods
from flask import Flask, render_template,request
app=Flask(__name__)

# Importing the Libraries

from tensorflow.keras.models import load_model
import numpy as np
import pickle

# Load the model and tokenizer

model = load_model('nextword1.h5')
tokenizer = pickle.load(open('tokenizer1.pkl', 'rb'))

predicted_text=""

def Predict_Next_Words(model, tokenizer, text):
    """
        In this function we are using the tokenizer and models trained
        and we are creating the sequence of the text entered and then
        using our model to predict and return the the predicted word.
    
    """
    for i in range(3):
        sequence = tokenizer.texts_to_sequences([text])[0]
        sequence = np.array(sequence)
        
        preds= np.argmax(model.predict(sequence), axis=-1)
        predicted_word = ""
        
        #print(preds)
        #print(tokenizer.word_index.items())
        
        li=[]
        global predicted_text
        predicted_text=""
        for key in tokenizer.word_index:
            if(tokenizer.word_index[key] in preds):
                #print(key)
                li.append(key)
                predicted_text=key
            
        #print(li)
        #return li
        return predicted_text

"""
    We are testing our model and we will run the model
    until the user decides to stop the script.
    While the script is running we try and check if 
    the prediction can be made on the text. If no
    prediction can be made we just continue.

"""

# text1 = "at the dull"
# text2 = "collection of textile"
# text3 = "what a strenuous"
# text4 = "stop the script"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def getvalue():
    name=request.form['name']
    #print(name)

    text = name
    if text == "stop the script":
        print("Ending The Program.....")

    else:
        try:
            text = text.split(" ")
            text = text[-1]

            text = ''.join(text)
            Predict_Next_Words(model, tokenizer, text)
            
        except:
            global predicted_text
            predicted_text=""

    return render_template('index.html', n=name, predicted_text=predicted_text)

if __name__=="__main__":
    app.run(debug=True)
