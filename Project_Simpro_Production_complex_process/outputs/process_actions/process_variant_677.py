def action_plan(entity, process_scenario_object):


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

    with process_scenario_object.coupeterinzage_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.coupeterinzage() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'coupeterinzage' ])

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

    with process_scenario_object.screeningantistoffenerytrocyten_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.screeningantistoffenerytrocyten() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'screeningantistoffenerytrocyten' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.echobovenbuik_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.echobovenbuik() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'echobovenbuik' ])

    with process_scenario_object.klinischeopnamea_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klinischeopnamea() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klinischeopnamea' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

    with process_scenario_object.klinischekaartanesthesie_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klinischekaartanesthesie() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klinischekaartanesthesie' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

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

    with process_scenario_object.glucose_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.glucose() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'glucose' ])

    with process_scenario_object.glucose_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.glucose() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'glucose' ])

    with process_scenario_object.glucose_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.glucose() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'glucose' ])

    with process_scenario_object.glucose_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.glucose() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'glucose' ])

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

    with process_scenario_object.hemoglobinefotoelektrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.hemoglobinefotoelektrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'hemoglobinefotoelektrisch' ])

    with process_scenario_object.hemoglobinefotoelektrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.hemoglobinefotoelektrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'hemoglobinefotoelektrisch' ])

    with process_scenario_object.hemoglobinefotoelektrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.hemoglobinefotoelektrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'hemoglobinefotoelektrisch' ])

    with process_scenario_object.hemoglobinefotoelektrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.hemoglobinefotoelektrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'hemoglobinefotoelektrisch' ])

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

    with process_scenario_object.natriumvlamfotometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrisch' ])

    with process_scenario_object.natriumvlamfotometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrisch' ])

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

    with process_scenario_object.kaliumpotentiometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumpotentiometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumpotentiometrisch' ])

    with process_scenario_object.kaliumpotentiometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumpotentiometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumpotentiometrisch' ])

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

    with process_scenario_object.melkzuurenzymatisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.melkzuurenzymatisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'melkzuurenzymatisch' ])

    with process_scenario_object.melkzuurenzymatisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.melkzuurenzymatisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'melkzuurenzymatisch' ])

    with process_scenario_object.melkzuurenzymatisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.melkzuurenzymatisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'melkzuurenzymatisch' ])

    with process_scenario_object.melkzuurenzymatisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.melkzuurenzymatisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'melkzuurenzymatisch' ])

    with process_scenario_object.calcium_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.calcium() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'calcium' ])

    with process_scenario_object.calcium_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.calcium() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'calcium' ])

    with process_scenario_object.calcium_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.calcium() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'calcium' ])

    with process_scenario_object.calcium_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.calcium() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'calcium' ])

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

    with process_scenario_object.thoraxopzaal_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.thoraxopzaal() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'thoraxopzaal' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

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

    with process_scenario_object.bilirubinetotaal_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bilirubinetotaal() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bilirubinetotaal' ])

    with process_scenario_object.glucose_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.glucose() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'glucose' ])

    with process_scenario_object.glucose_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.glucose() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'glucose' ])

    with process_scenario_object.glucose_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.glucose() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'glucose' ])

    with process_scenario_object.glucose_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.glucose() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'glucose' ])

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

    with process_scenario_object.ureum_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ureum() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ureum' ])

    with process_scenario_object.ureum_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ureum() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ureum' ])

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

    with process_scenario_object.hemoglobinefotoelektrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.hemoglobinefotoelektrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'hemoglobinefotoelektrisch' ])

    with process_scenario_object.hemoglobinefotoelektrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.hemoglobinefotoelektrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'hemoglobinefotoelektrisch' ])

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

    with process_scenario_object.creatinine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatinine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatinine' ])

    with process_scenario_object.creatinine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatinine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatinine' ])

    with process_scenario_object.creatinine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatinine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatinine' ])

    with process_scenario_object.chloride_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.chloride() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'chloride' ])

    with process_scenario_object.chloride_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.chloride() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'chloride' ])

    with process_scenario_object.fosfaat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.fosfaat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'fosfaat' ])

    with process_scenario_object.fosfaat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.fosfaat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'fosfaat' ])

    with process_scenario_object.alkalischefosfatasekinetisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.alkalischefosfatasekinetisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'alkalischefosfatasekinetisch' ])

    with process_scenario_object.natriumvlamfotometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrisch' ])

    with process_scenario_object.natriumvlamfotometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrisch' ])

    with process_scenario_object.natriumvlamfotometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrisch' ])

    with process_scenario_object.natriumvlamfotometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrisch' ])

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

    with process_scenario_object.kaliumpotentiometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumpotentiometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumpotentiometrisch' ])

    with process_scenario_object.kaliumpotentiometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumpotentiometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumpotentiometrisch' ])

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

    with process_scenario_object.leukocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leukocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leukocytentellenelektronisch' ])

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

    with process_scenario_object.melkzuurenzymatisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.melkzuurenzymatisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'melkzuurenzymatisch' ])

    with process_scenario_object.melkzuurenzymatisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.melkzuurenzymatisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'melkzuurenzymatisch' ])

    with process_scenario_object.melkzuurenzymatisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.melkzuurenzymatisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'melkzuurenzymatisch' ])

    with process_scenario_object.melkzuurenzymatisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.melkzuurenzymatisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'melkzuurenzymatisch' ])

    with process_scenario_object.melkzuurenzymatisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.melkzuurenzymatisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'melkzuurenzymatisch' ])

    with process_scenario_object.calcium_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.calcium() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'calcium' ])

    with process_scenario_object.calcium_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.calcium() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'calcium' ])

    with process_scenario_object.calcium_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.calcium() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'calcium' ])

    with process_scenario_object.calcium_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.calcium() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'calcium' ])

    with process_scenario_object.calcium_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.calcium() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'calcium' ])

    with process_scenario_object.calcium_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.calcium() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'calcium' ])

    with process_scenario_object.calcium_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.calcium() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'calcium' ])

    with process_scenario_object.crpcreactiefproteine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.crpcreactiefproteine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'crpcreactiefproteine' ])

    with process_scenario_object.crpcreactiefproteine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.crpcreactiefproteine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'crpcreactiefproteine' ])

    with process_scenario_object.albumine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.albumine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'albumine' ])

    with process_scenario_object.albumine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.albumine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'albumine' ])

    with process_scenario_object.albumine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.albumine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'albumine' ])

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

    with process_scenario_object.protrombinetijd_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.protrombinetijd() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'protrombinetijd' ])

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

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.echonierenurinewegen_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.echonierenurinewegen() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'echonierenurinewegen' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

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

    with process_scenario_object.natriumvlamfotometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrisch' ])

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

    with process_scenario_object.urinezuurmeturicaseuvspectrofotome_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.urinezuurmeturicaseuvspectrofotome() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'urinezuurmeturicaseuvspectrofotome' ])

    with process_scenario_object.creatinine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatinine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatinine' ])

    with process_scenario_object.fosfaat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.fosfaat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'fosfaat' ])

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

    with process_scenario_object.triglyceridenenzymatisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.triglyceridenenzymatisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'triglyceridenenzymatisch' ])

    with process_scenario_object.sgotasatkinetisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.sgotasatkinetisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'sgotasatkinetisch' ])

    with process_scenario_object.sgptalatkinetisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.sgptalatkinetisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'sgptalatkinetisch' ])

    with process_scenario_object.leukocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leukocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leukocytentellenelektronisch' ])

    with process_scenario_object.gammaglutamyltranspeptidase_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.gammaglutamyltranspeptidase() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'gammaglutamyltranspeptidase' ])

    with process_scenario_object.calcium_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.calcium() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'calcium' ])

    with process_scenario_object.urineonderzoekkwalitatief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.urineonderzoekkwalitatief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'urineonderzoekkwalitatief' ])

    with process_scenario_object.crpcreactiefproteine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.crpcreactiefproteine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'crpcreactiefproteine' ])

    with process_scenario_object.albumine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.albumine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'albumine' ])

    with process_scenario_object.magnesiumaas_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.magnesiumaas() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'magnesiumaas' ])

    with process_scenario_object.differentiatieleukocytenhandmatig_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.differentiatieleukocytenhandmatig() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'differentiatieleukocytenhandmatig' ])

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

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

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

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

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

    with process_scenario_object.urinezuurmeturicaseuvspectrofotome_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.urinezuurmeturicaseuvspectrofotome() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'urinezuurmeturicaseuvspectrofotome' ])

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

    with process_scenario_object.triglyceridenenzymatisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.triglyceridenenzymatisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'triglyceridenenzymatisch' ])

    with process_scenario_object.totaaleiwit_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.totaaleiwit() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'totaaleiwit' ])

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

    with process_scenario_object.gammaglutamyltranspeptidase_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.gammaglutamyltranspeptidase() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'gammaglutamyltranspeptidase' ])

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

    with process_scenario_object.screeningantistoffenerytrocyten_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.screeningantistoffenerytrocyten() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'screeningantistoffenerytrocyten' ])

    with process_scenario_object.magnesiumaas_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.magnesiumaas() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'magnesiumaas' ])

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

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

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

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

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

    with process_scenario_object.natriumvlamfotometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrisch' ])

    with process_scenario_object.kaliumpotentiometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumpotentiometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumpotentiometrisch' ])

    with process_scenario_object.leukocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leukocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leukocytentellenelektronisch' ])

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

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

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

    with process_scenario_object.amylase_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.amylase() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'amylase' ])

    with process_scenario_object.urinezuurmeturicaseuvspectrofotome_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.urinezuurmeturicaseuvspectrofotome() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'urinezuurmeturicaseuvspectrofotome' ])

    with process_scenario_object.creatinine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatinine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatinine' ])

    with process_scenario_object.fosfaat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.fosfaat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'fosfaat' ])

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

    with process_scenario_object.totaaleiwit_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.totaaleiwit() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'totaaleiwit' ])

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

    with process_scenario_object.thorax_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.thorax() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'thorax' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.intercconsultklinischlongziekten_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.intercconsultklinischlongziekten() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'intercconsultklinischlongziekten' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

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

    with process_scenario_object.creatinine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatinine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatinine' ])

    with process_scenario_object.fosfaat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.fosfaat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'fosfaat' ])

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

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

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

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.ureum_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ureum() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ureum' ])

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

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

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

    with process_scenario_object.natriumvlamfotometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrisch' ])

    with process_scenario_object.kaliumpotentiometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumpotentiometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumpotentiometrisch' ])

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

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

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

    with process_scenario_object.natriumvlamfotometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrisch' ])

    with process_scenario_object.kaliumpotentiometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumpotentiometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumpotentiometrisch' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

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

    with process_scenario_object.klinischeopnamea_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klinischeopnamea() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klinischeopnamea' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

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

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

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

    with process_scenario_object.microscopischonderzoekgekleurdenon_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.microscopischonderzoekgekleurdenon() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'microscopischonderzoekgekleurdenon' ])

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

    with process_scenario_object.bacteriologischonderzoekmetkweeknie_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bacteriologischonderzoekmetkweeknie() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bacteriologischonderzoekmetkweeknie' ])

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

    with process_scenario_object.resistentiebepalingenbepalingen_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.resistentiebepalingenbepalingen() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'resistentiebepalingenbepalingen' ])

    with process_scenario_object.leukocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leukocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leukocytentellenelektronisch' ])

    with process_scenario_object.hepatitisbsurfaceantigeenconfirmatie_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.hepatitisbsurfaceantigeenconfirmatie() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'hepatitisbsurfaceantigeenconfirmatie' ])

    with process_scenario_object.hepatitisbsurfaceantigeenconfirmatie_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.hepatitisbsurfaceantigeenconfirmatie() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'hepatitisbsurfaceantigeenconfirmatie' ])

    with process_scenario_object.hepatitisbsurfaceantigeenconfirmatie_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.hepatitisbsurfaceantigeenconfirmatie() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'hepatitisbsurfaceantigeenconfirmatie' ])

    with process_scenario_object.hepatitisbsurfaceantigeenconfirmatie_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.hepatitisbsurfaceantigeenconfirmatie() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'hepatitisbsurfaceantigeenconfirmatie' ])

    with process_scenario_object.hepatitisbsurfaceantigeenconfirmatie_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.hepatitisbsurfaceantigeenconfirmatie() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'hepatitisbsurfaceantigeenconfirmatie' ])

    with process_scenario_object.crpcreactiefproteine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.crpcreactiefproteine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'crpcreactiefproteine' ])

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

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

    with process_scenario_object.dieetnno_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dieetnno() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dieetnno' ])

    with process_scenario_object.dieetnno_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dieetnno() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dieetnno' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.buikproeflaparotomie_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.buikproeflaparotomie() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'buikproeflaparotomie' ])

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

    with process_scenario_object.bacteriologischonderzoekmetkweeknie_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bacteriologischonderzoekmetkweeknie() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bacteriologischonderzoekmetkweeknie' ])

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

    with process_scenario_object.ctabdomen_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ctabdomen() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ctabdomen' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

    with process_scenario_object.klinischekaartanesthesie_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klinischekaartanesthesie() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klinischekaartanesthesie' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

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

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

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

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

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

    with process_scenario_object.creatinine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatinine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatinine' ])

    with process_scenario_object.natriumvlamfotometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrisch' ])

    with process_scenario_object.glucose_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.glucose() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'glucose' ])

    with process_scenario_object.hemoglobinefotoelektrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.hemoglobinefotoelektrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'hemoglobinefotoelektrisch' ])

    with process_scenario_object.natriumvlamfotometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrisch' ])

    with process_scenario_object.kaliumpotentiometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumpotentiometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumpotentiometrisch' ])

    with process_scenario_object.microscopischonderzoekgekleurdenon_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.microscopischonderzoekgekleurdenon() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'microscopischonderzoekgekleurdenon' ])

    with process_scenario_object.bacteriologischonderzoekmetkweeknie_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bacteriologischonderzoekmetkweeknie() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bacteriologischonderzoekmetkweeknie' ])

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

    with process_scenario_object.melkzuurenzymatisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.melkzuurenzymatisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'melkzuurenzymatisch' ])

    with process_scenario_object.calcium_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.calcium() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'calcium' ])

    with process_scenario_object.urineonderzoekkwalitatief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.urineonderzoekkwalitatief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'urineonderzoekkwalitatief' ])

    with process_scenario_object.osaturatie_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.osaturatie() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'osaturatie' ])

    with process_scenario_object.protrombinetijd_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.protrombinetijd() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'protrombinetijd' ])

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

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

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

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

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

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

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

    with process_scenario_object.natriumvlamfotometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrisch' ])

    with process_scenario_object.kaliumpotentiometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumpotentiometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumpotentiometrisch' ])

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

    with process_scenario_object.echonierenurinewegen_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.echonierenurinewegen() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'echonierenurinewegen' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

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

    with process_scenario_object.natriumvlamfotometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrisch' ])

    with process_scenario_object.kaliumpotentiometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumpotentiometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumpotentiometrisch' ])

    with process_scenario_object.leukocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leukocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leukocytentellenelektronisch' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.ureum_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ureum() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ureum' ])

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

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

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

    with process_scenario_object.ureum_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ureum() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ureum' ])

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

    with process_scenario_object.creatinine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatinine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatinine' ])

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

    with process_scenario_object.kaliumpotentiometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumpotentiometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumpotentiometrisch' ])

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

    with process_scenario_object.hepatitisbsurfaceantigeenconfirmatie_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.hepatitisbsurfaceantigeenconfirmatie() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'hepatitisbsurfaceantigeenconfirmatie' ])

    with process_scenario_object.hepatitisbsurfaceantigeenconfirmatie_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.hepatitisbsurfaceantigeenconfirmatie() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'hepatitisbsurfaceantigeenconfirmatie' ])

    with process_scenario_object.crpcreactiefproteine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.crpcreactiefproteine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'crpcreactiefproteine' ])

    with process_scenario_object.crpcreactiefproteine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.crpcreactiefproteine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'crpcreactiefproteine' ])

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

    with process_scenario_object.buikoverzicht_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.buikoverzicht() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'buikoverzicht' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.toegangschircvdkatheterperifeerb_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.toegangschircvdkatheterperifeerb() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'toegangschircvdkatheterperifeerb' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.kaliumpotentiometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumpotentiometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumpotentiometrisch' ])

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

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

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

    with process_scenario_object.ureum_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ureum() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ureum' ])

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

    with process_scenario_object.leukocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leukocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leukocytentellenelektronisch' ])

    with process_scenario_object.crpcreactiefproteine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.crpcreactiefproteine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'crpcreactiefproteine' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

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

    with process_scenario_object.bacteriologischonderzoekmetkweeknie_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bacteriologischonderzoekmetkweeknie() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bacteriologischonderzoekmetkweeknie' ])

    with process_scenario_object.leukocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leukocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leukocytentellenelektronisch' ])

    with process_scenario_object.hepatitisbsurfaceantigeenconfirmatie_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.hepatitisbsurfaceantigeenconfirmatie() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'hepatitisbsurfaceantigeenconfirmatie' ])

    with process_scenario_object.hepatitisbsurfaceantigeenconfirmatie_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.hepatitisbsurfaceantigeenconfirmatie() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'hepatitisbsurfaceantigeenconfirmatie' ])

    with process_scenario_object.crpcreactiefproteine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.crpcreactiefproteine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'crpcreactiefproteine' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

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

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

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

    with process_scenario_object.leukocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leukocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leukocytentellenelektronisch' ])

    with process_scenario_object.cefalinetijdcoagulatie_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.cefalinetijdcoagulatie() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'cefalinetijdcoagulatie' ])

    with process_scenario_object.screeningantistoffenerytrocyten_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.screeningantistoffenerytrocyten() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'screeningantistoffenerytrocyten' ])

    with process_scenario_object.protrombinetijd_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.protrombinetijd() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'protrombinetijd' ])

    with process_scenario_object.differentiatieleukocytenhandmatig_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.differentiatieleukocytenhandmatig() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'differentiatieleukocytenhandmatig' ])

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

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

    with process_scenario_object.dieetnno_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dieetnno() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dieetnno' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

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

    with process_scenario_object.natriumvlamfotometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrisch' ])

    with process_scenario_object.kaliumpotentiometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumpotentiometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumpotentiometrisch' ])

    with process_scenario_object.leukocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leukocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leukocytentellenelektronisch' ])

    with process_scenario_object.trombocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.trombocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'trombocytentellenelektronisch' ])

    with process_scenario_object.crpcreactiefproteine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.crpcreactiefproteine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'crpcreactiefproteine' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

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

    with process_scenario_object.ureum_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ureum() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ureum' ])

    with process_scenario_object.creatinine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatinine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatinine' ])

    with process_scenario_object.creatinine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatinine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatinine' ])

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

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

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

    with process_scenario_object.hemoglobinefotoelektrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.hemoglobinefotoelektrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'hemoglobinefotoelektrisch' ])

    with process_scenario_object.fosfaat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.fosfaat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'fosfaat' ])

    with process_scenario_object.alkalischefosfatasekinetisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.alkalischefosfatasekinetisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'alkalischefosfatasekinetisch' ])

    with process_scenario_object.sgotasatkinetisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.sgotasatkinetisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'sgotasatkinetisch' ])

    with process_scenario_object.sgptalatkinetisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.sgptalatkinetisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'sgptalatkinetisch' ])

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

    with process_scenario_object.magnesiumaas_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.magnesiumaas() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'magnesiumaas' ])

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

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

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

    with process_scenario_object.kruisproefvolledigdriemethoden_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kruisproefvolledigdriemethoden() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kruisproefvolledigdriemethoden' ])

    with process_scenario_object.crpcreactiefproteine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.crpcreactiefproteine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'crpcreactiefproteine' ])

    with process_scenario_object.albumine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.albumine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'albumine' ])

    with process_scenario_object.screeningantistoffenerytrocyten_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.screeningantistoffenerytrocyten() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'screeningantistoffenerytrocyten' ])

    with process_scenario_object.magnesiumaas_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.magnesiumaas() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'magnesiumaas' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.echoabdomen_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.echoabdomen() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'echoabdomen' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

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

    with process_scenario_object.natriumvlamfotometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrisch' ])

    with process_scenario_object.kaliumpotentiometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumpotentiometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumpotentiometrisch' ])

    with process_scenario_object.leukocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leukocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leukocytentellenelektronisch' ])

    with process_scenario_object.crpcreactiefproteine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.crpcreactiefproteine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'crpcreactiefproteine' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.thorax_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.thorax() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'thorax' ])

    with process_scenario_object.ctabdomen_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ctabdomen() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ctabdomen' ])

    with process_scenario_object.vervolgconsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.vervolgconsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'vervolgconsultpoliklinisch' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.toegangschircvdkatheterperifeerb_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.toegangschircvdkatheterperifeerb() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'toegangschircvdkatheterperifeerb' ])

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

    with process_scenario_object.hemoglobinefotoelektrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.hemoglobinefotoelektrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'hemoglobinefotoelektrisch' ])

    with process_scenario_object.creatinine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatinine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatinine' ])

    with process_scenario_object.chloride_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.chloride() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'chloride' ])

    with process_scenario_object.fosfaat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.fosfaat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'fosfaat' ])

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

    with process_scenario_object.magnesiumaas_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.magnesiumaas() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'magnesiumaas' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.thorax_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.thorax() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'thorax' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

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

    with process_scenario_object.chloride_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.chloride() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'chloride' ])

    with process_scenario_object.fosfaat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.fosfaat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'fosfaat' ])

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

    with process_scenario_object.differentiatieleukocytenhandmatig_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.differentiatieleukocytenhandmatig() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'differentiatieleukocytenhandmatig' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

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

    with process_scenario_object.chloride_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.chloride() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'chloride' ])

    with process_scenario_object.fosfaat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.fosfaat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'fosfaat' ])

    with process_scenario_object.alkalischefosfatasekinetisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.alkalischefosfatasekinetisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'alkalischefosfatasekinetisch' ])

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

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

    with process_scenario_object.dieetnno_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dieetnno() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dieetnno' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

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

    with process_scenario_object.fosfaat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.fosfaat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'fosfaat' ])

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

    with process_scenario_object.leukocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leukocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leukocytentellenelektronisch' ])

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

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

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

    with process_scenario_object.fosfaat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.fosfaat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'fosfaat' ])

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

    with process_scenario_object.leukocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leukocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leukocytentellenelektronisch' ])

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

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

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

    with process_scenario_object.ureum_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ureum() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ureum' ])

    with process_scenario_object.creatinine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatinine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatinine' ])

    with process_scenario_object.chloride_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.chloride() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'chloride' ])

    with process_scenario_object.fosfaat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.fosfaat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'fosfaat' ])

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

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

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

    with process_scenario_object.chloride_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.chloride() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'chloride' ])

    with process_scenario_object.fosfaat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.fosfaat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'fosfaat' ])

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

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

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

    with process_scenario_object.creatinine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatinine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatinine' ])

    with process_scenario_object.chloride_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.chloride() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'chloride' ])

    with process_scenario_object.fosfaat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.fosfaat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'fosfaat' ])

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

    with process_scenario_object.leukocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leukocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leukocytentellenelektronisch' ])

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

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

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

    with process_scenario_object.creatinine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatinine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatinine' ])

    with process_scenario_object.chloride_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.chloride() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'chloride' ])

    with process_scenario_object.fosfaat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.fosfaat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'fosfaat' ])

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

    with process_scenario_object.leukocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leukocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leukocytentellenelektronisch' ])

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

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

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

    with process_scenario_object.creatinine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.creatinine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'creatinine' ])

    with process_scenario_object.chloride_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.chloride() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'chloride' ])

    with process_scenario_object.fosfaat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.fosfaat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'fosfaat' ])

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

    with process_scenario_object.leukocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leukocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leukocytentellenelektronisch' ])

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

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

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

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

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

    with process_scenario_object.sediment_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.sediment() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'sediment' ])

    with process_scenario_object.sediment_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.sediment() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'sediment' ])

    with process_scenario_object.microscopischonderzoekgekleurdenon_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.microscopischonderzoekgekleurdenon() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'microscopischonderzoekgekleurdenon' ])

    with process_scenario_object.bacteriologischonderzoekmetkweeknie_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bacteriologischonderzoekmetkweeknie() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bacteriologischonderzoekmetkweeknie' ])

    with process_scenario_object.urineonderzoekkwalitatief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.urineonderzoekkwalitatief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'urineonderzoekkwalitatief' ])

    with process_scenario_object.urineonderzoekkwalitatief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.urineonderzoekkwalitatief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'urineonderzoekkwalitatief' ])

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

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

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

    with process_scenario_object.natriumvlamfotometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.natriumvlamfotometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'natriumvlamfotometrisch' ])

    with process_scenario_object.kaliumpotentiometrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.kaliumpotentiometrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'kaliumpotentiometrisch' ])

    with process_scenario_object.leukocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leukocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leukocytentellenelektronisch' ])

    with process_scenario_object.crpcreactiefproteine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.crpcreactiefproteine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'crpcreactiefproteine' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

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

    with process_scenario_object.leukocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leukocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leukocytentellenelektronisch' ])

    with process_scenario_object.crpcreactiefproteine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.crpcreactiefproteine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'crpcreactiefproteine' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

    with process_scenario_object.dieetnno_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dieetnno() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dieetnno' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

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

    with process_scenario_object.leukocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leukocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leukocytentellenelektronisch' ])

    with process_scenario_object.clostridiumelisatest_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.clostridiumelisatest() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'clostridiumelisatest' ])

    with process_scenario_object.crpcreactiefproteine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.crpcreactiefproteine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'crpcreactiefproteine' ])

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

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

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

    with process_scenario_object.differentieletellingautomatisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.differentieletellingautomatisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'differentieletellingautomatisch' ])

    with process_scenario_object.leukocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leukocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leukocytentellenelektronisch' ])

    with process_scenario_object.leukocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leukocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leukocytentellenelektronisch' ])

    with process_scenario_object.trombocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.trombocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'trombocytentellenelektronisch' ])

    with process_scenario_object.crpcreactiefproteine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.crpcreactiefproteine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'crpcreactiefproteine' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

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

    with process_scenario_object.leukocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leukocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leukocytentellenelektronisch' ])

    with process_scenario_object.crpcreactiefproteine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.crpcreactiefproteine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'crpcreactiefproteine' ])

    with process_scenario_object.differentiatieleukocytenhandmatig_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.differentiatieleukocytenhandmatig() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'differentiatieleukocytenhandmatig' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

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

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.hemoglobinefotoelektrisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.hemoglobinefotoelektrisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'hemoglobinefotoelektrisch' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])
