# Q-learning-gridworld

Submission to Siraj Raval's [Q-learning competition](https://www.youtube.com/watch?v=A5eihauRQvo&t=1s)

> The challenge for this video is to 
> * modify the the game world so that it's bigger
> * add more obstacles
> * have the bot start in a different position
> * Bonus points if you modify the bot in some way that makes it more efficient

## Modifications done  
* All the things listed above and...
* Changed the bot's policy to epsilon-greedy
* Reduce epsilon (exploration) exponentialy
* Reduce alpha (learning rate) exponentialy
* Added Eligibilty traces with [Walkin's algorithm](https://webdocs.cs.ualberta.ca/~sutton/book/ebook/node78.html)

## Usage
Run python `Learner.py` in terminal

## Dependencies
None

## Credits
[Siraj Ravel](https://github.com/llSourcell/q_learning_demo/)
[PhillipeMorere](https://github.com/PhilippeMorere)
