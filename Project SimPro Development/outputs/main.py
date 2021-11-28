
def main():
    env = simpy.Environment
    env.process(run_process())
    env.run()