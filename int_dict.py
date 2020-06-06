from ferramentas import header
import json
import difflib
from sql_connector import connect_and_fetch

def load_data():
    
    return json.load(open('data.json'))

def get_word_local(word):
    
    return data[word]

def user_interaction():
    
    while True:
        word = str(input('Choose a word to look for: ')).lower()
        if word == 'q':
            return False
        elif word.isalpha():
            break
        else:
            print('Error! Type in a word only with letters!')
    
    return word

def print_defs(word):
    
    # for i, definition in enumerate(get_word_local(word)):
    #             print(f'{i+1}. {definition}')       (Using local database)
    results = connect_and_fetch(word)
    for i, definition in enumerate(results):
        print(f'{i+1}. {definition[1]}')
                

if __name__ == "__main__":
    
    header('Interactive English Dictionary')
    
    data = load_data()
    
    while True:
        print('Type "q" to end the programm')
        
        word = user_interaction()
        if not word:
            print('See you soon...')
            break
                
        try:
            print_defs(word)
        except:
            match = difflib.get_close_matches(word, list(data.keys()),
                                              n=2, cutoff=0.8)
            for guess in match:
                choice = str(input(f'Do you mean {guess}?(Y/N): ')).lower()
                if choice == 'y':
                    print_defs(guess)
                    break
                else:
                    continue