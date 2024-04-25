import numpy as np
import utils
from rlgame import Game


class LogisticPolicy:

    def __init__(self, theta, alpha, gamma):
        # Initialize paramters θ, learning rate α and discount factor γ

        self.theta = theta
        self.alpha = alpha
        self.gamma = gamma

    def logistic(self, gamma):
        # definition of logistic function

        return 1 / (1 + np.exp(-gamma))

    def probs(self, x):
        # returns probabilities of two actions

        y = x @ self.theta
        prob0 = self.logistic(y)

        return np.array([prob0, 1 - prob0])

    def act(self, x):
        # sample an action in proportion to probabilities

        probs = self.probs(x)
        action = np.random.choice([0, 1], p=probs)

        return action, probs[action]

    def grad_log_p(self, x):
        # calculate grad-log-probs

        y = x @ self.theta
        grad_log_p0 = x - x * self.logistic(y)
        grad_log_p1 = - x * self.logistic(y)

        return grad_log_p0, grad_log_p1

    def grad_log_p_dot_rewards(self, grad_log_p, actions, discounted_rewards):
        # dot grads with future rewards for each action in episode

        return grad_log_p.T @ discounted_rewards

    def discount_rewards(self, rewards):
        # calculate temporally adjusted, discounted rewards

        discounted_rewards = np.zeros(len(rewards))
        cumulative_rewards = 0
        for i in reversed(range(0, len(rewards))):
            cumulative_rewards = cumulative_rewards * self.gamma + rewards[i]
            discounted_rewards[i] = cumulative_rewards

        return discounted_rewards

    def update(self, rewards, obs, actions):
        # calculate gradients for each action over all observations
        grad_log_p = np.array([self.grad_log_p(ob)[action] for ob, action in zip(obs, actions)])

        assert grad_log_p.shape == (len(obs), 15)

        # calculate temporaly adjusted, discounted rewards
        discounted_rewards = self.discount_rewards(rewards)

        # gradients times rewards
        dot = self.grad_log_p_dot_rewards(grad_log_p, actions, discounted_rewards)

        # gradient ascent on parameters
        self.theta += self.alpha * dot


def run_episode(game, policy, grid, evaluate=False):
    observation = game.reset(grid)
    totalreward = 0

    observations = []
    actions = []
    rewards = []
    probs = []

    done = False

    while not done:
        observations.append(observation)
        action, prob = policy.act(observation)

        observation, reward, done, trunc = game.step(action)
        if evaluate:
            print("action, prob, reward, done, obs", action, prob, reward, done, observation)
        totalreward += reward
        rewards.append(reward)
        actions.append(action)
        probs.append(prob)

    return totalreward, np.array(rewards), np.array(observations), np.array(actions), np.array(probs)


def train(theta, alpha, gamma, Policy, MAX_EPISODES=1000, seed=None, evaluate=False):
    # initialize environment and policy

    game = Game(grid, width * height / 2, width * height / 4)
    ui = utils.initialize_ui(grid, game.robots)
    print("reach normally = ", utils.run_robots_reach_check(game.robots, ui, share_map=True))

    episode_rewards = []
    policy = Policy(theta, alpha, gamma)

    # train until MAX_EPISODES
    for i in range(MAX_EPISODES):
        # run a single episode
        total_reward, rewards, observations, actions, probs = run_episode(game, policy, grid)

        # keep track of episode rewards
        episode_rewards.append(total_reward)

        # update policy
        policy.update(rewards, observations, actions)
        #print("i = ", i)
        #print("EP: " + str(i) + " Score: " + str(total_reward) + " ", end="\r", flush=False)
    return episode_rewards, policy

width = 10
height = 10
grid = utils.initialize_grid(width, height, remove_walls=0)
# for reproducibility
GLOBAL_SEED = 0
np.random.seed(GLOBAL_SEED)

episode_rewards, policy = train(theta=np.random.rand(15),
                                alpha=0.002,
                                gamma=0.99,
                                Policy=LogisticPolicy,
                                MAX_EPISODES=10,
                                seed=GLOBAL_SEED,
                                evaluate=True)
evaluation_rewards = 0
# grid = utils.initialize_grid(width, height, remove_walls=0)
game = Game(grid, width * height / 2, width * height / 4)

for _ in range(100):
    tr, _, _, _, _ = run_episode(game, policy, grid, evaluate=True)
    print(policy)
    evaluation_rewards += tr
print("average reward = ", evaluation_rewards/100)