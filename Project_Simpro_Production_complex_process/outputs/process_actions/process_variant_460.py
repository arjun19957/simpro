def action_plan(entity, process_scenario_object):


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

    with process_scenario_object.sgotasatkinetisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.sgotasatkinetisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'sgotasatkinetisch' ])

    with process_scenario_object.sgptalatkinetisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.sgptalatkinetisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'sgptalatkinetisch' ])

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

    with process_scenario_object.screeningantistoffenerytrocyten_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.screeningantistoffenerytrocyten() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'screeningantistoffenerytrocyten' ])

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

    with process_scenario_object.dagverplegingallespecbehkindrev_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dagverplegingallespecbehkindrev() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dagverplegingallespecbehkindrev' ])

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

    with process_scenario_object.administratieftariefeerstepol_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.administratieftariefeerstepol() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'administratieftariefeerstepol' ])

    with process_scenario_object.dagverpleginga_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.dagverpleginga() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'dagverpleginga' ])

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.haemoglobinefotoelectrischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.haemoglobinefotoelectrischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'haemoglobinefotoelectrischspoed' ])

    with process_scenario_object.hematocrietspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.hematocrietspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'hematocrietspoed' ])

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

    with process_scenario_object.telefonischconsult_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.telefonischconsult() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'telefonischconsult' ])

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

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

    with process_scenario_object.gefiltreerderytrocytenconcentraat_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.gefiltreerderytrocytenconcentraat() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'gefiltreerderytrocytenconcentraat' ])
