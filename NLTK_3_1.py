#Excercises
#1
s='Colorless'
s[:4]+'u'+s[4:]

#2
#Removing affixes 
l=['dish-es', 'run-ning', 'nation-ality', 'un-do', 'pre-heat']
for i in l:
    print(re.findall(r'\w+',i)[0])

#3
s='Colorless'
s[-len(s)-1]

#4
#Using step size in slicing 
s='Colorless'
s[2:10]

#6
re.findall(r'[a-zA-Z]+',s)
#[a-zA-Z]+ finds the occurence of words in a string 
re.findall(r'[A-Z][a-z]*',s)
#[A-Z][a-z]* finds occurence of words in starting with caps 
re.findall(r'p[aeiou]{,2}t','pout')
#Looks for pattern such as 9.09
re.findall(r'\d+(\.\d+)?','9.09')
#Looks for pattern as described: consonant+vowel+consonant 
([^aeiou][aeiou][^aeiou])*
re.findall(r'([^aeiou][aeiou][^aeiou])*','yey')
#Pattern looks either for alphanumeric tokens or tokens with special characters 
re.findall(r'\w+|[^\w\s]+','´´´')


nltk.re_show(r'\d+(\.\d+)?','8.9.09')
nltk.re_show(r'([^aeiou][aeiou][^aeiou])*','ttyoytt')
nltk.re_show(r'\w+','´´´')

#7
#Looks for a single determiner(a,an,the)
##Still not perfect 
re.findall(r'(\s+a\s+|\s+an\s+|\s+the\s+|[^\w]*a\s+|[^\w]*an\s+|[^\w]*the\s+)','The secret to success is unfathomable amount of work and a tenancity which can be found nowhere'.lower())
#Looks for arithmetic expressions of the form 2*3+8 
re.findall(r'\d+\*\d+\+\d+','yyy2*3+8fernawrn')

#8
#A utility function to extract content from URL 
from bs4 import BeautifulSoup
def extractURL(link):
    from urllib import request
    url=request.urlopen(link).read().decode('utf8')
    return ' '.join(re.split(r'\s+',BeautifulSoup(url).get_text()))
extractURL('http://nltk.org/')

#9
with open('corpus.txt','w+') as file:
    for i in nltk.corpus.gutenberg.words()[:100]:
        print(i,end=" ",file=file)

#Creating a function that returns contents of the file as a string     
def load(f):
    with open(f,'r+') as file:
        return("".join(str(i) for i in file))
load('corpus.txt')            

#Creating a tokenizer to tokenize punctuation in the text 
punct_pattern=r'''(?x)
[,;'-]        #for apostrophes,commas,semi-colons and hyphens
'''
nltk.regexp_tokenize(load('corpus.txt'),punct_pattern) 

#Creating a tokenizer that tokenizes monetary values,dates,names of people and organizations 

pattern=r'''(?x)
\$\d+\.\d+                                   #for currencies
| \d{2}[-/]\d{2}[-/]\d{2,4}                  #for dates 
| [A-Z][a-z]+(?:\s[A-Z][a-z]+)?   #for names of persons and organizations 
'''
text='2010 - $1233.234 NUCLEAR FORENSICS OF SPECIAL NUCLEAR MATERIAL AT LOS ALAMOS: THREE RECENT STUDIES Purchase this article David L. Gallimore, Los Alamos National Laboratory Katherine Garduno, Los Alamos National Laboratory Russell C. Keller, Los Alamos National Laboratory  Nuclear forensics of special nuclear materials is a highly specialized field because there are few analytical laboratories in the world that can safely handle nuclear materials, perform high accuracy and precision analysis using validated analytical methods.'
nltk.regexp_tokenize(text,pattern)
re.findall(r'[A-Z][a-z]+(?:\s[A-Z][a-z]+)?',text)

#Not the perfect regex as it gives false positives such as 'Nuclear' and 'Purchase',but pretty close to what is required.

#10
#List comprehension for a logical loop
sent = ['The', 'dog', 'gave', 'John', 'the', 'newspaper']
result=[(word,len(word)) for word in sent]
result

#11
#Splitting a string on a predefined character 
raw='Programming  is    good'
import re
re.split(r's',raw)

#12
#Printing characters of a string one per line 
raw='Programming  is    good'
for i in raw:
    print(i)

#13
#
raw.split() 
raw.split(' ')
#If the string contains >1 space or tab characters then .split() will split the string again into non-space charachters,while .split(' ') will split the space charachters as well as non-space charachters 

#14
#Difference between sorted() and .sort()
sent.append('last')
sent.sort()
sorted(sent)

#14
#Difference between sort and sorted 
sorted(sent)
sent.sort(key=lambda x:x)
sent.sort(key=lambda x:x[1])
sent
#sorted returns a sorted() object and sort() doesn't return anything but sorts the list upon it is called

#17
name='Himanshu'
print('%6s'%name)

#18
#Reading text from corpus,tokenizing it and printing list of all 'wh' word types 
import nltk
wh_word_list=[]
import re
for i in nltk.tokenize.word_tokenize(nltk.corpus.movie_reviews.raw()):
    if re.match('^(wh)',i)!=None:
        wh_word_list.append(i)
set(sorted(wh_word_list))          

#19
#Reading a key value pair from a file and creating a list of list 
with open('freq.txt','w+') as file:
    words=[('fuzzy',23),('theoretically',35),('policy',40)]
    for i in words:
        print(i[0]+" "+str(i[1]),file=file)

freq_list=open('freq.txt','r').readlines()
[[i.split()[0],int(i.split()[1])] for i in freq_list]


#20
#Accessing a webpage and extracting required info 
sports_mail=extractURL('http://www.dailymail.co.uk/sport/index.html')
import nltk
sent=nltk.Text(nltk.sent_tokenize(sports_mail))
   

#21
#Devising a function unknown() which takes url as its argument and returns all the lowercased words,then segragating words based upon their presence in Words corpora
def unknown(link):
    from bs4 import BeautifulSoup
    from urllib import request
    url=request.urlopen(link).read().decode('utf8')
    words=re.split(r'\s+',BeautifulSoup(url,"lxml").get_text())
    return [i for i in words if i.islower()]    

unknown('http://nltk.org/')
for i in unknown('http://nltk.org/'):
    if re.search(r'^[\("]\s+[\.,]*',i)==None:
        print(i)

#23
#Bifurcating don't into don and 't
str="Why don't you mind your own business saashole"
nltk.regexp_tokenize(str,r'n\'t|\w+')


#24
#Converting text into hAck3r,where e →  3, i → 1, o → 0, l → |, s → 5, . → 5w33t!, ate → 8
def convert(text):
    text=text.lower()
    dict=[('e','3'),('i','1'),('o','0'),('l','|'),('\.','5w33t!'),('ate','8'),(r'(?<=\s)s','$'),('s','5')]
    print(text)
    for (key,value) in dict:
        text=re.sub(key,value,text)
    return text     
convert(str)    
#For replacing 's' located at the start of the word,'?<=' is used which implies that what precedes the string('s') is a space character(\s)
#Lookahead(?=),lookbehind(?<=),negative lookahead(?!) and negative lookbehind(?<!)


#25
#Transforming a word to Pig Latin
#a&c
def transform_pig_latin(word):
    
    for i in range(0,len(word)-1):
        if word[i] in ['a','e','i','o','u','A','E','I','O','U'] and len(re.findall(r'(?<=q)u|(?<=Q)u|^[^aeiouAEIOU]+(?=y)',word[0:i]))!=0:
            print(word[i:len(word)]+word[0:i]+'ay')
            break
    else:
        print(word+'ay')

transform_pig_latin('myth')   

#b
#Using matchObj concept to pass each word from the corresponding text to the 'transform_pig_latin' function which effectively transforms each word
def transform_pig_latin_text(text):
    def helper(matchObj):
        return transform_pig_latin(matchObj.group(0))
    return re.sub(r'[A-Za-z]+',helper,text)    
transform_pig_latin_text('Some quiet string here that should be converted to Pig Latin at once.')        


#26
#Extracting text from a language that has vowel harmony,extracting vowel sequences and creating a bigram table.
def vowel_bigrams(link):
    text=unknown(link)
    vowel_sequence=[]
    bigrams_list=[]
    for word in text:
        for i in re.findall(r'[aeiou]{1,5}',word):
            vowel_sequence.append(i)
    for sequence in vowel_sequence:
        count=0
        while(count<len(sequence)-1):
            bigrams_list.append((sequence[count],sequence[count+1]))
            count+=1
    import nltk
    cfd=nltk.ConditionalFreqDist(bigrams_list)
    vowels=['a','e','i','o','u']
    return cfd.tabulate(conditons=vowels,samples=vowels)
    
vowel_bigrams('https://tr.wikipedia.org/wiki/%C4%B0stanbul')            


#27
def laugh():
    raw=''.join(random.choice('aehh ') for x in range(500))
    return ' '.join(raw.split())
laugh()    


#29
#Producing a readability score for various text in Brown corpus 
def ARI(category):
    words=nltk.corpus.brown.words(categories=category)
    sents=nltk.corpus.brown.sents(categories=category)
    x=sum(len(word) for word in words)/len(words)
    y=sum(len(sent) for sent in sents)/len(sents)
    ARI=4.71*x+.5*y-21.43
    return ARI
ARI('lore')            
ARI('learned')        


#30
#Difference between Porter and Lancaster stemmer 
str='New rules allowing Sikh police officers to wear turbans instead of traditional police hats have been introduced in New York, officials say. The New York Police Department said the turbans must be navy blue and have the NYPD insignia attached. Under the new rules, religious members of the force are also permitted to grow beards up to half-an-inch long. Sikh officers have until now worn turbans under their caps. Beards have not been permitted.'
porter=nltk.PorterStemmer()
lancaster=nltk.LancasterStemmer()
tokens=nltk.wordpunct_tokenize(str)
[porter.stem(i) for i in tokens]
[lancaster.stem(j) for j in tokens]    

#31
saying=['After', 'all', 'is', 'said', 'and', 'done', ',', 'more',
'is', 'said', 'than', 'done', '.']
lengths=[]
for i in saying:
    lengths.append(len(i))
lengths=[len(k) for k in saying]
lengths

#32
silly='newly formed bland ideas are inexpressible in an infuriating way'
#a
bland=silly.split()
#b
''.join(word[1] for word in silly.split())
#c
' '.join(bland)
#d
\n.join(word for word in sorted(bland))

#33
#a Using a string sequence as index() argument 
'inexpressible'.index('re')
#b
words=['Pleasant','day']
words.index('day')
#c
phrase=bland[:bland.index('in')]
phrase


#34
#Converting nationality adjectives to their respective country names 
def convertNationalityconvert(adjective):
    if (adjective.endswith('dian') or adjective.endswith('ese')):
        return adjective[:-3] + 'a'
    elif (adjective.endswith('ian')):
        return adjective[:-1]
convertNationalityconvert('Burmese')


#36
#Converting lolspeak words to English
nltk.corpus.genesis.words('lolcat.txt')
import re

def lolspeak(word):
    if re.search(r'e$',word)!=None:
        print(word[0:len(word)-2]+'e'+word[len(word)-2])
    elif re.search(r'(er)$',word)!=None:
        print(word[0:len(word)-2]+'ah')
    elif re.search(r'y$',word)!=None:
        print(word[0:len(word)-1]+'eh')
    elif re.search(r'(le)$',word)!=None:
        print(word[0:len(word)-2]+'ul')
        
        
lolspeak('like')

#37 
#Removing tags from HTML page and normalizing whitespace 
def html_tag_removal(link):
    from urllib import request
    url=request.urlopen(link).read().decode('utf8')
    #return url
    tag_removal=re.sub(r'\<.*?\>','',url)
    return re.sub(r'\s+',' ',tag_removal)

html_tag_removal('http://nltk.org/')
        

#38
#Identifying words that are hyphenated(-) at line-breaks 
text='some text with long-\nterm and encyclo-\npedia'
re.findall(r'(\w+-\s\w+)',text)
#Replacing the line break from hyphenated words,which are have hyphen across a line break
re.sub

#39
#Soundex Algorithm
def soundex(name):
    #Appending required elements into list l
    l=[]
    #Appending the first letter 
    l.append(name[0].upper())
    #name=name[1:len(name)]
    #Normalizing string 
    name=name.lower()
    dict={}
    #Creating dict object 
    dict={('b', 'f', 'p', 'v'):'1',('c','g','j','k','q','s','x','z'):'2',('d','t'):'3',('l'):'4',('m','n'):'5',('r'):'6'}
    #Creating list for (h,w)
    exceptions=['h','w']
    #Retreving indexes of (h,w) in the string 
    indexes=[]
    for k in re.finditer('[hw]',name):
        indexes.append(k.start())
    #Encoding digits in place of letters and checking required conditions
    for i in range(1,len(name)):
        for j in list(dict.keys()):
            if name[i] in j and name[i-1] not in j and i not in indexes:
                l.append(dict[j])
            elif name[i] in j and name[i-2] in j and i in indexes:
                pass
    #Checking if the lenght of list is >=4,if it isn't then appending required zeros         
    len_l=len(l)            
    if len_l>=4:
        return ''.join(l[0:4])
    else:
        no_of_zeros=4-len_l
        for i in range(no_of_zeros):
            l.append('0')
        return ''.join(l[0:4])
                
                
soundex('smythe')

#40
#Calculating reading difficulty scores 
def ari(raw):
    sent_tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
    sents=sent_tokenizer.tokenize(raw)
    words=nltk.word_tokenize(raw)
    av_sents=sum(len(sent) for sent in sents)/len(sents)
    av_words=sum(len(word) for word in words)/len(words)
    return (4.71 * av_words) + (0.5 * av_sents) - 21.43

ari(nltk.corpus.abc.raw('rural.txt'))
ari(nltk.corpus.abc.raw('science.txt'))

#41
#Using list comprehension 
words=['attribution', 'confabulation', 'elocution','sequoia', 'tenacious', 'unidirectional','unidirectional']
vsequences=set(''.join(char for char in word if char in 'aeiou') for word in words)
sorted(vsequences)

#42
from nltk.corpus import wordnet as wn
class IndexedText(object):
    def __init__(self, stemmer, text):
        self._text = text
        self._stemmer = stemmer
        self._index = nltk.Index((self._stem(word), i)
            for (i, word) in enumerate(text))

    def concordance(self, word, width=40):
        key = self._stem(word)
        wc = int(width/4) # words of context
        for i in self._index[key]:
            lcontext = ' '.join(self._text[i-wc:i])
            rcontext = ' '.join(self._text[i:i+wc])
            offset = '(WordNet Offset: ' + str(wn.synsets(self._text[i])[0].offset()) + ')'
            ldisplay = '%*s' % (width, lcontext[-width:])
            rdisplay = '%-*s' % (width, rcontext[:width])
            print(ldisplay, rdisplay,offset)
                
    def _stem(self, word):
        return self._stemmer.stem(word).lower()

        
porter = nltk.PorterStemmer()        
grail = nltk.corpus.webtext.words('grail.txt')
text = IndexedText(porter, grail)
text.concordance('Holy')


#43
#Guessing language of previously unseen text by using freq distribution and Spearman correlation.Using words from nltk's Universal Declaration of Human Rights corpus.
def guesslanguage(text):
    #Tokenizing text and creating a dict of occurences of words in text 
    fdist_text=nltk.FreqDist(nltk.Text(nltk.wordpunct_tokenize(text)))
    #Creating a tuple to return combining the guessed language and corresponding Spearman score
    best_guess = ('', 0)
    #Iterating over languages with Latin font 
    for lang in nltk.corpus.udhr.fileids():
        if lang.endswith('-Latin1'):
            print(lang)
    #Creating a freq distribution of words in udhr corpus of nltk in respective languages 
            fdist_lang=nltk.FreqDist(nltk.corpus.udhr.words(fileids=lang))
    #Obtaining a intersection of words from text_dict and lang_dict created
            intersection=list(set(fdist_lang.keys()) & set(fdist_text.keys()))
            dict_text=[]
            dict_lang=[]
            for word in intersection:
    #Creating list of tuples with occurence count of words present in the text in both text and nltk's udhr corpus            
                dict_text.append((word,fdist_text[word]))
                dict_lang.append((word,fdist_lang[word]))
    #Getting the Spearman correlation score for list of tuples         
            spearman=nltk.spearman_correlation(dict_text,dict_lang)
            if (best_guess[1]==0 and spearman!=0.0) or (spearman!=0.0 and spearman>best_guess[1]):
                best_guess=(lang[:-7],spearman)
    #Returning best guess tuple with language and highest correlation score
    return best_guess            
guesslanguage('Carapax (von gr. charax „Befestigungsanlage“, „Palisade“ und pagios „fest“; Plural: Carapaces) ist eine Bezeichnung für eine bei verschiedenen Tiergruppen (Taxa) unabhängig voneinander entstandene harte Bedeckung der Körperoberseite.')
    


#44
def wordsense(text,word):
    stopwords = nltk.corpus.stopwords.words('english')
    enumerated_text=[(word,i) for (i,word) in enumerate(word.lower() for word in nltk.tokenize.RegexpTokenizer(r'\w+').tokenize(text) if word not in stopwords)]
    width=5
   
    lcontext=[]
    rcontext=[]
    oddest=False
    #print(enumerated_text)
    for i in enumerated_text:
        if i[0]==word and (len(enumerated_text)-i[1])>3 and i[1]>3:
            print(i)
            for j in range(1,4):
                if enumerated_text[i[1]-j][0]!=word:
                    lcontext.append(enumerated_text[i[1]-j][0])
                if enumerated_text[i[1]+j][0]!=word:
                    rcontext.append(enumerated_text[i[1]+j][0])
            for z in nltk.corpus.wordnet.synsets(i[0]):
                print(z)
                overall_sim=0
                count_comparisons=0
                for j in lcontext:
                    lcontext_synset=nltk.corpus.wordnet.synsets(j)
                    for k in lcontext_synset:
                        if z.path_similarity(k)!=None:
                            #print('Wordnet similarity between {} and {} : {}'.format(z,k,z.path_similarity(k)))
                            overall_sim+=z.path_similarity(k)
                            count_comparisons+=1
                print('lcontext Done')    
                for l in rcontext:
                    rcontext_synset=nltk.corpus.wordnet.synsets(l)
                    for m in rcontext_synset:
                        if z.path_similarity(m)!=None:
                            #print('Wordnet similarity between {} and {} : {}'.format(z,m,z.path_similarity(m)))
                            overall_sim+=z.path_similarity(m)
                            count_comparisons+=1
            print(overall_sim)
            print(count_comparisons)
        #Calculating an avg_similarity score for each occurecne of the 'word'
            avg_sim=overall_sim/count_comparisons
            if (oddest==False or oddest[1]>avg_sim):
                oddest=(i[1],avg_sim)

    if (oddest!=False):
        print(text[(oddest[0]-50):(oddest[0]+50)])
        print('Lowest average similarity obtained which indicates a novel usecase of the word: '+str(oddest[1]))
            
            
        
wordsense('Even today, typography as a discipline continues to be plagued by a Euro-centric bias. If any of the major typography reference books are to be believed, the development of typography has generally been limited to Western Europe. In Type & Typography (2002), the otherwise excellent book by Phil Baines and Andrew Haslam, the authors make a note that the history of writing and the alphabet goes back thousands of years, but they do not elaborate more on this. It goes without saying that their history of typography is only the history of Latin-based typography. Other books are even more blunt when it comes to the scope they cover. Classic volumes such as Updike’s obviously nationalistic Printing Type, first printed in 1922, or Harry Carter’s also already somewhat dated A View of Early Typography (1969) can be overlooked. But even recent books such Designing Type (2005) by Karen Cheng or A Typographic Workbook (2005) by Kate Clair & Cynthia Busic-Snyder don’t bother to mention that there is more to typography than Latin typography.','typography')


nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt'))
wordsense(nltk.corpus.gutenberg.raw('austen-emma.txt'),'love')    
    


