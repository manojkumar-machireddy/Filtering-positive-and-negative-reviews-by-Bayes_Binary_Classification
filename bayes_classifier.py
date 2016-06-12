#!/usr/bin/python

from __future__ import division

word_freq_p = {};
word_freq_n = {};

word_count_p = 0;
word_count_n = 0;

p_samples = 0;
n_samples = 0;

word_prob_p = {};
word_prob_n = {};

p_prob = 0;
n_prob = 0;



def update_words(document, status):
  status = status.rstrip("\n");
  words = document.split(' ');
  global word_count_p;
  global word_count_n;
  global word_freq_p;
  global word_freq_n;
  if( status == 'p' ):
   for word in words:
     word_count_p = word_count_p + 1;
     if( word in word_freq_p.keys() ):
       word_freq_p[word] = word_freq_p[word] + 1;
     else:
       word_freq_p[word] = 1;
       word_freq_n[word] = 0;
  else :
   for word in words:
     word_count_n = word_count_n + 1;
     if( word in word_freq_n.keys() ):
       word_freq_n[word] = word_freq_n[word] + 1;
     else:
       word_freq_n[word] = 1;
       word_freq_p[word] = 0;
   


def train():
  global word_prob_p;
  global word_prob_n;
  global word_count_p;
  global word_count_n;
  global word_freq_p;
  global word_freq_n;
  global p_samples;
  global n_samples;

  training_file = open("train.txt",'r');
  for line in training_file:
    doc = line.split(':');
    doc[1] = doc[1].rstrip('\n');
    if( doc[1] == 'p'): 
      p_samples += 1;
    else :
      n_samples += 1;
    update_words(doc[0],doc[1]);
  for word in word_freq_n.keys():
    word_prob_p[word] = float(word_freq_p[word]/word_count_p);
    word_prob_n[word] = float(word_freq_n[word]/word_count_n);

    if( word_prob_p[word] == 0 ):
      word_prob_p[word] = 1
    if( word_prob_n[word] == 0 ):
      word_prob_n[word] = 1

    print word_freq_p[word], word_count_p, word_prob_p[word];


def predict():
  predict_file = open("predict.txt", 'r');
  line = predict_file.readline();
  words = line.split(' ');
  final_prob_p = 1;
  final_prob_n = 1;
  for word in words:
    if( word in word_prob_p.keys()):
       final_prob_p = final_prob_p * word_prob_p[word];
    if( word in word_prob_n.keys()):
       final_prob_n = final_prob_n * word_prob_n[word];
    
  final_prob_p = final_prob_p * p_prob;
  final_prob_n = final_prob_n * n_prob;
  if( final_prob_p > final_prob_n):
    print "This document is positive"
  else :
    print "This document is negative"
  pass;


train();

p_prob = p_samples/(p_samples+n_samples);
n_prob = n_samples/(p_samples+n_samples);

print word_freq_p;
print word_freq_n;

print "";
print word_count_p;
print word_count_n;

print "";
print word_prob_p;
print word_prob_n;

print "";
print p_prob;
print n_prob;

print "";
print "";
print "";
print "";
print "";

predict();





