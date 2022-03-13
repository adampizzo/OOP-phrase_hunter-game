import random

from phrasehunter.phrase_generator import generate_phrase_list
from phrasehunter.phrase import Phrase
from phrasehunter.utils import s_sleep, m_sleep, l_sleep, s_clear



class Game:

    def __init__(self, lives):
        '''
        __init__ creates an instance of the Game class with a certain amount of lives based on input.

        Initially the current and default lives value to the same and instantiation. Default lives should never change.
        It will be the value we check against to determine how many lives were lost instead of using a counter.
        
        phrase will be where we store the phrase locally for checking against it. 
        
        games_won and games_lost keep track of how the player is doing after each round.
        
        round_active is used to determine if the current round is still being played.
        
        playing is used to determine if the game should still be played.

        Args:
            lives (_type_): Takes a value for how many lives to give the player for the game. Configurable during initialization.
        '''
        self.current_lives = lives
        self.DEFAULT_LIVES = lives
        self.phrase = ""
        self.games_won = 0
        self.games_lost = 0
        self.round_active = True
        self.playing = True
        
        # Welcome text during initial game run to show the rules.
        s_clear()
        s_sleep()
        print("Welcome to the Phrasehunter game!")
        m_sleep()
        print(f"In this game you have {self.current_lives} lives in which to guess a phrase.")
        l_sleep()
        print("The phrase is initially masked with underscores.")
        l_sleep()
        print("Everytime you guess a letter correctly, it will then appear on the screen.")
        l_sleep()
        print("Guess incorrectly, and watch one of your lives disappear.")
        l_sleep()
        print("When you get to zero, your game is over.")
        l_sleep()
        s_clear()


    def get_phrase(self):
        '''
        get_phrase uses the function from phrase_generator.py to a list of phrases.

        This is accompished by grabbing the data from one of my git hub projects that
        is hosting a text file with a large amount of phrases. More details can be found
        in the phrase_generator.py file.
        

        Returns:
            _type_: Returns a list of phrases.
        '''
        return random.choice(generate_phrase_list())


    def lose_life(self):
        '''
        lose_life - Removes a life from the user. If the user has no lives left, then
        don't print the last statement and a statement will be checked in the 
        continue_round method.
        '''
        self.current_lives -= 1
        if self.current_lives != 0:
            print(f"You've lost a life. You have {self.current_lives} remaining.")
        m_sleep()


    def evaluate_guess(self, guess):
        '''
        evaluate_guess is passed a boolean 'guess' to determine if the user guessed
        a letter correctly of not.

        Works in conjunction with the Phrase class. Specifically the guess_letter method.
        If that method returns True, then we don't do anything, if it returns False, then
        the user loses a life by calling the lose_life method.
        '''
        if not guess:
            self.lose_life()


    def continue_round(self):
        '''
        continue_round checks to see if the round should continue or not.

        If the player_won attribute of the phrase becomes True, then we run
        the if statement to congratulate the user. First we print the phrase out
        one more time. Then we congratulate the user. We tell them how many guesses
        they missed based on their current life value vs the default value.
        If the answer is 1, we format it so it says guess at the end instead of
        guesses. We increment the games_won attribute. We then return False to
        break the round.
        
        If the player_won attribute is not True, but the player's current lives
        are now at zero, they have lost. We let them know they have lost. We tell
        them what the phrase was. We increment the games_lost attribute and return
        False to break the round.
        
        If neither of the above conditions are true, then we return True to start
        the loop over again.

        Returns:
            _type_: returns False when we want to end the round, otherwise True.
        '''
        if self.phrase.player_won:
            print(" ".join(self.phrase.display_phrase()))
            m_sleep()
            print("\nCongratulations! You Win!\n")
            m_sleep()
            if (self.DEFAULT_LIVES - self.current_lives) == 1:
                print(
                    f"You missed {self.DEFAULT_LIVES - self.current_lives} guess.")
            else:
                print(
                    f"You missed {self.DEFAULT_LIVES - self.current_lives} guesses.")
            self.games_won += 1
            return False
        elif self.current_lives == 0:
            print(" ".join(self.phrase.display_phrase()))
            m_sleep()
            print("\nYou have no lives left, Game Over.\n")
            m_sleep()
            print("The phrase was:")
            m_sleep()
            print(self.phrase)
            l_sleep()
            self.games_lost += 1
            return False
        else:
            return True
        
    def keep_playing(self):
        '''
        keep_playing checks to see whether the user wants to keep playing.

        We have a list of accepted answer that are outlined in the input. If the user
        submits an answer that is not in the list, then we raise a ValueError to show
        that their answer was not acceptable and that they need to enter it again. It
        is in a while loop they cannot progress past this until they enter an answer
        that is in the accepted_answer list.
        
        When they do enter an answer that is in the list, then it is checked. If it is
        'n' or 'no' then we set the value of self.playing to False. We then break the
        loop and end the method.

        Raises:
            ValueError: tells the user that they have not entered a valid selection and
            to try again.
        '''
        accepted_answers = ['y', 'yes', 'n', 'no']
        while True:
            try:
                s_sleep()
                answer = input("\nDo you want to keep playing? (Y or Yes to continue. N or No to quit)\n")
                answer = answer.lower()
                if answer not in accepted_answers:
                    raise ValueError(
                        f"'{answer}' is not a valid answer, please try again")
            except ValueError as err:
                print(err)
            else:
                if answer == 'n' or answer == 'no':
                    self.playing = False
                break


    def game_results(self):
        '''
        game_results checks the value of the self.playing attribute and either
        resets the game attributes or displays games won and lost and ends the
        game.
        
        game_results works in conjunction with the keep_playing method. If the
        keep_playing method doesn't change the value of self.playing, the we
        reset the current life total to the default life total, we clear the
        set of guessed letters, and then we set the round_active attribute back
        to true so it starts looping the game_round loop again. We then print
        out that a new phrase is going to be picked and let the method end.
        
        Otherwise, we thank the player for playing. Display their wins and losses
        (formatted for plural/singular) and say good bye to the player.
        '''
        if self.playing:
            s_clear()
            self.current_lives = self.DEFAULT_LIVES
            self.phrase.is_guessed.clear()
            self.round_active = True
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
            if self.games_lost == 0:
                print("You didn't lose any games!")
            elif self.games_lost == 1:
                print(f"You lost {self.games_lost} game.")
            else:
                print(f"You lost {self.games_lost} games.")
            m_sleep()
            print("Good bye and we'll see you next time, on Phrasehunters!")
            m_sleep()


    def game_round(self):
        '''
        game_round runs a round in the game.

        While the round_active attribute is True, we will keep looping through.
        
        We clear the board to keep the formatting, spacing, and readibility all
        high. We print users current lives left. We print the letters that have
        been gussed by the player. 
        
        We then get the output of the display_phrase method and set phrase_print
        to it. This will be all underscores at first and it will eventually have
        any of the letters from the is_guessed phrase attribute.
        
        We check to see if the round should continue or not. If it should continue,
        then we should print the joined version of phrased_print for the user to see
        what they have guessed right. We then evaluate the guess to see if it was
        right or wrong. If it was right, then no negative consequences happen. If
        it was wrong, then a life will be deducted from the user.
        
        If round_active is instead False, then we won't run the if statement and
        will just let the loop exist.
        '''
        while self.round_active:
            s_clear()
            print(f"Lives Left: {self.current_lives}")
            print(f"Letters Guessed: {self.phrase.display_guessed()}\n")
            phrase_print = self.phrase.display_phrase()
            self.round_active = self.continue_round()
            if self.round_active:
                print(" ".join(phrase_print))
                self.evaluate_guess(self.phrase.guess_letter())


    def start_game(self):
        '''
        start_game runs the game. Game will continue while
        self.playing is True.
        
        Sets the lives of the player to the default life.
        
        Gets the phrase and sets it to the instance attribute phrase.
        
        Calls the game_round() method
        
        Calls the keep_playing() method
        
        Calls the game_results method
        '''
        while self.playing:
            self.lives = self.DEFAULT_LIVES
            self.phrase = Phrase(self.get_phrase())
            self.game_round()
            self.keep_playing()
            self.game_results()
            






