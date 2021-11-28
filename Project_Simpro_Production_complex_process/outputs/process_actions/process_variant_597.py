def action_plan(entity, process_scenario_object):


    with process_scenario_object.echografiegenitaliainterna_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.echografiegenitaliainterna() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'echografiegenitaliainterna' ])

    with process_scenario_object.econsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.econsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'econsultpoliklinisch' ])

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

    with process_scenario_object.echografiegenitaliainterna_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.echografiegenitaliainterna() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'echografiegenitaliainterna' ])

    with process_scenario_object.vervolgconsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.vervolgconsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'vervolgconsultpoliklinisch' ])

    with process_scenario_object.histologischonderzoekbioptennno_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.histologischonderzoekbioptennno() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'histologischonderzoekbioptennno' ])

    with process_scenario_object.econsultbezoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.econsultbezoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'econsultbezoek' ])

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

    with process_scenario_object.bloedgroepaboenrhesusfactor_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bloedgroepaboenrhesusfactor() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bloedgroepaboenrhesusfactor' ])

    with process_scenario_object.rhesusfactordcentrifugeermethodee_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.rhesusfactordcentrifugeermethodee() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'rhesusfactordcentrifugeermethodee' ])

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

    with process_scenario_object.ceatumormarkermbvmeia_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ceatumormarkermbvmeia() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ceatumormarkermbvmeia' ])

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

    with process_scenario_object.bovenregtoesla_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.bovenregtoesla() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'bovenregtoesla' ])

    with process_scenario_object.ligdagenallespecbehkindergreval_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ligdagenallespecbehkindergreval() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ligdagenallespecbehkindergreval' ])

    with process_scenario_object.buikstageringslaparotomoment_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.buikstageringslaparotomoment() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'buikstageringslaparotomoment' ])

    with process_scenario_object.immunopathologischonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.immunopathologischonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'immunopathologischonderzoek' ])

    with process_scenario_object.vriescoupe_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.vriescoupe() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'vriescoupe' ])

    with process_scenario_object.cytologischonderzoekascites_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.cytologischonderzoekascites() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'cytologischonderzoekascites' ])

    with process_scenario_object.histologischonderzoekgroteresectiep_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.histologischonderzoekgroteresectiep() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'histologischonderzoekgroteresectiep' ])

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

    with process_scenario_object.duplexscanvenenbeen_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.duplexscanvenenbeen() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'duplexscanvenenbeen' ])

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

    with process_scenario_object.hematocrietmbvcentrifuge_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.hematocrietmbvcentrifuge() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'hematocrietmbvcentrifuge' ])

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

    with process_scenario_object.echografiedopplervenenbeen_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.echografiedopplervenenbeen() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'echografiedopplervenenbeen' ])

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

    with process_scenario_object.aannamelaboratoriumonderzoek_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.aannamelaboratoriumonderzoek() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'aannamelaboratoriumonderzoek' ])

    with process_scenario_object.glucose_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.glucose() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'glucose' ])

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

    with process_scenario_object.protrombinetijdquickowrenofmodif_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.protrombinetijdquickowrenofmodif() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'protrombinetijdquickowrenofmodif' ])

    with process_scenario_object.hematocrietspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.hematocrietspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'hematocrietspoed' ])

    with process_scenario_object.trombocytentellenspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.trombocytentellenspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'trombocytentellenspoed' ])

    with process_scenario_object.heparinebepalingkaolinecefalinetij_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.heparinebepalingkaolinecefalinetij() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'heparinebepalingkaolinecefalinetij' ])

    with process_scenario_object.internationalnormalisedratiombvtromb_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.internationalnormalisedratiombvtromb() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'internationalnormalisedratiombvtromb' ])

    with process_scenario_object.leucocytentellenelectronischspoed_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.leucocytentellenelectronischspoed() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'leucocytentellenelectronischspoed' ])

    with process_scenario_object.crpcreactiefproteine_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.crpcreactiefproteine() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'crpcreactiefproteine' ])

    with process_scenario_object.ordertarief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.ordertarief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'ordertarief' ])

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

    with process_scenario_object.hepatitisbsurfaceantigeenconfirmatie_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.hepatitisbsurfaceantigeenconfirmatie() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'hepatitisbsurfaceantigeenconfirmatie' ])

    with process_scenario_object.urineonderzoekkwalitatief_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.urineonderzoekkwalitatief() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'urineonderzoekkwalitatief' ])

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

    with process_scenario_object.clostridiumelisatest_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.clostridiumelisatest() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'clostridiumelisatest' ])

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

    with process_scenario_object.coupeterinzage_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.coupeterinzage() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'coupeterinzage' ])

    with process_scenario_object.vervolgconsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.vervolgconsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'vervolgconsultpoliklinisch' ])

    with process_scenario_object.vervolgconsultpoliklinisch_resource.request() as request:
        yield request
        yield process_scenario_object.env.process( process_scenario_object.vervolgconsultpoliklinisch() )
        process_scenario_object.log_list.append([entity, process_scenario_object.env.now, 'vervolgconsultpoliklinisch' ])
