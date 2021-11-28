def action_plan(entity, process_scenario_object):


    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.hematologieontstekscinttotlichaam_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.hematologieontstekscinttotlichaam() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'hematologieontstekscinttotlichaam' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.bloedgroepaboenrhesusfactor_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bloedgroepaboenrhesusfactor() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bloedgroepaboenrhesusfactor' ])

    with process_scenario_object.rhesusfactordcentrifugeermethodee_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.rhesusfactordcentrifugeermethodee() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'rhesusfactordcentrifugeermethodee' ])

    with process_scenario_object.haemoglobinefotoelectrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.haemoglobinefotoelectrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'haemoglobinefotoelectrischspoed' ])

    with process_scenario_object.leukocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leukocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leukocytentellenelektronisch' ])

    with process_scenario_object.crpcreactiefproteine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.crpcreactiefproteine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'crpcreactiefproteine' ])

    with process_scenario_object.screeningantistoffenerytrocyten_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.screeningantistoffenerytrocyten() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'screeningantistoffenerytrocyten' ])

    with process_scenario_object.bezinkingssnelheidfotoelektrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bezinkingssnelheidfotoelektrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bezinkingssnelheidfotoelektrisch' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.klinischeopnamea_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klinischeopnamea() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klinischeopnamea' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ovariumadnexextirpatiedmvlapar_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ovariumadnexextirpatiedmvlapar() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ovariumadnexextirpatiedmvlapar' ])

    with process_scenario_object.histologischonderzoekkleineresectie_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.histologischonderzoekkleineresectie() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'histologischonderzoekkleineresectie' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.verloskgynaecjaarkaartkostenout_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.verloskgynaecjaarkaartkostenout() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'verloskgynaecjaarkaartkostenout' ])

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
