import gymnasium as gym
env = gym.make('CarRacing-v2', render_mode='human')
env.reset()
for episode in range(100):
    observation = env.reset() # train the agent for 100 times
    for _ in range(10000):
        env.render()
        action = env.action_space.sample() # choose an action in the action space randomly
        ovservation, reward, terminated, truncated, info = env.step(action)
        if terminated or truncated:
            print(f"{_+1} timesteps taken for the episode")
            break
env.close()
