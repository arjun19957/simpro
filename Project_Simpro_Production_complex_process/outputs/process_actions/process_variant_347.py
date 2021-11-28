def action_plan(entity, process_scenario_object):


    with process_scenario_object.verloskgynaecjaarkaartkostenout_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.verloskgynaecjaarkaartkostenout() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'verloskgynaecjaarkaartkostenout' ])

    with process_scenario_object.vervolgconsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.vervolgconsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'vervolgconsultpoliklinisch' ])

    with process_scenario_object.botdensitometrielwk_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.botdensitometrielwk() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'botdensitometrielwk' ])

    with process_scenario_object.botdensitometriefemurhals_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.botdensitometriefemurhals() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'botdensitometriefemurhals' ])

    with process_scenario_object.telefonischconsult_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.telefonischconsult() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'telefonischconsult' ])

    with process_scenario_object.vervolgconsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.vervolgconsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'vervolgconsultpoliklinisch' ])

    with process_scenario_object.administratieftariefeerstepol_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.administratieftariefeerstepol() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'administratieftariefeerstepol' ])

    with process_scenario_object.vervolgconsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.vervolgconsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'vervolgconsultpoliklinisch' ])

    with process_scenario_object.administratieftariefeerstepol_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.administratieftariefeerstepol() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'administratieftariefeerstepol' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.hydroxyprogesteronmbvria_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.hydroxyprogesteronmbvria() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'hydroxyprogesteronmbvria' ])

    with process_scenario_object.fshenzymimmunologisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.fshenzymimmunologisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'fshenzymimmunologisch' ])

    with process_scenario_object.lhmbvradioisotopen_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.lhmbvradioisotopen() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'lhmbvradioisotopen' ])

    with process_scenario_object.tshenzymimmunologisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.tshenzymimmunologisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'tshenzymimmunologisch' ])

    with process_scenario_object.prolactinembveia_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.prolactinembveia() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'prolactinembveia' ])

    with process_scenario_object.deltaandrosteendion_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.deltaandrosteendion() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'deltaandrosteendion' ])

    with process_scenario_object.testosteronmbvradioisotopen_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.testosteronmbvradioisotopen() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'testosteronmbvradioisotopen' ])

    with process_scenario_object.sexhormonebindingglobulinembvria_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.sexhormonebindingglobulinembvria() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'sexhormonebindingglobulinembvria' ])

    with process_scenario_object.dheasulfaatmetextractiembvria_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dheasulfaatmetextractiembvria() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dheasulfaatmetextractiembvria' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])
