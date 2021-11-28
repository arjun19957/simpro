def action_plan(entity, env, process_scenario_object):


    with register request_resource.request() as request:
        yield request
        env.process( process_scenario_object.register request(entity) )
        log_list.append([entity, env.now, 'register request' ])

    with examine casually_resource.request() as request:
        yield request
        env.process( process_scenario_object.examine casually(entity) )
        log_list.append([entity, env.now, 'examine casually' ])

    with check ticket_resource.request() as request:
        yield request
        env.process( process_scenario_object.check ticket(entity) )
        log_list.append([entity, env.now, 'check ticket' ])

    with decide_resource.request() as request:
        yield request
        env.process( process_scenario_object.decide(entity) )
        log_list.append([entity, env.now, 'decide' ])

    with reinitiate request_resource.request() as request:
        yield request
        env.process( process_scenario_object.reinitiate request(entity) )
        log_list.append([entity, env.now, 'reinitiate request' ])

    with check ticket_resource.request() as request:
        yield request
        env.process( process_scenario_object.check ticket(entity) )
        log_list.append([entity, env.now, 'check ticket' ])

    with examine casually_resource.request() as request:
        yield request
        env.process( process_scenario_object.examine casually(entity) )
        log_list.append([entity, env.now, 'examine casually' ])

    with decide_resource.request() as request:
        yield request
        env.process( process_scenario_object.decide(entity) )
        log_list.append([entity, env.now, 'decide' ])

    with reinitiate request_resource.request() as request:
        yield request
        env.process( process_scenario_object.reinitiate request(entity) )
        log_list.append([entity, env.now, 'reinitiate request' ])

    with examine casually_resource.request() as request:
        yield request
        env.process( process_scenario_object.examine casually(entity) )
        log_list.append([entity, env.now, 'examine casually' ])

    with check ticket_resource.request() as request:
        yield request
        env.process( process_scenario_object.check ticket(entity) )
        log_list.append([entity, env.now, 'check ticket' ])

    with decide_resource.request() as request:
        yield request
        env.process( process_scenario_object.decide(entity) )
        log_list.append([entity, env.now, 'decide' ])

    with reject request_resource.request() as request:
        yield request
        env.process( process_scenario_object.reject request(entity) )
        log_list.append([entity, env.now, 'reject request' ])
