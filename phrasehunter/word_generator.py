import urllib.request


def generate_word_list(min, max):
    ''' generate_word_list - Takes a list of words from 
        https://github.com/dwyl/english-words/blob/master/words_alpha.txt
        and reads, decodes, and splits each line, then saves it to a variable called WORDS.
        Thanks for the help, https://stackoverflow.com/questions/18834636/random-word-generator-python!
        Then we make a list from that list with words that are at between min and max characters in length.        
        
        Content Warning: There could be bad words in here. It's random. I'm sorry :| 
        
        ------------
        I made this when I thought it was a word guessing game. Whoops!
    '''

    word_site = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"
    response = urllib.request.urlopen(word_site)
    WORDS = response.read().decode().splitlines()
    word_list = [word for word in WORDS if len(word) >= min and len(word) <= max]    
    return word_list
