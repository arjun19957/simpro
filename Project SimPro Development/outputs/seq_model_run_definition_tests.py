def run_definition(env):
    entity = 1
   
    while env.now < 20:
        entity += 1
        yield env.timeout(2)
        env.process(action_plan(entity, env, process_scenario_object ))
        
      