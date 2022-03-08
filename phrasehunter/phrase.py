from phrasehunter.utils import s_sleep, m_sleep, l_sleep

class Phrase():
    is_guessed = set()
    
    def __init__(self, phrase):
        self.phrase = phrase                
        
    def __len__(self):
        return len(self.phrase)
    
    def __iter__(self):
        yield from self.phrase
        
    def __str__(self):
        return self.phrase
    
    def display_guessed(self):                
        return ", ".join(self.is_guessed)
            
            
    
    def phrase_to_list(self):
        phrase_as_list = []
        for character in self.phrase:
            phrase_as_list.append(character.lower())        
        return phrase_as_list        
    
    def display_phrase(self):        
        phrase_print = []
        last_item = " "
        player_won = False
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
            elif char == " ":
                pass
            else:
                phrase_print.append("_")
            last_item = char
        if "_" not in phrase_print:
            player_won = True
        return " ".join(phrase_print), player_won
    
    def guess_letter(self):
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
                    m_sleep()
                    return True
                else:
                    print(f"\n{guess} is not in the phrase.")
                    m_sleep()
                    return False
                    









