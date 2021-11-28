from outputs.utils import process_path_selector
from outputs.action_plan_list import action_plan_definer_instance


def run_definition(env, process_scenario_object, process_path_probabilities):
    entity = 1
   
    while env.now < 100:
        entity += 1
        yield env.timeout(2)
        
        entity_path = process_path_selector(process_path_probabilities)
        env.process(action_plan_definer_instance.action_plan_list[entity_path](entity, process_scenario_object))
        