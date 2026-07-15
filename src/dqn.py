from stable_baselines3 import DQN
from gym_environment import DynamicPricingGymEnv

# Create the environment
env = DynamicPricingGymEnv()

# Create the DQN model
model = DQN(
    policy="MlpPolicy",
    env=env,
    learning_rate=0.001,
    buffer_size=10000,
    learning_starts=100,
    batch_size=32,
    gamma=0.99,
    verbose=1
)

# Train the model
model.learn(total_timesteps=10000)

# Save the trained model
model.save("models/dynamic_pricing_dqn")

print("DQN Training Completed Successfully!")



from stable_baselines3 import DQN
from gym_environment import DynamicPricingGymEnv

env = DynamicPricingGymEnv()

model = DQN.load("models/dynamic_pricing_dqn")

state, info = env.reset()

done = False
total_reward = 0

while not done:
    action, _ = model.predict(state)

    state, reward, terminated, truncated, info = env.step(action)

    total_reward += reward

    done = terminated or truncated

print("Total Revenue:", total_reward)