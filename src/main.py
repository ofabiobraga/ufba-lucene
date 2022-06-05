import lucene
import document
import searcher
import writer
import time
import os

INDEXES_DIRECTORY = 'indexes'

class Main:
    def __init__(self):
        lucene.initVM()
        os.system('reset')

    ##
    #
    ###
    def run(self):
        print("|=================================================|")
        print("| Select an action: ")
        print("|-------------------------------------------------|")
        print("| ➕ (i) Insert a new registry to Lucene")
        print("| 🔍 (s) Search for a registry by a term on Lucene")
        print("| 🚪 (e) Exit from program")
        print("|=================================================|")
        while(True):
            command = input("| What do you want to do? ")

            if (command == 'i'):
                print("|-------------------------------------------------|")
                print("| ➕ Type data of the registry")
                title = input("├─ Title: ")
                artist = input("├─ Artist: ")
                lyrics = input("├─ Lyrics: ")
                self.__index(title, artist, lyrics)
                print("|-------------------------------------------------|")
                print("|  ✅ Registry successfully added!")
                print("|-------------------------------------------------|")
            if (command == 's'):
                print("|-------------------------------------------------|")
                print("| 🔍 Type terms, you want to search: ")
                query = input("├─    ")
                self.__search(query)
            elif (command == 'e'):
                print("| 🚪 Ok. See ya!")
                break
        return

    ##
    # Index a new document
    ###
    def __index(self, title, artist, lyrics):
        indexWriter = writer.Writer().create(INDEXES_DIRECTORY)
        indexWriter.addDocument(
            document.Document().create(int(time.time()), title, artist, lyrics)
        )
        indexWriter.commit()
        indexWriter.close()
        return

    ##
    #
    ###
    def __search(self, query):
        indexSearcher = searcher.Searcher().create(INDEXES_DIRECTORY)
        indexQuery = searcher.Searcher().query(query)
        indexDocuments = indexSearcher.search(indexQuery, 50).scoreDocs

        if (len(indexDocuments) == 0):
            print("|-------------------------------------------------|")
            print("| ❌ There's no records with the term '" + query + "'.")
            print("|=================================================|")
            return

        print("|=================================================|")
        print("| ✅ Your query returned", str(len(indexDocuments)), "results")
        print("|=================================================|")
        for i, indexDocument in enumerate(indexDocuments):
            fields = indexSearcher.doc(indexDocument.doc).getFields()

            print("[" + str(i + 1) + "]")
            for field in fields:
                if (field.name() != 'id'):
                    print("|", field.name() + ":\t", field.stringValue())
                else:
                    print("|", field.name() + ":\t\t", field.stringValue())
            
            print("|-------------------------------------------------|")
        return

main = Main()
main.run()
