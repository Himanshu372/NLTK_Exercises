#4
words=['is','NLP','fun','?']
tmp=words[1]
words[1]=words[0]
words[0]=tmp
words[3]='!'
words
words[0],words[1],words[2]=words[1],words[0],'!'


#9
#a
s=' Tenacity  is  the  key '
' '.join(i for i in s.split())
#b
import re 
' '.join(re.findall(r'\w+',s))


#10

def cmp_len(a,b):
    return (len(a)>len(b))-(len(a)<len(b))
cmp_len('Himanshu','Troy')    

#11
#a
sent1=['Tenacity','is','the','key']
sent2=sent1[:]
sent1[1]='was'
sent2
#b 
text1=[['Hi I am Himanshu'],['Tenacious'],['Workaholic'],['Persistence']]
text2=text1[:]
text1[0][0]='Monty'
text2
#c
from copy import deepcopy
help(deepcopy)
deepcopy(text1)


#12 
word_table=[['']*10]*10
word_table[1][2]='hello'
word_table


word_table=set([['' for i in range(10)] for j in range(10)])
word_table[1][2]='hello'  
word_table

#13
word_vowels=[[]]
words=['The', 'dog', 'gave', 'John', 'the', 'newspaper', 'The', 'cat', 'miowed']
word_vowels

for word in words:
    if (len(word)>len(word_vowels)-1):
        for i in range(len(word_vowels),len(word)+1):
            word_vowels.append([])
    num_vowels=len(re.findall(r'[aeiouAEIOU]',word))
    if num_vowels>len(word_vowels[len(word)]):
        for j in range(num_vowels+1):
            word_vowels[len(word)].append(set())
    word_vowels[len(word)][num_vowels].add(word)    

word_vowels

#14 
import nltk
def novel10(text):
        splitindex=round(.1*len(text))
        print([i for i in text[-splitindex:] if i not in text[:-splitindex]])

from nltk.book import *
novel10(text3)

#15

def sent_freq(sent):
    import nltk
    freq_dict=nltk.FreqDist(sorted(word.lower() for word in nltk.tokenize.RegexpTokenizer(r'\w+').tokenize(sent)))
    for entry in freq_dict:
        print(entry,str(freq_dict[entry]))

sent_freq('Progress is essential for existence!')  

#16
#a
def gematria(word):
    letter_vals = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':80, 'g':3, 'h':8,
    'i':10, 'j':10, 'k':20, 'l':30, 'm':40, 'n':50, 'o':70, 'p':80, 'q':100,
    'r':200, 's':300, 't':400, 'u':6, 'v':6, 'w':800, 'x':60, 'y':10, 'z':7}
    return sum(letter_vals[i.lower()] for i in word if i.lower() in letter_vals.keys())
gematria('Himanshu')

#b 
[(sum(1 for j in nltk.corpus.state_union.words(fileids=i) if gematria(j)==666),i)for i in nltk.corpus.state_union.fileids()]
 
#c
def decode(text):
    import random 
    random_num=random.randint(1,1000)
    tokenized_text=nltk.RegexpTokenizer(r'\w+').tokenize(text)
    return (random_num,set([i for i in tokenized_text if gematria(i)==random_num]))

from nltk import text1
decode(nltk.corpus.gutenberg.raw(fileids='bible-kjv.txt'))


#17 
def shorten(text,n):
    tokenized_set=set(nltk.RegexpTokenizer(r'\w+').tokenize(text))
    tokenized_text=nltk.RegexpTokenizer(r'\w+').tokenize(text)
    #print(tokenized_text[:100])
    for j in tokenized_set:
        freq=sum(1 for i in tokenized_text if i.lower()==j.lower())
        if freq>=n:
            print(j,freq)
            tokenized_text=[k for k in tokenized_text if k.lower()!=j.lower()]
    return ' '.join(tokenized_text)
import nltk
shorten(' '.join(nltk.book.text3),50)

#18
def getWords(prop, value):
    lexicon = [('fish', 'water animal', 'fish'), ('house', 'building', 'haus'), ('whale', 'water animal', 'wejl')]
    if prop == 'meaning':
        return [w for (w, m, p) in lexicon if m == value]
    if prop == 'pronunciation':
        return [w for (w, m, p) in lexicon if p == value]

getWords('meaning', 'water animal')

#19 
def proximity(synset):
    from nltk.corpus import wordnet as wn
    synset_list=[wn.synset('minke_whale.n.01'),wn.synset('orca.n.01'),wn.synset('novel.n.01'),wn.synset('tortoise.n.01')]
    given_synset=wn.synset(synset)
    return sorted([i for i in synset_list],key=lambda i:given_synset.shortest_path_distance(i))
proximity('right_whale.n.01')        

#20 
def sorted_desc_freq(l):
    return sorted(set(l),key=lambda i:l.count(i),reverse=True)

sorted_desc_freq(['one', 'two', 'two', 'four', 'four', 'four', 'four', 'three', 'three', 'three'])

#21
def set_diff(text,vocab):
    tokenized_text=set(nltk.RegexpTokenizer(r'\w+').tokenize(text))
    tokenized_vocab=vocab.keys()
    return tokenized_vocab.difference(tokenized_text)

#22 
from operator import itemgetter
words=['Efficiency','is','the','key']
sorted(words,key=itemgetter(1))
sorted(words,key=itemgetter(-1))
#Sorts each element according to the referenced element in itemgetter function.


#23 
import nltk
trie={}
def insert(trie, key, value):
    if key:
        first, rest = key[0], key[1:]
        if first not in trie:
            trie[first] = {}
        insert(trie[first], rest, value)
    else:
        trie['value'] = value   
    
insert(trie,'vanguard','vang')
trie

def lookup(trie, key):
    if len(key) == 0:
        if 'value' in trie:
            result = trie['value']
            return result
        elif (len(trie) == 1):
            keys = trie.keys()
            return lookup(trie[keys[0]], '')
        else:
            return 'no value found'
    else:
        if (key[0] in trie):
            return lookup(trie[key[0]], key[1:])
        else:
            return 'no value found'


lookup(trie,'vanguard')


#25 

def edit_distance(source,target):
    n=len(source)
    m=len(target)
    if n==0:
        print('Source string is empty,lenght of target is {}'.format(m))
    elif m==0:
        print('Target string is empty,lenght of source is {}'.format(n))
    d=[[0 for i in range(n+1)] for j in range(m+1)]
    for i in range(n+1):
        d[0][i]=i
    for j in range(m+1):
        d[j][0]=j
    for i in range(1,n+1):
        for j in range(1,m+1):
            if source[i-1]==target[j-1]:
                cost=0
            else:
                cost=1
            d[j][i]=min(d[j-1][i]+1,d[j][i-1]+1,d[j-1][i-1]+cost)
    print("Levenshtein distance between {} and {} is {}".format(source,target,d[m][n]))
            
                
    #    common=0
    #    for c in range(i):
    #        if source[c]==target[c]:
    #            common+=1                
    #    for j in range(1,m+1):
    #        if source[0:i]==target[0:j]:
    #            d[i][j]=0
    #        else:
    #            diff=i-j
    #            print(diff)
    #            cost=diff+(i-common)
    #            print(cost)
    #            d[j][i]=cost
    #           print(d)
        
    
edit_distance('dog','cat')    

#26
def catalan_recursive(num):
    if num==0:
        return 1
    else:
        result=0
        for i in range(num):
            result+=catalan_recursive(i)*catalan_recursive(num-1-i)
        return result    
catalan_recursive(20)            

#In Dynamic Programming, rather than recalculating results for each iteration of loop,we save the result in a data structure and return this results.
def catalan_dynamic(num,d={0:1}):
    if num in d:
        return d[num]
    else:
        result=0
        for i in range(num):
            if i not in d:
                d[i]=catalan_dynamic(i,d)
            if num-1-i not in d:
                d[num-1-i]=catalan_dynamic(num-1-i,d)
            result+=d[i]*d[num-1-i]
        return result    
        
catalan_dynamic(20)  

import timeit
t=timeit.Timer(lambda: catalan_recursive(20))
print(t.timeit(number=10))    
t=timeit.Timer(lambda: catalan_dynamic(20))
print(t.timeit(number=10))
    

#29
import nltk
trie=nltk.defaultdict(dict)
insert(trie, 'chat', 'cat')
insert(trie, 'chien', 'dog')
insert(trie, 'chair', 'flesh')
insert(trie, 'chic', 'stylish')
trie


def print_trie(trie,key=''):
    keys_list=sorted(trie.keys())
    if len(keys_list)==1:
        if keys_list[0]=='value':
            print(key+':\''+trie['value']+'\'')
        else:
            print_trie(trie[keys_list[0]],key+keys_list[0])
    else:
        for i in range(len(keys_list)):
            if i==0:
                print_trie(trie[keys_list[i]],key+keys_list[i])
            else:
                print_trie(trie[keys_list[i]],'-'*len(key)+''.join(keys_list[i]))
                
print_trie(trie) 

#30

def unique_lookup(trie,key,unique='',buffer_unique=''):
    #print(key)
    if len(key)==0:
        if len(buffer_unique)>0:
            return buffer_unique
        else:
            return unique
    if len(trie[key[0]])==1:
        if len(buffer_unique)>0:
            new_unique_buffer=buffer_unique
        else:
            new_unique_buffer=unique+key[0]
        return unique_lookup(trie[key[0]],key[1:],unique+key[0],new_unique_buffer)
    return unique_lookup(trie[key[0]],key[1:],unique+key[0])
    
    
    
def compressed(string):
    trie=nltk.defaultdict(dict)
    import re
    words=re.split(r'\s+',string)
    for w in words:
        insert(trie,w.lower(),w.lower())
    #print(trie)    
    return [unique_lookup(trie,w.lower()) for w in words] 
    
from nltk.book import *
compressed(' '.join(text1))     

print(' '.join(compressed(' '.join(text1)))[:200])       
#Compression ratio
full_text=len(text1)
compressed_text=len(compressed(' '.join(text1)))
print(100*(compressed_text/full_text))


#31
from nltk.book import *  
text=' '.join(text1)[:200]
text
#Adding extra spaces to the text
import re
spaced_text=re.sub(r'\s','  ',text)
import textwrap    
textwrap.wrap(text,width=50)
#Regardless of the spaces,the text gets broken into multiple lines of width=50 in the same manner
textwrap.wrap(spaced_text,width=50)

#32
def sent_freq_dist(doc,n=0):
    "'Function sent_freq_dist(doc,n) is used to return top n sentences from given doc which have highest sum of word frequency.'"
    import re
    #Removing extra spaces and escape characters in doc
    processed_doc=re.sub(r'\s{2,}|\n',' ',doc)
    #Creating a list of words from a given doc, first by splitting the doc on \. and joining by space(' ') in between and then splitting resulting doc on \s.
    words=re.split(r'\s',' '.join([i for i in re.split(r'\.',processed_doc)]))
    #Calculating word frequency using NLTK's in-built FreqDist() function
    word_freq=nltk.FreqDist(words)
    #Creating a list of sentences by splitting processed_doc on \.
    sents=re.split(r'\.',processed_doc)    
    #Creating a list wherein word frequency for each word in a sentence is summed and then sorting the list in descending order
    sorted_list=sorted([(sum([word_freq[j] for j in re.split(r'\s',i)]),i) for i in sents],key=lambda x:x[0],reverse=True)
    print(sorted_list[:n])
    
sent_freq_dist(nltk.corpus.brown.raw(categories='religion'),10)




#34
def wordsquares(n):
    import nltk
    from nltk.corpus import words
    import re
    #Collecting all the words from words corpus with the required length of n
    words_list=[i.lower() for i in re.split(r'\n',words.raw()) if len(i)==n]
    square=[]
    #A cache for words that have already been tested for
    skipwords=[[] for i in range(n)]
    #To check if the word can be added to the square
    def check_agianst_square(word):
        if word in square:
            return False
        for (index,square_word) in enumerate(square):
            if (word[index]!=square_word[len(square)]):
                return False
        return True
    #
    def add_word():
        if len(square)==n:
            return True
        for word in words_list:
            if len(square)==n:
                return True
            print(square)    
            if (word not in skipwords[len(square)]) and check_agianst_square(word):
                square.append(word)
                add_word()
        if len(square) != n and len(square) != 0:
    #Adding words to cache
            skipwords[len(square) - 1].append(square.pop())
    #Resetting parts of cache
            for i in range(len(square) + 1, n):
                skipwords[i] = []
            add_word()
        return False

    #
    if add_word():
        for word in square:
            print(word)
    else:
        print("No squares found")
        
wordsquares(2)    
    
    

