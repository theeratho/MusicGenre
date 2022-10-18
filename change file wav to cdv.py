#!/usr/bin/env python
# coding: utf-8

# In[2]:


import librosa as lr
import numpy as np
from glob import glob
import csv
import os
import warnings
warnings.filterwarnings('ignore')

data_dir='/Users/home/Desktop/Music_genre/Data/genres_makeup'
#getting path of all the files with .au extension in a list
audio_files=glob(data_dir+'/blues'+'/*.wav')
list3=['/classical','/country','/disco','/hiphop','/jazz','/metal','/pop','/reggae','/rock']
for element in list3 :
    to_extend=glob(data_dir+element+'/*.wav')
    audio_files.extend(to_extend)
    
print(len(audio_files))


#sample feature extraction of 1 audio file
#loading the audio
x, sr = lr.load(audio_files[0])
S, phase = lr.magphase(lr.stft(x))

zero_crossings_rate_mean= lr.feature.zero_crossing_rate(x)
print("zero crossing rate of the file is",np.mean(zero_crossings_rate_mean))

zero_crossings_rate_var= lr.feature.zero_crossing_rate(x)
print("zero crossing rate of the file is",np.var(zero_crossings_rate_var))

spectral_centroids_mean = lr.feature.spectral_centroid(x, sr)
print("spectral_centroid of the file is",np.mean(spectral_centroids_mean))

spectral_centroids_var = lr.feature.spectral_centroid(x, sr)
print("spectral_centroid of the file is",np.var(spectral_centroids_var))

spectral_rolloff_mean = lr.feature.spectral_rolloff(x+0.01, sr=sr)
print("spectral_rolloff of the file is",np.mean(spectral_rolloff_mean))

spectral_rolloff_var = lr.feature.spectral_rolloff(x+0.01, sr=sr)
print("spectral_rolloff of the file is",np.var(spectral_rolloff_var))

spectral_bandwidth_mean = lr.feature.spectral_bandwidth(x, sr=sr)
print("spectral_bandwidth of the file is",np.mean(spectral_bandwidth_mean))

spectral_bandwidth_var = lr.feature.spectral_bandwidth(x, sr=sr)
print("spectral_bandwidth of the file is",np.mean(spectral_bandwidth_var))

rms_mean = lr.feature.rms(S=S)
print("rms of the file is",np.mean(rms_mean))

rms_var = lr.feature.rms(S=S)
print("rms of the file is",np.var(rms_mean))

tempo = lr.beat.beat_track(x, sr=sr)
print("tempo of the file is",tempo[0])

##harm_mean, perc_mean = lr.effects.hpss(x)
##print("harmony of the file is",np.mean(harm_mean))

##harm_var, perc_var = lr.effects.hpss(x)
##print("harmony of the file is",np.var(harm_mean))

##harm_mean, perc_mean = lr.effects.hpss(x)
##print("perc of the file is",np.mean(perc_mean))

##harm_var, perc_var = lr.effects.hpss(x)
##print("harmony of the file is",np.var(perc_var))

hop_length = 512
chromagram_mean = lr.feature.chroma_stft(x, sr=sr, hop_length=hop_length)
print("chromagram of the file is",np.mean(chromagram_mean))

chromagram_var = lr.feature.chroma_stft(x, sr=sr, hop_length=hop_length)
print("chromagram of the file is",np.var(chromagram_var))





mfcc = lr.feature.mfcc(x, sr=sr)
i=1
for e in mfcc :
    print("mfcc_mean",i,"of the file is",np.mean(e))
    print("mfcc_var",i,"of the file is",np.var(e))
    i=i+1

#making a csv file
with open('genere_features.csv','w',newline ="") as file :
    TheWriter=csv.writer(file)
    l=["file name","zero_crossings_rate_mean","zero_crossings_rate_var","spectral_centroid_mean","spectral_centroid_var","Spectral Rolloff_mean","Spectral Rolloff_var","spectral_bandwidth_mean","spectral_bandwidth_var","rms_mean","rms_var","tempo","Chroma features_mean","Chroma features_var"]
    i="a"
    for e in mfcc :
        x="mfcc_mean"+"_"+i
        l.append(x)
        x="mfcc_var"+"_"+i
        l.append(x)
        i=chr(ord(i)+1)
    x="genre"
    l.append(x)
    TheWriter.writerow(l)
    i=1
    for audio in audio_files :
        x, sr = lr.load(audio,mono=True,duration=30)
        S, phase = lr.magphase(lr.stft(x))
        zero_crossings_rate=lr.feature.zero_crossing_rate(x)
        spectral_centroids = lr.feature.spectral_centroid(x, sr)
        spectral_rolloff = lr.feature.spectral_rolloff(x+0.01, sr=sr)
        spectral_bandwidth = lr.feature.spectral_bandwidth(x, sr=sr)
        rms = lr.feature.rms(S=S)
        tempo = lr.beat.beat_track(x, sr=sr)
        hop_length = 512
        chromagram = lr.feature.chroma_stft(x, sr=sr, hop_length=hop_length)
        mfcc = lr.feature.mfcc(x, sr=sr)
        list1=[audio,np.mean(zero_crossings_rate),np.var(zero_crossings_rate),np.mean(spectral_centroids),np.var(spectral_centroids),np.mean(spectral_rolloff),np.var(spectral_rolloff),np.mean(spectral_bandwidth),np.var(spectral_bandwidth),np.mean(rms),np.var(rms),tempo[0],np.mean(chromagram),np.var(chromagram)]
        to_extd=[]
        for e in mfcc :
            to_extd.append(np.mean(e))
            to_extd.append(np.var(e))
        list1.extend(to_extd)
        if i>0 and i<1001 :
            x="blues"
            list1.append(x)
        elif i>1000 and i<2001 :
            x="classical"
            list1.append(x)
        elif i>2000 and i<3001 :
            x="country"
            list1.append(x)
        elif i>3000 and i<4001 :
            x="disco"
            list1.append(x)
        elif i>4000 and i<5001 :
            x="hiphop"
            list1.append(x)
        elif i>5000 and i<6001 :
            x="jazz"
            list1.append(x)
        elif i>6000 and i<7001 :
            x="metal"
            list1.append(x)
        elif i>7000 and i<8001 :
            x="pop"
            list1.append(x)
        elif i>8000 and i<9001 :
            x="reggae"
            list1.append(x)
        else :
            x="rock"
            list1.append(x)

        i=i+1
        TheWriter.writerow(list1)

