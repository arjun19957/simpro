def action_plan(entity, process_scenario_object):


    with process_scenario_object.verloskgynaeckortekaartkostenout_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.verloskgynaeckortekaartkostenout() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'verloskgynaeckortekaartkostenout' ])

    with process_scenario_object.inwendgeneeskkortekaartkostenout_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.inwendgeneeskkortekaartkostenout() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'inwendgeneeskkortekaartkostenout' ])

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

    with process_scenario_object.cambvmeia_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.cambvmeia() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'cambvmeia' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.onderzoekvaneldersnietbeoordeeld_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.onderzoekvaneldersnietbeoordeeld() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'onderzoekvaneldersnietbeoordeeld' ])

    with process_scenario_object.onderzoekvaneldersnietbeoordeeld_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.onderzoekvaneldersnietbeoordeeld() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'onderzoekvaneldersnietbeoordeeld' ])

    with process_scenario_object.onderzoekvaneldersnietbeoordeeld_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.onderzoekvaneldersnietbeoordeeld() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'onderzoekvaneldersnietbeoordeeld' ])

    with process_scenario_object.onderzoekvaneldersnietbeoordeeld_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.onderzoekvaneldersnietbeoordeeld() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'onderzoekvaneldersnietbeoordeeld' ])

    with process_scenario_object.onderzoekvaneldersnietbeoordeeld_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.onderzoekvaneldersnietbeoordeeld() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'onderzoekvaneldersnietbeoordeeld' ])

    with process_scenario_object.onderzoekvaneldersnietbeoordeeld_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.onderzoekvaneldersnietbeoordeeld() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'onderzoekvaneldersnietbeoordeeld' ])

    with process_scenario_object.onderzoekvaneldersnietbeoordeeld_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.onderzoekvaneldersnietbeoordeeld() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'onderzoekvaneldersnietbeoordeeld' ])

    with process_scenario_object.econsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.econsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'econsultpoliklinisch' ])

    with process_scenario_object.econsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.econsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'econsultpoliklinisch' ])

    with process_scenario_object.administratieftariefeerstepol_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.administratieftariefeerstepol() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'administratieftariefeerstepol' ])

    with process_scenario_object.administratieftariefeerstepol_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.administratieftariefeerstepol() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'administratieftariefeerstepol' ])

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

    with process_scenario_object.inwendgeneeskaanvkaartkostenout_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.inwendgeneeskaanvkaartkostenout() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'inwendgeneeskaanvkaartkostenout' ])

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

    with process_scenario_object.gammaglutamyltranspeptidasespoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.gammaglutamyltranspeptidasespoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'gammaglutamyltranspeptidasespoed' ])

    with process_scenario_object.leucocytentellenelectronischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leucocytentellenelectronischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leucocytentellenelectronischspoed' ])

    with process_scenario_object.albuminespoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.albuminespoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'albuminespoed' ])

    with process_scenario_object.cambvmeia_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.cambvmeia() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'cambvmeia' ])

    with process_scenario_object.magnesiumaasspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.magnesiumaasspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'magnesiumaasspoed' ])

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

    with process_scenario_object.dagverplegingallespecbehkindrev_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dagverplegingallespecbehkindrev() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dagverplegingallespecbehkindrev' ])

    with process_scenario_object.dagverplegingallespecbehkindrev_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dagverplegingallespecbehkindrev() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dagverplegingallespecbehkindrev' ])

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

    with process_scenario_object.leucocytentellenelectronischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leucocytentellenelectronischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leucocytentellenelectronischspoed' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

    with process_scenario_object.dagverpleginga_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dagverpleginga() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dagverpleginga' ])

    with process_scenario_object.dagverpleginga_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dagverpleginga() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dagverpleginga' ])

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

    with process_scenario_object.gammaglutamyltranspeptidasespoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.gammaglutamyltranspeptidasespoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'gammaglutamyltranspeptidasespoed' ])

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

    with process_scenario_object.dagverplegingallespecbehkindrev_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dagverplegingallespecbehkindrev() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dagverplegingallespecbehkindrev' ])

    with process_scenario_object.dagverplegingallespecbehkindrev_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dagverplegingallespecbehkindrev() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dagverplegingallespecbehkindrev' ])

    with process_scenario_object.dagverplegingallespecbehkindrev_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dagverplegingallespecbehkindrev() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dagverplegingallespecbehkindrev' ])

    with process_scenario_object.dagverpleginga_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dagverpleginga() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dagverpleginga' ])

    with process_scenario_object.dagverpleginga_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dagverpleginga() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dagverpleginga' ])

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

    with process_scenario_object.ctabdomen_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ctabdomen() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ctabdomen' ])

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

    with process_scenario_object.bilirubinegeconjugeerd_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bilirubinegeconjugeerd() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bilirubinegeconjugeerd' ])

    with process_scenario_object.bilirubinetotaal_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bilirubinetotaal() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bilirubinetotaal' ])

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

    with process_scenario_object.differentieletellingautomatisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.differentieletellingautomatisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'differentieletellingautomatisch' ])

    with process_scenario_object.differentieletellingautomatisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.differentieletellingautomatisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'differentieletellingautomatisch' ])

    with process_scenario_object.haemoglobinefotoelectrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.haemoglobinefotoelectrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'haemoglobinefotoelectrischspoed' ])

    with process_scenario_object.leukocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leukocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leukocytentellenelektronisch' ])

    with process_scenario_object.trombocytentellenelektronisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.trombocytentellenelektronisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'trombocytentellenelektronisch' ])

    with process_scenario_object.trombocytentellenspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.trombocytentellenspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'trombocytentellenspoed' ])

    with process_scenario_object.cefalinetijdcoagulatie_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.cefalinetijdcoagulatie() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'cefalinetijdcoagulatie' ])

    with process_scenario_object.gammaglutamyltranspeptidase_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.gammaglutamyltranspeptidase() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'gammaglutamyltranspeptidase' ])

    with process_scenario_object.trombotest_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.trombotest() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'trombotest' ])

    with process_scenario_object.leucocytentellenelectronischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leucocytentellenelectronischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leucocytentellenelectronischspoed' ])

    with process_scenario_object.calcium_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.calcium() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'calcium' ])

    with process_scenario_object.cambvmeia_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.cambvmeia() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'cambvmeia' ])

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

    with process_scenario_object.bilirubinegeconjugeerd_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bilirubinegeconjugeerd() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bilirubinegeconjugeerd' ])

    with process_scenario_object.bilirubinetotaal_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bilirubinetotaal() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bilirubinetotaal' ])

    with process_scenario_object.amylase_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.amylase() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'amylase' ])

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

    with process_scenario_object.haemoglobinefotoelectrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.haemoglobinefotoelectrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'haemoglobinefotoelectrischspoed' ])

    with process_scenario_object.gammaglutamyltranspeptidase_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.gammaglutamyltranspeptidase() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'gammaglutamyltranspeptidase' ])

    with process_scenario_object.leucocytentellenelectronischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leucocytentellenelectronischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leucocytentellenelectronischspoed' ])

    with process_scenario_object.calcium_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.calcium() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'calcium' ])

    with process_scenario_object.crpcreactiefproteine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.crpcreactiefproteine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'crpcreactiefproteine' ])

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

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.klasseba_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.klasseba() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'klasseba' ])
