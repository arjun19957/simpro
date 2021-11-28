def action_plan(entity, process_scenario_object):


    with process_scenario_object.verloskgynaeckortekaartkostenout_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.verloskgynaeckortekaartkostenout() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'verloskgynaeckortekaartkostenout' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.fshenzymimmunologisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.fshenzymimmunologisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'fshenzymimmunologisch' ])

    with process_scenario_object.lhmbvradioisotopen_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.lhmbvradioisotopen() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'lhmbvradioisotopen' ])

    with process_scenario_object.progesteronmbvradioisotopen_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.progesteronmbvradioisotopen() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'progesteronmbvradioisotopen' ])

    with process_scenario_object.testosteronmbvradioisotopen_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.testosteronmbvradioisotopen() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'testosteronmbvradioisotopen' ])

    with process_scenario_object.sexhormonebindingglobulinembvria_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.sexhormonebindingglobulinembvria() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'sexhormonebindingglobulinembvria' ])

    with process_scenario_object.alfafoetoproteine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.alfafoetoproteine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'alfafoetoproteine' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.econsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.econsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'econsultpoliklinisch' ])

    with process_scenario_object.administratieftariefeerstepol_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.administratieftariefeerstepol() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'administratieftariefeerstepol' ])

    with process_scenario_object.telefonischconsult_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.telefonischconsult() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'telefonischconsult' ])

    with process_scenario_object.vervolgconsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.vervolgconsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'vervolgconsultpoliklinisch' ])

    with process_scenario_object.verloskgynaecaanvkaartkostenout_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.verloskgynaecaanvkaartkostenout() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'verloskgynaecaanvkaartkostenout' ])

    with process_scenario_object.echografiegenitaliainterna_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.echografiegenitaliainterna() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'echografiegenitaliainterna' ])

    with process_scenario_object.vervolgconsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.vervolgconsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'vervolgconsultpoliklinisch' ])

    with process_scenario_object.echografiegenitaliainterna_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.echografiegenitaliainterna() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'echografiegenitaliainterna' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.alfafoetoproteine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.alfafoetoproteine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'alfafoetoproteine' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.vervolgconsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.vervolgconsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'vervolgconsultpoliklinisch' ])

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

    with process_scenario_object.cytologischonderzoekectocervix_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.cytologischonderzoekectocervix() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'cytologischonderzoekectocervix' ])

    with process_scenario_object.telefonischconsult_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.telefonischconsult() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'telefonischconsult' ])

    with process_scenario_object.histologischonderzoekbioptennno_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.histologischonderzoekbioptennno() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'histologischonderzoekbioptennno' ])

    with process_scenario_object.econsultbezoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.econsultbezoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'econsultbezoek' ])

    with process_scenario_object.telefonischconsult_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.telefonischconsult() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'telefonischconsult' ])

    with process_scenario_object.cytologischonderzoekectocervix_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.cytologischonderzoekectocervix() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'cytologischonderzoekectocervix' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.hemoglobinefotoelektrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.hemoglobinefotoelektrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'hemoglobinefotoelektrisch' ])

    with process_scenario_object.tshenzymimmunologisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.tshenzymimmunologisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'tshenzymimmunologisch' ])

    with process_scenario_object.alfafoetoproteine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.alfafoetoproteine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'alfafoetoproteine' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.vervolgconsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.vervolgconsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'vervolgconsultpoliklinisch' ])

    with process_scenario_object.administratieftariefeerstepol_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.administratieftariefeerstepol() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'administratieftariefeerstepol' ])

    with process_scenario_object.telefonischconsult_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.telefonischconsult() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'telefonischconsult' ])
