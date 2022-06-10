
import random #membantu dalam membuat list kata agar chattbot yang dibuat tidak monoton dengan respon jawabannya
import nltk #untuk tokenisasi (library yang menyediakan corpus yang akan kita pakai dalam membuat chattbot)
import string #untuk keperluan data bertype string
from sklearn.feature_extraction.text import CountVectorizer #untuk ekstraksi fitur (atau vektorisasi) 
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np #library Python dasar untuk perhitungan matematis dan ilmiah.
import warnings #mendeteksi program jika terjadi error
warnings.filterwarnings('ignore') #mendeteksi program jika terjadi error

nltk.download('punkt')

with open ('testingdbwisata2.txt','r') as file:
  content = file.read()
  print(content)

from nltk.tokenize import word_tokenize, wordpunct_tokenize,sent_tokenize

sentences = sent_tokenize(content)
print(sentences)

#a function to return a random greeting response to a users greeting
def greeting_response(text):
    text = text.lower()
    
    #Bots greeting respone
    bot_greetings = ['halo','hai']
    
    #Users greeting
    user_greetings = ['Haloo jugaa','Haii there','Greetings']
    
    for word in text.split():
        if word in user_greetings:
            return random.choice(bot_greetings)
        
    #Random response to greeting
    def gratitude_response(text):
        text=text.lower()

def index_sort(list_var):
    length = len(list_var)
    list_index = list(range(0, length))
    
    x = list_var        
    for i in range(length):
        for j in range(length):
            if x[list_index[i]] > x[list_index[j]]:
                #swap
                temp = list_index[i]
                list_index[i] = list_index[j]
                list_index[j] = temp
                
    return list_index

# Creat Bots Response
def bot_response(user_input):
    user_input=user_input.lower()
    sentences.append(user_input)
    bot_response= ''
    cm=CountVectorizer().fit_transform(sentences)
    similarity_scores=cosine_similarity(cm[-1],cm)
    similarity_scores_list=similarity_scores.flatten()
    index=index_sort(similarity_scores_list)
    index=index[1:]
    response_flag=0
    
    j=0
    for i in range(len(index)):
        if similarity_scores_list[index[i]]>0.0:
            bot_response=bot_response+' '+sentences[index[i]]
            response_flag=1
            j=j+1
        if j>2:
            break

        if response_flag==0:
            bot_response=bot_response+" "+"Maaf, saya tidak mengerti"

        sentences.remove(user_input) 

        return bot_response

#Start Chat
print("Doc Bot: What's you need?")

exit_list=['exit','bye','keluar','quit','done']

while(True):
    user_input=input()
    if user_input.lower() in exit_list:
        print('Doc Bot: Terima kasih, sampai jumpa lagi!')
        break
    else:
        if greeting_response(user_input)!= None:
            print('Doc Bot: '+ greeting_response(user_input))
        else:
            print('Doc Bot: '+ bot_response(user_input))

