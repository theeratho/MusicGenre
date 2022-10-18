#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from pydub import AudioSegment 
from pydub.utils import make_chunks
import os

path = "/Users/home/Desktop/Music_genre/Data/genres_original"
dirs = os.listdir(path) 
def process_sudio(file_name):
    myaudio = AudioSegment.from_file(file_name,"wav")
    chunk_length_ms = len(myaudio)/10 # pydub calculates in millisec 
    chunks = make_chunks(myaudio,chunk_length_ms) #Make chunks of one sec 
    for i, chunk in enumerate(chunks):
        if i, chunk == 1000 :
            break
        chunk_name = './chunked/' + file_name + "_{0}.wav".format(i) 
        print ("exporting", chunk_name) 
        chunk.export(chunk_name, format="wav") 

all_file_names = os.listdir(path)

try:
    os.makedirs('chunked') # creating a folder named chunked
except:
    pass
for each_file in all_file_names:
    if ('.wav' in each_file):
        process_sudio(each_file)

