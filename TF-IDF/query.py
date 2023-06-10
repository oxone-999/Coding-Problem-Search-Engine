import prepare
import os
import re

def preprocess_name(name):
    #remove number. from the name
    #removing the digits
    pattern = r'\d+'
    name = re.sub(pattern, '', name)
    
    #remove dots and starting and ending spaces
    name = name.replace('.', '')
    name = name.strip()
    
    return name

def main():
    document = prepare.main()[1]
    TF_IDF_map = prepare.main()[0]
    
    query = input("Enter the query: ")
    query = query.split()
    
    potential_documents = {}
    
    for word in query:
        if word in TF_IDF_map:
            for index in TF_IDF_map[word]:
                if index in potential_documents:
                    potential_documents[index] += TF_IDF_map[word][index]
                else:
                    potential_documents[index] = TF_IDF_map[word][index]
                    
    potential_documents = sorted(potential_documents.items(), key=lambda x: x[1], reverse=True)
    
    document_links = []
    document_names = []
   
    #open the questions Link folder and read all the files and save all the content in a list
    targetDirectory = "../parsers/leetcode/questionLinks/"
    length = len(os.listdir(targetDirectory))
    
    for i in range(1,length+1):
        with open(targetDirectory + f'questionsLink_{i}.txt') as f:
            data = f.read()
            document_links.append(data)
            f.close()
            
    targetDirectory = "../parsers/leetcode/questionHeadings/"
    length = len(os.listdir(targetDirectory))         
            
    for i in range(1,length+1):
        with open(targetDirectory + f'questionsName_{i}.txt') as f:
            data = f.read()
            data = preprocess_name(data)
            document_names.append(data)
            f.close()
    
    for index , score in potential_documents:
        print(document_names[index])
        print(document_links[index])
        
    print("Total documents found: ", len(potential_documents))
    print()

if __name__ == "__main__":
    main()    