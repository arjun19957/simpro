def action_plan(entity, process_scenario_object):


    with process_scenario_object.econsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.econsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'econsultpoliklinisch' ])

    with process_scenario_object.administratieftariefeerstepol_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.administratieftariefeerstepol() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'administratieftariefeerstepol' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.vrwgeslorgcurettagegefractioneerd_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.vrwgeslorgcurettagegefractioneerd() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'vrwgeslorgcurettagegefractioneerd' ])

    with process_scenario_object.uterushysteroscopie_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.uterushysteroscopie() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'uterushysteroscopie' ])

    with process_scenario_object.klinischekaartverloskundeengynaeco_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klinischekaartverloskundeengynaeco() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klinischekaartverloskundeengynaeco' ])
