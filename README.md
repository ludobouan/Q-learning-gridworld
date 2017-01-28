# Q-learning-gridworld
Reinforcement learning on gridworld with Q-learning  
Submission to Siraj Raval's [Q-learning competition](https://www.youtube.com/watch?v=A5eihauRQvo&t=1s)

## Improvements over orignal code
* Made the code compatible with Python 3
* Changed the main loop to a more traditional episode - step structure
* Added [Eligibilty traces](https://webdocs.cs.ualberta.ca/~sutton/book/ebook/node72.html) with both TD-lambda and [Walkin's algorithm](https://webdocs.cs.ualberta.ca/~sutton/book/ebook/node78.html) for greedy and epsilon-greedy policies respectfully.
* Changed the bot's policy to [epsilon-greedy](http://www0.cs.ucl.ac.uk/staff/D.Silver/web/Teaching_files/XX.pdf)
* Logged the episode data to csv file in order to be analysed later in a jupyter notebook with matplotlib, pandas, and seaborn
 
## Comparison
| Original (greedy) | Greedy with eligibility traces | Epsilon-Greedy with eligibility traces |
| :------------- |:-------------:| :-----:|
| Greedy policy, Q values are initialized to 0.1 to induce exploration | Same greedy policy but uses eligibility traces to make learning considerably  faster | Uses epsilon-greedy policy and eligibility traces, turns out to be less effective than the greedy policy with traces but that may be due to my non-optimized hyperparemeters |  
| 40 episodes to solution | 10 episodes to solution | 15 episodes to solution |
| Sub-optimal solution | Sub-optimal solution | Will converge to optimal solution with right hyperparameters |

![Graphic of score as function of episode number](https://github.com/ludobouan/Q-learning-gridworld/blob/master/data/Compare.png)

## Usage
Run python `Learner.py` in terminal

## Dependencies
* Tkinter
* Matplotlib
* Seaborn

## Custom gridworld level
<img src="https://github.com/ludobouan/Q-learning-gridworld/blob/master/data/Level.png" alt="Image of custom gridworld level" width='250'/>

## Credits
[Siraj Ravel](https://github.com/llSourcell/q_learning_demo/)  
[PhillipeMorere](https://github.com/PhilippeMorere)
