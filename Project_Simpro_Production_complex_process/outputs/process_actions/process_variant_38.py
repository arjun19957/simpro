def action_plan(entity, process_scenario_object):


    with process_scenario_object.vrwgeslorgadnexextirpatiedmvlapar_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.vrwgeslorgadnexextirpatiedmvlapar() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'vrwgeslorgadnexextirpatiedmvlapar' ])
