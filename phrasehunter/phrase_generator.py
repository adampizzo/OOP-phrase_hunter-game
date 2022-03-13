import urllib.request


def generate_phrase_list():
    ''' generate_prase_list - Takes a webpage hosted on github that I created that has 
        a list of phrases. Then picks 1000 at random and adds them to a new list, sorts, 
        and returns it for use in the game.

        Attribution from source in github.
    '''
    phrase_site = "https://raw.githubusercontent.com/adampizzo/phrases/main/phrases.txt"
    response = urllib.request.urlopen(phrase_site)
    PHRASES = response.read().decode().splitlines()
    phrase_list = [phrase for phrase in PHRASES]
    return sorted(phrase_list)
    
