# Random codes

Collection of random codes to practice OOP or any cool code that I might have an interest to come back at it later.

---
### Card_Wars   

The name itself is pretty explanatory.
Card wars is a card game where a deck of cards is given to 2 participants and whoever draw the stronger(greater) card wins.   
For this exercise I use OOP as a way of practicing with it, but it was not necessary as the level of abstraction is not that high, nor inheritance or polymorphism is needed.

I import the itertool **PRODUCT** to create a list containing all the possibilitties from the list "suits"(trebol,spades,diamonds,hearts) combined with the list "values"(2,3,-j,q,k). Also imported **SHUFFLE** and **CHOICE** from the random module; Shuffe to desorganizes the list "deck" and choice to pseudo-random select an option from this list.

The game starts asking for the players' names, welcomes them and inmmediately starts getting the cards. After the card is "drawn" it is remove from the deck and pass it to the function "check_char" that checks if the card has J,Q,K or A in it to replace it for 11,12,13,14.
Then those values are pass to the function "card_battle" where are compared, if player one has a greater number it returns player 1 wins and the counter for player 1 is updated +1, otherwise player 2 wins and his counter is updated, if both cards has the same value is a draw.
Whoever gathers 10 wins first, wins, but if 10 draws have happend it would stop the game.

---   
### Word Cloud   

Word cloud is a picture with the most used words in a text, could be a conversation, book, webpage, etc.   
The function **get_wrds** opens the file and goes through every character in each line to ignore punctuation marks; adding all the characters(even spaces) to a string and then returning this string as a list. Later, we iterate over this list to see the frequency of each word, before counting its frequency the word is matched to the list **uninteresting_words**, if there's a match that word won't be added. This is to leave words as "I", "am", "and", "to", "is", etc that are common use words in the english language and keeping the word cloud interesting.   
Here's an example from the poem: The Raven   
![alt text](https://raw.githubusercontent.com/dsalzedon/Random/master/myfile.jpg)

