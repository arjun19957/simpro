def action_plan(entity, env, process_scenario_object):


    with register request_resource.request() as request:
        yield request
        env.process( process_scenario_object.register request(entity) )
        log_list.append([entity, env.now, 'register request' ])

    with check ticket_resource.request() as request:
        yield request
        env.process( process_scenario_object.check ticket(entity) )
        log_list.append([entity, env.now, 'check ticket' ])

    with examine thoroughly_resource.request() as request:
        yield request
        env.process( process_scenario_object.examine thoroughly(entity) )
        log_list.append([entity, env.now, 'examine thoroughly' ])

    with decide_resource.request() as request:
        yield request
        env.process( process_scenario_object.decide(entity) )
        log_list.append([entity, env.now, 'decide' ])

    with reject request_resource.request() as request:
        yield request
        env.process( process_scenario_object.reject request(entity) )
        log_list.append([entity, env.now, 'reject request' ])
