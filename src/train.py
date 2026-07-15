from environment import DynamicPricingEnvironment
from q_learning import QLearningAgent
from utils import print_episode

env = DynamicPricingEnvironment()
agent = QLearningAgent()

episodes = 100

for episode in range(episodes):

    state = env.reset()
    total_reward = 0
    done = False

    while not done:

        action = agent.choose_action(state)

        next_state, reward, done = env.step(action)

        agent.update_q_table(
            state,
            action,
            reward,
            next_state
        )

        total_reward += reward

        state = next_state

    print_episode(
        episode + 1,
        total_reward
    )

print("\nTraining Completed!")
print("States Learned:", len(agent.q_table))