import nltk
from nltk.book import *

#Exercises
#1
phrase=['Just','another','day']
phrase+phrase

#2
word_token=nltk.corpus.gutenberg.words('austen-persuasion.txt')   
len(word_token)
len(set(word_token))

#3
nltk.corpus.brown.categories()
for i in nltk.corpus.brown.categories():
    try:
        print(len(nltk.corpus.brown.words(categories=i)))
    except ValueError:
        print('Handled ValueError')
        print(i)
#4 Plotting occurences of 'men','women' and 'people' in all the state union addresses
cfd=nltk.ConditionalFreqDist(
    (target,i[0:4])
    for i in nltk.corpus.state_union.fileids()
    for w in nltk.corpus.state_union.words(fileids=i)
    for target in ['men','women','people']
    if w.lower() in target
    )            
cfd.plot()

#5
#Meronyms-part of
#Holonyms-Derived from 

#7
for i in range(1,10):
    print(nltk.book.texti.concordance('however'))

text1.concordance('however')

#8
    
nltk.corpus.names.fileids()
nfd=nltk.FreqDist(
    (gender,i)
    for gender in nltk.corpus.names.fileids()
    for count(i[0:1]) in nltk.corpus.names.words(fileids=gender)
    )


d={}
for i in nltk.corpus.names.fileids():
    d={}
    for j in nltk.corpus.names.words(fileids=i):
        if j[0:1] in d:
            d[j[0:1]]=d[j[0:1]]+1
        else:
            d[j[0:1]]=1
    if i=='male.txt':
        male_initials=d
    else:
        female_initials=d
male_initials    
female_initials   

#9
text1.concordance('monstrous')
text2.concordance('monstrous')
text2.similar('monstrous')
text1.vocab()

#10
#Accounting how many words make up one third of all the words used
word_token_count={}
type(word_token_count)
for i in text2.tokens:
    if i in word_token_count:
        word_token_count[i]=word_token_count[i]+1
    else:
        word_token_count[i]=1
word_token_count=sorted(word_token_count.items(),key=lambda x:x[1],reverse=True)

total=0
for i in word_token_count:
    total=total+i[1]
total
one_third=0
for i in word_token_count:
    one_third=one_third+i[1]
    print(one_third)
    if one_third>=round(1/3*(total),0):
        #print(word_token_count.index(i),i)
        print("A third of all words are accounted by {} different words".format(word_token_count.index(i)))
        break
    else:
        pass

#11
nltk.corpus.brown.categories()
fdist=nltk.FreqDist(w.lower() for w in nltk.corpus.brown.words())

for i in nltk.corpus.brown.categories():
    print("Category : "+i)
    fdist=nltk.FreqDist(w.lower() for w in nltk.corpus.brown.words(categories=i))
    for j in modal:
        print("{}: {}".format(j,fdist[j]),end=" ")
    print(" ")    

#12
entries=list(nltk.corpus.cmudict.entries()) 
nltk.corpus.cmudict.words()
for i in nltk.corpus.cmudict.entries()[0:10]:
    print(i[0],i)

for word,pron in nltk.corpus.cmudict.entries():
    if len(pron)>1:
        print(word,pron)
        
#Fraction of words with more than 1 pronunciation 
(len(entries)-len(set(nltk.corpus.cmudict.words())))/len(entries)*100

#13
noun_synsets=list(wn.all_synsets('n'))

def no_hyponyms_noun():
    no_hyponyms=[]
    for i in noun_synsets:
        if i.hyponyms()==[]:
            no_hyponyms.append(i)
    return(len(no_hyponyms)/len(noun_synsets)*100)        
no_hyponyms_noun()
#For getting hyponyms(),use wn.synset('sulky.n.01').hyponyms() 

#14
#Function supergloss which returns definition of a word and its hypernym and hyponym
def supergloss(s):
    return("{}: ".format(s)+"{}".format(s.definition())
            +"Hypernyms are :".join([i.definition() for i in s.hypernyms()])
            +"Hyponyms are :".join([i.definition() for i in s.hyponyms()]))
supergloss(wn.synset('sulky.n.01'))  

#15
def tri_words():
    for i in list(nltk.corpus.brown.words()):
        if list(nltk.corpus.brown.words()).count('i')>=3:
            print(i)
tri_words()

#16
#Calculating lexical diversity for all genres of brown corpus 
def lexical_diversity():
        for i in nltk.corpus.brown.categories():
            print("{}".format(i)+" "+str(round(len(set(nltk.corpus.brown.words(categories=i)))/len(nltk.corpus.brown.words(categories=i)),2)))
lexical_diversity()            
#Highest diversity is seen surprisingly for Humour.Science Fiction and Reviews are close second and third.

#17
def freq_words(text):
    count_dict={}
    text_list=[]
    from nltk.tokenize import RegexpTokenizer
    alphanumeric_tokenizer=RegexpTokenizer(r'\w+')
    #i=alphanumeric_tokenizer(i)
    for j in text:
        j=alphanumeric_tokenizer.tokenize(j)
        if j!=[]:
            text_list.append(j[0])
        else:
            pass
    for i in range(0,len(text_list)):
        if text_list[i] in count_dict:
            count_dict[text_list[i]]=count_dict[text_list[i]]+1
        elif text_list[i] not in nltk.corpus.stopwords.words(fileids='english'):
            count_dict[text_list[i]]=1
    from operator import itemgetter        
    return(sorted(count_dict.items(),key=itemgetter(1),reverse=True))      
freq_words(text3)


#18
def bigram(text):
    bigram={}
    text_list=[]
    from nltk.tokenize import RegexpTokenizer
    alphanumeric_tokenizer=RegexpTokenizer(r'\w+')
    for j in text:
        j=alphanumeric_tokenizer.tokenize(j)
        #print(j)
        if j!=[]:
            text_list.append(j[0])
        else:
            pass
        #print(text_list)
    for i in range(0,len(text_list)-1):
        if (text_list[i],text_list[i+1]) in bigram and text_list[i] not in nltk.corpus.stopwords.words(fileids='english') and text_list[i+1] not in nltk.corpus.stopwords.words(fileids='english'):
            bigram[(text_list[i],text_list[i+1])]=bigram[(text_list[i],text_list[i+1])]+1
        elif text_list[i] not in nltk.corpus.stopwords.words(fileids='english')  and text_list[i+1] not in nltk.corpus.stopwords.words(fileids='english'): 
            bigram[(text_list[i],text_list[i+1])]=1
    return(sorted(bigram,key=bigram.get,reverse=True))

bigram(text8)    
len(set(list(nltk.bigrams(text8))))

#20
#Function computing frequency for a particular word in a section of brown corpus
def word_freq(word,section):
    word_count={}
    for i in nltk.corpus.brown.words(categories=section):
        #print(i)
        if i==word and i in word_count:
            word_count[i]=word_count[i]+1
        else:
            word_count[i]=1
    print(word_count[word])    
    #return(word_count[word])        

word_freq('The','fiction') 


#Program for editing contents of a file
#Opening file in read mode and making an object out of its contents
with open('/Users/himanshusanjivjagtap/Downloads/ProductTest_duplicate_copy.sql','r+',encoding='utf-8') as file:
        lines=file.readlines()
#Writing contents of the file in a new file        
with open('/Users/himanshusanjivjagtap/Downloads/ProductTest_duplicate_copy copy.sql','w',encoding='utf-8') as file:
    for line in lines:
        counter=0
        for word in line.split(" "):
            if word[0:5] in dict.keys():
                print(word[0:5])
                line=line.replace(word[0:5],str(dict[word[0:5]]))
                file.write(line)
                counter+=1
            elif word[1:6] in dict.keys():
                print(word[1:6])
                line=line.replace(word[1:6],str(dict[word[1:6]]))
                file.write(line)
                counter+=1
        if counter==0:
            file.write(line)

#21
#Guessing number of syllable in a text using CMU pronouncing dictionary
def syllable_count(text):
    count=0
    dict=nltk.corpus.cmudict.dict()
    for word in text:
        if word in dict.keys():
            for j in dict[word]:
                #print(j,len(j))
                count+=len(j)
            #count+=len(nltk.corpus.cmudict.dict()[word])
            #print(count)
    return(count)        

syllable_count(text1)            

#23
#Zipf's law 
def freq_count(text):
    from collections import OrderedDict
    from operator import itemgetter
    freq_dict={}
    for i in text:
        if i in freq_dict:
            freq_dict[i]=freq_dict[i]+1
        elif i not in nltk.corpus.stopwords.words() and i not in freq_dict:
            freq_dict[i]=1
    freq_dict=list(sorted(freq_dict.items(),key=itemgetter(1),reverse=True))
    print(freq_dict)
    #print(type(freq_dict))
    #x,y=[i[0],i[1] for i in freq_dict]
    from matplotlib import pyplot as plt
    plt.plot(sorted([i[0] for i in freq_dict if i[1]>1000]),[i[1] for i in sorted(i for i in freq_dict if i[1]>1000)])
    #plt.yscale('log')
    plt.xlabel('WORD')
    plt.ylabel('COUNT')
    plt.title("ZIPF'S LAW")
    #plt.yscale('log')
freq_count(text5)

#24
#Generating random text using bigram
def generate_model(text,word,num=15):
    bigram_list=bigram(text)
    for i in range(num):
        print(word,end=' ')
        for j in bigram_list:
            if j[0].lower()==word.lower() and j[1] in [k[0] for k in bigram_list]:
                word=j[1]
                bigram_list.pop(bigram_list.index(j))
                break
            else:
                bigram_list.pop(bigram_list.index(j))
        else:
            break
        
        
generate_model(text1,'The')        
bigram(text5)


def freq_words(list):
    count_dict={}
    text_list=[]
    from nltk.tokenize import RegexpTokenizer
    alphanumeric_tokenizer=RegexpTokenizer(r'\w+')
    #i=alphanumeric_tokenizer(i)
    for j in list:
        j=alphanumeric_tokenizer.tokenize(j)
        if j!=[]:
            #print(j[0])
            text_list.append(j[0])
        else:
            pass
    for i in range(0,len(text_list)):
        if text_list[i] in count_dict:
            count_dict[text_list[i]]=count_dict[text_list[i]]+1
        elif text_list[i] not in nltk.corpus.stopwords.words(fileids='english'):
            count_dict[text_list[i]]=1
    from operator import 
    return(sorted(count_dict.items(),key=itemgetter(1),reverse=True))      

freq_words(text3)

#Generating random text using most likely words 
def generate_most_likely(list):
    words=freq_words(list)
    #print(words)
    import random
    for j in range(0,5):
        words_list=[]
        words_list=[i[0] for i in words[50*j:50*j+50]]
        print(random.choice(words_list),end=" ")
    print(" ")
        
for i in nltk.corpus.brown.categories():
    if i in ('romance','science_fiction'):
        generate_most_likely(nltk.corpus.brown.words(categories=i))


#25
def find_language(string):
    for i in nltk.corpus.udhr.fileids():
        if string in nltk.corpus.udhr.words(fileids=i) and nltk.corpus.udhr.encoding(i).lower()=='Latin-1'.lower():
            print(i)
find_language('')        

#26
count=0
length=0
for i in wn.all_synsets('n'):
    #print(i)
    hyponym_list=i.hyponyms()
    hypernym_list=i.hypernyms()
    if len(hyponym_list)!=0 and len(hypernym_list)!=0:
        #print(len(hypernym_list))
        length+=len(hypernym_list)
        count+=1
    #print(length)
    #print(count)
print(round((length/count),2))   


#27
import nltk
from nltk.corpus import wordnet as wn
len(wn.synsets('dog', 'n'))
for i in ['n','v']:
    count=0
    length=0
    for j in wn.all_lemma_names(pos=i):
        #print(j)
        length+=len(wn.synsets(j,i))
        count+=1
    print(round((length/count),2))    

#28
car=wn.synset('car.n.01')
automobile=wn.synset('automobile.n.01')
car.path_similarity(automobile)
wn.synsets('car')
wn.synsets('car')
similarity_list=[('car','automobile'),('gem','jewel'),('journey','voyage'),('boy','lad'),('coast','shore'),('asylum','madhouse'),('magician','wizard'),('midday','noon'),('furnace','stove'),('food','fruit'),('bird','cock'),('bird','crane'),('tool','implement'),('brother','monk'),('lad','brother'),('crane','implement'),('journey','car'),('monk','oracle'),('cemetery','woodland'),('food','rooster'),('coast','hill'),('forest','graveyard'),('shore','woodland'),('monk','slave'),('coast','forest'),('lad','wizard'),('chord','smile'),('glass','magician'),('rooster','voyage'),('noon','string')] 
for i in similarity_list:
    from nltk.corpus import wordnet as wn
    synsets_list_1=wn.synsets(lemma=i[0])
    synsets_list_2=wn.synsets(lemma=i[1])
    print(round((synsets_list_1[0].path_similarity(synsets_list_2[0])),2))
    
wn.synsets(lemma=str(car))    
    


