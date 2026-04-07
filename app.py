from env.curriculum_env import CurriculumEnv

env = CurriculumEnv()

state = env.reset()

done = False
while not done:
    action = input("Enter action: ")
    state, reward, done, _ = env.step(action)
    print("Reward:", reward)
    print("State:", state)