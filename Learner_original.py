__author__ = 'philippe'
import World
import threading
import time
import csv
import random

random.seed(0)

discount = 0.3
actions = World.actions
states = []
log = []
Q = {}
for i in range(World.x):
    for j in range(World.y):
        states.append((i, j))

for state in states:
    temp = {}
    for action in actions:
        temp[action] = 0.1
        World.set_cell_score(state, action, temp[action])
    Q[state] = temp

for (i, j, c, w) in World.specials:
    for action in actions:
        Q[(i, j)][action] = w
        World.set_cell_score((i, j), action, w)


def do_action(action):
    s = World.player
    r = -World.score
    if action == actions[0]:
        World.try_move(0, -1)
    elif action == actions[1]:
        World.try_move(0, 1)
    elif action == actions[2]:
        World.try_move(-1, 0)
    elif action == actions[3]:
        World.try_move(1, 0)
    else:
        return
    s2 = World.player
    r += World.score
    return s, action, r, s2


def max_Q(s):
    val = None
    act = None
    for a, q in Q[s].items():
        if val is None or (q > val):
            val = q
            act = a
    return act, val


def inc_Q(s, a, alpha, inc):
    Q[s][a] *= 1 - alpha
    Q[s][a] += alpha * inc
    World.set_cell_score(s, a, Q[s][a])


def run():
    global discount
    global log
    time.sleep(1)
    alpha = 1
    t = 1
    for episode_num in range(75):
        steps = 0
        score = 0
        t = 1.0
        while not World.has_restarted():
            # Pick the right action
            s = World.player
            max_act, max_val = max_Q(s)
            (s, a, r, s2) = do_action(max_act)
            score += r

            # Update Q
            max_act, max_val = max_Q(s2)
            inc_Q(s, a, alpha, r + discount * max_val)


            t += 1.0
            steps += 1

            # Update the learning rate
            alpha = pow(t, -0.1)

            # MODIFY THIS SLEEP IF THE GAME IS GOING TOO FAST.
            time.sleep(0.05)

        World.restart_game()
        log.append({'episode': episode_num, 'score': score, 'steps': steps, 'alpha': alpha, 'epsilon': 0})
        time.sleep(0.01)

    with open('data/log_original_0.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['episode', 'score', 'steps', 'alpha', 'epsilon'])
        writer.writeheader()
        for episode in log:
            writer.writerow(episode)
    print('Logged')


t = threading.Thread(target=run)
t.daemon = True
t.start()
World.start_game()