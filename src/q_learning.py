import random


class QLearningAgent:
    def __init__(self):
        self.q_table = {}

        self.learning_rate = 0.1
        self.discount_factor = 0.9
        self.epsilon = 0.1

        self.actions = [0, 1, 2]

    def get_state_key(self, state):
        return tuple(state)

    def choose_action(self, state):
        state = self.get_state_key(state)

        if state not in self.q_table:
            self.q_table[state] = [0, 0, 0]

        # Exploration
        if random.uniform(0, 1) < self.epsilon:
            return random.choice(self.actions)

        # Exploitation
        return self.q_table[state].index(max(self.q_table[state]))

    def update_q_table(self, state, action, reward, next_state):
        state = self.get_state_key(state)
        next_state = self.get_state_key(next_state)

        if state not in self.q_table:
            self.q_table[state] = [0, 0, 0]

        if next_state not in self.q_table:
            self.q_table[next_state] = [0, 0, 0]

        old_value = self.q_table[state][action]

        next_max = max(self.q_table[next_state])

        new_value = old_value + self.learning_rate * (
            reward + self.discount_factor * next_max - old_value
        )

        self.q_table[state][action] = new_value