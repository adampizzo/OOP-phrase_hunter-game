from phrasehunter.utils import s_sleep, m_sleep


class Phrase():
    
    def __init__(self, phrase):
        '''
        __init__ initializes the phrase class with a phrase.

        The way this works in our program is to grab a random
        phrase from a list generated in the phrase_generator.py
        program.
        
        The phrase attribute is set to the value of the supplied phrase.
        
        the is_guessed attribute is set to the value of an empty set.
        
        The player_won attribute is set to False by default.

        Args:
            phrase (_type_): phrase supplied by the user. We will use it to
            for all of the methods in this class.
        '''
        self.phrase = phrase
        self.is_guessed = set()
        self.player_won = False
    
    def __len__(self):
        '''
        __len__ returns the length of the phrase attribute.
        '''
        return len(self.phrase)
    
    def __iter__(self):
        '''
        __iter__ iterates through the phrase attribute.
        '''
        yield from self.phrase
        
    def __str__(self):
        '''
        __str__ displays the phrase as a string.
        '''
        return self.phrase
    
    def display_guessed(self):
        '''
        display_guessed returns the items in the is_guessed set.

        Returns a joined string of all of the items in the
        is_guessed set. 
        '''
        return ", ".join(self.is_guessed)
            

    def display_phrase(self):
        '''
        display_phrase generates a list of characters to display for the user.

        For each letter in the phrase we will want to check and see if it has been
        guessed. The phrase is in all caps, so we don't want to just have all capital
        letters being displayed as that, to me, doesn't look as good as a more "title"
        kind of view. So, when we are looking at each char, we want to make it lowercase.
        We then check if the char meets certain criteria.
        
        First, was the previous character a space. This tells me whether or not we should
        print that letter as is, or lower case it. We then check to see if the character
        in the is an alphabet character. If it isn't, then we just print the character.
        This is used for when we're dealing with spaces and special character. Finally,
        if the character is not in is_guessed or a special character, then we print an
        underscore.
        
        Finally, we check whether or not there are any underscores in the phrase_print
        list. If there are, then we just return the list. If there are not, then the
        user has won and we set the attribute to True.
        
        Returns:
            _type_: returns a list of all of the characters in phrase_print.
        '''
        phrase_print = []
        last_item = " "        
        for char in self.phrase:
            if last_item == " ":
                if char.lower() in self.is_guessed:
                    phrase_print.append(char)
                elif not char.isalpha():
                    phrase_print.append(char)
                else:
                    phrase_print.append("_")
            elif char.lower() in self.is_guessed:
                phrase_print.append(char.lower())
            elif not char.isalpha():
                phrase_print.append(char)            
            else:
                phrase_print.append("_")
            last_item = char
        if "_" not in phrase_print:
            self.player_won = True
            return phrase_print
        else:
            return phrase_print
    
    def guess_letter(self):
        '''
        guess_letter Gets a guess from the user and checks whether it is in the phrase.

        Asks for the user to enter a letter they want to guess. We perform error checking
        to makes sure that the guess is not shorter or longer than 1 letter, makes sure
        that the guess is an alphabet character, and that it hasn't been guessed already.
        
        If the guess is in the phrase, then let the user know and return True. Otherwise,
        let the user know and return false.
        '''
        while True:
            try:
                guess = input("\nEnter the letter that you want to guess:  ")
                guess = guess.lower()
                if len(guess) == 0 or len(guess) > 1:
                    raise ValueError(f"'{guess}' is not a proper guess. Your guess should be one letter. Please try again.")                    
                elif not guess.isalpha():
                    raise ValueError(f"'{guess}' is not a letter. Please try again.")
                elif guess in self.is_guessed:
                    raise ValueError(f"'{guess}' has already been guessed. Please try again.")
            except ValueError as err:
                print(err)
                m_sleep()                
            else:
                self.is_guessed.add(guess)
                if guess in self.phrase.lower():
                    print(f"\n{guess} is in the phrase!")
                    s_sleep()
                    return True
                else:
                    print(f"\n{guess} is not in the phrase.")
                    s_sleep()
                    return False
                    









