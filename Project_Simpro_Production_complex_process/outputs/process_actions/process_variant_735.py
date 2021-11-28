def action_plan(entity, process_scenario_object):


    with process_scenario_object.cytologischonderzoekbuiktumorpunctie_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.cytologischonderzoekbuiktumorpunctie() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'cytologischonderzoekbuiktumorpunctie' ])

    with process_scenario_object.thorax_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.thorax() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'thorax' ])

    with process_scenario_object.econsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.econsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'econsultpoliklinisch' ])

    with process_scenario_object.administratieftariefeerstepol_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.administratieftariefeerstepol() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'administratieftariefeerstepol' ])
