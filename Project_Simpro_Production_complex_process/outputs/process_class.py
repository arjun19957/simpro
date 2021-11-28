import simpy

class process_definition():

    def __init__(self,env):
        self.env = env
        self.log_list = []
        
        self.econsultpoliklinisch_resource = simpy.Resource(env, capacity = 1)
        
        self.administratieftariefeerstepol_resource = simpy.Resource(env, capacity = 1)
        
        self.verloskgynaeckortekaartkostenout_resource = simpy.Resource(env, capacity = 1)
        
        self.echografiegenitaliainterna_resource = simpy.Resource(env, capacity = 1)
        
        self.simulatorgebruikvooraanvangmegavol_resource = simpy.Resource(env, capacity = 1)
        
        self.behandeltijdeenheidtmegavolt_resource = simpy.Resource(env, capacity = 1)
        
        self.teletherapiemegavoltfotonenbestrali_resource = simpy.Resource(env, capacity = 1)
        
        self.aannamelaboratoriumonderzoek_resource = simpy.Resource(env, capacity = 1)
        
        self.ureum_resource = simpy.Resource(env, capacity = 1)
        
        self.hemoglobinefotoelektrisch_resource = simpy.Resource(env, capacity = 1)
        
        self.creatinine_resource = simpy.Resource(env, capacity = 1)
        
        self.natriumvlamfotometrisch_resource = simpy.Resource(env, capacity = 1)
        
        self.kaliumpotentiometrisch_resource = simpy.Resource(env, capacity = 1)
        
        self.leukocytentellenelektronisch_resource = simpy.Resource(env, capacity = 1)
        
        self.trombocytentellenelektronisch_resource = simpy.Resource(env, capacity = 1)
        
        self.ordertarief_resource = simpy.Resource(env, capacity = 1)
        
        self.ligdagenallespecbehkindergreval_resource = simpy.Resource(env, capacity = 1)
        
        self.sedimentspoed_resource = simpy.Resource(env, capacity = 1)
        
        self.bacteriologischonderzoekmetkweeknie_resource = simpy.Resource(env, capacity = 1)
        
        self.resistentiebepalingenbepalingen_resource = simpy.Resource(env, capacity = 1)
        
        self.hepatitisbsurfaceantigeenconfirmatie_resource = simpy.Resource(env, capacity = 1)
        
        self.urineonderzoekkwalitatief_resource = simpy.Resource(env, capacity = 1)
        
        self.klinischeopnamea_resource = simpy.Resource(env, capacity = 1)
        
        self.klasseba_resource = simpy.Resource(env, capacity = 1)
        
        self.sgotasatkinetisch_resource = simpy.Resource(env, capacity = 1)
        
        self.sgptalatkinetisch_resource = simpy.Resource(env, capacity = 1)
        
        self.melkzuurdehydrogenaseldhkinetisch_resource = simpy.Resource(env, capacity = 1)
        
        self.differentieletellingautomatisch_resource = simpy.Resource(env, capacity = 1)
        
        self.trombotest_resource = simpy.Resource(env, capacity = 1)
        
        self.crpcreactiefproteine_resource = simpy.Resource(env, capacity = 1)
        
        self.brachytherapieinterstitieelintensi_resource = simpy.Resource(env, capacity = 1)
        
        self.inwendgeneeskkortekaartkostenout_resource = simpy.Resource(env, capacity = 1)
        
        self.vervolgconsultpoliklinisch_resource = simpy.Resource(env, capacity = 1)
        
        self.creatininespoed_resource = simpy.Resource(env, capacity = 1)
        
        self.ijzer_resource = simpy.Resource(env, capacity = 1)
        
        self.natriumvlamfotometrischspoed_resource = simpy.Resource(env, capacity = 1)
        
        self.kaliumvlamfotometrischspoed_resource = simpy.Resource(env, capacity = 1)
        
        self.foliumzuurmbvradioisotopen_resource = simpy.Resource(env, capacity = 1)
        
        self.vitaminebmbvchemieluminescentie_resource = simpy.Resource(env, capacity = 1)
        
        self.bloedgroepaboenrhesusfactor_resource = simpy.Resource(env, capacity = 1)
        
        self.rhesusfactordcentrifugeermethodee_resource = simpy.Resource(env, capacity = 1)
        
        self.haemoglobinefotoelectrischspoed_resource = simpy.Resource(env, capacity = 1)
        
        self.trombocytentellenspoed_resource = simpy.Resource(env, capacity = 1)
        
        self.reticulocytentellenmbvfacscan_resource = simpy.Resource(env, capacity = 1)
        
        self.cdefenotypering_resource = simpy.Resource(env, capacity = 1)
        
        self.bloedgroepantigenenanderedanaborhesu_resource = simpy.Resource(env, capacity = 1)
        
        self.kruisproefvolledigdriemethoden_resource = simpy.Resource(env, capacity = 1)
        
        self.leucocytentellenelectronischspoed_resource = simpy.Resource(env, capacity = 1)
        
        self.crpcreactiefproteinespoed_resource = simpy.Resource(env, capacity = 1)
        
        self.screeningantistoffenerytrocyten_resource = simpy.Resource(env, capacity = 1)
        
        self.transferrinembvics_resource = simpy.Resource(env, capacity = 1)
        
        self.bovenregtoesla_resource = simpy.Resource(env, capacity = 1)
        
        self.gefiltreerderytrocytenconcentraat_resource = simpy.Resource(env, capacity = 1)
        
        self.echonierenurinewegen_resource = simpy.Resource(env, capacity = 1)
        
        self.intercconsultklinischanesthesie_resource = simpy.Resource(env, capacity = 1)
        
        self.ureumspoed_resource = simpy.Resource(env, capacity = 1)
        
        self.sgptalatkinetischspoed_resource = simpy.Resource(env, capacity = 1)
        
        self.sgotasatkinetischspoed_resource = simpy.Resource(env, capacity = 1)
        
        self.internationalnormalisedratiombvtromb_resource = simpy.Resource(env, capacity = 1)
        
        self.dagverplegingallespecbehkindrev_resource = simpy.Resource(env, capacity = 1)
        
        self.dagverpleginga_resource = simpy.Resource(env, capacity = 1)
        
        self.urinezuurmeturicaseuvspectrofotome_resource = simpy.Resource(env, capacity = 1)
        
        self.melkzuurdehydrogenasespoed_resource = simpy.Resource(env, capacity = 1)
        
        self.echoabdomen_resource = simpy.Resource(env, capacity = 1)
        
        self.sediment_resource = simpy.Resource(env, capacity = 1)
        
        self.klinischekaartinwendigegeneeskunde_resource = simpy.Resource(env, capacity = 1)
        
        self.inwendgeneeskaanvkaartkostenout_resource = simpy.Resource(env, capacity = 1)
        
        self.squamouscellcarcinomambveia_resource = simpy.Resource(env, capacity = 1)
        
        self.ctabdomen_resource = simpy.Resource(env, capacity = 1)
        
        self.cambvmeia_resource = simpy.Resource(env, capacity = 1)
        
        self.telefonischconsult_resource = simpy.Resource(env, capacity = 1)
        
        self.patientnietverschenenradiologie_resource = simpy.Resource(env, capacity = 1)
        
        self.homocystinechromatografisch_resource = simpy.Resource(env, capacity = 1)
        
        self.cytologischonderzoekectocervix_resource = simpy.Resource(env, capacity = 1)
        
        self.bilirubinegeconjugeerd_resource = simpy.Resource(env, capacity = 1)
        
        self.bilirubinetotaal_resource = simpy.Resource(env, capacity = 1)
        
        self.glucose_resource = simpy.Resource(env, capacity = 1)
        
        self.alkalischefosfatasekinetisch_resource = simpy.Resource(env, capacity = 1)
        
        self.gammaglutamyltranspeptidase_resource = simpy.Resource(env, capacity = 1)
        
        self.ceatumormarkermbvmeia_resource = simpy.Resource(env, capacity = 1)
        
        self.calcium_resource = simpy.Resource(env, capacity = 1)
        
        self.albumine_resource = simpy.Resource(env, capacity = 1)
        
        self.thorax_resource = simpy.Resource(env, capacity = 1)
        
        self.klasseaa_resource = simpy.Resource(env, capacity = 1)
        
        self.buikstaglaptumorredomentec_resource = simpy.Resource(env, capacity = 1)
        
        self.immunopathologischonderzoek_resource = simpy.Resource(env, capacity = 1)
        
        self.cytologischonderzoekascites_resource = simpy.Resource(env, capacity = 1)
        
        self.histologischonderzoekgroteresectiep_resource = simpy.Resource(env, capacity = 1)
        
        self.glucosespoed_resource = simpy.Resource(env, capacity = 1)
        
        self.calciumspoed_resource = simpy.Resource(env, capacity = 1)
        
        self.melkzuurenzymatischspoed_resource = simpy.Resource(env, capacity = 1)
        
        self.osaturatie_resource = simpy.Resource(env, capacity = 1)
        
        self.ctthorax_resource = simpy.Resource(env, capacity = 1)
        
        self.verloskgynaecaanvkaartkostenout_resource = simpy.Resource(env, capacity = 1)
        
        self.hematocrietmbvcentrifuge_resource = simpy.Resource(env, capacity = 1)
        
        self.totaaleiwit_resource = simpy.Resource(env, capacity = 1)
        
        self.vulvaradvulvectomieoppend_resource = simpy.Resource(env, capacity = 1)
        
        self.microscopischonderzoekgekleurdenon_resource = simpy.Resource(env, capacity = 1)
        
        self.coupeterinzage_resource = simpy.Resource(env, capacity = 1)
        
        self.mribekken_resource = simpy.Resource(env, capacity = 1)
        
        self.skeletscintigrafietotalelichaam_resource = simpy.Resource(env, capacity = 1)
        
        self.histologischonderzoekbioptennno_resource = simpy.Resource(env, capacity = 1)
        
        self.citohistologischonderzoek_resource = simpy.Resource(env, capacity = 1)
        
        self.fosfaat_resource = simpy.Resource(env, capacity = 1)
        
        self.ctbovenbuik_resource = simpy.Resource(env, capacity = 1)
        
        self.blaasuretrocystoscopienno_resource = simpy.Resource(env, capacity = 1)
        
        self.vaginatoucheronderanesthesie_resource = simpy.Resource(env, capacity = 1)
        
        self.wervelkolomlumbaal_resource = simpy.Resource(env, capacity = 1)
        
        self.cthersenen_resource = simpy.Resource(env, capacity = 1)
        
        self.differentiatieleukocytenhandmatig_resource = simpy.Resource(env, capacity = 1)
        
        self.anesthesiebijbehandelingmetradium_resource = simpy.Resource(env, capacity = 1)
        
        self.albuminespoed_resource = simpy.Resource(env, capacity = 1)
        
        self.bilirubinekwantitatieftotaalofdirect_resource = simpy.Resource(env, capacity = 1)
        
        self.alfaamylasespoed_resource = simpy.Resource(env, capacity = 1)
        
        self.chloridespoed_resource = simpy.Resource(env, capacity = 1)
        
        self.fosfaatspoed_resource = simpy.Resource(env, capacity = 1)
        
        self.alkalischefosfatasekinetischspoed_resource = simpy.Resource(env, capacity = 1)
        
        self.totaaleiwitcolorimetrischspoed_resource = simpy.Resource(env, capacity = 1)
        
        self.kreatininefosfokinasespoed_resource = simpy.Resource(env, capacity = 1)
        
        self.hematocrietspoed_resource = simpy.Resource(env, capacity = 1)
        
        self.gammaglutamyltranspeptidasespoed_resource = simpy.Resource(env, capacity = 1)
        
        self.ferritinekwnmbvchemieluminescentie_resource = simpy.Resource(env, capacity = 1)
        
        self.erythrocytentellenelectronischspoed_resource = simpy.Resource(env, capacity = 1)
        
        self.osmolaliteitspoed_resource = simpy.Resource(env, capacity = 1)
        
        self.bezinkingssnelheidfotoelektrisch_resource = simpy.Resource(env, capacity = 1)
        
        self.magnesiumaasspoed_resource = simpy.Resource(env, capacity = 1)
        
        self.mriwervelkolomcervicaal_resource = simpy.Resource(env, capacity = 1)
        
        self.mriwervelkolomthoracaal_resource = simpy.Resource(env, capacity = 1)
        
        self.mriwervelkolomlumbaal_resource = simpy.Resource(env, capacity = 1)
        
        self.cortisolimmunofluorimetrisch_resource = simpy.Resource(env, capacity = 1)
        
        self.tshenzymimmunologisch_resource = simpy.Resource(env, capacity = 1)
        
        self.cortisol_resource = simpy.Resource(env, capacity = 1)
        
        self.vatenvenapunctie_resource = simpy.Resource(env, capacity = 1)
        
        self.acthmbvradioisotopen_resource = simpy.Resource(env, capacity = 1)
        
        self.ecgelektrocardiografie_resource = simpy.Resource(env, capacity = 1)
        
        self.lithium_resource = simpy.Resource(env, capacity = 1)
        
        self.vrijtmbvriaft_resource = simpy.Resource(env, capacity = 1)
        
        self.econsultbezoek_resource = simpy.Resource(env, capacity = 1)
        
        self.lymfeklierscintsentinelnodedynamis_resource = simpy.Resource(env, capacity = 1)
        
        self.lymfeklierscintsentinelnodevervolg_resource = simpy.Resource(env, capacity = 1)
        
        self.lymfeklierscintsentinelnodemetpro_resource = simpy.Resource(env, capacity = 1)
        
        self.vulvaradicalevulvectzndingu_resource = simpy.Resource(env, capacity = 1)
        
        self.vriescoupe_resource = simpy.Resource(env, capacity = 1)
        
        self.methemoglobinesulfhemoglobineelk_resource = simpy.Resource(env, capacity = 1)
        
        self.bicarbonaat_resource = simpy.Resource(env, capacity = 1)
        
        self.cohbkwn_resource = simpy.Resource(env, capacity = 1)
        
        self.actuelephpcostandbicarbonaat_resource = simpy.Resource(env, capacity = 1)
        
        self.lithiumspoed_resource = simpy.Resource(env, capacity = 1)
        
        self.verloskgynaecjaarkaartkostenout_resource = simpy.Resource(env, capacity = 1)
        
        self.histologischonderzoekkleineresectie_resource = simpy.Resource(env, capacity = 1)
        
        self.vrwgeslorgbiopsiepunctiecytologie_resource = simpy.Resource(env, capacity = 1)
        
        self.buikoverzicht_resource = simpy.Resource(env, capacity = 1)
        
        self.klinischekaartanesthesie_resource = simpy.Resource(env, capacity = 1)
        
        self.arteriepunctietbvverblijfsnaald_resource = simpy.Resource(env, capacity = 1)
        
        self.thoraxopzaal_resource = simpy.Resource(env, capacity = 1)
        
        self.protrombinetijdquickowrenofmodif_resource = simpy.Resource(env, capacity = 1)
        
        self.heparinebepalingkaolinecefalinetij_resource = simpy.Resource(env, capacity = 1)
        
        self.intercconsultklinischlongziekten_resource = simpy.Resource(env, capacity = 1)
        
        self.dieetnno_resource = simpy.Resource(env, capacity = 1)
        
        self.buikprimairestageringsoperati_resource = simpy.Resource(env, capacity = 1)
        
        self.antihivmbvelisa_resource = simpy.Resource(env, capacity = 1)
        
        self.patientnietverschenenngivnoshow_resource = simpy.Resource(env, capacity = 1)
        
        self.infuusinbrengen_resource = simpy.Resource(env, capacity = 1)
        
        self.cytologischonderzoekvagina_resource = simpy.Resource(env, capacity = 1)
        
        self.tumorpetscantotalelichaam_resource = simpy.Resource(env, capacity = 1)
        
        self.blaascystoscopiemetbiopsie_resource = simpy.Resource(env, capacity = 1)
        
        self.cytologischonderzoeklymfeklierpuncti_resource = simpy.Resource(env, capacity = 1)
        
        self.diagnostischepunctieonderechocontrole_resource = simpy.Resource(env, capacity = 1)
        
        self.echoschoudermzbovenarm_resource = simpy.Resource(env, capacity = 1)
        
        self.cytologischonderzoekpancreaspunctie_resource = simpy.Resource(env, capacity = 1)
        
        self.echobovenbuik_resource = simpy.Resource(env, capacity = 1)
        
        self.hyperthermie_resource = simpy.Resource(env, capacity = 1)
        
        self.helebovenbeenmetonderbeenenvoet_resource = simpy.Resource(env, capacity = 1)
        
        self.magnesiumaas_resource = simpy.Resource(env, capacity = 1)
        
        self.bekken_resource = simpy.Resource(env, capacity = 1)
        
        self.bekkenliggend_resource = simpy.Resource(env, capacity = 1)
        
        self.fdpdimeerimmunologisch_resource = simpy.Resource(env, capacity = 1)
        
        self.ctartenvenpulmonales_resource = simpy.Resource(env, capacity = 1)
        
        self.paclitaxel_resource = simpy.Resource(env, capacity = 1)
        
        self.chloride_resource = simpy.Resource(env, capacity = 1)
        
        self.bovenbeen_resource = simpy.Resource(env, capacity = 1)
        
        self.onderbeen_resource = simpy.Resource(env, capacity = 1)
        
        self.cefalinetijdcoagulatie_resource = simpy.Resource(env, capacity = 1)
        
        self.protrombinetijd_resource = simpy.Resource(env, capacity = 1)
        
        self.vulvaincisieoverige_resource = simpy.Resource(env, capacity = 1)
        
        self.echografieblaasextern_resource = simpy.Resource(env, capacity = 1)
        
        self.punctietbvcytologischonderzoekdoorp_resource = simpy.Resource(env, capacity = 1)
        
        self.vulvavulvectomieliesblok_resource = simpy.Resource(env, capacity = 1)
        
        self.microscopischonderzoekelektronenmic_resource = simpy.Resource(env, capacity = 1)
        
        self.buikstageringslaparotomoment_resource = simpy.Resource(env, capacity = 1)
        
        self.mammografiethoraxwand_resource = simpy.Resource(env, capacity = 1)
        
        self.echomamma_resource = simpy.Resource(env, capacity = 1)
        
        self.vrwgeslorgcurettagegefractioneerd_resource = simpy.Resource(env, capacity = 1)
        
        self.vulvabiopsiepunctiecytologie_resource = simpy.Resource(env, capacity = 1)
        
        self.uterushysteroscopie_resource = simpy.Resource(env, capacity = 1)
        
        self.uterusextirpabdradlymfaden_resource = simpy.Resource(env, capacity = 1)
        
        self.toonaudiometrieaudiologischcentrum_resource = simpy.Resource(env, capacity = 1)
        
        self.hoogfrequenteaudiometrieaudiologisch_resource = simpy.Resource(env, capacity = 1)
        
        self.tympanometriestandaardaudiologisch_resource = simpy.Resource(env, capacity = 1)
        
        self.patientenkontaktaudiologiekorterdan_resource = simpy.Resource(env, capacity = 1)
        
        self.anesthesiebijspeconderzenverrge_resource = simpy.Resource(env, capacity = 1)
        
        self.bekkenstaand_resource = simpy.Resource(env, capacity = 1)
        
        self.cytologischonderzoeknierpunctie_resource = simpy.Resource(env, capacity = 1)
        
        self.doorlichtingzonderopnamethorax_resource = simpy.Resource(env, capacity = 1)
        
        self.eiwitbeperktmineralenbeperkt_resource = simpy.Resource(env, capacity = 1)
        
        self.pyelografieantegraadviadrain_resource = simpy.Resource(env, capacity = 1)
        
        self.verwisselenvannefrostomiedrain_resource = simpy.Resource(env, capacity = 1)
        
        self.lipase_resource = simpy.Resource(env, capacity = 1)
        
        self.hemoglobinea_resource = simpy.Resource(env, capacity = 1)
        
        self.zwaredagverpleginga_resource = simpy.Resource(env, capacity = 1)
        
        self.mriabdomen_resource = simpy.Resource(env, capacity = 1)
        
        self.directeantiglobulinetestcoombs_resource = simpy.Resource(env, capacity = 1)
        
        self.antistoffentegenerysspecificiteit_resource = simpy.Resource(env, capacity = 1)
        
        self.identirregulaireastegenerysnapo_resource = simpy.Resource(env, capacity = 1)
        
        self.afwezigheidsdaga_resource = simpy.Resource(env, capacity = 1)
        
        self.ligasechainreactionlcr_resource = simpy.Resource(env, capacity = 1)
        
        self.uterusintrauterinedeviceinbre_resource = simpy.Resource(env, capacity = 1)
        
        self.mribijnier_resource = simpy.Resource(env, capacity = 1)
        
        self.melkzuurenzymatisch_resource = simpy.Resource(env, capacity = 1)
        
        self.blaascatheterademeureinbre_resource = simpy.Resource(env, capacity = 1)
        
        self.betasubunitbepmbvriahcg_resource = simpy.Resource(env, capacity = 1)
        
        self.sikkelcel_resource = simpy.Resource(env, capacity = 1)
        
        self.alfafoetoproteine_resource = simpy.Resource(env, capacity = 1)
        
        self.cholesteroltotaal_resource = simpy.Resource(env, capacity = 1)
        
        self.triglyceridenenzymatisch_resource = simpy.Resource(env, capacity = 1)
        
        self.cholesterolhdl_resource = simpy.Resource(env, capacity = 1)
        
        self.afereseplasmagesplitstfqenfq_resource = simpy.Resource(env, capacity = 1)
        
        self.catumormarkermbvmeia_resource = simpy.Resource(env, capacity = 1)
        
        self.catumormarker_resource = simpy.Resource(env, capacity = 1)
        
        self.ctbekken_resource = simpy.Resource(env, capacity = 1)
        
        self.heup_resource = simpy.Resource(env, capacity = 1)
        
        self.ctwervelkolomlumbaal_resource = simpy.Resource(env, capacity = 1)
        
        self.botdensitometrielwk_resource = simpy.Resource(env, capacity = 1)
        
        self.botdensitometriefemurhals_resource = simpy.Resource(env, capacity = 1)
        
        self.titratiedirecteantiglobulinetestcoo_resource = simpy.Resource(env, capacity = 1)
        
        self.vrwgeslorgexcdestructpathafwijkin_resource = simpy.Resource(env, capacity = 1)
        
        self.analgesieepiduraaldooranesthesist_resource = simpy.Resource(env, capacity = 1)
        
        self.urinewegenurodynamischonderzoekvij_resource = simpy.Resource(env, capacity = 1)
        
        self.uterusextirpatieabdominaalradi_resource = simpy.Resource(env, capacity = 1)
        
        self.maagontledigscintvastvloeibvoeds_resource = simpy.Resource(env, capacity = 1)
        
        self.darmcolonpassagescintcompvervolg_resource = simpy.Resource(env, capacity = 1)
        
        self.mriheup_resource = simpy.Resource(env, capacity = 1)
        
        self.echoonderbuik_resource = simpy.Resource(env, capacity = 1)
        
        self.creatinefosfokinasembspoed_resource = simpy.Resource(env, capacity = 1)
        
        self.troponinetmbvelisa_resource = simpy.Resource(env, capacity = 1)
        
        self.ovariumdebulkingovariumcarcinoom_resource = simpy.Resource(env, capacity = 1)
        
        self.cervixlisexcisieportiodiathe_resource = simpy.Resource(env, capacity = 1)
        
        self.uterusextirpatieabdominaaltota_resource = simpy.Resource(env, capacity = 1)
        
        self.hartdopplerechocardiografie_resource = simpy.Resource(env, capacity = 1)
        
        self.uteruscarccervixvlgswerthei_resource = simpy.Resource(env, capacity = 1)
        
        self.hematologieontstekscinttotlichaam_resource = simpy.Resource(env, capacity = 1)
        
        self.ovariumadnexextirpatiedmvlapar_resource = simpy.Resource(env, capacity = 1)
        
        self.pyelografiewoniertransplantaat_resource = simpy.Resource(env, capacity = 1)
        
        self.longfunctiecocapnografie_resource = simpy.Resource(env, capacity = 1)
        
        self.amylase_resource = simpy.Resource(env, capacity = 1)
        
        self.ammoniak_resource = simpy.Resource(env, capacity = 1)
        
        self.fibrinogeen_resource = simpy.Resource(env, capacity = 1)
        
        self.trombocytenleukoverwijderddonor_resource = simpy.Resource(env, capacity = 1)
        
        self.haptoglobine_resource = simpy.Resource(env, capacity = 1)
        
        self.trombinetijd_resource = simpy.Resource(env, capacity = 1)
        
        self.celkweekenisolatie_resource = simpy.Resource(env, capacity = 1)
        
        self.determinatieenorienttyperingdmvce_resource = simpy.Resource(env, capacity = 1)
        
        self.buikproeflaparotomie_resource = simpy.Resource(env, capacity = 1)
        
        self.blaassuprapubischekatheterinb_resource = simpy.Resource(env, capacity = 1)
        
        self.dikkedarmsigmoidoscopiemetflexibe_resource = simpy.Resource(env, capacity = 1)
        
        self.vulvavulvectomiezonderlieskli_resource = simpy.Resource(env, capacity = 1)
        
        self.intercconsultklinischradiotherapie_resource = simpy.Resource(env, capacity = 1)
        
        self.zwangerschapsreactiespoed_resource = simpy.Resource(env, capacity = 1)
        
        self.creatinefosfokinasekinetisch_resource = simpy.Resource(env, capacity = 1)
        
        self.ethanolenzymatischofgaschromatografi_resource = simpy.Resource(env, capacity = 1)
        
        self.coloninloop_resource = simpy.Resource(env, capacity = 1)
        
        self.inwendgeneeskjaarkaartkostenout_resource = simpy.Resource(env, capacity = 1)
        
        self.vitamined_resource = simpy.Resource(env, capacity = 1)
        
        self.onderzoekdunnedarmmzduodenum_resource = simpy.Resource(env, capacity = 1)
        
        self.wervelkolomcervicaal_resource = simpy.Resource(env, capacity = 1)
        
        self.ammoniakspoed_resource = simpy.Resource(env, capacity = 1)
        
        self.fenytoinekwantitatief_resource = simpy.Resource(env, capacity = 1)
        
        self.antitrombineiiimbvchromogeennsubstr_resource = simpy.Resource(env, capacity = 1)
        
        self.mrigrotehersenen_resource = simpy.Resource(env, capacity = 1)
        
        self.wervelkolomthoracaal_resource = simpy.Resource(env, capacity = 1)
        
        self.wervelkolomthoracolumbaleovergang_resource = simpy.Resource(env, capacity = 1)
        
        self.toegangschircvdkatheterperifeerb_resource = simpy.Resource(env, capacity = 1)
        
        self.erytrocytenleukocytenverwijderdbestra_resource = simpy.Resource(env, capacity = 1)
        
        self.intercconsultklinischneurologie_resource = simpy.Resource(env, capacity = 1)
        
        self.echogeleidealsassbijpunctiebiopsie_resource = simpy.Resource(env, capacity = 1)
        
        self.pijnbestrijdaanleggenpatientcontroll_resource = simpy.Resource(env, capacity = 1)
        
        self.ctapulmonalis_resource = simpy.Resource(env, capacity = 1)
        
        self.cytologischonderzoekliquorcerebrosp_resource = simpy.Resource(env, capacity = 1)
        
        self.erytrocyten_resource = simpy.Resource(env, capacity = 1)
        
        self.buffycoat_resource = simpy.Resource(env, capacity = 1)
        
        self.klinischtarief_resource = simpy.Resource(env, capacity = 1)
        
        self.cytologischonderzoekdiversen_resource = simpy.Resource(env, capacity = 1)
        
        self.totaaltthyroxineimmunofluorimetris_resource = simpy.Resource(env, capacity = 1)
        
        self.vaginabiopsiepunctiecytologie_resource = simpy.Resource(env, capacity = 1)
        
        self.blaascystoscopie_resource = simpy.Resource(env, capacity = 1)
        
        self.sinus_resource = simpy.Resource(env, capacity = 1)
        
        self.clostridiumelisatest_resource = simpy.Resource(env, capacity = 1)
        
        self.kaliumvlamfotometrisch_resource = simpy.Resource(env, capacity = 1)
        
        self.perifvatenduplexonderzoekveneus_resource = simpy.Resource(env, capacity = 1)
        
        self.dikkedarmappendectomienno_resource = simpy.Resource(env, capacity = 1)
        
        self.intercconsultklinischchirurgie_resource = simpy.Resource(env, capacity = 1)
        
        self.voet_resource = simpy.Resource(env, capacity = 1)
        
        self.cytologischonderzoekurineniercyste_resource = simpy.Resource(env, capacity = 1)
        
        self.schoudergewricht_resource = simpy.Resource(env, capacity = 1)
        
        self.chlorideionselectief_resource = simpy.Resource(env, capacity = 1)
        
        self.antinucleairefactoranf_resource = simpy.Resource(env, capacity = 1)
        
        self.bovenarm_resource = simpy.Resource(env, capacity = 1)
        
        self.vaginascopieinclevtvulvabiops_resource = simpy.Resource(env, capacity = 1)
        
        self.vaginaoverigeexcisiepathologis_resource = simpy.Resource(env, capacity = 1)
        
        self.vulvaruimelokaleexcisievana_resource = simpy.Resource(env, capacity = 1)
        
        self.nierenrenografielasix_resource = simpy.Resource(env, capacity = 1)
        
        self.parathormoonmbvradioisotopen_resource = simpy.Resource(env, capacity = 1)
        
        self.orthopantomogrampanoramixopnamegebit_resource = simpy.Resource(env, capacity = 1)
        
        self.echohalswaaronderschildklier_resource = simpy.Resource(env, capacity = 1)
        
        self.mecabepalingvoormrsambvpcr_resource = simpy.Resource(env, capacity = 1)
        
        self.buikpunctieascitesontlastend_resource = simpy.Resource(env, capacity = 1)
        
        self.uterusextirpatieabdominaalme_resource = simpy.Resource(env, capacity = 1)
        
        self.doxorubicineliposomalcaelyx_resource = simpy.Resource(env, capacity = 1)
        
        self.ctleverengalwegen_resource = simpy.Resource(env, capacity = 1)
        
        self.onderzoekvaneldersnietbeoordeeld_resource = simpy.Resource(env, capacity = 1)
        
        self.cervixconisatie_resource = simpy.Resource(env, capacity = 1)
        
        self.morfometrie_resource = simpy.Resource(env, capacity = 1)
        
        self.bloedgroepbepandersdanaboperbloedg_resource = simpy.Resource(env, capacity = 1)
        
        self.uitsluitenirregulaireastegenerysd_resource = simpy.Resource(env, capacity = 1)
        
        self.punctiecystetumoreddoorradioloogo_resource = simpy.Resource(env, capacity = 1)
        
        self.pyelografieantegraadviapunctie_resource = simpy.Resource(env, capacity = 1)
        
        self.vitamineb_resource = simpy.Resource(env, capacity = 1)
        
        self.vitamineehplcmethode_resource = simpy.Resource(env, capacity = 1)
        
        self.vitaminebthiamine_resource = simpy.Resource(env, capacity = 1)
        
        self.intercconsultvervolgklinischinterne_resource = simpy.Resource(env, capacity = 1)
        
        self.intensivecareligdagetotenmete_resource = simpy.Resource(env, capacity = 1)
        
        self.anesthesiebijvervoerbeademdepatie_resource = simpy.Resource(env, capacity = 1)
        
        self.creatinefosfokinaseisoenzymckmb_resource = simpy.Resource(env, capacity = 1)
        
        self.cvvhdcontinuevenoveneuzehemo_resource = simpy.Resource(env, capacity = 1)
        
        self.intensivecareligdagetotenmet_resource = simpy.Resource(env, capacity = 1)
        
        self.uteruscurettagediagnostisch_resource = simpy.Resource(env, capacity = 1)
        
        self.cervixcurettage_resource = simpy.Resource(env, capacity = 1)
        
        self.buikstaglaparotomomentect_resource = simpy.Resource(env, capacity = 1)
        
        self.echotractusurogenitalisbekken_resource = simpy.Resource(env, capacity = 1)
        
        self.eiwitcolorimetrischtotaal_resource = simpy.Resource(env, capacity = 1)
        
        self.microalbumineimmunonefelometrisch_resource = simpy.Resource(env, capacity = 1)
        
        self.cthals_resource = simpy.Resource(env, capacity = 1)
        
        self.aluminium_resource = simpy.Resource(env, capacity = 1)
        
        self.erytrocytentellenelektronisch_resource = simpy.Resource(env, capacity = 1)
        
        self.duplexscanvenenbeen_resource = simpy.Resource(env, capacity = 1)
        
        self.fshenzymimmunologisch_resource = simpy.Resource(env, capacity = 1)
        
        self.lhmbvradioisotopen_resource = simpy.Resource(env, capacity = 1)
        
        self.progesteronmbvradioisotopen_resource = simpy.Resource(env, capacity = 1)
        
        self.prolactinembveia_resource = simpy.Resource(env, capacity = 1)
        
        self.oestradiolmbvradioisotopenria_resource = simpy.Resource(env, capacity = 1)
        
        self.vrwgeslorgplastischeoperatievanvu_resource = simpy.Resource(env, capacity = 1)
        
        self.testosteronmbvradioisotopen_resource = simpy.Resource(env, capacity = 1)
        
        self.sexhormonebindingglobulinembvria_resource = simpy.Resource(env, capacity = 1)
        
        self.vaginatensionfreevaginaltape_resource = simpy.Resource(env, capacity = 1)
        
        self.vaginacolpocleisislefort_resource = simpy.Resource(env, capacity = 1)
        
        self.gemcitabine_resource = simpy.Resource(env, capacity = 1)
        
        self.buikoverzichtopzaal_resource = simpy.Resource(env, capacity = 1)
        
        self.echografiedopplervenacavainferioren_resource = simpy.Resource(env, capacity = 1)
        
        self.echobeen_resource = simpy.Resource(env, capacity = 1)
        
        self.vitaminea_resource = simpy.Resource(env, capacity = 1)
        
        self.beademinganesthesieeerstedag_resource = simpy.Resource(env, capacity = 1)
        
        self.lymfsyststageringslymfadenectomie_resource = simpy.Resource(env, capacity = 1)
        
        self.widalagglutinatieyersinia_resource = simpy.Resource(env, capacity = 1)
        
        self.dikkedarmcolonoscopiemetbiopsie_resource = simpy.Resource(env, capacity = 1)
        
        self.darmkatheteriserenstoma_resource = simpy.Resource(env, capacity = 1)
        
        self.intercconsultvervolgklinischanesthe_resource = simpy.Resource(env, capacity = 1)
        
        self.hartfunctiegatedbloodpoolrust_resource = simpy.Resource(env, capacity = 1)
        
        self.echografieavueivwzwangerschapmet_resource = simpy.Resource(env, capacity = 1)
        
        self.onderzoekviapercutaneveneuzekatheter_resource = simpy.Resource(env, capacity = 1)
        
        self.echografiedopplervjugularis_resource = simpy.Resource(env, capacity = 1)
        
        self.vendsavenacavainferior_resource = simpy.Resource(env, capacity = 1)
        
        self.antihepatitiscvirusmbvelisa_resource = simpy.Resource(env, capacity = 1)
        
        self.beademinganesthesietweedetmvijf_resource = simpy.Resource(env, capacity = 1)
        
        self.klinischekaartverloskundeengynaeco_resource = simpy.Resource(env, capacity = 1)
        
        self.vulvapartielevulvectomie_resource = simpy.Resource(env, capacity = 1)
        
        self.vrwgeslorgadnexextirpatiedmvlapar_resource = simpy.Resource(env, capacity = 1)
        
        self.zwangerschapsreactie_resource = simpy.Resource(env, capacity = 1)
        
        self.ribsternum_resource = simpy.Resource(env, capacity = 1)
        
        self.intercconsultklinischinterneziekten_resource = simpy.Resource(env, capacity = 1)
        
        self.brachytherapieinterstitieelbijzond_resource = simpy.Resource(env, capacity = 1)
        
        self.osmolaliteit_resource = simpy.Resource(env, capacity = 1)
        
        self.digoxine_resource = simpy.Resource(env, capacity = 1)
        
        self.hepatitiscvirusrochehcvrmbvpcr_resource = simpy.Resource(env, capacity = 1)
        
        self.cervixportiolasercoagulatie_resource = simpy.Resource(env, capacity = 1)
        
        self.vaginascopieexclweefselwegname_resource = simpy.Resource(env, capacity = 1)
        
        self.cytologischonderzoekpleuravocht_resource = simpy.Resource(env, capacity = 1)
        
        self.huidplastiekzplastiekhuidhoofdenh_resource = simpy.Resource(env, capacity = 1)
        
        self.cttotalelichaam_resource = simpy.Resource(env, capacity = 1)
        
        self.pyelografieretrograad_resource = simpy.Resource(env, capacity = 1)
        
        self.echopancreasenmilt_resource = simpy.Resource(env, capacity = 1)
        
        self.brainnatriureticpeptidebnpmbvimmu_resource = simpy.Resource(env, capacity = 1)
        
        self.duodenumoesofagogastroduodenoscopi_resource = simpy.Resource(env, capacity = 1)
        
        self.intercconsultklinischurologie_resource = simpy.Resource(env, capacity = 1)
        
        self.darmcolonpassagescintcompstatisch_resource = simpy.Resource(env, capacity = 1)
        
        self.echoenrontgenalsassbijdrainageab_resource = simpy.Resource(env, capacity = 1)
        
        self.gentamycinekwnimmunoassay_resource = simpy.Resource(env, capacity = 1)
        
        self.echothorax_resource = simpy.Resource(env, capacity = 1)
        
        self.rogelalsassbijpunktiebiopsiet_resource = simpy.Resource(env, capacity = 1)
        
        self.onderznaaraanwezigheidvankoudeanti_resource = simpy.Resource(env, capacity = 1)
        
        self.gebantistoffentegenerysdircoombs_resource = simpy.Resource(env, capacity = 1)
        
        self.gebantistoffentegenerysdircoomb_resource = simpy.Resource(env, capacity = 1)
        
        self.ovariumredebulkingovariumcarcin_resource = simpy.Resource(env, capacity = 1)
        
        self.ovariumexcisiecystevialaparosc_resource = simpy.Resource(env, capacity = 1)
        
        self.behandeleninhyperpressietank_resource = simpy.Resource(env, capacity = 1)
        
        self.perifvatendoppleronderzoppervlven_resource = simpy.Resource(env, capacity = 1)
        
        self.perifvatenduplexscanarterieelcruro_resource = simpy.Resource(env, capacity = 1)
        
        self.buiksecondlookoperstagering_resource = simpy.Resource(env, capacity = 1)
        
        self.elutievanautoantistoffentegenerytro_resource = simpy.Resource(env, capacity = 1)
        
        self.bloedgroepbepalingandersdanabokidd_resource = simpy.Resource(env, capacity = 1)
        
        self.buikexcisiepathologafwijking_resource = simpy.Resource(env, capacity = 1)
        
        self.hydroxyprogesteronmbvria_resource = simpy.Resource(env, capacity = 1)
        
        self.deltaandrosteendion_resource = simpy.Resource(env, capacity = 1)
        
        self.dheasulfaatmetextractiembvria_resource = simpy.Resource(env, capacity = 1)
        
        self.enkel_resource = simpy.Resource(env, capacity = 1)
        
        self.vrwgeslorgaspiratieofmicrocurett_resource = simpy.Resource(env, capacity = 1)
        
        self.bronchusbronchtoiletdoorverpl_resource = simpy.Resource(env, capacity = 1)
        
        self.immunoglobulineaiga_resource = simpy.Resource(env, capacity = 1)
        
        self.heparineantixa_resource = simpy.Resource(env, capacity = 1)
        
        self.rogelalsassbijdrainageniernefro_resource = simpy.Resource(env, capacity = 1)
        
        self.echonier_resource = simpy.Resource(env, capacity = 1)
        
        self.occultbloedkwalitatief_resource = simpy.Resource(env, capacity = 1)
        
        self.echobuikwand_resource = simpy.Resource(env, capacity = 1)
        
        self.cytologischonderzoekbuiktumorpunctie_resource = simpy.Resource(env, capacity = 1)
        
        self.buikomentumplastiek_resource = simpy.Resource(env, capacity = 1)
        
        self.ctnier_resource = simpy.Resource(env, capacity = 1)
        
        self.cytologischonderzoekleverpunctie_resource = simpy.Resource(env, capacity = 1)
        
        self.hartresuscitatie_resource = simpy.Resource(env, capacity = 1)
        
        self.uterusextirpatieabdomtotaalme_resource = simpy.Resource(env, capacity = 1)
        
        self.vrwgeslorgadhesiolysisovariumplus_resource = simpy.Resource(env, capacity = 1)
        
        self.cytologischonderzoekvulva_resource = simpy.Resource(env, capacity = 1)
        
        self.ctretroperitoneum_resource = simpy.Resource(env, capacity = 1)
        
        self.antihavigofiggelisaofriaineen_resource = simpy.Resource(env, capacity = 1)
        
        self.antisttegenhepatitisbsurfaceantigee_resource = simpy.Resource(env, capacity = 1)
        
        self.hepatitisbanticoreigm_resource = simpy.Resource(env, capacity = 1)
        
        self.buiklittekenbreukplastische_resource = simpy.Resource(env, capacity = 1)
        
        self.vaginaoperatievesicovaginalefi_resource = simpy.Resource(env, capacity = 1)
        
        self.vulvahechtenvanvulva_resource = simpy.Resource(env, capacity = 1)
        
        self.mycobacteriummbvpcr_resource = simpy.Resource(env, capacity = 1)
        
        self.huidtranscutanepoenpcome_resource = simpy.Resource(env, capacity = 1)
        
        self.glucosebepalingkwantitatief_resource = simpy.Resource(env, capacity = 1)
        
        self.ctgelalsassbijpunctiebiopsiei_resource = simpy.Resource(env, capacity = 1)
        
        self.cytologischonderzoekendocervix_resource = simpy.Resource(env, capacity = 1)
        
        self.oestronmbvradioisotopen_resource = simpy.Resource(env, capacity = 1)
        
        self.lymfsystlymfadenectomiedmvlaparo_resource = simpy.Resource(env, capacity = 1)
        
        self.cytostaticainfuustherapie_resource = simpy.Resource(env, capacity = 1)
        
        self.echogeleidealsassbijdrainageintrap_resource = simpy.Resource(env, capacity = 1)
        
        self.rituximab_resource = simpy.Resource(env, capacity = 1)
        
        self.vaginavaginotomie_resource = simpy.Resource(env, capacity = 1)
        
        self.echografieavueivmzwangerschaprout_resource = simpy.Resource(env, capacity = 1)
        
        self.blaasvoorsteenachtersteexent_resource = simpy.Resource(env, capacity = 1)
        
        self.uretersplintografiecqopspuitenuret_resource = simpy.Resource(env, capacity = 1)
        
        self.blaasbladderwashout_resource = simpy.Resource(env, capacity = 1)
        
        self.duodenuminbrengenvoedingssondein_resource = simpy.Resource(env, capacity = 1)
        
        self.emgelektromyografischonderzo_resource = simpy.Resource(env, capacity = 1)
        
        self.kniemzonderbeen_resource = simpy.Resource(env, capacity = 1)
        
        self.ctarterienhersenen_resource = simpy.Resource(env, capacity = 1)
        
        self.iggantistoffentegenheparinepfcompl_resource = simpy.Resource(env, capacity = 1)
        
        self.abortusoverigetechnieken_resource = simpy.Resource(env, capacity = 1)
        
        self.echografietransuretraalprostaat_resource = simpy.Resource(env, capacity = 1)
        
        self.eiwitspectrumelektroforesekwnbepf_resource = simpy.Resource(env, capacity = 1)
        
        self.immunoglobulinegigg_resource = simpy.Resource(env, capacity = 1)
        
        self.immunoglobulinemigm_resource = simpy.Resource(env, capacity = 1)
        
        self.paraproteinetyperingmbvmonospecifieke_resource = simpy.Resource(env, capacity = 1)
        
        self.eiwitfractioneringmbvief_resource = simpy.Resource(env, capacity = 1)
        
        self.immunofixatie_resource = simpy.Resource(env, capacity = 1)
        
        self.immunoforesenaconcentratie_resource = simpy.Resource(env, capacity = 1)
        
        self.drainageprocedureonderrontgencontrole_resource = simpy.Resource(env, capacity = 1)
        
        self.antigeendetectiedirectpreparaaths_resource = simpy.Resource(env, capacity = 1)
        
        self.antigeendetectiedirectpreparaatvz_resource = simpy.Resource(env, capacity = 1)
        
        self.nietdeclarabeledagverplegingbvklinp_resource = simpy.Resource(env, capacity = 1)
        
        self.intercconsultklinischreumatologie_resource = simpy.Resource(env, capacity = 1)
        
        self.anticytomegalovirusigofiggelisa_resource = simpy.Resource(env, capacity = 1)
        
        self.igmastegencmvvirus_resource = simpy.Resource(env, capacity = 1)
        
        self.antiepsteinbarrvcaigmmbvelisa_resource = simpy.Resource(env, capacity = 1)
        
        self.antiepsteinbarrnaiggmbvelisa_resource = simpy.Resource(env, capacity = 1)
        
        self.antiepsteinbarrvcaiggmbvelisa_resource = simpy.Resource(env, capacity = 1)
        
        self.complementcomponentckwn_resource = simpy.Resource(env, capacity = 1)
        
        self.dnafarrassaymbvria_resource = simpy.Resource(env, capacity = 1)
        
        self.legionellaantigeensneltest_resource = simpy.Resource(env, capacity = 1)
        
        self.complementdeficientieondbijafwezigha_resource = simpy.Resource(env, capacity = 1)
        
        self.longfunctiespirometrie_resource = simpy.Resource(env, capacity = 1)
        
        self.longfunctiestroomvolumecurve_resource = simpy.Resource(env, capacity = 1)
        
        self.sacrumoscoccygissigewrichten_resource = simpy.Resource(env, capacity = 1)
        
        self.proteinecactiviteit_resource = simpy.Resource(env, capacity = 1)
        
        self.igmanticardiolipinembvelisa_resource = simpy.Resource(env, capacity = 1)
        
        self.igganticardiolipinembvelisa_resource = simpy.Resource(env, capacity = 1)
        
        self.antistspecifiekmbvelisahistonenof_resource = simpy.Resource(env, capacity = 1)
        
        self.stollingsfactorviiiactiviteit_resource = simpy.Resource(env, capacity = 1)
        
        self.anticoagulanslupusmbvelisa_resource = simpy.Resource(env, capacity = 1)
        
        self.proteinesantigeentotaal_resource = simpy.Resource(env, capacity = 1)
        
        self.proteinesantigeenvrij_resource = simpy.Resource(env, capacity = 1)
        
        self.factoriimutatiembvpcr_resource = simpy.Resource(env, capacity = 1)
        
        self.factorvleidenrqmbvdnatest_resource = simpy.Resource(env, capacity = 1)
        
        self.lymfsystlymfekliertoiletdiepli_resource = simpy.Resource(env, capacity = 1)
        
        self.tubauterinaexcisieparovarialecyste_resource = simpy.Resource(env, capacity = 1)
        
        self.echobovenbeen_resource = simpy.Resource(env, capacity = 1)
        
        self.phmeting_resource = simpy.Resource(env, capacity = 1)
        
        self.spraakaudiometriestandaardaudiol_resource = simpy.Resource(env, capacity = 1)
        
        self.mandibulakaakgewricht_resource = simpy.Resource(env, capacity = 1)
        
        self.mriorbita_resource = simpy.Resource(env, capacity = 1)
        
        self.highsensitivecrphscrpnefelometrisc_resource = simpy.Resource(env, capacity = 1)
        
        self.echoarteriaecarotissinistra_resource = simpy.Resource(env, capacity = 1)
        
        self.echoarteriaecarotisdextra_resource = simpy.Resource(env, capacity = 1)
        
        self.bloedstollingsfactorxiactiviteit_resource = simpy.Resource(env, capacity = 1)
        
        self.bloedstollingsfactorxiiactiviteit_resource = simpy.Resource(env, capacity = 1)
        
        self.bloedstollingsfactorixcoagulatie_resource = simpy.Resource(env, capacity = 1)
        
        self.uterusexcisiedestructiepathaf_resource = simpy.Resource(env, capacity = 1)
        
        self.hyperthermiebehandelingh_resource = simpy.Resource(env, capacity = 1)
        
        self.inbrengenvoedingsoflavagesondeduode_resource = simpy.Resource(env, capacity = 1)
        
        self.echopleura_resource = simpy.Resource(env, capacity = 1)
        
        self.pleurapunctiediagnostisch_resource = simpy.Resource(env, capacity = 1)
        
        self.alfaamylase_resource = simpy.Resource(env, capacity = 1)
        
        self.vancomycinekwnimmunoassay_resource = simpy.Resource(env, capacity = 1)
        
        self.intercconsultvervolgklinischchirurg_resource = simpy.Resource(env, capacity = 1)
        
        self.echografiedopplervenenbeen_resource = simpy.Resource(env, capacity = 1)
        
        self.mictiecystouretrografie_resource = simpy.Resource(env, capacity = 1)
        
        self.totalegebitsstatus_resource = simpy.Resource(env, capacity = 1)
        
        self.vrwgeslorgadhesiolysisovariatubae_resource = simpy.Resource(env, capacity = 1)
        
        self.ctpancreasenmilt_resource = simpy.Resource(env, capacity = 1)
        
        self.doorlichtingzonderopnamebuik_resource = simpy.Resource(env, capacity = 1)
        
        self.echogeleidealsassbijpunctieabdomen_resource = simpy.Resource(env, capacity = 1)
        
        self.cytologischonderzoektbvbevolkingsonde_resource = simpy.Resource(env, capacity = 1)
        
        self.bloedstollingsfactorvkwantitatief_resource = simpy.Resource(env, capacity = 1)
        
        self.bloedstollingsfactorviicoagulatie_resource = simpy.Resource(env, capacity = 1)
        
        self.vonwillebrandprofielmbvprotease_resource = simpy.Resource(env, capacity = 1)
        
        self.cytologischonderzoekschildklierpun_resource = simpy.Resource(env, capacity = 1)
        
        self.uterusextirpatievaginaaltotaal_resource = simpy.Resource(env, capacity = 1)
        
        self.nucleaironderzoekvanelders_resource = simpy.Resource(env, capacity = 1)
        
        self.unknown_resource = simpy.Resource(env, capacity = 1)
        
        self.peritoneumomentectomie_resource = simpy.Resource(env, capacity = 1)
        
        self.vulvatherapeutischepunctieaan_resource = simpy.Resource(env, capacity = 1)
        
        self.urethradilatatiemeatus_resource = simpy.Resource(env, capacity = 1)
        
        self.antisttegenacetylcholinereceptoren_resource = simpy.Resource(env, capacity = 1)
        
        self.aspectsupernatant_resource = simpy.Resource(env, capacity = 1)
        
        self.infuusbloed_resource = simpy.Resource(env, capacity = 1)
        
        self.thoraxzuigdrainagebehandelinga_resource = simpy.Resource(env, capacity = 1)
        
        self.ovariumovariopexieexcltorsie_resource = simpy.Resource(env, capacity = 1)
        
        self.prostaatspecifiekantigeenpsambvimm_resource = simpy.Resource(env, capacity = 1)
        
        self.antisttegenhiveofhivc_resource = simpy.Resource(env, capacity = 1)
        
        self.directondznaarrsvirusantigeenmbv_resource = simpy.Resource(env, capacity = 1)
        
        self.parainfluenzavirusmbvpcr_resource = simpy.Resource(env, capacity = 1)
        
        self.humaanmetapneumoviruskwlmbvdnarna_resource = simpy.Resource(env, capacity = 1)
        
        self.antigeendetectiembviftinfluenzaa_resource = simpy.Resource(env, capacity = 1)
        
        self.antigeendetectiembviftinfluenzab_resource = simpy.Resource(env, capacity = 1)
        
        self.buiklaparoscopiediagnostisc_resource = simpy.Resource(env, capacity = 1)
        
        self.wormeierenuitgebreidvervolg_resource = simpy.Resource(env, capacity = 1)
        
        self.zink_resource = simpy.Resource(env, capacity = 1)
        
        self.vrwgeslorgoperatievanclitorisnno_resource = simpy.Resource(env, capacity = 1)
        
        self.opnamevolgensbarsonie_resource = simpy.Resource(env, capacity = 1)
        
        self.lymfsystlymfeklierextirpatiepara_resource = simpy.Resource(env, capacity = 1)
        
        self.uterusextirpabdvagradlymfa_resource = simpy.Resource(env, capacity = 1)
        
        self.buikoverzichtstaand_resource = simpy.Resource(env, capacity = 1)
        
        self.dunnedarmmechileusadhesstrengi_resource = simpy.Resource(env, capacity = 1)
        
        self.cytologischonderzoekhersenen_resource = simpy.Resource(env, capacity = 1)
        
        self.antirubellaiggelisaineenmonster_resource = simpy.Resource(env, capacity = 1)
        
        self.antichlamydiaigambvelisa_resource = simpy.Resource(env, capacity = 1)
        
        self.antichlamydiaiggmbvindift_resource = simpy.Resource(env, capacity = 1)
        
        self.buikadhesiolyseenbiopsiedmv_resource = simpy.Resource(env, capacity = 1)
        
        self.endoretrogradecholangiografie_resource = simpy.Resource(env, capacity = 1)
        
        self.cystografieretrograad_resource = simpy.Resource(env, capacity = 1)
        
        self.doorlichtingbijniersteenvergruizing_resource = simpy.Resource(env, capacity = 1)
        
        self.wisselendrainonderrontgencontrole_resource = simpy.Resource(env, capacity = 1)
        
        self.kleurproefsabinfeldmanleishmania_resource = simpy.Resource(env, capacity = 1)
        
        self.toxoplasmosembveiatoxoigg_resource = simpy.Resource(env, capacity = 1)
        
        self.toxoplasmosembveiatoxoigm_resource = simpy.Resource(env, capacity = 1)
        
        self.antirubellaigmelisa_resource = simpy.Resource(env, capacity = 1)
        
        self.cbrcoxsackiebvirus_resource = simpy.Resource(env, capacity = 1)
        
        self.antiparvovirusigofiggantistind_resource = simpy.Resource(env, capacity = 1)
        
        self.antiparvovirusigmmbvindift_resource = simpy.Resource(env, capacity = 1)
        
        self.tubauterinaaanbrengenclipstijdensl_resource = simpy.Resource(env, capacity = 1)
        
        self.partusklinofpoliklinmetvoorb_resource = simpy.Resource(env, capacity = 1)
        
        self.sectcaesarmetvoorbehandelingenkra_resource = simpy.Resource(env, capacity = 1)
        
        self.mritractusurogenitalis_resource = simpy.Resource(env, capacity = 1)
        
        self.opspuitenhickmankatheter_resource = simpy.Resource(env, capacity = 1)
        
        self.rogelalsassbijpunctiebiopsiel_resource = simpy.Resource(env, capacity = 1)
        
        self.lymfsystregionalelymfeklierdissec_resource = simpy.Resource(env, capacity = 1)
        
        self.dtoegangschircvdcatheterv_resource = simpy.Resource(env, capacity = 1)
        
        self.hemoglobinenabnormaalinclhba_resource = simpy.Resource(env, capacity = 1)
        
        self.iggindex_resource = simpy.Resource(env, capacity = 1)
        
        self.albumineratio_resource = simpy.Resource(env, capacity = 1)
        
        self.immunoelektroforeseliquornaconcentra_resource = simpy.Resource(env, capacity = 1)
        
        self.huidverwijderenretentiecyste_resource = simpy.Resource(env, capacity = 1)
        
        self.rogelalsassbijinbrengenendoproth_resource = simpy.Resource(env, capacity = 1)
        
        self.leverexcisietumorofmetastase_resource = simpy.Resource(env, capacity = 1)
        
        self.lymfsystsentinelnodeprocedureli_resource = simpy.Resource(env, capacity = 1)
        
        self.gipskamerokgebruik_resource = simpy.Resource(env, capacity = 1)
        
        self.standaardmateriaalnno_resource = simpy.Resource(env, capacity = 1)
        
        self.zwachtelverbandslingaanleggen_resource = simpy.Resource(env, capacity = 1)
        
        self.partielegebitsstatus_resource = simpy.Resource(env, capacity = 1)
        
        self.intercconsultpoliklinisch_resource = simpy.Resource(env, capacity = 1)
        
        self.vrwgeslorgsecondlookoperovariumca_resource = simpy.Resource(env, capacity = 1)
        
        self.oesofagografieoraal_resource = simpy.Resource(env, capacity = 1)
        
        self.ohvitaminedmbvhplc_resource = simpy.Resource(env, capacity = 1)
        
        self.perifvatenverwijderenportacath_resource = simpy.Resource(env, capacity = 1)
        
        self.perifvateninbrengenportacathsyst_resource = simpy.Resource(env, capacity = 1)
        
        self.rontgenonderzoekonvolledig_resource = simpy.Resource(env, capacity = 1)
        
        self.mriartenvenabdomen_resource = simpy.Resource(env, capacity = 1)
        
        self.vaginaextirpatievanvaginamet_resource = simpy.Resource(env, capacity = 1)
        
        self.neuronspecifiekenolase_resource = simpy.Resource(env, capacity = 1)
        
        self.ctknie_resource = simpy.Resource(env, capacity = 1)
        
        self.tubauterinareanastomosenasterilisat_resource = simpy.Resource(env, capacity = 1)
        
        self.obductie_resource = simpy.Resource(env, capacity = 1)
        
        self.anesthesieepiduraalmetbloedpatch_resource = simpy.Resource(env, capacity = 1)
        
        self.dikkedarmresectiesigmoidmetprima_resource = simpy.Resource(env, capacity = 1)
        
        self.dikkedarmappendectomieacuutviame_resource = simpy.Resource(env, capacity = 1)
        
        self.totaalttrijoodthyroninembvradiois_resource = simpy.Resource(env, capacity = 1)
        
        self.tuptakelatentebindingscapgebtbg_resource = simpy.Resource(env, capacity = 1)
        
        self.echobekkeninhoudmuvanatomiecodet_resource = simpy.Resource(env, capacity = 1)
        
        self.uterustotlaparoscopischehyste_resource = simpy.Resource(env, capacity = 1)
        
        self.plaatsenvanvcavafilter_resource = simpy.Resource(env, capacity = 1)
        
        self.eerstehulpnietsehafdelingelders_resource = simpy.Resource(env, capacity = 1)
        
        self.buiksecondlookoperovariumca_resource = simpy.Resource(env, capacity = 1)
        
        self.itraconazolmbvhplc_resource = simpy.Resource(env, capacity = 1)
        
        self.bepalinghepatitisbeantigeen_resource = simpy.Resource(env, capacity = 1)
        
        self.bepalingantisthepatitisbeantigeen_resource = simpy.Resource(env, capacity = 1)
        
    
    
    def econsultpoliklinisch(self):
            yield self.env.timeout(2) 
    
    def administratieftariefeerstepol(self):
            yield self.env.timeout(2) 
    
    def verloskgynaeckortekaartkostenout(self):
            yield self.env.timeout(2) 
    
    def echografiegenitaliainterna(self):
            yield self.env.timeout(2) 
    
    def simulatorgebruikvooraanvangmegavol(self):
            yield self.env.timeout(2) 
    
    def behandeltijdeenheidtmegavolt(self):
            yield self.env.timeout(2) 
    
    def teletherapiemegavoltfotonenbestrali(self):
            yield self.env.timeout(2) 
    
    def aannamelaboratoriumonderzoek(self):
            yield self.env.timeout(2) 
    
    def ureum(self):
            yield self.env.timeout(2) 
    
    def hemoglobinefotoelektrisch(self):
            yield self.env.timeout(2) 
    
    def creatinine(self):
            yield self.env.timeout(2) 
    
    def natriumvlamfotometrisch(self):
            yield self.env.timeout(2) 
    
    def kaliumpotentiometrisch(self):
            yield self.env.timeout(2) 
    
    def leukocytentellenelektronisch(self):
            yield self.env.timeout(2) 
    
    def trombocytentellenelektronisch(self):
            yield self.env.timeout(2) 
    
    def ordertarief(self):
            yield self.env.timeout(2) 
    
    def ligdagenallespecbehkindergreval(self):
            yield self.env.timeout(2) 
    
    def sedimentspoed(self):
            yield self.env.timeout(2) 
    
    def bacteriologischonderzoekmetkweeknie(self):
            yield self.env.timeout(2) 
    
    def resistentiebepalingenbepalingen(self):
            yield self.env.timeout(2) 
    
    def hepatitisbsurfaceantigeenconfirmatie(self):
            yield self.env.timeout(2) 
    
    def urineonderzoekkwalitatief(self):
            yield self.env.timeout(2) 
    
    def klinischeopnamea(self):
            yield self.env.timeout(2) 
    
    def klasseba(self):
            yield self.env.timeout(2) 
    
    def sgotasatkinetisch(self):
            yield self.env.timeout(2) 
    
    def sgptalatkinetisch(self):
            yield self.env.timeout(2) 
    
    def melkzuurdehydrogenaseldhkinetisch(self):
            yield self.env.timeout(2) 
    
    def differentieletellingautomatisch(self):
            yield self.env.timeout(2) 
    
    def trombotest(self):
            yield self.env.timeout(2) 
    
    def crpcreactiefproteine(self):
            yield self.env.timeout(2) 
    
    def brachytherapieinterstitieelintensi(self):
            yield self.env.timeout(2) 
    
    def inwendgeneeskkortekaartkostenout(self):
            yield self.env.timeout(2) 
    
    def vervolgconsultpoliklinisch(self):
            yield self.env.timeout(2) 
    
    def creatininespoed(self):
            yield self.env.timeout(2) 
    
    def ijzer(self):
            yield self.env.timeout(2) 
    
    def natriumvlamfotometrischspoed(self):
            yield self.env.timeout(2) 
    
    def kaliumvlamfotometrischspoed(self):
            yield self.env.timeout(2) 
    
    def foliumzuurmbvradioisotopen(self):
            yield self.env.timeout(2) 
    
    def vitaminebmbvchemieluminescentie(self):
            yield self.env.timeout(2) 
    
    def bloedgroepaboenrhesusfactor(self):
            yield self.env.timeout(2) 
    
    def rhesusfactordcentrifugeermethodee(self):
            yield self.env.timeout(2) 
    
    def haemoglobinefotoelectrischspoed(self):
            yield self.env.timeout(2) 
    
    def trombocytentellenspoed(self):
            yield self.env.timeout(2) 
    
    def reticulocytentellenmbvfacscan(self):
            yield self.env.timeout(2) 
    
    def cdefenotypering(self):
            yield self.env.timeout(2) 
    
    def bloedgroepantigenenanderedanaborhesu(self):
            yield self.env.timeout(2) 
    
    def kruisproefvolledigdriemethoden(self):
            yield self.env.timeout(2) 
    
    def leucocytentellenelectronischspoed(self):
            yield self.env.timeout(2) 
    
    def crpcreactiefproteinespoed(self):
            yield self.env.timeout(2) 
    
    def screeningantistoffenerytrocyten(self):
            yield self.env.timeout(2) 
    
    def transferrinembvics(self):
            yield self.env.timeout(2) 
    
    def bovenregtoesla(self):
            yield self.env.timeout(2) 
    
    def gefiltreerderytrocytenconcentraat(self):
            yield self.env.timeout(2) 
    
    def echonierenurinewegen(self):
            yield self.env.timeout(2) 
    
    def intercconsultklinischanesthesie(self):
            yield self.env.timeout(2) 
    
    def ureumspoed(self):
            yield self.env.timeout(2) 
    
    def sgptalatkinetischspoed(self):
            yield self.env.timeout(2) 
    
    def sgotasatkinetischspoed(self):
            yield self.env.timeout(2) 
    
    def internationalnormalisedratiombvtromb(self):
            yield self.env.timeout(2) 
    
    def dagverplegingallespecbehkindrev(self):
            yield self.env.timeout(2) 
    
    def dagverpleginga(self):
            yield self.env.timeout(2) 
    
    def urinezuurmeturicaseuvspectrofotome(self):
            yield self.env.timeout(2) 
    
    def melkzuurdehydrogenasespoed(self):
            yield self.env.timeout(2) 
    
    def echoabdomen(self):
            yield self.env.timeout(2) 
    
    def sediment(self):
            yield self.env.timeout(2) 
    
    def klinischekaartinwendigegeneeskunde(self):
            yield self.env.timeout(2) 
    
    def inwendgeneeskaanvkaartkostenout(self):
            yield self.env.timeout(2) 
    
    def squamouscellcarcinomambveia(self):
            yield self.env.timeout(2) 
    
    def ctabdomen(self):
            yield self.env.timeout(2) 
    
    def cambvmeia(self):
            yield self.env.timeout(2) 
    
    def telefonischconsult(self):
            yield self.env.timeout(2) 
    
    def patientnietverschenenradiologie(self):
            yield self.env.timeout(2) 
    
    def homocystinechromatografisch(self):
            yield self.env.timeout(2) 
    
    def cytologischonderzoekectocervix(self):
            yield self.env.timeout(2) 
    
    def bilirubinegeconjugeerd(self):
            yield self.env.timeout(2) 
    
    def bilirubinetotaal(self):
            yield self.env.timeout(2) 
    
    def glucose(self):
            yield self.env.timeout(2) 
    
    def alkalischefosfatasekinetisch(self):
            yield self.env.timeout(2) 
    
    def gammaglutamyltranspeptidase(self):
            yield self.env.timeout(2) 
    
    def ceatumormarkermbvmeia(self):
            yield self.env.timeout(2) 
    
    def calcium(self):
            yield self.env.timeout(2) 
    
    def albumine(self):
            yield self.env.timeout(2) 
    
    def thorax(self):
            yield self.env.timeout(2) 
    
    def klasseaa(self):
            yield self.env.timeout(2) 
    
    def buikstaglaptumorredomentec(self):
            yield self.env.timeout(2) 
    
    def immunopathologischonderzoek(self):
            yield self.env.timeout(2) 
    
    def cytologischonderzoekascites(self):
            yield self.env.timeout(2) 
    
    def histologischonderzoekgroteresectiep(self):
            yield self.env.timeout(2) 
    
    def glucosespoed(self):
            yield self.env.timeout(2) 
    
    def calciumspoed(self):
            yield self.env.timeout(2) 
    
    def melkzuurenzymatischspoed(self):
            yield self.env.timeout(2) 
    
    def osaturatie(self):
            yield self.env.timeout(2) 
    
    def ctthorax(self):
            yield self.env.timeout(2) 
    
    def verloskgynaecaanvkaartkostenout(self):
            yield self.env.timeout(2) 
    
    def hematocrietmbvcentrifuge(self):
            yield self.env.timeout(2) 
    
    def totaaleiwit(self):
            yield self.env.timeout(2) 
    
    def vulvaradvulvectomieoppend(self):
            yield self.env.timeout(2) 
    
    def microscopischonderzoekgekleurdenon(self):
            yield self.env.timeout(2) 
    
    def coupeterinzage(self):
            yield self.env.timeout(2) 
    
    def mribekken(self):
            yield self.env.timeout(2) 
    
    def skeletscintigrafietotalelichaam(self):
            yield self.env.timeout(2) 
    
    def histologischonderzoekbioptennno(self):
            yield self.env.timeout(2) 
    
    def citohistologischonderzoek(self):
            yield self.env.timeout(2) 
    
    def fosfaat(self):
            yield self.env.timeout(2) 
    
    def ctbovenbuik(self):
            yield self.env.timeout(2) 
    
    def blaasuretrocystoscopienno(self):
            yield self.env.timeout(2) 
    
    def vaginatoucheronderanesthesie(self):
            yield self.env.timeout(2) 
    
    def wervelkolomlumbaal(self):
            yield self.env.timeout(2) 
    
    def cthersenen(self):
            yield self.env.timeout(2) 
    
    def differentiatieleukocytenhandmatig(self):
            yield self.env.timeout(2) 
    
    def anesthesiebijbehandelingmetradium(self):
            yield self.env.timeout(2) 
    
    def albuminespoed(self):
            yield self.env.timeout(2) 
    
    def bilirubinekwantitatieftotaalofdirect(self):
            yield self.env.timeout(2) 
    
    def alfaamylasespoed(self):
            yield self.env.timeout(2) 
    
    def chloridespoed(self):
            yield self.env.timeout(2) 
    
    def fosfaatspoed(self):
            yield self.env.timeout(2) 
    
    def alkalischefosfatasekinetischspoed(self):
            yield self.env.timeout(2) 
    
    def totaaleiwitcolorimetrischspoed(self):
            yield self.env.timeout(2) 
    
    def kreatininefosfokinasespoed(self):
            yield self.env.timeout(2) 
    
    def hematocrietspoed(self):
            yield self.env.timeout(2) 
    
    def gammaglutamyltranspeptidasespoed(self):
            yield self.env.timeout(2) 
    
    def ferritinekwnmbvchemieluminescentie(self):
            yield self.env.timeout(2) 
    
    def erythrocytentellenelectronischspoed(self):
            yield self.env.timeout(2) 
    
    def osmolaliteitspoed(self):
            yield self.env.timeout(2) 
    
    def bezinkingssnelheidfotoelektrisch(self):
            yield self.env.timeout(2) 
    
    def magnesiumaasspoed(self):
            yield self.env.timeout(2) 
    
    def mriwervelkolomcervicaal(self):
            yield self.env.timeout(2) 
    
    def mriwervelkolomthoracaal(self):
            yield self.env.timeout(2) 
    
    def mriwervelkolomlumbaal(self):
            yield self.env.timeout(2) 
    
    def cortisolimmunofluorimetrisch(self):
            yield self.env.timeout(2) 
    
    def tshenzymimmunologisch(self):
            yield self.env.timeout(2) 
    
    def cortisol(self):
            yield self.env.timeout(2) 
    
    def vatenvenapunctie(self):
            yield self.env.timeout(2) 
    
    def acthmbvradioisotopen(self):
            yield self.env.timeout(2) 
    
    def ecgelektrocardiografie(self):
            yield self.env.timeout(2) 
    
    def lithium(self):
            yield self.env.timeout(2) 
    
    def vrijtmbvriaft(self):
            yield self.env.timeout(2) 
    
    def econsultbezoek(self):
            yield self.env.timeout(2) 
    
    def lymfeklierscintsentinelnodedynamis(self):
            yield self.env.timeout(2) 
    
    def lymfeklierscintsentinelnodevervolg(self):
            yield self.env.timeout(2) 
    
    def lymfeklierscintsentinelnodemetpro(self):
            yield self.env.timeout(2) 
    
    def vulvaradicalevulvectzndingu(self):
            yield self.env.timeout(2) 
    
    def vriescoupe(self):
            yield self.env.timeout(2) 
    
    def methemoglobinesulfhemoglobineelk(self):
            yield self.env.timeout(2) 
    
    def bicarbonaat(self):
            yield self.env.timeout(2) 
    
    def cohbkwn(self):
            yield self.env.timeout(2) 
    
    def actuelephpcostandbicarbonaat(self):
            yield self.env.timeout(2) 
    
    def lithiumspoed(self):
            yield self.env.timeout(2) 
    
    def verloskgynaecjaarkaartkostenout(self):
            yield self.env.timeout(2) 
    
    def histologischonderzoekkleineresectie(self):
            yield self.env.timeout(2) 
    
    def vrwgeslorgbiopsiepunctiecytologie(self):
            yield self.env.timeout(2) 
    
    def buikoverzicht(self):
            yield self.env.timeout(2) 
    
    def klinischekaartanesthesie(self):
            yield self.env.timeout(2) 
    
    def arteriepunctietbvverblijfsnaald(self):
            yield self.env.timeout(2) 
    
    def thoraxopzaal(self):
            yield self.env.timeout(2) 
    
    def protrombinetijdquickowrenofmodif(self):
            yield self.env.timeout(2) 
    
    def heparinebepalingkaolinecefalinetij(self):
            yield self.env.timeout(2) 
    
    def intercconsultklinischlongziekten(self):
            yield self.env.timeout(2) 
    
    def dieetnno(self):
            yield self.env.timeout(2) 
    
    def buikprimairestageringsoperati(self):
            yield self.env.timeout(2) 
    
    def antihivmbvelisa(self):
            yield self.env.timeout(2) 
    
    def patientnietverschenenngivnoshow(self):
            yield self.env.timeout(2) 
    
    def infuusinbrengen(self):
            yield self.env.timeout(2) 
    
    def cytologischonderzoekvagina(self):
            yield self.env.timeout(2) 
    
    def tumorpetscantotalelichaam(self):
            yield self.env.timeout(2) 
    
    def blaascystoscopiemetbiopsie(self):
            yield self.env.timeout(2) 
    
    def cytologischonderzoeklymfeklierpuncti(self):
            yield self.env.timeout(2) 
    
    def diagnostischepunctieonderechocontrole(self):
            yield self.env.timeout(2) 
    
    def echoschoudermzbovenarm(self):
            yield self.env.timeout(2) 
    
    def cytologischonderzoekpancreaspunctie(self):
            yield self.env.timeout(2) 
    
    def echobovenbuik(self):
            yield self.env.timeout(2) 
    
    def hyperthermie(self):
            yield self.env.timeout(2) 
    
    def helebovenbeenmetonderbeenenvoet(self):
            yield self.env.timeout(2) 
    
    def magnesiumaas(self):
            yield self.env.timeout(2) 
    
    def bekken(self):
            yield self.env.timeout(2) 
    
    def bekkenliggend(self):
            yield self.env.timeout(2) 
    
    def fdpdimeerimmunologisch(self):
            yield self.env.timeout(2) 
    
    def ctartenvenpulmonales(self):
            yield self.env.timeout(2) 
    
    def paclitaxel(self):
            yield self.env.timeout(2) 
    
    def chloride(self):
            yield self.env.timeout(2) 
    
    def bovenbeen(self):
            yield self.env.timeout(2) 
    
    def onderbeen(self):
            yield self.env.timeout(2) 
    
    def cefalinetijdcoagulatie(self):
            yield self.env.timeout(2) 
    
    def protrombinetijd(self):
            yield self.env.timeout(2) 
    
    def vulvaincisieoverige(self):
            yield self.env.timeout(2) 
    
    def echografieblaasextern(self):
            yield self.env.timeout(2) 
    
    def punctietbvcytologischonderzoekdoorp(self):
            yield self.env.timeout(2) 
    
    def vulvavulvectomieliesblok(self):
            yield self.env.timeout(2) 
    
    def microscopischonderzoekelektronenmic(self):
            yield self.env.timeout(2) 
    
    def buikstageringslaparotomoment(self):
            yield self.env.timeout(2) 
    
    def mammografiethoraxwand(self):
            yield self.env.timeout(2) 
    
    def echomamma(self):
            yield self.env.timeout(2) 
    
    def vrwgeslorgcurettagegefractioneerd(self):
            yield self.env.timeout(2) 
    
    def vulvabiopsiepunctiecytologie(self):
            yield self.env.timeout(2) 
    
    def uterushysteroscopie(self):
            yield self.env.timeout(2) 
    
    def uterusextirpabdradlymfaden(self):
            yield self.env.timeout(2) 
    
    def toonaudiometrieaudiologischcentrum(self):
            yield self.env.timeout(2) 
    
    def hoogfrequenteaudiometrieaudiologisch(self):
            yield self.env.timeout(2) 
    
    def tympanometriestandaardaudiologisch(self):
            yield self.env.timeout(2) 
    
    def patientenkontaktaudiologiekorterdan(self):
            yield self.env.timeout(2) 
    
    def anesthesiebijspeconderzenverrge(self):
            yield self.env.timeout(2) 
    
    def bekkenstaand(self):
            yield self.env.timeout(2) 
    
    def cytologischonderzoeknierpunctie(self):
            yield self.env.timeout(2) 
    
    def doorlichtingzonderopnamethorax(self):
            yield self.env.timeout(2) 
    
    def eiwitbeperktmineralenbeperkt(self):
            yield self.env.timeout(2) 
    
    def pyelografieantegraadviadrain(self):
            yield self.env.timeout(2) 
    
    def verwisselenvannefrostomiedrain(self):
            yield self.env.timeout(2) 
    
    def lipase(self):
            yield self.env.timeout(2) 
    
    def hemoglobinea(self):
            yield self.env.timeout(2) 
    
    def zwaredagverpleginga(self):
            yield self.env.timeout(2) 
    
    def mriabdomen(self):
            yield self.env.timeout(2) 
    
    def directeantiglobulinetestcoombs(self):
            yield self.env.timeout(2) 
    
    def antistoffentegenerysspecificiteit(self):
            yield self.env.timeout(2) 
    
    def identirregulaireastegenerysnapo(self):
            yield self.env.timeout(2) 
    
    def afwezigheidsdaga(self):
            yield self.env.timeout(2) 
    
    def ligasechainreactionlcr(self):
            yield self.env.timeout(2) 
    
    def uterusintrauterinedeviceinbre(self):
            yield self.env.timeout(2) 
    
    def mribijnier(self):
            yield self.env.timeout(2) 
    
    def melkzuurenzymatisch(self):
            yield self.env.timeout(2) 
    
    def blaascatheterademeureinbre(self):
            yield self.env.timeout(2) 
    
    def betasubunitbepmbvriahcg(self):
            yield self.env.timeout(2) 
    
    def sikkelcel(self):
            yield self.env.timeout(2) 
    
    def alfafoetoproteine(self):
            yield self.env.timeout(2) 
    
    def cholesteroltotaal(self):
            yield self.env.timeout(2) 
    
    def triglyceridenenzymatisch(self):
            yield self.env.timeout(2) 
    
    def cholesterolhdl(self):
            yield self.env.timeout(2) 
    
    def afereseplasmagesplitstfqenfq(self):
            yield self.env.timeout(2) 
    
    def catumormarkermbvmeia(self):
            yield self.env.timeout(2) 
    
    def catumormarker(self):
            yield self.env.timeout(2) 
    
    def ctbekken(self):
            yield self.env.timeout(2) 
    
    def heup(self):
            yield self.env.timeout(2) 
    
    def ctwervelkolomlumbaal(self):
            yield self.env.timeout(2) 
    
    def botdensitometrielwk(self):
            yield self.env.timeout(2) 
    
    def botdensitometriefemurhals(self):
            yield self.env.timeout(2) 
    
    def titratiedirecteantiglobulinetestcoo(self):
            yield self.env.timeout(2) 
    
    def vrwgeslorgexcdestructpathafwijkin(self):
            yield self.env.timeout(2) 
    
    def analgesieepiduraaldooranesthesist(self):
            yield self.env.timeout(2) 
    
    def urinewegenurodynamischonderzoekvij(self):
            yield self.env.timeout(2) 
    
    def uterusextirpatieabdominaalradi(self):
            yield self.env.timeout(2) 
    
    def maagontledigscintvastvloeibvoeds(self):
            yield self.env.timeout(2) 
    
    def darmcolonpassagescintcompvervolg(self):
            yield self.env.timeout(2) 
    
    def mriheup(self):
            yield self.env.timeout(2) 
    
    def echoonderbuik(self):
            yield self.env.timeout(2) 
    
    def creatinefosfokinasembspoed(self):
            yield self.env.timeout(2) 
    
    def troponinetmbvelisa(self):
            yield self.env.timeout(2) 
    
    def ovariumdebulkingovariumcarcinoom(self):
            yield self.env.timeout(2) 
    
    def cervixlisexcisieportiodiathe(self):
            yield self.env.timeout(2) 
    
    def uterusextirpatieabdominaaltota(self):
            yield self.env.timeout(2) 
    
    def hartdopplerechocardiografie(self):
            yield self.env.timeout(2) 
    
    def uteruscarccervixvlgswerthei(self):
            yield self.env.timeout(2) 
    
    def hematologieontstekscinttotlichaam(self):
            yield self.env.timeout(2) 
    
    def ovariumadnexextirpatiedmvlapar(self):
            yield self.env.timeout(2) 
    
    def pyelografiewoniertransplantaat(self):
            yield self.env.timeout(2) 
    
    def longfunctiecocapnografie(self):
            yield self.env.timeout(2) 
    
    def amylase(self):
            yield self.env.timeout(2) 
    
    def ammoniak(self):
            yield self.env.timeout(2) 
    
    def fibrinogeen(self):
            yield self.env.timeout(2) 
    
    def trombocytenleukoverwijderddonor(self):
            yield self.env.timeout(2) 
    
    def haptoglobine(self):
            yield self.env.timeout(2) 
    
    def trombinetijd(self):
            yield self.env.timeout(2) 
    
    def celkweekenisolatie(self):
            yield self.env.timeout(2) 
    
    def determinatieenorienttyperingdmvce(self):
            yield self.env.timeout(2) 
    
    def buikproeflaparotomie(self):
            yield self.env.timeout(2) 
    
    def blaassuprapubischekatheterinb(self):
            yield self.env.timeout(2) 
    
    def dikkedarmsigmoidoscopiemetflexibe(self):
            yield self.env.timeout(2) 
    
    def vulvavulvectomiezonderlieskli(self):
            yield self.env.timeout(2) 
    
    def intercconsultklinischradiotherapie(self):
            yield self.env.timeout(2) 
    
    def zwangerschapsreactiespoed(self):
            yield self.env.timeout(2) 
    
    def creatinefosfokinasekinetisch(self):
            yield self.env.timeout(2) 
    
    def ethanolenzymatischofgaschromatografi(self):
            yield self.env.timeout(2) 
    
    def coloninloop(self):
            yield self.env.timeout(2) 
    
    def inwendgeneeskjaarkaartkostenout(self):
            yield self.env.timeout(2) 
    
    def vitamined(self):
            yield self.env.timeout(2) 
    
    def onderzoekdunnedarmmzduodenum(self):
            yield self.env.timeout(2) 
    
    def wervelkolomcervicaal(self):
            yield self.env.timeout(2) 
    
    def ammoniakspoed(self):
            yield self.env.timeout(2) 
    
    def fenytoinekwantitatief(self):
            yield self.env.timeout(2) 
    
    def antitrombineiiimbvchromogeennsubstr(self):
            yield self.env.timeout(2) 
    
    def mrigrotehersenen(self):
            yield self.env.timeout(2) 
    
    def wervelkolomthoracaal(self):
            yield self.env.timeout(2) 
    
    def wervelkolomthoracolumbaleovergang(self):
            yield self.env.timeout(2) 
    
    def toegangschircvdkatheterperifeerb(self):
            yield self.env.timeout(2) 
    
    def erytrocytenleukocytenverwijderdbestra(self):
            yield self.env.timeout(2) 
    
    def intercconsultklinischneurologie(self):
            yield self.env.timeout(2) 
    
    def echogeleidealsassbijpunctiebiopsie(self):
            yield self.env.timeout(2) 
    
    def pijnbestrijdaanleggenpatientcontroll(self):
            yield self.env.timeout(2) 
    
    def ctapulmonalis(self):
            yield self.env.timeout(2) 
    
    def cytologischonderzoekliquorcerebrosp(self):
            yield self.env.timeout(2) 
    
    def erytrocyten(self):
            yield self.env.timeout(2) 
    
    def buffycoat(self):
            yield self.env.timeout(2) 
    
    def klinischtarief(self):
            yield self.env.timeout(2) 
    
    def cytologischonderzoekdiversen(self):
            yield self.env.timeout(2) 
    
    def totaaltthyroxineimmunofluorimetris(self):
            yield self.env.timeout(2) 
    
    def vaginabiopsiepunctiecytologie(self):
            yield self.env.timeout(2) 
    
    def blaascystoscopie(self):
            yield self.env.timeout(2) 
    
    def sinus(self):
            yield self.env.timeout(2) 
    
    def clostridiumelisatest(self):
            yield self.env.timeout(2) 
    
    def kaliumvlamfotometrisch(self):
            yield self.env.timeout(2) 
    
    def perifvatenduplexonderzoekveneus(self):
            yield self.env.timeout(2) 
    
    def dikkedarmappendectomienno(self):
            yield self.env.timeout(2) 
    
    def intercconsultklinischchirurgie(self):
            yield self.env.timeout(2) 
    
    def voet(self):
            yield self.env.timeout(2) 
    
    def cytologischonderzoekurineniercyste(self):
            yield self.env.timeout(2) 
    
    def schoudergewricht(self):
            yield self.env.timeout(2) 
    
    def chlorideionselectief(self):
            yield self.env.timeout(2) 
    
    def antinucleairefactoranf(self):
            yield self.env.timeout(2) 
    
    def bovenarm(self):
            yield self.env.timeout(2) 
    
    def vaginascopieinclevtvulvabiops(self):
            yield self.env.timeout(2) 
    
    def vaginaoverigeexcisiepathologis(self):
            yield self.env.timeout(2) 
    
    def vulvaruimelokaleexcisievana(self):
            yield self.env.timeout(2) 
    
    def nierenrenografielasix(self):
            yield self.env.timeout(2) 
    
    def parathormoonmbvradioisotopen(self):
            yield self.env.timeout(2) 
    
    def orthopantomogrampanoramixopnamegebit(self):
            yield self.env.timeout(2) 
    
    def echohalswaaronderschildklier(self):
            yield self.env.timeout(2) 
    
    def mecabepalingvoormrsambvpcr(self):
            yield self.env.timeout(2) 
    
    def buikpunctieascitesontlastend(self):
            yield self.env.timeout(2) 
    
    def uterusextirpatieabdominaalme(self):
            yield self.env.timeout(2) 
    
    def doxorubicineliposomalcaelyx(self):
            yield self.env.timeout(2) 
    
    def ctleverengalwegen(self):
            yield self.env.timeout(2) 
    
    def onderzoekvaneldersnietbeoordeeld(self):
            yield self.env.timeout(2) 
    
    def cervixconisatie(self):
            yield self.env.timeout(2) 
    
    def morfometrie(self):
            yield self.env.timeout(2) 
    
    def bloedgroepbepandersdanaboperbloedg(self):
            yield self.env.timeout(2) 
    
    def uitsluitenirregulaireastegenerysd(self):
            yield self.env.timeout(2) 
    
    def punctiecystetumoreddoorradioloogo(self):
            yield self.env.timeout(2) 
    
    def pyelografieantegraadviapunctie(self):
            yield self.env.timeout(2) 
    
    def vitamineb(self):
            yield self.env.timeout(2) 
    
    def vitamineehplcmethode(self):
            yield self.env.timeout(2) 
    
    def vitaminebthiamine(self):
            yield self.env.timeout(2) 
    
    def intercconsultvervolgklinischinterne(self):
            yield self.env.timeout(2) 
    
    def intensivecareligdagetotenmete(self):
            yield self.env.timeout(2) 
    
    def anesthesiebijvervoerbeademdepatie(self):
            yield self.env.timeout(2) 
    
    def creatinefosfokinaseisoenzymckmb(self):
            yield self.env.timeout(2) 
    
    def cvvhdcontinuevenoveneuzehemo(self):
            yield self.env.timeout(2) 
    
    def intensivecareligdagetotenmet(self):
            yield self.env.timeout(2) 
    
    def uteruscurettagediagnostisch(self):
            yield self.env.timeout(2) 
    
    def cervixcurettage(self):
            yield self.env.timeout(2) 
    
    def buikstaglaparotomomentect(self):
            yield self.env.timeout(2) 
    
    def echotractusurogenitalisbekken(self):
            yield self.env.timeout(2) 
    
    def eiwitcolorimetrischtotaal(self):
            yield self.env.timeout(2) 
    
    def microalbumineimmunonefelometrisch(self):
            yield self.env.timeout(2) 
    
    def cthals(self):
            yield self.env.timeout(2) 
    
    def aluminium(self):
            yield self.env.timeout(2) 
    
    def erytrocytentellenelektronisch(self):
            yield self.env.timeout(2) 
    
    def duplexscanvenenbeen(self):
            yield self.env.timeout(2) 
    
    def fshenzymimmunologisch(self):
            yield self.env.timeout(2) 
    
    def lhmbvradioisotopen(self):
            yield self.env.timeout(2) 
    
    def progesteronmbvradioisotopen(self):
            yield self.env.timeout(2) 
    
    def prolactinembveia(self):
            yield self.env.timeout(2) 
    
    def oestradiolmbvradioisotopenria(self):
            yield self.env.timeout(2) 
    
    def vrwgeslorgplastischeoperatievanvu(self):
            yield self.env.timeout(2) 
    
    def testosteronmbvradioisotopen(self):
            yield self.env.timeout(2) 
    
    def sexhormonebindingglobulinembvria(self):
            yield self.env.timeout(2) 
    
    def vaginatensionfreevaginaltape(self):
            yield self.env.timeout(2) 
    
    def vaginacolpocleisislefort(self):
            yield self.env.timeout(2) 
    
    def gemcitabine(self):
            yield self.env.timeout(2) 
    
    def buikoverzichtopzaal(self):
            yield self.env.timeout(2) 
    
    def echografiedopplervenacavainferioren(self):
            yield self.env.timeout(2) 
    
    def echobeen(self):
            yield self.env.timeout(2) 
    
    def vitaminea(self):
            yield self.env.timeout(2) 
    
    def beademinganesthesieeerstedag(self):
            yield self.env.timeout(2) 
    
    def lymfsyststageringslymfadenectomie(self):
            yield self.env.timeout(2) 
    
    def widalagglutinatieyersinia(self):
            yield self.env.timeout(2) 
    
    def dikkedarmcolonoscopiemetbiopsie(self):
            yield self.env.timeout(2) 
    
    def darmkatheteriserenstoma(self):
            yield self.env.timeout(2) 
    
    def intercconsultvervolgklinischanesthe(self):
            yield self.env.timeout(2) 
    
    def hartfunctiegatedbloodpoolrust(self):
            yield self.env.timeout(2) 
    
    def echografieavueivwzwangerschapmet(self):
            yield self.env.timeout(2) 
    
    def onderzoekviapercutaneveneuzekatheter(self):
            yield self.env.timeout(2) 
    
    def echografiedopplervjugularis(self):
            yield self.env.timeout(2) 
    
    def vendsavenacavainferior(self):
            yield self.env.timeout(2) 
    
    def antihepatitiscvirusmbvelisa(self):
            yield self.env.timeout(2) 
    
    def beademinganesthesietweedetmvijf(self):
            yield self.env.timeout(2) 
    
    def klinischekaartverloskundeengynaeco(self):
            yield self.env.timeout(2) 
    
    def vulvapartielevulvectomie(self):
            yield self.env.timeout(2) 
    
    def vrwgeslorgadnexextirpatiedmvlapar(self):
            yield self.env.timeout(2) 
    
    def zwangerschapsreactie(self):
            yield self.env.timeout(2) 
    
    def ribsternum(self):
            yield self.env.timeout(2) 
    
    def intercconsultklinischinterneziekten(self):
            yield self.env.timeout(2) 
    
    def brachytherapieinterstitieelbijzond(self):
            yield self.env.timeout(2) 
    
    def osmolaliteit(self):
            yield self.env.timeout(2) 
    
    def digoxine(self):
            yield self.env.timeout(2) 
    
    def hepatitiscvirusrochehcvrmbvpcr(self):
            yield self.env.timeout(2) 
    
    def cervixportiolasercoagulatie(self):
            yield self.env.timeout(2) 
    
    def vaginascopieexclweefselwegname(self):
            yield self.env.timeout(2) 
    
    def cytologischonderzoekpleuravocht(self):
            yield self.env.timeout(2) 
    
    def huidplastiekzplastiekhuidhoofdenh(self):
            yield self.env.timeout(2) 
    
    def cttotalelichaam(self):
            yield self.env.timeout(2) 
    
    def pyelografieretrograad(self):
            yield self.env.timeout(2) 
    
    def echopancreasenmilt(self):
            yield self.env.timeout(2) 
    
    def brainnatriureticpeptidebnpmbvimmu(self):
            yield self.env.timeout(2) 
    
    def duodenumoesofagogastroduodenoscopi(self):
            yield self.env.timeout(2) 
    
    def intercconsultklinischurologie(self):
            yield self.env.timeout(2) 
    
    def darmcolonpassagescintcompstatisch(self):
            yield self.env.timeout(2) 
    
    def echoenrontgenalsassbijdrainageab(self):
            yield self.env.timeout(2) 
    
    def gentamycinekwnimmunoassay(self):
            yield self.env.timeout(2) 
    
    def echothorax(self):
            yield self.env.timeout(2) 
    
    def rogelalsassbijpunktiebiopsiet(self):
            yield self.env.timeout(2) 
    
    def onderznaaraanwezigheidvankoudeanti(self):
            yield self.env.timeout(2) 
    
    def gebantistoffentegenerysdircoombs(self):
            yield self.env.timeout(2) 
    
    def gebantistoffentegenerysdircoomb(self):
            yield self.env.timeout(2) 
    
    def ovariumredebulkingovariumcarcin(self):
            yield self.env.timeout(2) 
    
    def ovariumexcisiecystevialaparosc(self):
            yield self.env.timeout(2) 
    
    def behandeleninhyperpressietank(self):
            yield self.env.timeout(2) 
    
    def perifvatendoppleronderzoppervlven(self):
            yield self.env.timeout(2) 
    
    def perifvatenduplexscanarterieelcruro(self):
            yield self.env.timeout(2) 
    
    def buiksecondlookoperstagering(self):
            yield self.env.timeout(2) 
    
    def elutievanautoantistoffentegenerytro(self):
            yield self.env.timeout(2) 
    
    def bloedgroepbepalingandersdanabokidd(self):
            yield self.env.timeout(2) 
    
    def buikexcisiepathologafwijking(self):
            yield self.env.timeout(2) 
    
    def hydroxyprogesteronmbvria(self):
            yield self.env.timeout(2) 
    
    def deltaandrosteendion(self):
            yield self.env.timeout(2) 
    
    def dheasulfaatmetextractiembvria(self):
            yield self.env.timeout(2) 
    
    def enkel(self):
            yield self.env.timeout(2) 
    
    def vrwgeslorgaspiratieofmicrocurett(self):
            yield self.env.timeout(2) 
    
    def bronchusbronchtoiletdoorverpl(self):
            yield self.env.timeout(2) 
    
    def immunoglobulineaiga(self):
            yield self.env.timeout(2) 
    
    def heparineantixa(self):
            yield self.env.timeout(2) 
    
    def rogelalsassbijdrainageniernefro(self):
            yield self.env.timeout(2) 
    
    def echonier(self):
            yield self.env.timeout(2) 
    
    def occultbloedkwalitatief(self):
            yield self.env.timeout(2) 
    
    def echobuikwand(self):
            yield self.env.timeout(2) 
    
    def cytologischonderzoekbuiktumorpunctie(self):
            yield self.env.timeout(2) 
    
    def buikomentumplastiek(self):
            yield self.env.timeout(2) 
    
    def ctnier(self):
            yield self.env.timeout(2) 
    
    def cytologischonderzoekleverpunctie(self):
            yield self.env.timeout(2) 
    
    def hartresuscitatie(self):
            yield self.env.timeout(2) 
    
    def uterusextirpatieabdomtotaalme(self):
            yield self.env.timeout(2) 
    
    def vrwgeslorgadhesiolysisovariumplus(self):
            yield self.env.timeout(2) 
    
    def cytologischonderzoekvulva(self):
            yield self.env.timeout(2) 
    
    def ctretroperitoneum(self):
            yield self.env.timeout(2) 
    
    def antihavigofiggelisaofriaineen(self):
            yield self.env.timeout(2) 
    
    def antisttegenhepatitisbsurfaceantigee(self):
            yield self.env.timeout(2) 
    
    def hepatitisbanticoreigm(self):
            yield self.env.timeout(2) 
    
    def buiklittekenbreukplastische(self):
            yield self.env.timeout(2) 
    
    def vaginaoperatievesicovaginalefi(self):
            yield self.env.timeout(2) 
    
    def vulvahechtenvanvulva(self):
            yield self.env.timeout(2) 
    
    def mycobacteriummbvpcr(self):
            yield self.env.timeout(2) 
    
    def huidtranscutanepoenpcome(self):
            yield self.env.timeout(2) 
    
    def glucosebepalingkwantitatief(self):
            yield self.env.timeout(2) 
    
    def ctgelalsassbijpunctiebiopsiei(self):
            yield self.env.timeout(2) 
    
    def cytologischonderzoekendocervix(self):
            yield self.env.timeout(2) 
    
    def oestronmbvradioisotopen(self):
            yield self.env.timeout(2) 
    
    def lymfsystlymfadenectomiedmvlaparo(self):
            yield self.env.timeout(2) 
    
    def cytostaticainfuustherapie(self):
            yield self.env.timeout(2) 
    
    def echogeleidealsassbijdrainageintrap(self):
            yield self.env.timeout(2) 
    
    def rituximab(self):
            yield self.env.timeout(2) 
    
    def vaginavaginotomie(self):
            yield self.env.timeout(2) 
    
    def echografieavueivmzwangerschaprout(self):
            yield self.env.timeout(2) 
    
    def blaasvoorsteenachtersteexent(self):
            yield self.env.timeout(2) 
    
    def uretersplintografiecqopspuitenuret(self):
            yield self.env.timeout(2) 
    
    def blaasbladderwashout(self):
            yield self.env.timeout(2) 
    
    def duodenuminbrengenvoedingssondein(self):
            yield self.env.timeout(2) 
    
    def emgelektromyografischonderzo(self):
            yield self.env.timeout(2) 
    
    def kniemzonderbeen(self):
            yield self.env.timeout(2) 
    
    def ctarterienhersenen(self):
            yield self.env.timeout(2) 
    
    def iggantistoffentegenheparinepfcompl(self):
            yield self.env.timeout(2) 
    
    def abortusoverigetechnieken(self):
            yield self.env.timeout(2) 
    
    def echografietransuretraalprostaat(self):
            yield self.env.timeout(2) 
    
    def eiwitspectrumelektroforesekwnbepf(self):
            yield self.env.timeout(2) 
    
    def immunoglobulinegigg(self):
            yield self.env.timeout(2) 
    
    def immunoglobulinemigm(self):
            yield self.env.timeout(2) 
    
    def paraproteinetyperingmbvmonospecifieke(self):
            yield self.env.timeout(2) 
    
    def eiwitfractioneringmbvief(self):
            yield self.env.timeout(2) 
    
    def immunofixatie(self):
            yield self.env.timeout(2) 
    
    def immunoforesenaconcentratie(self):
            yield self.env.timeout(2) 
    
    def drainageprocedureonderrontgencontrole(self):
            yield self.env.timeout(2) 
    
    def antigeendetectiedirectpreparaaths(self):
            yield self.env.timeout(2) 
    
    def antigeendetectiedirectpreparaatvz(self):
            yield self.env.timeout(2) 
    
    def nietdeclarabeledagverplegingbvklinp(self):
            yield self.env.timeout(2) 
    
    def intercconsultklinischreumatologie(self):
            yield self.env.timeout(2) 
    
    def anticytomegalovirusigofiggelisa(self):
            yield self.env.timeout(2) 
    
    def igmastegencmvvirus(self):
            yield self.env.timeout(2) 
    
    def antiepsteinbarrvcaigmmbvelisa(self):
            yield self.env.timeout(2) 
    
    def antiepsteinbarrnaiggmbvelisa(self):
            yield self.env.timeout(2) 
    
    def antiepsteinbarrvcaiggmbvelisa(self):
            yield self.env.timeout(2) 
    
    def complementcomponentckwn(self):
            yield self.env.timeout(2) 
    
    def dnafarrassaymbvria(self):
            yield self.env.timeout(2) 
    
    def legionellaantigeensneltest(self):
            yield self.env.timeout(2) 
    
    def complementdeficientieondbijafwezigha(self):
            yield self.env.timeout(2) 
    
    def longfunctiespirometrie(self):
            yield self.env.timeout(2) 
    
    def longfunctiestroomvolumecurve(self):
            yield self.env.timeout(2) 
    
    def sacrumoscoccygissigewrichten(self):
            yield self.env.timeout(2) 
    
    def proteinecactiviteit(self):
            yield self.env.timeout(2) 
    
    def igmanticardiolipinembvelisa(self):
            yield self.env.timeout(2) 
    
    def igganticardiolipinembvelisa(self):
            yield self.env.timeout(2) 
    
    def antistspecifiekmbvelisahistonenof(self):
            yield self.env.timeout(2) 
    
    def stollingsfactorviiiactiviteit(self):
            yield self.env.timeout(2) 
    
    def anticoagulanslupusmbvelisa(self):
            yield self.env.timeout(2) 
    
    def proteinesantigeentotaal(self):
            yield self.env.timeout(2) 
    
    def proteinesantigeenvrij(self):
            yield self.env.timeout(2) 
    
    def factoriimutatiembvpcr(self):
            yield self.env.timeout(2) 
    
    def factorvleidenrqmbvdnatest(self):
            yield self.env.timeout(2) 
    
    def lymfsystlymfekliertoiletdiepli(self):
            yield self.env.timeout(2) 
    
    def tubauterinaexcisieparovarialecyste(self):
            yield self.env.timeout(2) 
    
    def echobovenbeen(self):
            yield self.env.timeout(2) 
    
    def phmeting(self):
            yield self.env.timeout(2) 
    
    def spraakaudiometriestandaardaudiol(self):
            yield self.env.timeout(2) 
    
    def mandibulakaakgewricht(self):
            yield self.env.timeout(2) 
    
    def mriorbita(self):
            yield self.env.timeout(2) 
    
    def highsensitivecrphscrpnefelometrisc(self):
            yield self.env.timeout(2) 
    
    def echoarteriaecarotissinistra(self):
            yield self.env.timeout(2) 
    
    def echoarteriaecarotisdextra(self):
            yield self.env.timeout(2) 
    
    def bloedstollingsfactorxiactiviteit(self):
            yield self.env.timeout(2) 
    
    def bloedstollingsfactorxiiactiviteit(self):
            yield self.env.timeout(2) 
    
    def bloedstollingsfactorixcoagulatie(self):
            yield self.env.timeout(2) 
    
    def uterusexcisiedestructiepathaf(self):
            yield self.env.timeout(2) 
    
    def hyperthermiebehandelingh(self):
            yield self.env.timeout(2) 
    
    def inbrengenvoedingsoflavagesondeduode(self):
            yield self.env.timeout(2) 
    
    def echopleura(self):
            yield self.env.timeout(2) 
    
    def pleurapunctiediagnostisch(self):
            yield self.env.timeout(2) 
    
    def alfaamylase(self):
            yield self.env.timeout(2) 
    
    def vancomycinekwnimmunoassay(self):
            yield self.env.timeout(2) 
    
    def intercconsultvervolgklinischchirurg(self):
            yield self.env.timeout(2) 
    
    def echografiedopplervenenbeen(self):
            yield self.env.timeout(2) 
    
    def mictiecystouretrografie(self):
            yield self.env.timeout(2) 
    
    def totalegebitsstatus(self):
            yield self.env.timeout(2) 
    
    def vrwgeslorgadhesiolysisovariatubae(self):
            yield self.env.timeout(2) 
    
    def ctpancreasenmilt(self):
            yield self.env.timeout(2) 
    
    def doorlichtingzonderopnamebuik(self):
            yield self.env.timeout(2) 
    
    def echogeleidealsassbijpunctieabdomen(self):
            yield self.env.timeout(2) 
    
    def cytologischonderzoektbvbevolkingsonde(self):
            yield self.env.timeout(2) 
    
    def bloedstollingsfactorvkwantitatief(self):
            yield self.env.timeout(2) 
    
    def bloedstollingsfactorviicoagulatie(self):
            yield self.env.timeout(2) 
    
    def vonwillebrandprofielmbvprotease(self):
            yield self.env.timeout(2) 
    
    def cytologischonderzoekschildklierpun(self):
            yield self.env.timeout(2) 
    
    def uterusextirpatievaginaaltotaal(self):
            yield self.env.timeout(2) 
    
    def nucleaironderzoekvanelders(self):
            yield self.env.timeout(2) 
    
    def unknown(self):
            yield self.env.timeout(2) 
    
    def peritoneumomentectomie(self):
            yield self.env.timeout(2) 
    
    def vulvatherapeutischepunctieaan(self):
            yield self.env.timeout(2) 
    
    def urethradilatatiemeatus(self):
            yield self.env.timeout(2) 
    
    def antisttegenacetylcholinereceptoren(self):
            yield self.env.timeout(2) 
    
    def aspectsupernatant(self):
            yield self.env.timeout(2) 
    
    def infuusbloed(self):
            yield self.env.timeout(2) 
    
    def thoraxzuigdrainagebehandelinga(self):
            yield self.env.timeout(2) 
    
    def ovariumovariopexieexcltorsie(self):
            yield self.env.timeout(2) 
    
    def prostaatspecifiekantigeenpsambvimm(self):
            yield self.env.timeout(2) 
    
    def antisttegenhiveofhivc(self):
            yield self.env.timeout(2) 
    
    def directondznaarrsvirusantigeenmbv(self):
            yield self.env.timeout(2) 
    
    def parainfluenzavirusmbvpcr(self):
            yield self.env.timeout(2) 
    
    def humaanmetapneumoviruskwlmbvdnarna(self):
            yield self.env.timeout(2) 
    
    def antigeendetectiembviftinfluenzaa(self):
            yield self.env.timeout(2) 
    
    def antigeendetectiembviftinfluenzab(self):
            yield self.env.timeout(2) 
    
    def buiklaparoscopiediagnostisc(self):
            yield self.env.timeout(2) 
    
    def wormeierenuitgebreidvervolg(self):
            yield self.env.timeout(2) 
    
    def zink(self):
            yield self.env.timeout(2) 
    
    def vrwgeslorgoperatievanclitorisnno(self):
            yield self.env.timeout(2) 
    
    def opnamevolgensbarsonie(self):
            yield self.env.timeout(2) 
    
    def lymfsystlymfeklierextirpatiepara(self):
            yield self.env.timeout(2) 
    
    def uterusextirpabdvagradlymfa(self):
            yield self.env.timeout(2) 
    
    def buikoverzichtstaand(self):
            yield self.env.timeout(2) 
    
    def dunnedarmmechileusadhesstrengi(self):
            yield self.env.timeout(2) 
    
    def cytologischonderzoekhersenen(self):
            yield self.env.timeout(2) 
    
    def antirubellaiggelisaineenmonster(self):
            yield self.env.timeout(2) 
    
    def antichlamydiaigambvelisa(self):
            yield self.env.timeout(2) 
    
    def antichlamydiaiggmbvindift(self):
            yield self.env.timeout(2) 
    
    def buikadhesiolyseenbiopsiedmv(self):
            yield self.env.timeout(2) 
    
    def endoretrogradecholangiografie(self):
            yield self.env.timeout(2) 
    
    def cystografieretrograad(self):
            yield self.env.timeout(2) 
    
    def doorlichtingbijniersteenvergruizing(self):
            yield self.env.timeout(2) 
    
    def wisselendrainonderrontgencontrole(self):
            yield self.env.timeout(2) 
    
    def kleurproefsabinfeldmanleishmania(self):
            yield self.env.timeout(2) 
    
    def toxoplasmosembveiatoxoigg(self):
            yield self.env.timeout(2) 
    
    def toxoplasmosembveiatoxoigm(self):
            yield self.env.timeout(2) 
    
    def antirubellaigmelisa(self):
            yield self.env.timeout(2) 
    
    def cbrcoxsackiebvirus(self):
            yield self.env.timeout(2) 
    
    def antiparvovirusigofiggantistind(self):
            yield self.env.timeout(2) 
    
    def antiparvovirusigmmbvindift(self):
            yield self.env.timeout(2) 
    
    def tubauterinaaanbrengenclipstijdensl(self):
            yield self.env.timeout(2) 
    
    def partusklinofpoliklinmetvoorb(self):
            yield self.env.timeout(2) 
    
    def sectcaesarmetvoorbehandelingenkra(self):
            yield self.env.timeout(2) 
    
    def mritractusurogenitalis(self):
            yield self.env.timeout(2) 
    
    def opspuitenhickmankatheter(self):
            yield self.env.timeout(2) 
    
    def rogelalsassbijpunctiebiopsiel(self):
            yield self.env.timeout(2) 
    
    def lymfsystregionalelymfeklierdissec(self):
            yield self.env.timeout(2) 
    
    def dtoegangschircvdcatheterv(self):
            yield self.env.timeout(2) 
    
    def hemoglobinenabnormaalinclhba(self):
            yield self.env.timeout(2) 
    
    def iggindex(self):
            yield self.env.timeout(2) 
    
    def albumineratio(self):
            yield self.env.timeout(2) 
    
    def immunoelektroforeseliquornaconcentra(self):
            yield self.env.timeout(2) 
    
    def huidverwijderenretentiecyste(self):
            yield self.env.timeout(2) 
    
    def rogelalsassbijinbrengenendoproth(self):
            yield self.env.timeout(2) 
    
    def leverexcisietumorofmetastase(self):
            yield self.env.timeout(2) 
    
    def lymfsystsentinelnodeprocedureli(self):
            yield self.env.timeout(2) 
    
    def gipskamerokgebruik(self):
            yield self.env.timeout(2) 
    
    def standaardmateriaalnno(self):
            yield self.env.timeout(2) 
    
    def zwachtelverbandslingaanleggen(self):
            yield self.env.timeout(2) 
    
    def partielegebitsstatus(self):
            yield self.env.timeout(2) 
    
    def intercconsultpoliklinisch(self):
            yield self.env.timeout(2) 
    
    def vrwgeslorgsecondlookoperovariumca(self):
            yield self.env.timeout(2) 
    
    def oesofagografieoraal(self):
            yield self.env.timeout(2) 
    
    def ohvitaminedmbvhplc(self):
            yield self.env.timeout(2) 
    
    def perifvatenverwijderenportacath(self):
            yield self.env.timeout(2) 
    
    def perifvateninbrengenportacathsyst(self):
            yield self.env.timeout(2) 
    
    def rontgenonderzoekonvolledig(self):
            yield self.env.timeout(2) 
    
    def mriartenvenabdomen(self):
            yield self.env.timeout(2) 
    
    def vaginaextirpatievanvaginamet(self):
            yield self.env.timeout(2) 
    
    def neuronspecifiekenolase(self):
            yield self.env.timeout(2) 
    
    def ctknie(self):
            yield self.env.timeout(2) 
    
    def tubauterinareanastomosenasterilisat(self):
            yield self.env.timeout(2) 
    
    def obductie(self):
            yield self.env.timeout(2) 
    
    def anesthesieepiduraalmetbloedpatch(self):
            yield self.env.timeout(2) 
    
    def dikkedarmresectiesigmoidmetprima(self):
            yield self.env.timeout(2) 
    
    def dikkedarmappendectomieacuutviame(self):
            yield self.env.timeout(2) 
    
    def totaalttrijoodthyroninembvradiois(self):
            yield self.env.timeout(2) 
    
    def tuptakelatentebindingscapgebtbg(self):
            yield self.env.timeout(2) 
    
    def echobekkeninhoudmuvanatomiecodet(self):
            yield self.env.timeout(2) 
    
    def uterustotlaparoscopischehyste(self):
            yield self.env.timeout(2) 
    
    def plaatsenvanvcavafilter(self):
            yield self.env.timeout(2) 
    
    def eerstehulpnietsehafdelingelders(self):
            yield self.env.timeout(2) 
    
    def buiksecondlookoperovariumca(self):
            yield self.env.timeout(2) 
    
    def itraconazolmbvhplc(self):
            yield self.env.timeout(2) 
    
    def bepalinghepatitisbeantigeen(self):
            yield self.env.timeout(2) 
    
    def bepalingantisthepatitisbeantigeen(self):
            yield self.env.timeout(2) 
    