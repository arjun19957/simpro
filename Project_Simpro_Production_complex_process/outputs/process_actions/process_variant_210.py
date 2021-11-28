def action_plan(entity, process_scenario_object):


    with process_scenario_object.verloskgynaeckortekaartkostenout_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.verloskgynaeckortekaartkostenout() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'verloskgynaeckortekaartkostenout' ])

    with process_scenario_object.echografiegenitaliainterna_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.echografiegenitaliainterna() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'echografiegenitaliainterna' ])

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

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.bilirubinegeconjugeerd_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bilirubinegeconjugeerd() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bilirubinegeconjugeerd' ])

    with process_scenario_object.bilirubinetotaal_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bilirubinetotaal() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bilirubinetotaal' ])

    with process_scenario_object.glucose_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.glucose() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'glucose' ])

    with process_scenario_object.ureum_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ureum() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ureum' ])

    with process_scenario_object.hemoglobinefotoelektrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.hemoglobinefotoelektrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'hemoglobinefotoelektrisch' ])

    with process_scenario_object.creatinine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatinine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatinine' ])

    with process_scenario_object.alkalischefosfatasekinetisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.alkalischefosfatasekinetisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'alkalischefosfatasekinetisch' ])

    with process_scenario_object.natriumvlamfotometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrisch' ])

    with process_scenario_object.kaliumpotentiometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumpotentiometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumpotentiometrisch' ])

    with process_scenario_object.sgotasatkinetisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.sgotasatkinetisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'sgotasatkinetisch' ])

    with process_scenario_object.sgptalatkinetisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.sgptalatkinetisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'sgptalatkinetisch' ])

    with process_scenario_object.melkzuurdehydrogenaseldhkinetisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.melkzuurdehydrogenaseldhkinetisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'melkzuurdehydrogenaseldhkinetisch' ])

    with process_scenario_object.bloedgroepaboenrhesusfactor_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bloedgroepaboenrhesusfactor() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bloedgroepaboenrhesusfactor' ])

    with process_scenario_object.rhesusfactordcentrifugeermethodee_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.rhesusfactordcentrifugeermethodee() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'rhesusfactordcentrifugeermethodee' ])

    with process_scenario_object.leukocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leukocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leukocytentellenelektronisch' ])

    with process_scenario_object.trombocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.trombocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'trombocytentellenelektronisch' ])

    with process_scenario_object.gammaglutamyltranspeptidase_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.gammaglutamyltranspeptidase() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'gammaglutamyltranspeptidase' ])

    with process_scenario_object.ceatumormarkermbvmeia_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ceatumormarkermbvmeia() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ceatumormarkermbvmeia' ])

    with process_scenario_object.calcium_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.calcium() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'calcium' ])

    with process_scenario_object.albumine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.albumine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'albumine' ])

    with process_scenario_object.screeningantistoffenerytrocyten_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.screeningantistoffenerytrocyten() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'screeningantistoffenerytrocyten' ])

    with process_scenario_object.cambvmeia_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.cambvmeia() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'cambvmeia' ])

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

    with process_scenario_object.echogeleidealsassbijpunctiebiopsie_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.echogeleidealsassbijpunctiebiopsie() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'echogeleidealsassbijpunctiebiopsie' ])

    with process_scenario_object.vervolgconsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.vervolgconsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'vervolgconsultpoliklinisch' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

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

    with process_scenario_object.glucose_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.glucose() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'glucose' ])

    with process_scenario_object.hemoglobinefotoelektrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.hemoglobinefotoelektrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'hemoglobinefotoelektrisch' ])

    with process_scenario_object.bloedgroepaboenrhesusfactor_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bloedgroepaboenrhesusfactor() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bloedgroepaboenrhesusfactor' ])

    with process_scenario_object.rhesusfactordcentrifugeermethodee_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.rhesusfactordcentrifugeermethodee() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'rhesusfactordcentrifugeermethodee' ])

    with process_scenario_object.hematocrietmbvcentrifuge_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.hematocrietmbvcentrifuge() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'hematocrietmbvcentrifuge' ])

    with process_scenario_object.gammaglutamyltranspeptidase_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.gammaglutamyltranspeptidase() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'gammaglutamyltranspeptidase' ])

    with process_scenario_object.screeningantistoffenerytrocyten_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.screeningantistoffenerytrocyten() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'screeningantistoffenerytrocyten' ])

    with process_scenario_object.cambvmeia_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.cambvmeia() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'cambvmeia' ])

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

    with process_scenario_object.buikstageringslaparotomoment_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.buikstageringslaparotomoment() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'buikstageringslaparotomoment' ])

    with process_scenario_object.cytologischonderzoekascites_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.cytologischonderzoekascites() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'cytologischonderzoekascites' ])

    with process_scenario_object.histologischonderzoekkleineresectie_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.histologischonderzoekkleineresectie() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'histologischonderzoekkleineresectie' ])

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

    with process_scenario_object.glucosespoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.glucosespoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'glucosespoed' ])

    with process_scenario_object.glucosespoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.glucosespoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'glucosespoed' ])

    with process_scenario_object.glucosespoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.glucosespoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'glucosespoed' ])

    with process_scenario_object.methemoglobinesulfhemoglobineelk_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.methemoglobinesulfhemoglobineelk() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'methemoglobinesulfhemoglobineelk' ])

    with process_scenario_object.methemoglobinesulfhemoglobineelk_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.methemoglobinesulfhemoglobineelk() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'methemoglobinesulfhemoglobineelk' ])

    with process_scenario_object.methemoglobinesulfhemoglobineelk_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.methemoglobinesulfhemoglobineelk() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'methemoglobinesulfhemoglobineelk' ])

    with process_scenario_object.bicarbonaat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bicarbonaat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bicarbonaat' ])

    with process_scenario_object.bicarbonaat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bicarbonaat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bicarbonaat' ])

    with process_scenario_object.bicarbonaat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bicarbonaat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bicarbonaat' ])

    with process_scenario_object.calciumspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.calciumspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'calciumspoed' ])

    with process_scenario_object.calciumspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.calciumspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'calciumspoed' ])

    with process_scenario_object.calciumspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.calciumspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'calciumspoed' ])

    with process_scenario_object.cohbkwn_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.cohbkwn() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'cohbkwn' ])

    with process_scenario_object.cohbkwn_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.cohbkwn() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'cohbkwn' ])

    with process_scenario_object.cohbkwn_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.cohbkwn() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'cohbkwn' ])

    with process_scenario_object.natriumvlamfotometrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrischspoed' ])

    with process_scenario_object.natriumvlamfotometrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrischspoed' ])

    with process_scenario_object.natriumvlamfotometrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrischspoed' ])

    with process_scenario_object.kaliumvlamfotometrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumvlamfotometrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumvlamfotometrischspoed' ])

    with process_scenario_object.kaliumvlamfotometrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumvlamfotometrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumvlamfotometrischspoed' ])

    with process_scenario_object.kaliumvlamfotometrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumvlamfotometrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumvlamfotometrischspoed' ])

    with process_scenario_object.haemoglobinefotoelectrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.haemoglobinefotoelectrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'haemoglobinefotoelectrischspoed' ])

    with process_scenario_object.haemoglobinefotoelectrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.haemoglobinefotoelectrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'haemoglobinefotoelectrischspoed' ])

    with process_scenario_object.haemoglobinefotoelectrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.haemoglobinefotoelectrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'haemoglobinefotoelectrischspoed' ])

    with process_scenario_object.actuelephpcostandbicarbonaat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.actuelephpcostandbicarbonaat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'actuelephpcostandbicarbonaat' ])

    with process_scenario_object.actuelephpcostandbicarbonaat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.actuelephpcostandbicarbonaat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'actuelephpcostandbicarbonaat' ])

    with process_scenario_object.actuelephpcostandbicarbonaat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.actuelephpcostandbicarbonaat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'actuelephpcostandbicarbonaat' ])

    with process_scenario_object.kruisproefvolledigdriemethoden_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kruisproefvolledigdriemethoden() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kruisproefvolledigdriemethoden' ])

    with process_scenario_object.kruisproefvolledigdriemethoden_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kruisproefvolledigdriemethoden() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kruisproefvolledigdriemethoden' ])

    with process_scenario_object.melkzuurenzymatischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.melkzuurenzymatischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'melkzuurenzymatischspoed' ])

    with process_scenario_object.melkzuurenzymatischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.melkzuurenzymatischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'melkzuurenzymatischspoed' ])

    with process_scenario_object.melkzuurenzymatischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.melkzuurenzymatischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'melkzuurenzymatischspoed' ])

    with process_scenario_object.osaturatie_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.osaturatie() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'osaturatie' ])

    with process_scenario_object.osaturatie_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.osaturatie() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'osaturatie' ])

    with process_scenario_object.osaturatie_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.osaturatie() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'osaturatie' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

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

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.sedimentspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.sedimentspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'sedimentspoed' ])

    with process_scenario_object.bilirubinekwantitatieftotaalofdirect_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bilirubinekwantitatieftotaalofdirect() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bilirubinekwantitatieftotaalofdirect' ])

    with process_scenario_object.glucosespoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.glucosespoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'glucosespoed' ])

    with process_scenario_object.ureumspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ureumspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ureumspoed' ])

    with process_scenario_object.alfaamylasespoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.alfaamylasespoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'alfaamylasespoed' ])

    with process_scenario_object.creatininespoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatininespoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatininespoed' ])

    with process_scenario_object.alkalischefosfatasekinetischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.alkalischefosfatasekinetischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'alkalischefosfatasekinetischspoed' ])

    with process_scenario_object.natriumvlamfotometrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrischspoed' ])

    with process_scenario_object.kaliumvlamfotometrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumvlamfotometrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumvlamfotometrischspoed' ])

    with process_scenario_object.totaaleiwitcolorimetrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.totaaleiwitcolorimetrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'totaaleiwitcolorimetrischspoed' ])

    with process_scenario_object.sgptalatkinetischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.sgptalatkinetischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'sgptalatkinetischspoed' ])

    with process_scenario_object.sgotasatkinetischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.sgotasatkinetischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'sgotasatkinetischspoed' ])

    with process_scenario_object.bacteriologischonderzoekmetkweeknie_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bacteriologischonderzoekmetkweeknie() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bacteriologischonderzoekmetkweeknie' ])

    with process_scenario_object.bacteriologischonderzoekmetkweeknie_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bacteriologischonderzoekmetkweeknie() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bacteriologischonderzoekmetkweeknie' ])

    with process_scenario_object.differentieletellingautomatisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.differentieletellingautomatisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'differentieletellingautomatisch' ])

    with process_scenario_object.haemoglobinefotoelectrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.haemoglobinefotoelectrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'haemoglobinefotoelectrischspoed' ])

    with process_scenario_object.haemoglobinefotoelectrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.haemoglobinefotoelectrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'haemoglobinefotoelectrischspoed' ])

    with process_scenario_object.hematocrietspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.hematocrietspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'hematocrietspoed' ])

    with process_scenario_object.trombocytentellenspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.trombocytentellenspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'trombocytentellenspoed' ])

    with process_scenario_object.gammaglutamyltranspeptidasespoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.gammaglutamyltranspeptidasespoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'gammaglutamyltranspeptidasespoed' ])

    with process_scenario_object.leucocytentellenelectronischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leucocytentellenelectronischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leucocytentellenelectronischspoed' ])

    with process_scenario_object.urineonderzoekkwalitatief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.urineonderzoekkwalitatief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'urineonderzoekkwalitatief' ])

    with process_scenario_object.crpcreactiefproteinespoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.crpcreactiefproteinespoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'crpcreactiefproteinespoed' ])

    with process_scenario_object.albuminespoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.albuminespoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'albuminespoed' ])

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

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.thorax_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.thorax() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'thorax' ])

    with process_scenario_object.buikoverzicht_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.buikoverzicht() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'buikoverzicht' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ecgelektrocardiografie_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ecgelektrocardiografie() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ecgelektrocardiografie' ])

    with process_scenario_object.pijnbestrijdaanleggenpatientcontroll_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.pijnbestrijdaanleggenpatientcontroll() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'pijnbestrijdaanleggenpatientcontroll' ])

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

    with process_scenario_object.ureumspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ureumspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ureumspoed' ])

    with process_scenario_object.creatininespoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatininespoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatininespoed' ])

    with process_scenario_object.chloridespoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.chloridespoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'chloridespoed' ])

    with process_scenario_object.bicarbonaat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bicarbonaat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bicarbonaat' ])

    with process_scenario_object.bicarbonaat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bicarbonaat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bicarbonaat' ])

    with process_scenario_object.bicarbonaat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bicarbonaat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bicarbonaat' ])

    with process_scenario_object.calciumspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.calciumspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'calciumspoed' ])

    with process_scenario_object.natriumvlamfotometrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrischspoed' ])

    with process_scenario_object.kaliumvlamfotometrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumvlamfotometrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumvlamfotometrischspoed' ])

    with process_scenario_object.fibrinogeen_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.fibrinogeen() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'fibrinogeen' ])

    with process_scenario_object.bacteriologischonderzoekmetkweeknie_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bacteriologischonderzoekmetkweeknie() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bacteriologischonderzoekmetkweeknie' ])

    with process_scenario_object.bacteriologischonderzoekmetkweeknie_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bacteriologischonderzoekmetkweeknie() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bacteriologischonderzoekmetkweeknie' ])

    with process_scenario_object.differentieletellingautomatisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.differentieletellingautomatisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'differentieletellingautomatisch' ])

    with process_scenario_object.haemoglobinefotoelectrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.haemoglobinefotoelectrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'haemoglobinefotoelectrischspoed' ])

    with process_scenario_object.trombocytentellenspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.trombocytentellenspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'trombocytentellenspoed' ])

    with process_scenario_object.actuelephpcostandbicarbonaat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.actuelephpcostandbicarbonaat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'actuelephpcostandbicarbonaat' ])

    with process_scenario_object.actuelephpcostandbicarbonaat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.actuelephpcostandbicarbonaat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'actuelephpcostandbicarbonaat' ])

    with process_scenario_object.actuelephpcostandbicarbonaat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.actuelephpcostandbicarbonaat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'actuelephpcostandbicarbonaat' ])

    with process_scenario_object.fdpdimeerimmunologisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.fdpdimeerimmunologisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'fdpdimeerimmunologisch' ])

    with process_scenario_object.leucocytentellenelectronischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leucocytentellenelectronischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leucocytentellenelectronischspoed' ])

    with process_scenario_object.crpcreactiefproteinespoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.crpcreactiefproteinespoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'crpcreactiefproteinespoed' ])

    with process_scenario_object.albuminespoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.albuminespoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'albuminespoed' ])

    with process_scenario_object.osaturatie_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.osaturatie() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'osaturatie' ])

    with process_scenario_object.osaturatie_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.osaturatie() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'osaturatie' ])

    with process_scenario_object.osaturatie_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.osaturatie() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'osaturatie' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.ctapulmonalis_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ctapulmonalis() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ctapulmonalis' ])

    with process_scenario_object.thoraxopzaal_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.thoraxopzaal() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'thoraxopzaal' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.verloskgynaecaanvkaartkostenout_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.verloskgynaecaanvkaartkostenout() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'verloskgynaecaanvkaartkostenout' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.creatininespoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatininespoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatininespoed' ])

    with process_scenario_object.natriumvlamfotometrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrischspoed' ])

    with process_scenario_object.kaliumvlamfotometrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumvlamfotometrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumvlamfotometrischspoed' ])

    with process_scenario_object.haemoglobinefotoelectrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.haemoglobinefotoelectrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'haemoglobinefotoelectrischspoed' ])

    with process_scenario_object.leucocytentellenelectronischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leucocytentellenelectronischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leucocytentellenelectronischspoed' ])

    with process_scenario_object.crpcreactiefproteinespoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.crpcreactiefproteinespoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'crpcreactiefproteinespoed' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

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

    with process_scenario_object.differentieletellingautomatisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.differentieletellingautomatisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'differentieletellingautomatisch' ])

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

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.afwezigheidsdaga_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.afwezigheidsdaga() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'afwezigheidsdaga' ])

    with process_scenario_object.afwezigheidsdaga_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.afwezigheidsdaga() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'afwezigheidsdaga' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

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

    with process_scenario_object.ureum_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ureum() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ureum' ])

    with process_scenario_object.creatininespoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatininespoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatininespoed' ])

    with process_scenario_object.natriumvlamfotometrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrischspoed' ])

    with process_scenario_object.kaliumvlamfotometrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumvlamfotometrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumvlamfotometrischspoed' ])

    with process_scenario_object.bloedgroepaboenrhesusfactor_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bloedgroepaboenrhesusfactor() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bloedgroepaboenrhesusfactor' ])

    with process_scenario_object.rhesusfactordcentrifugeermethodee_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.rhesusfactordcentrifugeermethodee() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'rhesusfactordcentrifugeermethodee' ])

    with process_scenario_object.differentieletellingautomatisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.differentieletellingautomatisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'differentieletellingautomatisch' ])

    with process_scenario_object.haemoglobinefotoelectrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.haemoglobinefotoelectrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'haemoglobinefotoelectrischspoed' ])

    with process_scenario_object.trombocytentellenspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.trombocytentellenspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'trombocytentellenspoed' ])

    with process_scenario_object.kruisproefvolledigdriemethoden_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kruisproefvolledigdriemethoden() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kruisproefvolledigdriemethoden' ])

    with process_scenario_object.kruisproefvolledigdriemethoden_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kruisproefvolledigdriemethoden() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kruisproefvolledigdriemethoden' ])

    with process_scenario_object.kruisproefvolledigdriemethoden_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kruisproefvolledigdriemethoden() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kruisproefvolledigdriemethoden' ])

    with process_scenario_object.leucocytentellenelectronischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leucocytentellenelectronischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leucocytentellenelectronischspoed' ])

    with process_scenario_object.screeningantistoffenerytrocyten_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.screeningantistoffenerytrocyten() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'screeningantistoffenerytrocyten' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.gefiltreerderytrocytenconcentraat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.gefiltreerderytrocytenconcentraat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'gefiltreerderytrocytenconcentraat' ])

    with process_scenario_object.gefiltreerderytrocytenconcentraat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.gefiltreerderytrocytenconcentraat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'gefiltreerderytrocytenconcentraat' ])

    with process_scenario_object.gefiltreerderytrocytenconcentraat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.gefiltreerderytrocytenconcentraat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'gefiltreerderytrocytenconcentraat' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.sgptalatkinetischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.sgptalatkinetischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'sgptalatkinetischspoed' ])

    with process_scenario_object.sgotasatkinetischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.sgotasatkinetischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'sgotasatkinetischspoed' ])

    with process_scenario_object.haemoglobinefotoelectrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.haemoglobinefotoelectrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'haemoglobinefotoelectrischspoed' ])

    with process_scenario_object.trombocytentellenspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.trombocytentellenspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'trombocytentellenspoed' ])

    with process_scenario_object.leucocytentellenelectronischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leucocytentellenelectronischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leucocytentellenelectronischspoed' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.ctabdomen_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ctabdomen() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ctabdomen' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.paclitaxel_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.paclitaxel() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'paclitaxel' ])

    with process_scenario_object.inwendgeneeskkortekaartkostenout_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.inwendgeneeskkortekaartkostenout() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'inwendgeneeskkortekaartkostenout' ])

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

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.differentieletellingautomatisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.differentieletellingautomatisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'differentieletellingautomatisch' ])

    with process_scenario_object.haemoglobinefotoelectrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.haemoglobinefotoelectrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'haemoglobinefotoelectrischspoed' ])

    with process_scenario_object.trombocytentellenspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.trombocytentellenspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'trombocytentellenspoed' ])

    with process_scenario_object.leucocytentellenelectronischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leucocytentellenelectronischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leucocytentellenelectronischspoed' ])

    with process_scenario_object.cambvmeia_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.cambvmeia() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'cambvmeia' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.vervolgconsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.vervolgconsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'vervolgconsultpoliklinisch' ])

    with process_scenario_object.paclitaxel_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.paclitaxel() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'paclitaxel' ])

    with process_scenario_object.dagverplegingallespecbehkindrev_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dagverplegingallespecbehkindrev() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dagverplegingallespecbehkindrev' ])

    with process_scenario_object.dagverpleginga_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dagverpleginga() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dagverpleginga' ])

    with process_scenario_object.vervolgconsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.vervolgconsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'vervolgconsultpoliklinisch' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.sgptalatkinetischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.sgptalatkinetischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'sgptalatkinetischspoed' ])

    with process_scenario_object.sgotasatkinetischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.sgotasatkinetischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'sgotasatkinetischspoed' ])

    with process_scenario_object.kreatininefosfokinasespoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kreatininefosfokinasespoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kreatininefosfokinasespoed' ])

    with process_scenario_object.creatinefosfokinasembspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatinefosfokinasembspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatinefosfokinasembspoed' ])

    with process_scenario_object.troponinetmbvelisa_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.troponinetmbvelisa() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'troponinetmbvelisa' ])

    with process_scenario_object.cambvmeia_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.cambvmeia() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'cambvmeia' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.vervolgconsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.vervolgconsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'vervolgconsultpoliklinisch' ])

    with process_scenario_object.klinischeopnamea_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klinischeopnamea() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klinischeopnamea' ])

    with process_scenario_object.paclitaxel_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.paclitaxel() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'paclitaxel' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

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

    with process_scenario_object.bilirubinekwantitatieftotaalofdirect_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bilirubinekwantitatieftotaalofdirect() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bilirubinekwantitatieftotaalofdirect' ])

    with process_scenario_object.creatininespoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatininespoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatininespoed' ])

    with process_scenario_object.alkalischefosfatasekinetischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.alkalischefosfatasekinetischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'alkalischefosfatasekinetischspoed' ])

    with process_scenario_object.natriumvlamfotometrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrischspoed' ])

    with process_scenario_object.kaliumvlamfotometrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumvlamfotometrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumvlamfotometrischspoed' ])

    with process_scenario_object.sgotasatkinetischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.sgotasatkinetischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'sgotasatkinetischspoed' ])

    with process_scenario_object.bacteriologischonderzoekmetkweeknie_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bacteriologischonderzoekmetkweeknie() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bacteriologischonderzoekmetkweeknie' ])

    with process_scenario_object.bacteriologischonderzoekmetkweeknie_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bacteriologischonderzoekmetkweeknie() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bacteriologischonderzoekmetkweeknie' ])

    with process_scenario_object.haemoglobinefotoelectrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.haemoglobinefotoelectrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'haemoglobinefotoelectrischspoed' ])

    with process_scenario_object.hematocrietspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.hematocrietspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'hematocrietspoed' ])

    with process_scenario_object.trombocytentellenspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.trombocytentellenspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'trombocytentellenspoed' ])

    with process_scenario_object.leucocytentellenelectronischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leucocytentellenelectronischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leucocytentellenelectronischspoed' ])

    with process_scenario_object.crpcreactiefproteine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.crpcreactiefproteine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'crpcreactiefproteine' ])

    with process_scenario_object.albuminespoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.albuminespoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'albuminespoed' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.thorax_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.thorax() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'thorax' ])

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

    with process_scenario_object.ecgelektrocardiografie_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ecgelektrocardiografie() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ecgelektrocardiografie' ])

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

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.bilirubinekwantitatieftotaalofdirect_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bilirubinekwantitatieftotaalofdirect() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bilirubinekwantitatieftotaalofdirect' ])

    with process_scenario_object.ureumspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ureumspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ureumspoed' ])

    with process_scenario_object.urinezuurmeturicaseuvspectrofotome_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.urinezuurmeturicaseuvspectrofotome() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'urinezuurmeturicaseuvspectrofotome' ])

    with process_scenario_object.creatininespoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatininespoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatininespoed' ])

    with process_scenario_object.alkalischefosfatasekinetischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.alkalischefosfatasekinetischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'alkalischefosfatasekinetischspoed' ])

    with process_scenario_object.bicarbonaat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bicarbonaat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bicarbonaat' ])

    with process_scenario_object.calciumspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.calciumspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'calciumspoed' ])

    with process_scenario_object.natriumvlamfotometrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrischspoed' ])

    with process_scenario_object.kaliumvlamfotometrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumvlamfotometrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumvlamfotometrischspoed' ])

    with process_scenario_object.sgptalatkinetischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.sgptalatkinetischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'sgptalatkinetischspoed' ])

    with process_scenario_object.sgotasatkinetischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.sgotasatkinetischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'sgotasatkinetischspoed' ])

    with process_scenario_object.bacteriologischonderzoekmetkweeknie_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bacteriologischonderzoekmetkweeknie() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bacteriologischonderzoekmetkweeknie' ])

    with process_scenario_object.bloedgroepaboenrhesusfactor_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bloedgroepaboenrhesusfactor() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bloedgroepaboenrhesusfactor' ])

    with process_scenario_object.rhesusfactordcentrifugeermethodee_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.rhesusfactordcentrifugeermethodee() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'rhesusfactordcentrifugeermethodee' ])

    with process_scenario_object.differentieletellingautomatisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.differentieletellingautomatisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'differentieletellingautomatisch' ])

    with process_scenario_object.haemoglobinefotoelectrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.haemoglobinefotoelectrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'haemoglobinefotoelectrischspoed' ])

    with process_scenario_object.trombocytentellenspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.trombocytentellenspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'trombocytentellenspoed' ])

    with process_scenario_object.actuelephpcostandbicarbonaat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.actuelephpcostandbicarbonaat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'actuelephpcostandbicarbonaat' ])

    with process_scenario_object.kruisproefvolledigdriemethoden_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kruisproefvolledigdriemethoden() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kruisproefvolledigdriemethoden' ])

    with process_scenario_object.kruisproefvolledigdriemethoden_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kruisproefvolledigdriemethoden() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kruisproefvolledigdriemethoden' ])

    with process_scenario_object.kruisproefvolledigdriemethoden_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kruisproefvolledigdriemethoden() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kruisproefvolledigdriemethoden' ])

    with process_scenario_object.kruisproefvolledigdriemethoden_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kruisproefvolledigdriemethoden() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kruisproefvolledigdriemethoden' ])

    with process_scenario_object.leucocytentellenelectronischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leucocytentellenelectronischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leucocytentellenelectronischspoed' ])

    with process_scenario_object.albuminespoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.albuminespoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'albuminespoed' ])

    with process_scenario_object.osaturatie_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.osaturatie() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'osaturatie' ])

    with process_scenario_object.screeningantistoffenerytrocyten_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.screeningantistoffenerytrocyten() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'screeningantistoffenerytrocyten' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.dieetnno_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dieetnno() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dieetnno' ])

    with process_scenario_object.gefiltreerderytrocytenconcentraat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.gefiltreerderytrocytenconcentraat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'gefiltreerderytrocytenconcentraat' ])

    with process_scenario_object.gefiltreerderytrocytenconcentraat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.gefiltreerderytrocytenconcentraat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'gefiltreerderytrocytenconcentraat' ])

    with process_scenario_object.gefiltreerderytrocytenconcentraat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.gefiltreerderytrocytenconcentraat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'gefiltreerderytrocytenconcentraat' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ecgelektrocardiografie_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ecgelektrocardiografie() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ecgelektrocardiografie' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.dieetnno_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dieetnno() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dieetnno' ])

    with process_scenario_object.gefiltreerderytrocytenconcentraat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.gefiltreerderytrocytenconcentraat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'gefiltreerderytrocytenconcentraat' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.bilirubinetotaal_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bilirubinetotaal() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bilirubinetotaal' ])

    with process_scenario_object.ureum_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ureum() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ureum' ])

    with process_scenario_object.hemoglobinefotoelektrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.hemoglobinefotoelektrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'hemoglobinefotoelektrisch' ])

    with process_scenario_object.urinezuurmeturicaseuvspectrofotome_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.urinezuurmeturicaseuvspectrofotome() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'urinezuurmeturicaseuvspectrofotome' ])

    with process_scenario_object.creatinine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatinine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatinine' ])

    with process_scenario_object.alkalischefosfatasekinetisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.alkalischefosfatasekinetisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'alkalischefosfatasekinetisch' ])

    with process_scenario_object.natriumvlamfotometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrisch' ])

    with process_scenario_object.kaliumpotentiometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumpotentiometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumpotentiometrisch' ])

    with process_scenario_object.sgotasatkinetisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.sgotasatkinetisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'sgotasatkinetisch' ])

    with process_scenario_object.sgptalatkinetisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.sgptalatkinetisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'sgptalatkinetisch' ])

    with process_scenario_object.differentieletellingautomatisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.differentieletellingautomatisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'differentieletellingautomatisch' ])

    with process_scenario_object.leukocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leukocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leukocytentellenelektronisch' ])

    with process_scenario_object.trombocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.trombocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'trombocytentellenelektronisch' ])

    with process_scenario_object.calcium_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.calcium() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'calcium' ])

    with process_scenario_object.crpcreactiefproteine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.crpcreactiefproteine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'crpcreactiefproteine' ])

    with process_scenario_object.albumine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.albumine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'albumine' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.dagverplegingallespecbehkindrev_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dagverplegingallespecbehkindrev() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dagverplegingallespecbehkindrev' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.creatininespoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatininespoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatininespoed' ])

    with process_scenario_object.natriumvlamfotometrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrischspoed' ])

    with process_scenario_object.kaliumvlamfotometrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumvlamfotometrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumvlamfotometrischspoed' ])

    with process_scenario_object.differentieletellingautomatisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.differentieletellingautomatisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'differentieletellingautomatisch' ])

    with process_scenario_object.haemoglobinefotoelectrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.haemoglobinefotoelectrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'haemoglobinefotoelectrischspoed' ])

    with process_scenario_object.trombocytentellenspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.trombocytentellenspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'trombocytentellenspoed' ])

    with process_scenario_object.leucocytentellenelectronischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leucocytentellenelectronischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leucocytentellenelectronischspoed' ])

    with process_scenario_object.cambvmeia_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.cambvmeia() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'cambvmeia' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.vervolgconsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.vervolgconsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'vervolgconsultpoliklinisch' ])

    with process_scenario_object.klinischeopnamea_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klinischeopnamea() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klinischeopnamea' ])

    with process_scenario_object.klinischeopnamea_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klinischeopnamea() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klinischeopnamea' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.dagverpleginga_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dagverpleginga() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dagverpleginga' ])

    with process_scenario_object.paclitaxel_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.paclitaxel() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'paclitaxel' ])

    with process_scenario_object.dieetnno_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dieetnno() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dieetnno' ])

    with process_scenario_object.ctabdomen_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ctabdomen() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ctabdomen' ])

    with process_scenario_object.inwendgeneeskaanvkaartkostenout_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.inwendgeneeskaanvkaartkostenout() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'inwendgeneeskaanvkaartkostenout' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

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

    with process_scenario_object.bilirubinetotaal_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bilirubinetotaal() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bilirubinetotaal' ])

    with process_scenario_object.glucose_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.glucose() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'glucose' ])

    with process_scenario_object.ureum_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ureum() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ureum' ])

    with process_scenario_object.hemoglobinefotoelektrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.hemoglobinefotoelektrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'hemoglobinefotoelektrisch' ])

    with process_scenario_object.creatinine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatinine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatinine' ])

    with process_scenario_object.alkalischefosfatasekinetisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.alkalischefosfatasekinetisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'alkalischefosfatasekinetisch' ])

    with process_scenario_object.natriumvlamfotometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrisch' ])

    with process_scenario_object.kaliumpotentiometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumpotentiometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumpotentiometrisch' ])

    with process_scenario_object.sgotasatkinetisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.sgotasatkinetisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'sgotasatkinetisch' ])

    with process_scenario_object.sgptalatkinetisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.sgptalatkinetisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'sgptalatkinetisch' ])

    with process_scenario_object.bloedgroepaboenrhesusfactor_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bloedgroepaboenrhesusfactor() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bloedgroepaboenrhesusfactor' ])

    with process_scenario_object.rhesusfactordcentrifugeermethodee_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.rhesusfactordcentrifugeermethodee() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'rhesusfactordcentrifugeermethodee' ])

    with process_scenario_object.differentieletellingautomatisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.differentieletellingautomatisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'differentieletellingautomatisch' ])

    with process_scenario_object.protrombinetijdquickowrenofmodif_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.protrombinetijdquickowrenofmodif() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'protrombinetijdquickowrenofmodif' ])

    with process_scenario_object.leukocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leukocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leukocytentellenelektronisch' ])

    with process_scenario_object.trombocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.trombocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'trombocytentellenelektronisch' ])

    with process_scenario_object.heparinebepalingkaolinecefalinetij_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.heparinebepalingkaolinecefalinetij() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'heparinebepalingkaolinecefalinetij' ])

    with process_scenario_object.gammaglutamyltranspeptidase_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.gammaglutamyltranspeptidase() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'gammaglutamyltranspeptidase' ])

    with process_scenario_object.calcium_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.calcium() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'calcium' ])

    with process_scenario_object.albumine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.albumine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'albumine' ])

    with process_scenario_object.screeningantistoffenerytrocyten_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.screeningantistoffenerytrocyten() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'screeningantistoffenerytrocyten' ])

    with process_scenario_object.cambvmeia_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.cambvmeia() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'cambvmeia' ])

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

    with process_scenario_object.buikstageringslaparotomoment_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.buikstageringslaparotomoment() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'buikstageringslaparotomoment' ])

    with process_scenario_object.histologischonderzoekgroteresectiep_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.histologischonderzoekgroteresectiep() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'histologischonderzoekgroteresectiep' ])

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

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.glucosespoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.glucosespoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'glucosespoed' ])

    with process_scenario_object.glucosespoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.glucosespoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'glucosespoed' ])

    with process_scenario_object.glucosespoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.glucosespoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'glucosespoed' ])

    with process_scenario_object.glucosespoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.glucosespoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'glucosespoed' ])

    with process_scenario_object.methemoglobinesulfhemoglobineelk_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.methemoglobinesulfhemoglobineelk() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'methemoglobinesulfhemoglobineelk' ])

    with process_scenario_object.methemoglobinesulfhemoglobineelk_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.methemoglobinesulfhemoglobineelk() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'methemoglobinesulfhemoglobineelk' ])

    with process_scenario_object.methemoglobinesulfhemoglobineelk_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.methemoglobinesulfhemoglobineelk() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'methemoglobinesulfhemoglobineelk' ])

    with process_scenario_object.methemoglobinesulfhemoglobineelk_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.methemoglobinesulfhemoglobineelk() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'methemoglobinesulfhemoglobineelk' ])

    with process_scenario_object.bicarbonaat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bicarbonaat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bicarbonaat' ])

    with process_scenario_object.bicarbonaat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bicarbonaat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bicarbonaat' ])

    with process_scenario_object.bicarbonaat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bicarbonaat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bicarbonaat' ])

    with process_scenario_object.bicarbonaat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bicarbonaat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bicarbonaat' ])

    with process_scenario_object.calciumspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.calciumspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'calciumspoed' ])

    with process_scenario_object.calciumspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.calciumspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'calciumspoed' ])

    with process_scenario_object.calciumspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.calciumspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'calciumspoed' ])

    with process_scenario_object.calciumspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.calciumspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'calciumspoed' ])

    with process_scenario_object.cohbkwn_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.cohbkwn() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'cohbkwn' ])

    with process_scenario_object.cohbkwn_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.cohbkwn() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'cohbkwn' ])

    with process_scenario_object.cohbkwn_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.cohbkwn() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'cohbkwn' ])

    with process_scenario_object.cohbkwn_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.cohbkwn() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'cohbkwn' ])

    with process_scenario_object.natriumvlamfotometrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrischspoed' ])

    with process_scenario_object.natriumvlamfotometrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrischspoed' ])

    with process_scenario_object.natriumvlamfotometrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrischspoed' ])

    with process_scenario_object.natriumvlamfotometrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrischspoed' ])

    with process_scenario_object.kaliumvlamfotometrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumvlamfotometrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumvlamfotometrischspoed' ])

    with process_scenario_object.kaliumvlamfotometrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumvlamfotometrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumvlamfotometrischspoed' ])

    with process_scenario_object.kaliumvlamfotometrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumvlamfotometrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumvlamfotometrischspoed' ])

    with process_scenario_object.kaliumvlamfotometrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumvlamfotometrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumvlamfotometrischspoed' ])

    with process_scenario_object.haemoglobinefotoelectrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.haemoglobinefotoelectrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'haemoglobinefotoelectrischspoed' ])

    with process_scenario_object.haemoglobinefotoelectrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.haemoglobinefotoelectrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'haemoglobinefotoelectrischspoed' ])

    with process_scenario_object.haemoglobinefotoelectrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.haemoglobinefotoelectrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'haemoglobinefotoelectrischspoed' ])

    with process_scenario_object.haemoglobinefotoelectrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.haemoglobinefotoelectrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'haemoglobinefotoelectrischspoed' ])

    with process_scenario_object.protrombinetijdquickowrenofmodif_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.protrombinetijdquickowrenofmodif() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'protrombinetijdquickowrenofmodif' ])

    with process_scenario_object.trombocytentellenspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.trombocytentellenspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'trombocytentellenspoed' ])

    with process_scenario_object.trombocytentellenspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.trombocytentellenspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'trombocytentellenspoed' ])

    with process_scenario_object.heparinebepalingkaolinecefalinetij_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.heparinebepalingkaolinecefalinetij() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'heparinebepalingkaolinecefalinetij' ])

    with process_scenario_object.actuelephpcostandbicarbonaat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.actuelephpcostandbicarbonaat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'actuelephpcostandbicarbonaat' ])

    with process_scenario_object.actuelephpcostandbicarbonaat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.actuelephpcostandbicarbonaat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'actuelephpcostandbicarbonaat' ])

    with process_scenario_object.actuelephpcostandbicarbonaat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.actuelephpcostandbicarbonaat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'actuelephpcostandbicarbonaat' ])

    with process_scenario_object.actuelephpcostandbicarbonaat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.actuelephpcostandbicarbonaat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'actuelephpcostandbicarbonaat' ])

    with process_scenario_object.kruisproefvolledigdriemethoden_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kruisproefvolledigdriemethoden() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kruisproefvolledigdriemethoden' ])

    with process_scenario_object.kruisproefvolledigdriemethoden_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kruisproefvolledigdriemethoden() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kruisproefvolledigdriemethoden' ])

    with process_scenario_object.melkzuurenzymatischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.melkzuurenzymatischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'melkzuurenzymatischspoed' ])

    with process_scenario_object.melkzuurenzymatischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.melkzuurenzymatischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'melkzuurenzymatischspoed' ])

    with process_scenario_object.melkzuurenzymatischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.melkzuurenzymatischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'melkzuurenzymatischspoed' ])

    with process_scenario_object.melkzuurenzymatischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.melkzuurenzymatischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'melkzuurenzymatischspoed' ])

    with process_scenario_object.osaturatie_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.osaturatie() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'osaturatie' ])

    with process_scenario_object.osaturatie_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.osaturatie() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'osaturatie' ])

    with process_scenario_object.osaturatie_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.osaturatie() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'osaturatie' ])

    with process_scenario_object.osaturatie_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.osaturatie() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'osaturatie' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.thoraxopzaal_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.thoraxopzaal() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'thoraxopzaal' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.trombocytenleukoverwijderddonor_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.trombocytenleukoverwijderddonor() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'trombocytenleukoverwijderddonor' ])

    with process_scenario_object.gefiltreerderytrocytenconcentraat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.gefiltreerderytrocytenconcentraat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'gefiltreerderytrocytenconcentraat' ])

    with process_scenario_object.gefiltreerderytrocytenconcentraat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.gefiltreerderytrocytenconcentraat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'gefiltreerderytrocytenconcentraat' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

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

    with process_scenario_object.sedimentspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.sedimentspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'sedimentspoed' ])

    with process_scenario_object.bacteriologischonderzoekmetkweeknie_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bacteriologischonderzoekmetkweeknie() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bacteriologischonderzoekmetkweeknie' ])

    with process_scenario_object.haemoglobinefotoelectrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.haemoglobinefotoelectrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'haemoglobinefotoelectrischspoed' ])

    with process_scenario_object.trombocytentellenspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.trombocytentellenspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'trombocytentellenspoed' ])

    with process_scenario_object.leucocytentellenelectronischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leucocytentellenelectronischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leucocytentellenelectronischspoed' ])

    with process_scenario_object.urineonderzoekkwalitatief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.urineonderzoekkwalitatief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'urineonderzoekkwalitatief' ])

    with process_scenario_object.crpcreactiefproteinespoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.crpcreactiefproteinespoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'crpcreactiefproteinespoed' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

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

    with process_scenario_object.hematocrietspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.hematocrietspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'hematocrietspoed' ])

    with process_scenario_object.trombocytentellenspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.trombocytentellenspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'trombocytentellenspoed' ])

    with process_scenario_object.kruisproefvolledigdriemethoden_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kruisproefvolledigdriemethoden() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kruisproefvolledigdriemethoden' ])

    with process_scenario_object.kruisproefvolledigdriemethoden_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kruisproefvolledigdriemethoden() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kruisproefvolledigdriemethoden' ])

    with process_scenario_object.kruisproefvolledigdriemethoden_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kruisproefvolledigdriemethoden() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kruisproefvolledigdriemethoden' ])

    with process_scenario_object.screeningantistoffenerytrocyten_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.screeningantistoffenerytrocyten() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'screeningantistoffenerytrocyten' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.gefiltreerderytrocytenconcentraat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.gefiltreerderytrocytenconcentraat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'gefiltreerderytrocytenconcentraat' ])

    with process_scenario_object.gefiltreerderytrocytenconcentraat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.gefiltreerderytrocytenconcentraat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'gefiltreerderytrocytenconcentraat' ])

    with process_scenario_object.gefiltreerderytrocytenconcentraat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.gefiltreerderytrocytenconcentraat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'gefiltreerderytrocytenconcentraat' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

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

    with process_scenario_object.creatinine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatinine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatinine' ])

    with process_scenario_object.natriumvlamfotometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrisch' ])

    with process_scenario_object.kaliumpotentiometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumpotentiometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumpotentiometrisch' ])

    with process_scenario_object.differentieletellingautomatisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.differentieletellingautomatisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'differentieletellingautomatisch' ])

    with process_scenario_object.leukocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leukocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leukocytentellenelektronisch' ])

    with process_scenario_object.trombocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.trombocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'trombocytentellenelektronisch' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.dagverplegingallespecbehkindrev_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dagverplegingallespecbehkindrev() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dagverplegingallespecbehkindrev' ])

    with process_scenario_object.dagverpleginga_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dagverpleginga() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dagverpleginga' ])

    with process_scenario_object.paclitaxel_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.paclitaxel() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'paclitaxel' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.creatininespoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatininespoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatininespoed' ])

    with process_scenario_object.natriumvlamfotometrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrischspoed' ])

    with process_scenario_object.kaliumvlamfotometrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumvlamfotometrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumvlamfotometrischspoed' ])

    with process_scenario_object.differentieletellingautomatisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.differentieletellingautomatisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'differentieletellingautomatisch' ])

    with process_scenario_object.haemoglobinefotoelectrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.haemoglobinefotoelectrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'haemoglobinefotoelectrischspoed' ])

    with process_scenario_object.trombocytentellenspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.trombocytentellenspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'trombocytentellenspoed' ])

    with process_scenario_object.leucocytentellenelectronischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leucocytentellenelectronischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leucocytentellenelectronischspoed' ])

    with process_scenario_object.cambvmeia_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.cambvmeia() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'cambvmeia' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.vervolgconsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.vervolgconsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'vervolgconsultpoliklinisch' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.creatininespoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatininespoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatininespoed' ])

    with process_scenario_object.natriumvlamfotometrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrischspoed' ])

    with process_scenario_object.kaliumvlamfotometrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumvlamfotometrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumvlamfotometrischspoed' ])

    with process_scenario_object.differentieletellingautomatisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.differentieletellingautomatisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'differentieletellingautomatisch' ])

    with process_scenario_object.haemoglobinefotoelectrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.haemoglobinefotoelectrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'haemoglobinefotoelectrischspoed' ])

    with process_scenario_object.trombocytentellenspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.trombocytentellenspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'trombocytentellenspoed' ])

    with process_scenario_object.leucocytentellenelectronischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leucocytentellenelectronischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leucocytentellenelectronischspoed' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.vervolgconsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.vervolgconsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'vervolgconsultpoliklinisch' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.dagverplegingallespecbehkindrev_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dagverplegingallespecbehkindrev() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dagverplegingallespecbehkindrev' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.creatininespoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatininespoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatininespoed' ])

    with process_scenario_object.natriumvlamfotometrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrischspoed' ])

    with process_scenario_object.kaliumvlamfotometrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumvlamfotometrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumvlamfotometrischspoed' ])

    with process_scenario_object.differentieletellingautomatisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.differentieletellingautomatisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'differentieletellingautomatisch' ])

    with process_scenario_object.haemoglobinefotoelectrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.haemoglobinefotoelectrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'haemoglobinefotoelectrischspoed' ])

    with process_scenario_object.trombocytentellenspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.trombocytentellenspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'trombocytentellenspoed' ])

    with process_scenario_object.leucocytentellenelectronischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leucocytentellenelectronischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leucocytentellenelectronischspoed' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.vervolgconsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.vervolgconsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'vervolgconsultpoliklinisch' ])

    with process_scenario_object.klinischeopnamea_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klinischeopnamea() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klinischeopnamea' ])

    with process_scenario_object.klinischeopnamea_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klinischeopnamea() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klinischeopnamea' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.dagverpleginga_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dagverpleginga() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dagverpleginga' ])

    with process_scenario_object.paclitaxel_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.paclitaxel() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'paclitaxel' ])

    with process_scenario_object.verloskgynaeckortekaartkostenout_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.verloskgynaeckortekaartkostenout() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'verloskgynaeckortekaartkostenout' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.creatininespoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatininespoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatininespoed' ])

    with process_scenario_object.natriumvlamfotometrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrischspoed' ])

    with process_scenario_object.kaliumvlamfotometrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumvlamfotometrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumvlamfotometrischspoed' ])

    with process_scenario_object.sgptalatkinetischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.sgptalatkinetischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'sgptalatkinetischspoed' ])

    with process_scenario_object.sgotasatkinetischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.sgotasatkinetischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'sgotasatkinetischspoed' ])

    with process_scenario_object.kreatininefosfokinasespoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kreatininefosfokinasespoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kreatininefosfokinasespoed' ])

    with process_scenario_object.differentieletellingautomatisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.differentieletellingautomatisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'differentieletellingautomatisch' ])

    with process_scenario_object.haemoglobinefotoelectrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.haemoglobinefotoelectrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'haemoglobinefotoelectrischspoed' ])

    with process_scenario_object.trombocytentellenspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.trombocytentellenspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'trombocytentellenspoed' ])

    with process_scenario_object.leucocytentellenelectronischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leucocytentellenelectronischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leucocytentellenelectronischspoed' ])

    with process_scenario_object.creatinefosfokinasembspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatinefosfokinasembspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatinefosfokinasembspoed' ])

    with process_scenario_object.crpcreactiefproteinespoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.crpcreactiefproteinespoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'crpcreactiefproteinespoed' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.econsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.econsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'econsultpoliklinisch' ])

    with process_scenario_object.klinischeopnamea_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klinischeopnamea() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klinischeopnamea' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

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

    with process_scenario_object.kruisproefvolledigdriemethoden_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kruisproefvolledigdriemethoden() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kruisproefvolledigdriemethoden' ])

    with process_scenario_object.kruisproefvolledigdriemethoden_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kruisproefvolledigdriemethoden() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kruisproefvolledigdriemethoden' ])

    with process_scenario_object.screeningantistoffenerytrocyten_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.screeningantistoffenerytrocyten() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'screeningantistoffenerytrocyten' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.gefiltreerderytrocytenconcentraat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.gefiltreerderytrocytenconcentraat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'gefiltreerderytrocytenconcentraat' ])

    with process_scenario_object.gefiltreerderytrocytenconcentraat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.gefiltreerderytrocytenconcentraat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'gefiltreerderytrocytenconcentraat' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.dagverplegingallespecbehkindrev_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dagverplegingallespecbehkindrev() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dagverplegingallespecbehkindrev' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.creatininespoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatininespoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatininespoed' ])

    with process_scenario_object.natriumvlamfotometrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrischspoed' ])

    with process_scenario_object.kaliumvlamfotometrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumvlamfotometrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumvlamfotometrischspoed' ])

    with process_scenario_object.differentieletellingautomatisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.differentieletellingautomatisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'differentieletellingautomatisch' ])

    with process_scenario_object.haemoglobinefotoelectrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.haemoglobinefotoelectrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'haemoglobinefotoelectrischspoed' ])

    with process_scenario_object.trombocytentellenspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.trombocytentellenspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'trombocytentellenspoed' ])

    with process_scenario_object.leucocytentellenelectronischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leucocytentellenelectronischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leucocytentellenelectronischspoed' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.vervolgconsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.vervolgconsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'vervolgconsultpoliklinisch' ])

    with process_scenario_object.klinischeopnamea_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klinischeopnamea() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klinischeopnamea' ])

    with process_scenario_object.klinischeopnamea_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klinischeopnamea() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klinischeopnamea' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.dagverpleginga_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dagverpleginga() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dagverpleginga' ])

    with process_scenario_object.paclitaxel_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.paclitaxel() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'paclitaxel' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.bilirubinekwantitatieftotaalofdirect_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bilirubinekwantitatieftotaalofdirect() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bilirubinekwantitatieftotaalofdirect' ])

    with process_scenario_object.glucosespoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.glucosespoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'glucosespoed' ])

    with process_scenario_object.ureumspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ureumspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ureumspoed' ])

    with process_scenario_object.creatininespoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatininespoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatininespoed' ])

    with process_scenario_object.alkalischefosfatasekinetischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.alkalischefosfatasekinetischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'alkalischefosfatasekinetischspoed' ])

    with process_scenario_object.calciumspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.calciumspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'calciumspoed' ])

    with process_scenario_object.natriumvlamfotometrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrischspoed' ])

    with process_scenario_object.kaliumvlamfotometrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumvlamfotometrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumvlamfotometrischspoed' ])

    with process_scenario_object.sgptalatkinetischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.sgptalatkinetischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'sgptalatkinetischspoed' ])

    with process_scenario_object.melkzuurdehydrogenasespoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.melkzuurdehydrogenasespoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'melkzuurdehydrogenasespoed' ])

    with process_scenario_object.sgotasatkinetischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.sgotasatkinetischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'sgotasatkinetischspoed' ])

    with process_scenario_object.differentieletellingautomatisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.differentieletellingautomatisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'differentieletellingautomatisch' ])

    with process_scenario_object.haemoglobinefotoelectrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.haemoglobinefotoelectrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'haemoglobinefotoelectrischspoed' ])

    with process_scenario_object.trombocytentellenspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.trombocytentellenspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'trombocytentellenspoed' ])

    with process_scenario_object.leucocytentellenelectronischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leucocytentellenelectronischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leucocytentellenelectronischspoed' ])

    with process_scenario_object.albuminespoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.albuminespoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'albuminespoed' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.vervolgconsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.vervolgconsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'vervolgconsultpoliklinisch' ])

    with process_scenario_object.dagverplegingallespecbehkindrev_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dagverplegingallespecbehkindrev() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dagverplegingallespecbehkindrev' ])

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

    with process_scenario_object.kruisproefvolledigdriemethoden_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kruisproefvolledigdriemethoden() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kruisproefvolledigdriemethoden' ])

    with process_scenario_object.kruisproefvolledigdriemethoden_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kruisproefvolledigdriemethoden() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kruisproefvolledigdriemethoden' ])

    with process_scenario_object.screeningantistoffenerytrocyten_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.screeningantistoffenerytrocyten() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'screeningantistoffenerytrocyten' ])

    with process_scenario_object.cambvmeia_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.cambvmeia() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'cambvmeia' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.dagverpleginga_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dagverpleginga() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dagverpleginga' ])

    with process_scenario_object.gefiltreerderytrocytenconcentraat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.gefiltreerderytrocytenconcentraat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'gefiltreerderytrocytenconcentraat' ])

    with process_scenario_object.gefiltreerderytrocytenconcentraat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.gefiltreerderytrocytenconcentraat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'gefiltreerderytrocytenconcentraat' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.creatininespoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatininespoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatininespoed' ])

    with process_scenario_object.natriumvlamfotometrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrischspoed' ])

    with process_scenario_object.kaliumvlamfotometrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumvlamfotometrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumvlamfotometrischspoed' ])

    with process_scenario_object.differentieletellingautomatisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.differentieletellingautomatisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'differentieletellingautomatisch' ])

    with process_scenario_object.haemoglobinefotoelectrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.haemoglobinefotoelectrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'haemoglobinefotoelectrischspoed' ])

    with process_scenario_object.trombocytentellenspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.trombocytentellenspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'trombocytentellenspoed' ])

    with process_scenario_object.leucocytentellenelectronischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leucocytentellenelectronischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leucocytentellenelectronischspoed' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.vervolgconsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.vervolgconsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'vervolgconsultpoliklinisch' ])

    with process_scenario_object.ctabdomen_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ctabdomen() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ctabdomen' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.creatininespoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatininespoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatininespoed' ])

    with process_scenario_object.natriumvlamfotometrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrischspoed' ])

    with process_scenario_object.kaliumvlamfotometrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumvlamfotometrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumvlamfotometrischspoed' ])

    with process_scenario_object.differentieletellingautomatisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.differentieletellingautomatisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'differentieletellingautomatisch' ])

    with process_scenario_object.haemoglobinefotoelectrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.haemoglobinefotoelectrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'haemoglobinefotoelectrischspoed' ])

    with process_scenario_object.trombocytentellenspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.trombocytentellenspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'trombocytentellenspoed' ])

    with process_scenario_object.leucocytentellenelectronischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leucocytentellenelectronischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leucocytentellenelectronischspoed' ])

    with process_scenario_object.cambvmeia_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.cambvmeia() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'cambvmeia' ])

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

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.bilirubinegeconjugeerd_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bilirubinegeconjugeerd() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bilirubinegeconjugeerd' ])

    with process_scenario_object.hemoglobinefotoelektrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.hemoglobinefotoelektrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'hemoglobinefotoelektrisch' ])

    with process_scenario_object.creatinine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatinine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatinine' ])

    with process_scenario_object.sgotasatkinetisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.sgotasatkinetisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'sgotasatkinetisch' ])

    with process_scenario_object.sgptalatkinetisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.sgptalatkinetisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'sgptalatkinetisch' ])

    with process_scenario_object.melkzuurdehydrogenaseldhkinetisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.melkzuurdehydrogenaseldhkinetisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'melkzuurdehydrogenaseldhkinetisch' ])

    with process_scenario_object.cambvmeia_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.cambvmeia() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'cambvmeia' ])

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

    with process_scenario_object.ctabdomen_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ctabdomen() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ctabdomen' ])

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

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.creatinine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatinine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatinine' ])

    with process_scenario_object.natriumvlamfotometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrisch' ])

    with process_scenario_object.kaliumpotentiometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumpotentiometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumpotentiometrisch' ])

    with process_scenario_object.differentieletellingautomatisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.differentieletellingautomatisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'differentieletellingautomatisch' ])

    with process_scenario_object.haemoglobinefotoelectrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.haemoglobinefotoelectrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'haemoglobinefotoelectrischspoed' ])

    with process_scenario_object.trombocytentellenspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.trombocytentellenspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'trombocytentellenspoed' ])

    with process_scenario_object.leucocytentellenelectronischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leucocytentellenelectronischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leucocytentellenelectronischspoed' ])

    with process_scenario_object.cambvmeia_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.cambvmeia() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'cambvmeia' ])

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

    with process_scenario_object.ctthorax_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ctthorax() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ctthorax' ])

    with process_scenario_object.ctabdomen_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ctabdomen() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ctabdomen' ])

    with process_scenario_object.dagverplegingallespecbehkindrev_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dagverplegingallespecbehkindrev() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dagverplegingallespecbehkindrev' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.cambvmeia_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.cambvmeia() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'cambvmeia' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.dagverpleginga_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dagverpleginga() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dagverpleginga' ])

    with process_scenario_object.paclitaxel_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.paclitaxel() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'paclitaxel' ])

    with process_scenario_object.dagverplegingallespecbehkindrev_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dagverplegingallespecbehkindrev() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dagverplegingallespecbehkindrev' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.creatinine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatinine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatinine' ])

    with process_scenario_object.natriumvlamfotometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrisch' ])

    with process_scenario_object.kaliumpotentiometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumpotentiometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumpotentiometrisch' ])

    with process_scenario_object.differentieletellingautomatisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.differentieletellingautomatisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'differentieletellingautomatisch' ])

    with process_scenario_object.haemoglobinefotoelectrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.haemoglobinefotoelectrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'haemoglobinefotoelectrischspoed' ])

    with process_scenario_object.trombocytentellenspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.trombocytentellenspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'trombocytentellenspoed' ])

    with process_scenario_object.leucocytentellenelectronischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leucocytentellenelectronischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leucocytentellenelectronischspoed' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.vervolgconsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.vervolgconsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'vervolgconsultpoliklinisch' ])

    with process_scenario_object.dagverpleginga_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dagverpleginga() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dagverpleginga' ])

    with process_scenario_object.paclitaxel_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.paclitaxel() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'paclitaxel' ])

    with process_scenario_object.paclitaxel_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.paclitaxel() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'paclitaxel' ])

    with process_scenario_object.dagverplegingallespecbehkindrev_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dagverplegingallespecbehkindrev() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dagverplegingallespecbehkindrev' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.creatinine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatinine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatinine' ])

    with process_scenario_object.natriumvlamfotometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrisch' ])

    with process_scenario_object.kaliumpotentiometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumpotentiometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumpotentiometrisch' ])

    with process_scenario_object.differentieletellingautomatisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.differentieletellingautomatisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'differentieletellingautomatisch' ])

    with process_scenario_object.haemoglobinefotoelectrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.haemoglobinefotoelectrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'haemoglobinefotoelectrischspoed' ])

    with process_scenario_object.trombocytentellenspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.trombocytentellenspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'trombocytentellenspoed' ])

    with process_scenario_object.leucocytentellenelectronischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leucocytentellenelectronischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leucocytentellenelectronischspoed' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.vervolgconsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.vervolgconsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'vervolgconsultpoliklinisch' ])

    with process_scenario_object.dagverpleginga_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dagverpleginga() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dagverpleginga' ])

    with process_scenario_object.econsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.econsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'econsultpoliklinisch' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.creatinine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatinine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatinine' ])

    with process_scenario_object.natriumvlamfotometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrisch' ])

    with process_scenario_object.kaliumpotentiometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumpotentiometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumpotentiometrisch' ])

    with process_scenario_object.differentieletellingautomatisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.differentieletellingautomatisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'differentieletellingautomatisch' ])

    with process_scenario_object.haemoglobinefotoelectrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.haemoglobinefotoelectrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'haemoglobinefotoelectrischspoed' ])

    with process_scenario_object.trombocytentellenspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.trombocytentellenspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'trombocytentellenspoed' ])

    with process_scenario_object.leucocytentellenelectronischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leucocytentellenelectronischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leucocytentellenelectronischspoed' ])

    with process_scenario_object.cambvmeia_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.cambvmeia() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'cambvmeia' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.vervolgconsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.vervolgconsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'vervolgconsultpoliklinisch' ])

    with process_scenario_object.dagverplegingallespecbehkindrev_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dagverplegingallespecbehkindrev() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dagverplegingallespecbehkindrev' ])

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

    with process_scenario_object.kruisproefvolledigdriemethoden_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kruisproefvolledigdriemethoden() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kruisproefvolledigdriemethoden' ])

    with process_scenario_object.kruisproefvolledigdriemethoden_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kruisproefvolledigdriemethoden() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kruisproefvolledigdriemethoden' ])

    with process_scenario_object.kruisproefvolledigdriemethoden_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kruisproefvolledigdriemethoden() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kruisproefvolledigdriemethoden' ])

    with process_scenario_object.screeningantistoffenerytrocyten_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.screeningantistoffenerytrocyten() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'screeningantistoffenerytrocyten' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.dagverpleginga_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dagverpleginga() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dagverpleginga' ])

    with process_scenario_object.gefiltreerderytrocytenconcentraat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.gefiltreerderytrocytenconcentraat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'gefiltreerderytrocytenconcentraat' ])

    with process_scenario_object.gefiltreerderytrocytenconcentraat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.gefiltreerderytrocytenconcentraat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'gefiltreerderytrocytenconcentraat' ])

    with process_scenario_object.gefiltreerderytrocytenconcentraat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.gefiltreerderytrocytenconcentraat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'gefiltreerderytrocytenconcentraat' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.creatinine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatinine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatinine' ])

    with process_scenario_object.natriumvlamfotometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrisch' ])

    with process_scenario_object.kaliumpotentiometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumpotentiometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumpotentiometrisch' ])

    with process_scenario_object.differentieletellingautomatisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.differentieletellingautomatisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'differentieletellingautomatisch' ])

    with process_scenario_object.haemoglobinefotoelectrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.haemoglobinefotoelectrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'haemoglobinefotoelectrischspoed' ])

    with process_scenario_object.trombocytentellenspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.trombocytentellenspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'trombocytentellenspoed' ])

    with process_scenario_object.leucocytentellenelectronischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leucocytentellenelectronischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leucocytentellenelectronischspoed' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.creatinine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatinine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatinine' ])

    with process_scenario_object.natriumvlamfotometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrisch' ])

    with process_scenario_object.kaliumpotentiometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumpotentiometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumpotentiometrisch' ])

    with process_scenario_object.differentieletellingautomatisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.differentieletellingautomatisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'differentieletellingautomatisch' ])

    with process_scenario_object.haemoglobinefotoelectrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.haemoglobinefotoelectrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'haemoglobinefotoelectrischspoed' ])

    with process_scenario_object.trombocytentellenspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.trombocytentellenspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'trombocytentellenspoed' ])

    with process_scenario_object.leucocytentellenelectronischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leucocytentellenelectronischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leucocytentellenelectronischspoed' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.vervolgconsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.vervolgconsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'vervolgconsultpoliklinisch' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.dagverplegingallespecbehkindrev_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dagverplegingallespecbehkindrev() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dagverplegingallespecbehkindrev' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.creatinine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatinine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatinine' ])

    with process_scenario_object.natriumvlamfotometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrisch' ])

    with process_scenario_object.kaliumpotentiometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumpotentiometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumpotentiometrisch' ])

    with process_scenario_object.differentieletellingautomatisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.differentieletellingautomatisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'differentieletellingautomatisch' ])

    with process_scenario_object.haemoglobinefotoelectrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.haemoglobinefotoelectrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'haemoglobinefotoelectrischspoed' ])

    with process_scenario_object.trombocytentellenspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.trombocytentellenspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'trombocytentellenspoed' ])

    with process_scenario_object.leucocytentellenelectronischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leucocytentellenelectronischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leucocytentellenelectronischspoed' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.vervolgconsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.vervolgconsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'vervolgconsultpoliklinisch' ])

    with process_scenario_object.klinischeopnamea_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klinischeopnamea() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klinischeopnamea' ])

    with process_scenario_object.klinischeopnamea_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klinischeopnamea() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klinischeopnamea' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.dagverpleginga_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dagverpleginga() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dagverpleginga' ])

    with process_scenario_object.paclitaxel_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.paclitaxel() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'paclitaxel' ])

    with process_scenario_object.paclitaxel_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.paclitaxel() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'paclitaxel' ])

    with process_scenario_object.dagverplegingallespecbehkindrev_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dagverplegingallespecbehkindrev() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dagverplegingallespecbehkindrev' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.creatinine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatinine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatinine' ])

    with process_scenario_object.natriumvlamfotometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrisch' ])

    with process_scenario_object.kaliumpotentiometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumpotentiometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumpotentiometrisch' ])

    with process_scenario_object.differentieletellingautomatisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.differentieletellingautomatisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'differentieletellingautomatisch' ])

    with process_scenario_object.haemoglobinefotoelectrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.haemoglobinefotoelectrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'haemoglobinefotoelectrischspoed' ])

    with process_scenario_object.trombocytentellenspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.trombocytentellenspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'trombocytentellenspoed' ])

    with process_scenario_object.leucocytentellenelectronischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leucocytentellenelectronischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leucocytentellenelectronischspoed' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.vervolgconsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.vervolgconsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'vervolgconsultpoliklinisch' ])

    with process_scenario_object.dagverpleginga_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dagverpleginga() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dagverpleginga' ])

    with process_scenario_object.paclitaxel_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.paclitaxel() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'paclitaxel' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.dagverplegingallespecbehkindrev_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dagverplegingallespecbehkindrev() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dagverplegingallespecbehkindrev' ])

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

    with process_scenario_object.hemoglobinefotoelektrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.hemoglobinefotoelektrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'hemoglobinefotoelektrisch' ])

    with process_scenario_object.creatinine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatinine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatinine' ])

    with process_scenario_object.natriumvlamfotometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrisch' ])

    with process_scenario_object.kaliumpotentiometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumpotentiometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumpotentiometrisch' ])

    with process_scenario_object.bloedgroepaboenrhesusfactor_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bloedgroepaboenrhesusfactor() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bloedgroepaboenrhesusfactor' ])

    with process_scenario_object.rhesusfactordcentrifugeermethodee_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.rhesusfactordcentrifugeermethodee() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'rhesusfactordcentrifugeermethodee' ])

    with process_scenario_object.differentieletellingautomatisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.differentieletellingautomatisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'differentieletellingautomatisch' ])

    with process_scenario_object.leukocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leukocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leukocytentellenelektronisch' ])

    with process_scenario_object.trombocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.trombocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'trombocytentellenelektronisch' ])

    with process_scenario_object.kruisproefvolledigdriemethoden_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kruisproefvolledigdriemethoden() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kruisproefvolledigdriemethoden' ])

    with process_scenario_object.kruisproefvolledigdriemethoden_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kruisproefvolledigdriemethoden() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kruisproefvolledigdriemethoden' ])

    with process_scenario_object.screeningantistoffenerytrocyten_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.screeningantistoffenerytrocyten() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'screeningantistoffenerytrocyten' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.vervolgconsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.vervolgconsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'vervolgconsultpoliklinisch' ])

    with process_scenario_object.klinischeopnamea_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klinischeopnamea() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klinischeopnamea' ])

    with process_scenario_object.klinischeopnamea_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klinischeopnamea() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klinischeopnamea' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.dagverpleginga_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dagverpleginga() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dagverpleginga' ])

    with process_scenario_object.paclitaxel_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.paclitaxel() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'paclitaxel' ])

    with process_scenario_object.gefiltreerderytrocytenconcentraat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.gefiltreerderytrocytenconcentraat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'gefiltreerderytrocytenconcentraat' ])

    with process_scenario_object.gefiltreerderytrocytenconcentraat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.gefiltreerderytrocytenconcentraat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'gefiltreerderytrocytenconcentraat' ])

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

    with process_scenario_object.creatinine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatinine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatinine' ])

    with process_scenario_object.natriumvlamfotometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrisch' ])

    with process_scenario_object.kaliumpotentiometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumpotentiometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumpotentiometrisch' ])

    with process_scenario_object.differentieletellingautomatisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.differentieletellingautomatisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'differentieletellingautomatisch' ])

    with process_scenario_object.leukocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leukocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leukocytentellenelektronisch' ])

    with process_scenario_object.trombocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.trombocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'trombocytentellenelektronisch' ])

    with process_scenario_object.cambvmeia_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.cambvmeia() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'cambvmeia' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.telefonischconsult_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.telefonischconsult() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'telefonischconsult' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.hemoglobinefotoelektrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.hemoglobinefotoelektrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'hemoglobinefotoelektrisch' ])

    with process_scenario_object.leukocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leukocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leukocytentellenelektronisch' ])

    with process_scenario_object.trombocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.trombocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'trombocytentellenelektronisch' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

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

    with process_scenario_object.creatinine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatinine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatinine' ])

    with process_scenario_object.natriumvlamfotometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrisch' ])

    with process_scenario_object.kaliumpotentiometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumpotentiometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumpotentiometrisch' ])

    with process_scenario_object.differentieletellingautomatisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.differentieletellingautomatisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'differentieletellingautomatisch' ])

    with process_scenario_object.leukocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leukocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leukocytentellenelektronisch' ])

    with process_scenario_object.trombocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.trombocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'trombocytentellenelektronisch' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.vervolgconsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.vervolgconsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'vervolgconsultpoliklinisch' ])

    with process_scenario_object.ctabdomen_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ctabdomen() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ctabdomen' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.dagverplegingallespecbehkindrev_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dagverplegingallespecbehkindrev() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dagverplegingallespecbehkindrev' ])

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

    with process_scenario_object.hemoglobinefotoelektrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.hemoglobinefotoelektrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'hemoglobinefotoelektrisch' ])

    with process_scenario_object.creatinine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatinine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatinine' ])

    with process_scenario_object.natriumvlamfotometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrisch' ])

    with process_scenario_object.kaliumpotentiometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumpotentiometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumpotentiometrisch' ])

    with process_scenario_object.bloedgroepaboenrhesusfactor_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bloedgroepaboenrhesusfactor() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bloedgroepaboenrhesusfactor' ])

    with process_scenario_object.rhesusfactordcentrifugeermethodee_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.rhesusfactordcentrifugeermethodee() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'rhesusfactordcentrifugeermethodee' ])

    with process_scenario_object.differentieletellingautomatisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.differentieletellingautomatisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'differentieletellingautomatisch' ])

    with process_scenario_object.leukocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leukocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leukocytentellenelektronisch' ])

    with process_scenario_object.trombocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.trombocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'trombocytentellenelektronisch' ])

    with process_scenario_object.kruisproefvolledigdriemethoden_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kruisproefvolledigdriemethoden() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kruisproefvolledigdriemethoden' ])

    with process_scenario_object.kruisproefvolledigdriemethoden_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kruisproefvolledigdriemethoden() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kruisproefvolledigdriemethoden' ])

    with process_scenario_object.screeningantistoffenerytrocyten_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.screeningantistoffenerytrocyten() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'screeningantistoffenerytrocyten' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.vervolgconsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.vervolgconsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'vervolgconsultpoliklinisch' ])

    with process_scenario_object.klinischeopnamea_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klinischeopnamea() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klinischeopnamea' ])

    with process_scenario_object.klinischeopnamea_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klinischeopnamea() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klinischeopnamea' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.dagverpleginga_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dagverpleginga() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dagverpleginga' ])

    with process_scenario_object.paclitaxel_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.paclitaxel() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'paclitaxel' ])

    with process_scenario_object.gefiltreerderytrocytenconcentraat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.gefiltreerderytrocytenconcentraat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'gefiltreerderytrocytenconcentraat' ])

    with process_scenario_object.gefiltreerderytrocytenconcentraat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.gefiltreerderytrocytenconcentraat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'gefiltreerderytrocytenconcentraat' ])

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

    with process_scenario_object.creatinine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatinine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatinine' ])

    with process_scenario_object.natriumvlamfotometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrisch' ])

    with process_scenario_object.kaliumpotentiometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumpotentiometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumpotentiometrisch' ])

    with process_scenario_object.differentieletellingautomatisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.differentieletellingautomatisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'differentieletellingautomatisch' ])

    with process_scenario_object.leukocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leukocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leukocytentellenelektronisch' ])

    with process_scenario_object.trombocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.trombocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'trombocytentellenelektronisch' ])

    with process_scenario_object.cambvmeia_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.cambvmeia() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'cambvmeia' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.vervolgconsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.vervolgconsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'vervolgconsultpoliklinisch' ])

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

    with process_scenario_object.creatinine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatinine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatinine' ])

    with process_scenario_object.natriumvlamfotometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrisch' ])

    with process_scenario_object.kaliumpotentiometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumpotentiometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumpotentiometrisch' ])

    with process_scenario_object.differentieletellingautomatisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.differentieletellingautomatisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'differentieletellingautomatisch' ])

    with process_scenario_object.leukocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leukocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leukocytentellenelektronisch' ])

    with process_scenario_object.trombocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.trombocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'trombocytentellenelektronisch' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.vervolgconsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.vervolgconsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'vervolgconsultpoliklinisch' ])

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

    with process_scenario_object.creatinine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatinine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatinine' ])

    with process_scenario_object.natriumvlamfotometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrisch' ])

    with process_scenario_object.kaliumpotentiometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumpotentiometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumpotentiometrisch' ])

    with process_scenario_object.differentieletellingautomatisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.differentieletellingautomatisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'differentieletellingautomatisch' ])

    with process_scenario_object.leukocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leukocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leukocytentellenelektronisch' ])

    with process_scenario_object.trombocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.trombocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'trombocytentellenelektronisch' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.vervolgconsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.vervolgconsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'vervolgconsultpoliklinisch' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.dagverplegingallespecbehkindrev_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dagverplegingallespecbehkindrev() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dagverplegingallespecbehkindrev' ])

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

    with process_scenario_object.hemoglobinefotoelektrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.hemoglobinefotoelektrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'hemoglobinefotoelektrisch' ])

    with process_scenario_object.creatinine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatinine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatinine' ])

    with process_scenario_object.natriumvlamfotometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrisch' ])

    with process_scenario_object.kaliumpotentiometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumpotentiometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumpotentiometrisch' ])

    with process_scenario_object.bloedgroepaboenrhesusfactor_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bloedgroepaboenrhesusfactor() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bloedgroepaboenrhesusfactor' ])

    with process_scenario_object.rhesusfactordcentrifugeermethodee_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.rhesusfactordcentrifugeermethodee() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'rhesusfactordcentrifugeermethodee' ])

    with process_scenario_object.differentieletellingautomatisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.differentieletellingautomatisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'differentieletellingautomatisch' ])

    with process_scenario_object.leukocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leukocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leukocytentellenelektronisch' ])

    with process_scenario_object.trombocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.trombocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'trombocytentellenelektronisch' ])

    with process_scenario_object.kruisproefvolledigdriemethoden_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kruisproefvolledigdriemethoden() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kruisproefvolledigdriemethoden' ])

    with process_scenario_object.kruisproefvolledigdriemethoden_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kruisproefvolledigdriemethoden() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kruisproefvolledigdriemethoden' ])

    with process_scenario_object.screeningantistoffenerytrocyten_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.screeningantistoffenerytrocyten() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'screeningantistoffenerytrocyten' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.vervolgconsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.vervolgconsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'vervolgconsultpoliklinisch' ])

    with process_scenario_object.klinischeopnamea_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klinischeopnamea() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klinischeopnamea' ])

    with process_scenario_object.klinischeopnamea_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klinischeopnamea() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klinischeopnamea' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.dagverpleginga_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dagverpleginga() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dagverpleginga' ])

    with process_scenario_object.paclitaxel_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.paclitaxel() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'paclitaxel' ])

    with process_scenario_object.gefiltreerderytrocytenconcentraat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.gefiltreerderytrocytenconcentraat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'gefiltreerderytrocytenconcentraat' ])

    with process_scenario_object.gefiltreerderytrocytenconcentraat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.gefiltreerderytrocytenconcentraat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'gefiltreerderytrocytenconcentraat' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.dagverplegingallespecbehkindrev_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dagverplegingallespecbehkindrev() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dagverplegingallespecbehkindrev' ])

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

    with process_scenario_object.creatinine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatinine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatinine' ])

    with process_scenario_object.natriumvlamfotometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrisch' ])

    with process_scenario_object.kaliumpotentiometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumpotentiometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumpotentiometrisch' ])

    with process_scenario_object.differentieletellingautomatisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.differentieletellingautomatisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'differentieletellingautomatisch' ])

    with process_scenario_object.leukocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leukocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leukocytentellenelektronisch' ])

    with process_scenario_object.trombocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.trombocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'trombocytentellenelektronisch' ])

    with process_scenario_object.cambvmeia_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.cambvmeia() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'cambvmeia' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.vervolgconsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.vervolgconsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'vervolgconsultpoliklinisch' ])

    with process_scenario_object.klinischeopnamea_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klinischeopnamea() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klinischeopnamea' ])

    with process_scenario_object.klinischeopnamea_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klinischeopnamea() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klinischeopnamea' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.dagverpleginga_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dagverpleginga() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dagverpleginga' ])

    with process_scenario_object.paclitaxel_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.paclitaxel() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'paclitaxel' ])

    with process_scenario_object.dagverplegingallespecbehkindrev_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dagverplegingallespecbehkindrev() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dagverplegingallespecbehkindrev' ])

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

    with process_scenario_object.creatinine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatinine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatinine' ])

    with process_scenario_object.natriumvlamfotometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrisch' ])

    with process_scenario_object.kaliumpotentiometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumpotentiometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumpotentiometrisch' ])

    with process_scenario_object.differentieletellingautomatisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.differentieletellingautomatisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'differentieletellingautomatisch' ])

    with process_scenario_object.leukocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leukocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leukocytentellenelektronisch' ])

    with process_scenario_object.trombocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.trombocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'trombocytentellenelektronisch' ])

    with process_scenario_object.cambvmeia_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.cambvmeia() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'cambvmeia' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.vervolgconsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.vervolgconsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'vervolgconsultpoliklinisch' ])

    with process_scenario_object.dagverpleginga_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dagverpleginga() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dagverpleginga' ])

    with process_scenario_object.paclitaxel_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.paclitaxel() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'paclitaxel' ])

    with process_scenario_object.dagverplegingallespecbehkindrev_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dagverplegingallespecbehkindrev() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dagverplegingallespecbehkindrev' ])

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

    with process_scenario_object.creatinine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatinine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatinine' ])

    with process_scenario_object.natriumvlamfotometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrisch' ])

    with process_scenario_object.kaliumpotentiometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumpotentiometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumpotentiometrisch' ])

    with process_scenario_object.differentieletellingautomatisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.differentieletellingautomatisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'differentieletellingautomatisch' ])

    with process_scenario_object.leukocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leukocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leukocytentellenelektronisch' ])

    with process_scenario_object.trombocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.trombocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'trombocytentellenelektronisch' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.vervolgconsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.vervolgconsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'vervolgconsultpoliklinisch' ])

    with process_scenario_object.dagverpleginga_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dagverpleginga() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dagverpleginga' ])

    with process_scenario_object.paclitaxel_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.paclitaxel() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'paclitaxel' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.dagverplegingallespecbehkindrev_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dagverplegingallespecbehkindrev() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dagverplegingallespecbehkindrev' ])

    with process_scenario_object.infuusinbrengen_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.infuusinbrengen() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'infuusinbrengen' ])

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

    with process_scenario_object.creatinine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatinine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatinine' ])

    with process_scenario_object.natriumvlamfotometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrisch' ])

    with process_scenario_object.kaliumpotentiometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumpotentiometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumpotentiometrisch' ])

    with process_scenario_object.differentieletellingautomatisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.differentieletellingautomatisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'differentieletellingautomatisch' ])

    with process_scenario_object.leukocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leukocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leukocytentellenelektronisch' ])

    with process_scenario_object.trombocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.trombocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'trombocytentellenelektronisch' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.vervolgconsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.vervolgconsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'vervolgconsultpoliklinisch' ])

    with process_scenario_object.klinischeopnamea_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klinischeopnamea() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klinischeopnamea' ])

    with process_scenario_object.klinischeopnamea_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klinischeopnamea() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klinischeopnamea' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.dagverpleginga_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dagverpleginga() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dagverpleginga' ])

    with process_scenario_object.paclitaxel_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.paclitaxel() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'paclitaxel' ])

    with process_scenario_object.ctabdomen_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ctabdomen() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ctabdomen' ])

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

    with process_scenario_object.creatinine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatinine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatinine' ])

    with process_scenario_object.natriumvlamfotometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrisch' ])

    with process_scenario_object.kaliumpotentiometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumpotentiometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumpotentiometrisch' ])

    with process_scenario_object.differentieletellingautomatisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.differentieletellingautomatisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'differentieletellingautomatisch' ])

    with process_scenario_object.leukocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leukocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leukocytentellenelektronisch' ])

    with process_scenario_object.trombocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.trombocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'trombocytentellenelektronisch' ])

    with process_scenario_object.cambvmeia_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.cambvmeia() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'cambvmeia' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.vervolgconsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.vervolgconsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'vervolgconsultpoliklinisch' ])

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

    with process_scenario_object.creatinine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatinine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatinine' ])

    with process_scenario_object.natriumvlamfotometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrisch' ])

    with process_scenario_object.kaliumpotentiometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumpotentiometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumpotentiometrisch' ])

    with process_scenario_object.sgotasatkinetisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.sgotasatkinetisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'sgotasatkinetisch' ])

    with process_scenario_object.sgptalatkinetisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.sgptalatkinetisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'sgptalatkinetisch' ])

    with process_scenario_object.melkzuurdehydrogenaseldhkinetisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.melkzuurdehydrogenaseldhkinetisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'melkzuurdehydrogenaseldhkinetisch' ])

    with process_scenario_object.differentieletellingautomatisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.differentieletellingautomatisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'differentieletellingautomatisch' ])

    with process_scenario_object.leukocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leukocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leukocytentellenelektronisch' ])

    with process_scenario_object.trombocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.trombocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'trombocytentellenelektronisch' ])

    with process_scenario_object.cambvmeia_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.cambvmeia() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'cambvmeia' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.vervolgconsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.vervolgconsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'vervolgconsultpoliklinisch' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

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

    with process_scenario_object.sediment_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.sediment() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'sediment' ])

    with process_scenario_object.glucose_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.glucose() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'glucose' ])

    with process_scenario_object.hemoglobinefotoelektrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.hemoglobinefotoelektrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'hemoglobinefotoelektrisch' ])

    with process_scenario_object.creatinine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatinine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatinine' ])

    with process_scenario_object.natriumvlamfotometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrisch' ])

    with process_scenario_object.kaliumpotentiometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumpotentiometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumpotentiometrisch' ])

    with process_scenario_object.sgotasatkinetisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.sgotasatkinetisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'sgotasatkinetisch' ])

    with process_scenario_object.microscopischonderzoekgekleurdenon_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.microscopischonderzoekgekleurdenon() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'microscopischonderzoekgekleurdenon' ])

    with process_scenario_object.bacteriologischonderzoekmetkweeknie_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bacteriologischonderzoekmetkweeknie() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bacteriologischonderzoekmetkweeknie' ])

    with process_scenario_object.bacteriologischonderzoekmetkweeknie_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bacteriologischonderzoekmetkweeknie() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bacteriologischonderzoekmetkweeknie' ])

    with process_scenario_object.resistentiebepalingenbepalingen_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.resistentiebepalingenbepalingen() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'resistentiebepalingenbepalingen' ])

    with process_scenario_object.leukocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leukocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leukocytentellenelektronisch' ])

    with process_scenario_object.trombocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.trombocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'trombocytentellenelektronisch' ])

    with process_scenario_object.gammaglutamyltranspeptidase_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.gammaglutamyltranspeptidase() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'gammaglutamyltranspeptidase' ])

    with process_scenario_object.hepatitisbsurfaceantigeenconfirmatie_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.hepatitisbsurfaceantigeenconfirmatie() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'hepatitisbsurfaceantigeenconfirmatie' ])

    with process_scenario_object.urineonderzoekkwalitatief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.urineonderzoekkwalitatief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'urineonderzoekkwalitatief' ])

    with process_scenario_object.crpcreactiefproteine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.crpcreactiefproteine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'crpcreactiefproteine' ])

    with process_scenario_object.cambvmeia_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.cambvmeia() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'cambvmeia' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.cthersenen_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.cthersenen() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'cthersenen' ])

    with process_scenario_object.cthersenen_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.cthersenen() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'cthersenen' ])

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

    with process_scenario_object.cytologischonderzoekliquorcerebrosp_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.cytologischonderzoekliquorcerebrosp() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'cytologischonderzoekliquorcerebrosp' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.glucose_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.glucose() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'glucose' ])

    with process_scenario_object.erytrocyten_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.erytrocyten() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'erytrocyten' ])

    with process_scenario_object.totaaleiwit_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.totaaleiwit() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'totaaleiwit' ])

    with process_scenario_object.buffycoat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.buffycoat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'buffycoat' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

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

    with process_scenario_object.cambvmeia_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.cambvmeia() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'cambvmeia' ])

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

    with process_scenario_object.telefonischconsult_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.telefonischconsult() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'telefonischconsult' ])

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

    with process_scenario_object.creatinine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatinine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatinine' ])

    with process_scenario_object.leukocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leukocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leukocytentellenelektronisch' ])

    with process_scenario_object.trombocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.trombocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'trombocytentellenelektronisch' ])

    with process_scenario_object.cambvmeia_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.cambvmeia() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'cambvmeia' ])

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

    with process_scenario_object.ctabdomen_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ctabdomen() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ctabdomen' ])

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

    with process_scenario_object.creatinine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatinine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatinine' ])

    with process_scenario_object.natriumvlamfotometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrisch' ])

    with process_scenario_object.kaliumpotentiometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumpotentiometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumpotentiometrisch' ])

    with process_scenario_object.differentieletellingautomatisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.differentieletellingautomatisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'differentieletellingautomatisch' ])

    with process_scenario_object.hematocrietmbvcentrifuge_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.hematocrietmbvcentrifuge() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'hematocrietmbvcentrifuge' ])

    with process_scenario_object.leukocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leukocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leukocytentellenelektronisch' ])

    with process_scenario_object.trombocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.trombocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'trombocytentellenelektronisch' ])

    with process_scenario_object.cambvmeia_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.cambvmeia() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'cambvmeia' ])

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

    with process_scenario_object.creatinine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatinine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatinine' ])

    with process_scenario_object.natriumvlamfotometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrisch' ])

    with process_scenario_object.kaliumpotentiometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumpotentiometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumpotentiometrisch' ])

    with process_scenario_object.differentieletellingautomatisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.differentieletellingautomatisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'differentieletellingautomatisch' ])

    with process_scenario_object.hematocrietmbvcentrifuge_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.hematocrietmbvcentrifuge() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'hematocrietmbvcentrifuge' ])

    with process_scenario_object.leukocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leukocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leukocytentellenelektronisch' ])

    with process_scenario_object.trombocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.trombocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'trombocytentellenelektronisch' ])

    with process_scenario_object.cambvmeia_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.cambvmeia() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'cambvmeia' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.vervolgconsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.vervolgconsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'vervolgconsultpoliklinisch' ])

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

    with process_scenario_object.creatinine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatinine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatinine' ])

    with process_scenario_object.natriumvlamfotometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrisch' ])

    with process_scenario_object.kaliumpotentiometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumpotentiometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumpotentiometrisch' ])

    with process_scenario_object.differentieletellingautomatisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.differentieletellingautomatisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'differentieletellingautomatisch' ])

    with process_scenario_object.hematocrietmbvcentrifuge_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.hematocrietmbvcentrifuge() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'hematocrietmbvcentrifuge' ])

    with process_scenario_object.leukocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leukocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leukocytentellenelektronisch' ])

    with process_scenario_object.trombocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.trombocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'trombocytentellenelektronisch' ])

    with process_scenario_object.cambvmeia_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.cambvmeia() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'cambvmeia' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.ctthorax_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ctthorax() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ctthorax' ])

    with process_scenario_object.ctabdomen_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ctabdomen() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ctabdomen' ])

    with process_scenario_object.vervolgconsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.vervolgconsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'vervolgconsultpoliklinisch' ])
