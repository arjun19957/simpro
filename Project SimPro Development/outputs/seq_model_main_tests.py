env = simpy.Environment
env.process(run_definition(env))
env.run()