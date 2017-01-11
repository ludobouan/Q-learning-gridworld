# Q-learning-gridworld

Submission to Siraj Raval's [Q-learning competition](https://www.youtube.com/watch?v=A5eihauRQvo&t=1s)

> The challenge for this video is to 
> * modify the the game world so that it's bigger
> * add more obstacles
> * have the bot start in a different position
> * Bonus points if you modify the bot in some way that makes it more efficient

## Improvements 
* All the things listed above (Smiley face level that is bigger, has more obstacles, and the bot starts in a different position)
* Changed the main loop to a more traditional episode - step structure
* Added [Eligibilty traces](https://webdocs.cs.ualberta.ca/~sutton/book/ebook/node72.html) with both TD-lambda and [Walkin's algorithm](https://webdocs.cs.ualberta.ca/~sutton/book/ebook/node78.html) for greedy and epsilon-greedy policies respectfully.
* Changed the bot's policy to [epsilon-greedy](http://www0.cs.ucl.ac.uk/staff/D.Silver/web/Teaching_files/XX.pdf)
* Logged the episode data to csv file in order to be analysed later in a jupyter notebook with matplotlib, pandas, and seaborn
 
## Comparison
| Original (greedy) | Greedy with eligibility traces | Epsilon-Greedy with eligibility traces |
| :------------- |:-------------:| :-----:|
| your-text-here Greedy policy, Q values are initialized to 0.1 to induce exploration | Same greedy policy but uses eligibility traces to make learning considerably  faster | Uses epsilon-greedy policy and eligibility traces, turns out to be less effective than the greedy policy with traces but that may be due to my non-optimized hyperparemeters |  
| 40 episodes to solution | 10 episodes to solution | 15 episodes to solution |
| Sub-optimal solution | Sub-optimal solution | Will converge to optimal solution with right hyperparameters |

![Graphic of score as function of episode number](https://github.com/ludobouan/Q-learning-gridworld/blob/master/data/Compare.png)

## Custom gridworld level
<img src="https://github.com/ludobouan/Q-learning-gridworld/blob/master/data/Level.png" alt="Image of custom gridworld level" style="width: 200px;"/>
## Usage
Run python `Learner.py` in terminal

## Dependencies
* Matplotlib
* Seaborn

## Credits
[Siraj Ravel](https://github.com/llSourcell/q_learning_demo/)  
[PhillipeMorere](https://github.com/PhilippeMorere)
