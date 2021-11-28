def action_plan(entity, process_scenario_object):


    with process_scenario_object.verloskgynaeckortekaartkostenout_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.verloskgynaeckortekaartkostenout() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'verloskgynaeckortekaartkostenout' ])

    with process_scenario_object.echografiegenitaliainterna_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.echografiegenitaliainterna() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'echografiegenitaliainterna' ])

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

    with process_scenario_object.mriabdomen_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.mriabdomen() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'mriabdomen' ])

    with process_scenario_object.mribekken_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.mribekken() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'mribekken' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.blaasuretrocystoscopienno_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.blaasuretrocystoscopienno() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'blaasuretrocystoscopienno' ])

    with process_scenario_object.vaginatoucheronderanesthesie_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.vaginatoucheronderanesthesie() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'vaginatoucheronderanesthesie' ])

    with process_scenario_object.immunopathologischonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.immunopathologischonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'immunopathologischonderzoek' ])

    with process_scenario_object.histologischonderzoekbioptennno_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.histologischonderzoekbioptennno() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'histologischonderzoekbioptennno' ])

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

    with process_scenario_object.bloedgroepaboenrhesusfactor_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bloedgroepaboenrhesusfactor() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bloedgroepaboenrhesusfactor' ])

    with process_scenario_object.rhesusfactordcentrifugeermethodee_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.rhesusfactordcentrifugeermethodee() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'rhesusfactordcentrifugeermethodee' ])

    with process_scenario_object.cdefenotypering_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.cdefenotypering() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'cdefenotypering' ])

    with process_scenario_object.bloedgroepantigenenanderedanaborhesu_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bloedgroepantigenenanderedanaborhesu() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bloedgroepantigenenanderedanaborhesu' ])

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

    with process_scenario_object.econsultbezoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.econsultbezoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'econsultbezoek' ])

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

    with process_scenario_object.buikproeflaparotomie_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.buikproeflaparotomie() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'buikproeflaparotomie' ])

    with process_scenario_object.vrwgeslorgadnexextirpatiedmvlapar_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.vrwgeslorgadnexextirpatiedmvlapar() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'vrwgeslorgadnexextirpatiedmvlapar' ])

    with process_scenario_object.abortusoverigetechnieken_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.abortusoverigetechnieken() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'abortusoverigetechnieken' ])

    with process_scenario_object.cytologischonderzoekascites_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.cytologischonderzoekascites() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'cytologischonderzoekascites' ])

    with process_scenario_object.histologischonderzoekkleineresectie_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.histologischonderzoekkleineresectie() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'histologischonderzoekkleineresectie' ])

    with process_scenario_object.citohistologischonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.citohistologischonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'citohistologischonderzoek' ])

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

    with process_scenario_object.echografietransuretraalprostaat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.echografietransuretraalprostaat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'echografietransuretraalprostaat' ])

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

    with process_scenario_object.fosfaat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.fosfaat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'fosfaat' ])

    with process_scenario_object.natriumvlamfotometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrisch' ])

    with process_scenario_object.kaliumpotentiometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumpotentiometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumpotentiometrisch' ])

    with process_scenario_object.melkzuurdehydrogenaseldhkinetisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.melkzuurdehydrogenaseldhkinetisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'melkzuurdehydrogenaseldhkinetisch' ])

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

    with process_scenario_object.screeningantistoffenerytrocyten_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.screeningantistoffenerytrocyten() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'screeningantistoffenerytrocyten' ])

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

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.kruisproefvolledigdriemethoden_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kruisproefvolledigdriemethoden() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kruisproefvolledigdriemethoden' ])

    with process_scenario_object.kruisproefvolledigdriemethoden_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kruisproefvolledigdriemethoden() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kruisproefvolledigdriemethoden' ])

    with process_scenario_object.behandeltijdeenheidtmegavolt_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.behandeltijdeenheidtmegavolt() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'behandeltijdeenheidtmegavolt' ])

    with process_scenario_object.teletherapiemegavoltfotonenbestrali_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.teletherapiemegavoltfotonenbestrali() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'teletherapiemegavoltfotonenbestrali' ])

    with process_scenario_object.klinischeopnamea_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klinischeopnamea() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klinischeopnamea' ])

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

    with process_scenario_object.immunopathologischonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.immunopathologischonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'immunopathologischonderzoek' ])

    with process_scenario_object.histologischonderzoekkleineresectie_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.histologischonderzoekkleineresectie() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'histologischonderzoekkleineresectie' ])

    with process_scenario_object.citohistologischonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.citohistologischonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'citohistologischonderzoek' ])

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

    with process_scenario_object.klinischeopnamea_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klinischeopnamea() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klinischeopnamea' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.anesthesiebijbehandelingmetradium_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.anesthesiebijbehandelingmetradium() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'anesthesiebijbehandelingmetradium' ])

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

    with process_scenario_object.methemoglobinesulfhemoglobineelk_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.methemoglobinesulfhemoglobineelk() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'methemoglobinesulfhemoglobineelk' ])

    with process_scenario_object.bicarbonaat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bicarbonaat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bicarbonaat' ])

    with process_scenario_object.calciumspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.calciumspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'calciumspoed' ])

    with process_scenario_object.cohbkwn_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.cohbkwn() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'cohbkwn' ])

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

    with process_scenario_object.actuelephpcostandbicarbonaat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.actuelephpcostandbicarbonaat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'actuelephpcostandbicarbonaat' ])

    with process_scenario_object.melkzuurenzymatischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.melkzuurenzymatischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'melkzuurenzymatischspoed' ])

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

    with process_scenario_object.brachytherapieinterstitieelintensi_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.brachytherapieinterstitieelintensi() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'brachytherapieinterstitieelintensi' ])

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

    with process_scenario_object.haemoglobinefotoelectrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.haemoglobinefotoelectrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'haemoglobinefotoelectrischspoed' ])

    with process_scenario_object.magnesiumaas_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.magnesiumaas() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'magnesiumaas' ])

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

    with process_scenario_object.creatinine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatinine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatinine' ])

    with process_scenario_object.chloride_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.chloride() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'chloride' ])

    with process_scenario_object.bicarbonaat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bicarbonaat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bicarbonaat' ])

    with process_scenario_object.natriumvlamfotometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrisch' ])

    with process_scenario_object.kaliumpotentiometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumpotentiometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumpotentiometrisch' ])

    with process_scenario_object.magnesiumaas_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.magnesiumaas() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'magnesiumaas' ])

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

    with process_scenario_object.magnesiumaas_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.magnesiumaas() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'magnesiumaas' ])

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

    with process_scenario_object.econsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.econsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'econsultpoliklinisch' ])

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

    with process_scenario_object.behandeltijdeenheidtmegavolt_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.behandeltijdeenheidtmegavolt() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'behandeltijdeenheidtmegavolt' ])

    with process_scenario_object.teletherapiemegavoltfotonenbestrali_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.teletherapiemegavoltfotonenbestrali() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'teletherapiemegavoltfotonenbestrali' ])

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

    with process_scenario_object.mriabdomen_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.mriabdomen() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'mriabdomen' ])

    with process_scenario_object.vervolgconsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.vervolgconsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'vervolgconsultpoliklinisch' ])

    with process_scenario_object.histologischonderzoekbioptennno_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.histologischonderzoekbioptennno() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'histologischonderzoekbioptennno' ])

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

    with process_scenario_object.magnesiumaas_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.magnesiumaas() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'magnesiumaas' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.vervolgconsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.vervolgconsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'vervolgconsultpoliklinisch' ])

    with process_scenario_object.vervolgconsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.vervolgconsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'vervolgconsultpoliklinisch' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.klinischeopnamea_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klinischeopnamea() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klinischeopnamea' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.dieetnno_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dieetnno() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dieetnno' ])

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

    with process_scenario_object.haemoglobinefotoelectrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.haemoglobinefotoelectrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'haemoglobinefotoelectrischspoed' ])

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

    with process_scenario_object.gammaglutamyltranspeptidase_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.gammaglutamyltranspeptidase() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'gammaglutamyltranspeptidase' ])

    with process_scenario_object.calcium_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.calcium() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'calcium' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

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

    with process_scenario_object.creatinine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatinine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatinine' ])

    with process_scenario_object.fosfaat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.fosfaat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'fosfaat' ])

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

    with process_scenario_object.squamouscellcarcinomambveia_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.squamouscellcarcinomambveia() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'squamouscellcarcinomambveia' ])

    with process_scenario_object.albumine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.albumine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'albumine' ])

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

    with process_scenario_object.ctthorax_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ctthorax() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ctthorax' ])

    with process_scenario_object.ctabdomen_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ctabdomen() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ctabdomen' ])

    with process_scenario_object.telefonischconsult_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.telefonischconsult() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'telefonischconsult' ])

    with process_scenario_object.econsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.econsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'econsultpoliklinisch' ])

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

    with process_scenario_object.gammaglutamyltranspeptidase_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.gammaglutamyltranspeptidase() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'gammaglutamyltranspeptidase' ])

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

    with process_scenario_object.dagverplegingallespecbehkindrev_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dagverplegingallespecbehkindrev() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dagverplegingallespecbehkindrev' ])

    with process_scenario_object.infuusinbrengen_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.infuusinbrengen() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'infuusinbrengen' ])

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

    with process_scenario_object.vervolgconsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.vervolgconsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'vervolgconsultpoliklinisch' ])

    with process_scenario_object.ctthorax_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ctthorax() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ctthorax' ])

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

    with process_scenario_object.echografiegenitaliainterna_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.echografiegenitaliainterna() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'echografiegenitaliainterna' ])

    with process_scenario_object.vervolgconsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.vervolgconsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'vervolgconsultpoliklinisch' ])

    with process_scenario_object.vervolgconsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.vervolgconsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'vervolgconsultpoliklinisch' ])

    with process_scenario_object.behandeltijdeenheidtmegavolt_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.behandeltijdeenheidtmegavolt() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'behandeltijdeenheidtmegavolt' ])

    with process_scenario_object.teletherapiemegavoltfotonenbestrali_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.teletherapiemegavoltfotonenbestrali() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'teletherapiemegavoltfotonenbestrali' ])

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

    with process_scenario_object.cefalinetijdcoagulatie_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.cefalinetijdcoagulatie() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'cefalinetijdcoagulatie' ])

    with process_scenario_object.internationalnormalisedratiombvtromb_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.internationalnormalisedratiombvtromb() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'internationalnormalisedratiombvtromb' ])

    with process_scenario_object.gammaglutamyltranspeptidase_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.gammaglutamyltranspeptidase() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'gammaglutamyltranspeptidase' ])

    with process_scenario_object.calcium_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.calcium() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'calcium' ])

    with process_scenario_object.cambvmeia_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.cambvmeia() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'cambvmeia' ])

    with process_scenario_object.protrombinetijd_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.protrombinetijd() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'protrombinetijd' ])

    with process_scenario_object.bezinkingssnelheidfotoelektrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bezinkingssnelheidfotoelektrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bezinkingssnelheidfotoelektrisch' ])

    with process_scenario_object.erytrocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.erytrocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'erytrocytentellenelektronisch' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.behandeltijdeenheidtmegavolt_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.behandeltijdeenheidtmegavolt() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'behandeltijdeenheidtmegavolt' ])

    with process_scenario_object.teletherapiemegavoltfotonenbestrali_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.teletherapiemegavoltfotonenbestrali() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'teletherapiemegavoltfotonenbestrali' ])

    with process_scenario_object.econsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.econsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'econsultpoliklinisch' ])

    with process_scenario_object.cthersenen_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.cthersenen() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'cthersenen' ])

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

    with process_scenario_object.telefonischconsult_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.telefonischconsult() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'telefonischconsult' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ecgelektrocardiografie_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ecgelektrocardiografie() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ecgelektrocardiografie' ])

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

    with process_scenario_object.bilirubinegeconjugeerd_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bilirubinegeconjugeerd() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bilirubinegeconjugeerd' ])

    with process_scenario_object.glucose_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.glucose() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'glucose' ])

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

    with process_scenario_object.hemoglobinefotoelektrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.hemoglobinefotoelektrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'hemoglobinefotoelektrisch' ])

    with process_scenario_object.amylase_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.amylase() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'amylase' ])

    with process_scenario_object.creatinine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatinine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatinine' ])

    with process_scenario_object.alkalischefosfatasekinetisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.alkalischefosfatasekinetisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'alkalischefosfatasekinetisch' ])

    with process_scenario_object.bicarbonaat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bicarbonaat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bicarbonaat' ])

    with process_scenario_object.natriumvlamfotometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrisch' ])

    with process_scenario_object.natriumvlamfotometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrisch' ])

    with process_scenario_object.kaliumpotentiometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumpotentiometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumpotentiometrisch' ])

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

    with process_scenario_object.creatinefosfokinasekinetisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatinefosfokinasekinetisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatinefosfokinasekinetisch' ])

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

    with process_scenario_object.cefalinetijdcoagulatie_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.cefalinetijdcoagulatie() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'cefalinetijdcoagulatie' ])

    with process_scenario_object.actuelephpcostandbicarbonaat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.actuelephpcostandbicarbonaat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'actuelephpcostandbicarbonaat' ])

    with process_scenario_object.brainnatriureticpeptidebnpmbvimmu_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.brainnatriureticpeptidebnpmbvimmu() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'brainnatriureticpeptidebnpmbvimmu' ])

    with process_scenario_object.fdpdimeerimmunologisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.fdpdimeerimmunologisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'fdpdimeerimmunologisch' ])

    with process_scenario_object.melkzuurenzymatisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.melkzuurenzymatisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'melkzuurenzymatisch' ])

    with process_scenario_object.creatinefosfokinaseisoenzymckmb_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatinefosfokinaseisoenzymckmb() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatinefosfokinaseisoenzymckmb' ])

    with process_scenario_object.crpcreactiefproteine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.crpcreactiefproteine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'crpcreactiefproteine' ])

    with process_scenario_object.albumine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.albumine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'albumine' ])

    with process_scenario_object.osaturatie_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.osaturatie() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'osaturatie' ])

    with process_scenario_object.troponinetmbvelisa_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.troponinetmbvelisa() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'troponinetmbvelisa' ])

    with process_scenario_object.screeningantistoffenerytrocyten_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.screeningantistoffenerytrocyten() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'screeningantistoffenerytrocyten' ])

    with process_scenario_object.protrombinetijd_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.protrombinetijd() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'protrombinetijd' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.thoraxopzaal_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.thoraxopzaal() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'thoraxopzaal' ])

    with process_scenario_object.telefonischconsult_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.telefonischconsult() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'telefonischconsult' ])

    with process_scenario_object.klinischeopnamea_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klinischeopnamea() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klinischeopnamea' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])
