import gymnasium as gym
import random
env = gym.make('CarRacing-v2') # simulate the game using make function
# env.configure(remotes=1) # automatically creates a local docker container
observation_n = env.reset()

# Move left
left = [('KeyEvent', 'ArrowUp', True), ('KeyEvent', 'ArrowLeft', True), ('KeyEvent', 'ArrowRight', False)]

# Move right
right = [('KeyEvent', 'ArrowUp', True), ('KeyEvent', 'ArrowLeft', False), ('KeyEvent', 'ArrowRight', True)]
# Move forward
forward = [('KeyEvent', 'ArrowUp', True), ('KeyEvent', 'ArrowLeft', False), ('KeyEvent', 'ArrowRight', False), ('KeyEvent', 'n', True)]

turn = 0 # to decide whether to turn or not
rewards=[] # store rewards
beffer_size = 100
action = forward
while True:
    turn-=1 # no need to turn when turn <0
    if turn <=0:
        action = forward
        turn = 0
    action_n = [action for ob in observation_n]
    observation_n, reward_n, done_n, info = env.step(action_n)
    if len(rewards)>=buffer_size:
        mean = sum(rewards)/len(rewards)
        if mean==0:
            turn=20
            if random.random()<0.5:
                action=right
            else:
                action=left
        rewards=[]

