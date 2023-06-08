import os
import re
import string
import math

targetDirectory = "../parsers/leetcode/QData/"
length = len(os.listdir(targetDirectory))

def writeToVacab(vocab):
    with open("document.txt", "w" , encoding="utf-8") as f:
        f.write(vocab)
        f.close()
        
    #store all the words from vocab string to a set
    vocab = vocab.split()
    vocab = set(vocab)
    return vocab
    f.close()
        
def cleaningData(data):
    #lowering the case
    data = data.lower()
    
    # removing the after part of example
    data = data.split("Example 1")[0]
    
    #removing the digits
    pattern = r'\d+'
    data = re.sub(pattern, '', data)
    
    #removing punctuations
    translator = str.maketrans('', '', string.punctuation)
    data = data.translate(translator)
    
    #remove extra spaces and next lines
    data = data.replace('\n', ' ')
    data = re.sub(' +', ' ', data)
    
    #remove stop words
    stop_words = ['the', 'a', 'an', 'is', 'are', 'was', 'were', 'has', 'have', 'had', 'been', 'will', 'shall', 'be', 'to', 'of', 'and', 'in', 'that', 'for', 'on', 'with', 'by', 'at', 'from', 'as', 'into', 'through', 'during', 'including', 'until', 'against', 'among', 'throughout', 'despite', 'towards', 'upon']
    data = ' '.join([word for word in data.split() if word not in stop_words])
    
    #remove all the words with length less than 3
    data = ' '.join([w for w in data.split() if len(w)>2])
    
    #remove all the words like its thats you etc
    filler_words = [
    'like', 'um', 'uh', 'ah', 'er', 'well', 'you know', 'actually', 'basically', 'literally',
    'honestly', 'seriously', 'right', 'so', 'anyway', 'anyhow', 'really', 'kind of', 'sort of',
    'pretty', 'quite', 'somewhat', 'just', 'still', 'now','can','this','all','make' ,'there', 'then', 'therefore', 'thus', 'hence','its','you','thats'
    ]

    data = ' '.join([w for w in data.split() if w not in filler_words])
        
    return data

def main():
    document = []
    
    for i in range(1, length+1):
        folder_path = '../parsers/leetcode/QData/' + str(i)
        for filename in os.listdir(folder_path):
            with open(folder_path + '/' + filename, 'r', encoding="utf-8") as f:
                data = f.read()
                data = cleaningData(data)
                document.append(data)
                f.close()
                
    var = IDF(document)
    inverse_vocab_map = var[0]
    IDF_map = var[1]
    
    TF_map = TF(document, inverse_vocab_map, IDF_map)
    
    #import questionLink List from parsers -> leetcode -> 
    
    TF_IDF_map = TF_IDF(TF_map, IDF_map)
    return TF_IDF_map,document

def TF_IDF(TF_map, IDF_map):
    TF_IDF_map = {}
    
    for word in IDF_map:
        TF_IDF_map[word] = {}
        for index in TF_map[word]:
            TF_IDF_map[word][index] = TF_map[word][index] * IDF_map[word]
    
    return TF_IDF_map
    
def TF(document, inverse_vocab_map , IDF_map):
    TF_map = {}
    
    for word in IDF_map:
        TF_map[word] = {}
        list = inverse_vocab_map[word]
        
        for index in list:
            para = document[index]
            para = para.split()
            if word in para:
                TF_map[word][index] = para.count(word)/len(para)
            else:
                TF_map[word][index] = 0
    
    return TF_map
    
def IDF(document):
    IDF_map = {}
    inverse_vocab_map = {}
    index = 0
    
    for para in document:
        para = set(para.split())
        for word in para:
            if word not in inverse_vocab_map:
                inverse_vocab_map[word] = []
            inverse_vocab_map[word].append(index)
            if word in IDF_map:
                IDF_map[word] += 1
            else:
                IDF_map[word] = 1
        index += 1
                
    for word in IDF_map:
        IDF_map[word] = 1 + math.log(len(document)/IDF_map[word])
        
    return inverse_vocab_map, IDF_map

if __name__ == "__main__":
    main()