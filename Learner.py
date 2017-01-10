__author__ = 'philippe'
import World
import threading
import time
from random import random, choice, shuffle

discount = 0.95
epsilon = 0.25
e_decay = 0.99
actions = World.actions
states = []
Q = {}
E = {}
for i in range(World.x):
    for j in range(World.y):
        states.append((i, j))

for state in states:
    temp = {}
    temp_e = {}
    for action in actions:
        temp[action] = 0.1
        temp_e[action] = 0.0
        World.set_cell_score(state, action, temp[action])
    Q[state] = temp
    E[state] = temp_e

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


def reset_E():
    for state in states:
        for action in actions:
            E[state][action] = 0

def max_Q(s):
    val = None
    act = None
    for a, q in Q[s].items():
        if val is None or (q > val):
            val = q
            act = a
    #print('max: ', Q[s].items(), act, val)
    return act, val


def policy(s, eps=epsilon):
    if random() > eps:
        return max_Q(s)
    else:
        # print('random')
        l = [(a, q) for a, q in Q[s].items()]
        shuffle(l)
        return choice(l)


def inc_Q(s, a, alpha, inc):
    Q[s][a] += alpha * inc * E[s][a]
    World.set_cell_score(s, a, Q[s][a])


def run():
    global discount
    global epsilon
    time.sleep(1)
    alpha = 1
    t = 1
    s1 = World.player
    a1, q_val1 = policy(s1)
    while True:
        # Do the action
        (s1, a1, r1, s2) = do_action(a1)


        # Update Q
        a2, q_val2 = policy(s2)
        a_best, q_best = max_Q(s2)
        delta = r1 + discount * q_best - Q[s1][a1]
        E[s1][a1] = 1


        for state in states:
            for action in actions:
                inc_Q(state, action, alpha, delta)
                if a_best == a2:
                    E[state][action] *= discount * e_decay
                else:
                    E[state][action] = 0
        # print('new q:', Q[s1][a1])
        s1 = s2
        a1 = a2
        q_val1 = q_val2

        # Check if the game has restarted
        t += 1.0
        if World.has_restarted():
            World.restart_game()
            reset_E()
            time.sleep(0.01)

            # print(epsilon, alpha)

            t = 1.0

        # Update the learning rate
        alpha *= 0.9998
        epsilon *= 0.9995

        # MODIFY THIS SLEEP IF THE GAME IS GOING TOO FAST.
        time.sleep(0.05)


t = threading.Thread(target=run)
t.daemon = True
t.start()
World.start_game()
