import prepare

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
    
    for index, score in potential_documents:
        print(document[index] + "\n")
        print("Score: ", score)
        print()
        
    print("Total documents found: ", len(potential_documents))
    print()

if __name__ == "__main__":
    main()    