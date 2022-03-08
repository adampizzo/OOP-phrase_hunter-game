# Create your Game class logic in here.
from phrasehunter.phrase_generator import generate_phrase_list
from phrasehunter.phrase import Phrase
from phrasehunter.utils import s_sleep, m_sleep, l_sleep, s_clear
import time
import random




class Game:

    def __init__(self, lives):
        self.current_lives = lives
        self.default_lives = lives
        self.phrase = ""
        self.games_won = 0
        s_clear()
        # s_sleep()
        # print("Welcome to the Phrasehunter game!")
        # m_sleep()
        # print(f"In this game you have {self.current_lives} lives in which to guess a phrase.")
        # l_sleep()
        # print("The phrase is initially masked with underscores.")
        # l_sleep()
        # print("Everytime you guess a letter correctly, it will then appear on the screen.")
        # l_sleep()
        # print("Guess incorrectly, and watch one of your lives disappear.")
        # l_sleep()
        # print("When you get to zero, your game is over.")
        # l_sleep()
        # s_clear()


    def get_phrase(self):
        return random.choice(generate_phrase_list())


    def lose_life(self):
        '''
        lose_life - Removes a life from the user.
        '''
        self.current_lives -= 1
        if self.current_lives != 0:
            print(f"You've lost a life. You have {self.current_lives} remaining.")
        m_sleep()


    def is_alive(self):
        if self.current_lives == 0:
            m_sleep()
            print("You have no lives left!")
            m_sleep()
            print("The phrase was:")
            m_sleep()
            print(self.phrase)
            l_sleep()
            return False

    def keep_playing(self):
        accepted_answers = ['y','yes','n','no']
        while True:
            try:
                s_sleep()
                answer = input("\nDo you want to keep playing? (Y or Yes to continue. N or No to quit)\n")
                if answer not in accepted_answers:
                    raise ValueError(f"'{answer}' is not a valid answer, please try again")
            except ValueError as err:
                print(err)
            else:
                if answer.lower() == 'y' or answer.lower() == 'yes':
                    return True
                else:
                    return False
                


    def wrong_answer(self):        
        self.lose_life()
        self.is_alive()


    def score(self, guess):
        if not guess:
            self.wrong_answer()


    def start_game(self):        
        playing = True
        while playing:
            won = False
            self.lives = self.default_lives
            self.phrase = Phrase(self.get_phrase())
            self.phrase.phrase_to_list()
            while self.current_lives > 0:
                s_clear()
                print(f"Lives Left: {self.current_lives}")
                print(f"Letters Guessed: {self.phrase.display_guessed()}\n")
                s_sleep()
                print_phrase, won = self.phrase.display_phrase()                
                print(print_phrase)
                s_sleep()
                if won:
                    print("\nCongratulations! You Win!")
                    l_sleep()
                    if (self.current_lives - self.default_lives) == 1:
                        print(f"\nYou missed {self.default_lives - self.current_lives} guess")
                    else:
                        print(f"\nYou missed {self.default_lives - self.current_lives} guesses")
                    self.games_won += 1
                    break
                else:    
                    self.score(self.phrase.guess_letter())
            playing = self.keep_playing()
            if playing:
                s_clear()
                self.current_lives = self.default_lives
                self.phrase.is_guessed.clear()
                print("New Phrase incoming!")
                m_sleep()
            else:
                s_clear()                
                print("Thank you for playing!")
                if self.games_won == 0:
                    print("You didn't win any games!")
                elif self.games_won == 1:
                    print(f"You won {self.games_won} game.")
                else:
                    print(f"You won {self.games_won} games.")
                m_sleep()
                print("Good bye and we'll see you next time, on Phrasehunters!")
                m_sleep()





