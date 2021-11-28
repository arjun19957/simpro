def action_plan(entity, process_scenario_object):


    with process_scenario_object.register_request_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.register_request() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'register_request' ])

    with process_scenario_object.examine_thoroughly_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.examine_thoroughly() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'examine_thoroughly' ])

    with process_scenario_object.check_ticket_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.check_ticket() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'check_ticket' ])

    with process_scenario_object.decide_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.decide() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'decide' ])

    with process_scenario_object.reject_request_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.reject_request() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'reject_request' ])
