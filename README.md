# Random codes

Collection of random codes to practice OOP or any cool code that I might have an interest to come back at it later.

### Card_Wars   

The name itself is pretty explanatory.
Card wars is a card game where a deck of cards is given to 2 participants and whoever draw the stronger(greater) card wins.   
For this exercise I use OOP as a way of practicing with it, but it was not necessary as the level of abstraction is not that high, nor inheritance or polymorfism is needed.

I import the itertool **PRODUCT** to create a list containing all the possibilitties from the list "suits"(trebol,spades,diamonds,hearts) combined with the list "values"(2,3,-j,q,k). Also import **SHUFFLE** and **CHOICE** from the random module; Shuffe to desorganizes the list "deck" and choice to pseudo-random select an option from this list.

The game starts asking for the players' names, welcomes them and inmmediately starts getting the cards. After the card is "drawn" it is remove from the deck and pass it to the function "check_char" that checks if the card has J,Q,K or A in it to replace it for 11,12,13,14.
Then those values are pass to the function "card_battle" where are compared, if player one has a greater number it returns player 1 wins and the counter for player 1 is update +1, otherwise player 2 wins and his counter is updated, if both cards has the same value is a draw.
Whoever gathers 10 wins first, wins, but if 10 draws have happend it would stop the game.

---
