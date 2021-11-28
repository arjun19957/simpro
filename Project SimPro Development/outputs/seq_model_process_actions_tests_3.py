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

    with pay compensation_resource.request() as request:
        yield request
        env.process( process_scenario_object.pay compensation(entity) )
        log_list.append([entity, env.now, 'pay compensation' ])
