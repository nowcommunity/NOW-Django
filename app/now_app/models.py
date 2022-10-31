# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Log(models.Model):
    log_id = models.AutoField(primary_key=True)
    event_time = models.DateTimeField(blank=True, null=True)
    user_name = models.CharField(max_length=100, blank=True, null=True)
    server_name = models.CharField(max_length=50, blank=True, null=True)
    table_name = models.CharField(max_length=50, blank=True, null=True)
    pk_data = models.CharField(max_length=200, blank=True, null=True)
    column_name = models.CharField(max_length=50, blank=True, null=True)
    log_action = models.IntegerField(blank=True, null=True)
    old_data = models.CharField(max_length=255, blank=True, null=True)
    new_data = models.CharField(max_length=255, blank=True, null=True)
    luid = models.IntegerField(blank=True, null=True)
    suid = models.IntegerField(blank=True, null=True)
    tuid = models.IntegerField(blank=True, null=True)
    buid = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'log'

class ComFamilySynonym(models.Model):
    syn_family_name = models.CharField(primary_key=True, max_length=30)
    family_name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = 'com_family_synonym'


class ComGenusSynonym(models.Model):
    syn_genus_name = models.CharField(primary_key=True, max_length=30)
    genus_name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = 'com_genus_synonym'


class ComMain(models.Model):
    one = models.IntegerField(primary_key=True)

    class Meta:
        db_table = 'com_main'


class ComMuseumList(models.Model):
    museum = models.CharField(primary_key=True, max_length=10)
    institution = models.CharField(max_length=120)
    alt_int_name = models.CharField(max_length=120, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state_code = models.CharField(max_length=5, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    used_morph = models.IntegerField(blank=True, null=True)
    used_now = models.IntegerField(blank=True, null=True)
    used_gene = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'com_mlist'


class ComOrderSynonym(models.Model):
    syn_order_name = models.CharField(primary_key=True, max_length=30)
    order_name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = 'com_order_synonym'


class ComPeople(models.Model):
    initials = models.CharField(primary_key=True, max_length=10)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    surname = models.CharField(max_length=80)
    full_name = models.CharField(max_length=80)
    format = models.CharField(max_length=1, blank=True, null=True)
    email = models.CharField(max_length=120, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    organization = models.CharField(max_length=80, blank=True, null=True)
    country = models.CharField(max_length=80, blank=True, null=True)
    password_set = models.DateField(blank=True, null=True)
    used_morph = models.IntegerField(blank=True, null=True)
    used_now = models.IntegerField(blank=True, null=True)
    used_gene = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'com_people'


class ComSpecies(models.Model):
    species_id = models.AutoField(primary_key=True)
    class_name = models.CharField(max_length=30)
    order_name = models.CharField(max_length=30)
    family_name = models.CharField(max_length=30)
    subclass_or_superorder_name = models.CharField(max_length=30, blank=True, null=True)
    suborder_or_superfamily_name = models.CharField(max_length=30, blank=True, null=True)
    subfamily_name = models.CharField(max_length=30, blank=True, null=True)
    genus_name = models.CharField(max_length=30)
    species_name = models.CharField(max_length=30)
    unique_identifier = models.CharField(max_length=50)
    taxonomic_status = models.CharField(max_length=50, blank=True, null=True)
    common_name = models.CharField(max_length=50, blank=True, null=True)
    sp_author = models.CharField(max_length=50, blank=True, null=True)
    strain = models.CharField(max_length=50, blank=True, null=True)
    gene = models.CharField(max_length=30, blank=True, null=True)
    taxon_status = models.CharField(max_length=10, blank=True, null=True)
    diet1 = models.CharField(max_length=1, blank=True, null=True)
    diet2 = models.CharField(max_length=9, blank=True, null=True)
    diet3 = models.CharField(max_length=10, blank=True, null=True)
    diet_description = models.CharField(max_length=255, blank=True, null=True)
    rel_fib = models.CharField(max_length=1, blank=True, null=True)
    selectivity = models.CharField(max_length=1, blank=True, null=True)
    digestion = models.CharField(max_length=2, blank=True, null=True)
    feedinghab1 = models.CharField(max_length=2, blank=True, null=True)
    feedinghab2 = models.CharField(max_length=8, blank=True, null=True)
    shelterhab1 = models.CharField(max_length=2, blank=True, null=True)
    shelterhab2 = models.CharField(max_length=8, blank=True, null=True)
    locomo1 = models.CharField(max_length=2, blank=True, null=True)
    locomo2 = models.CharField(max_length=15, blank=True, null=True)
    locomo3 = models.CharField(max_length=15, blank=True, null=True)
    hunt_forage = models.CharField(max_length=8, blank=True, null=True)
    body_mass = models.BigIntegerField(blank=True, null=True)
    brain_mass = models.IntegerField(blank=True, null=True)
    sv_length = models.CharField(max_length=7, blank=True, null=True)
    activity = models.CharField(max_length=1, blank=True, null=True)
    sd_size = models.CharField(max_length=1, blank=True, null=True)
    sd_display = models.CharField(max_length=1, blank=True, null=True)
    tshm = models.CharField(max_length=3, blank=True, null=True)
    symph_mob = models.CharField(max_length=1, blank=True, null=True)
    relative_blade_length = models.FloatField(blank=True, null=True)
    tht = models.CharField(max_length=3, blank=True, null=True)
    crowntype = models.CharField(max_length=6, blank=True, null=True)
    microwear = models.CharField(max_length=7, blank=True, null=True)
    horizodonty = models.CharField(max_length=3, blank=True, null=True)
    cusp_shape = models.CharField(max_length=1, blank=True, null=True)
    cusp_count_buccal = models.CharField(max_length=1, blank=True, null=True)
    cusp_count_lingual = models.CharField(max_length=1, blank=True, null=True)
    loph_count_lon = models.CharField(max_length=1, blank=True, null=True)
    loph_count_trs = models.CharField(max_length=1, blank=True, null=True)
    fct_al = models.CharField(max_length=1, blank=True, null=True)
    fct_ol = models.CharField(max_length=1, blank=True, null=True)
    fct_sf = models.CharField(max_length=1, blank=True, null=True)
    fct_ot = models.CharField(max_length=1, blank=True, null=True)
    fct_cm = models.CharField(max_length=1, blank=True, null=True)
    mesowear = models.CharField(max_length=3, blank=True, null=True)
    mw_or_high = models.IntegerField(blank=True, null=True)
    mw_or_low = models.IntegerField(blank=True, null=True)
    mw_cs_sharp = models.IntegerField(blank=True, null=True)
    mw_cs_round = models.IntegerField(blank=True, null=True)
    mw_cs_blunt = models.IntegerField(blank=True, null=True)
    mw_scale_min = models.IntegerField(blank=True, null=True)
    mw_scale_max = models.IntegerField(blank=True, null=True)
    mw_value = models.IntegerField(blank=True, null=True)
    pop_struc = models.CharField(max_length=3, blank=True, null=True)
    sp_status = models.IntegerField(blank=True, null=True)
    used_morph = models.IntegerField(blank=True, null=True)
    used_now = models.IntegerField(blank=True, null=True)
    used_gene = models.IntegerField(blank=True, null=True)
    sp_comment = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'com_species'


class ComSubfamilySynonym(models.Model):
    syn_subfamily_name = models.CharField(primary_key=True, max_length=30)
    subfamily_name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = 'com_subfamily_synonym'


class ComTaxaSynonym(models.Model):
    synonym_id = models.AutoField(primary_key=True)
    species_id = models.ForeignKey(ComSpecies, on_delete=models.DO_NOTHING)
    syn_genus_name = models.CharField(max_length=30, blank=True, null=True)
    syn_species_name = models.CharField(max_length=30, blank=True, null=True)
    syn_comment = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'com_taxa_synonym'


class ComUsers(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    last_login = models.DateField(blank=True, null=True)
    now_user_group = models.CharField(max_length=30, blank=True, null=True)
    mor_user_group = models.CharField(max_length=30, blank=True, null=True)
    gen_user_group = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = 'com_users'

class NowTimeUnitBoundary(models.Model):
    bid = models.AutoField(primary_key=True)
    b_name = models.CharField(max_length=150, blank=True, null=True)
    age = models.FloatField(blank=True, null=True)
    b_comment = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'now_tu_bound'

class NowTimeUnitBoundaryUpdate(models.Model):
    buid = models.AutoField(primary_key=True)
    bau_coordinator = models.ForeignKey(ComPeople, models.DO_NOTHING, db_column='bau_coordinator', related_name='%(class)s_bau_coordinator')
    bau_authorizer = models.ForeignKey(ComPeople, models.DO_NOTHING, db_column='bau_authorizer', related_name='%(class)s_bau_authorizer')
    bid = models.ForeignKey(NowTimeUnitBoundary, models.CASCADE, db_column='bid')
    bau_date = models.DateField(blank=True, null=True)
    bau_comment = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'now_bau'

class RefReferenceType(models.Model):
    ref_type_id = models.AutoField(primary_key=True)
    ref_type = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = 'ref_ref_type'

class RefJournal(models.Model):
    journal_id = models.AutoField(primary_key=True)
    journal_title = models.CharField(max_length=255, blank=True, null=True)
    short_title = models.CharField(max_length=100, blank=True, null=True)
    alt_title = models.CharField(max_length=255, blank=True, null=True)
    issn = models.CharField(db_column='ISSN', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'ref_journal'

class RefReference(models.Model):
    rid = models.AutoField(primary_key=True)
    ref_type = models.ForeignKey(RefReferenceType, models.DO_NOTHING)
    journal = models.ForeignKey(RefJournal, models.DO_NOTHING, blank=True, null=True)
    title_primary = models.CharField(max_length=255, blank=True, null=True)
    date_primary = models.IntegerField(blank=True, null=True)
    volume = models.CharField(max_length=10, blank=True, null=True)
    issue = models.CharField(max_length=10, blank=True, null=True)
    start_page = models.IntegerField(blank=True, null=True)
    end_page = models.IntegerField(blank=True, null=True)
    publisher = models.CharField(max_length=255, blank=True, null=True)
    pub_place = models.CharField(max_length=255, blank=True, null=True)
    title_secondary = models.CharField(max_length=255, blank=True, null=True)
    date_secondary = models.IntegerField(blank=True, null=True)
    title_series = models.CharField(max_length=255, blank=True, null=True)
    issn_isbn = models.CharField(max_length=30, blank=True, null=True)
    ref_abstract = models.TextField(blank=True, null=True)
    web_url = models.CharField(max_length=255, blank=True, null=True)
    misc_1 = models.CharField(max_length=255, blank=True, null=True)
    misc_2 = models.CharField(max_length=255, blank=True, null=True)
    gen_notes = models.CharField(max_length=255, blank=True, null=True)
    printed_language = models.CharField(max_length=50, blank=True, null=True)
    exact_date = models.DateField(blank=True, null=True)
    used_morph = models.IntegerField(blank=True, null=True)
    used_now = models.IntegerField(blank=True, null=True)
    used_gene = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'ref_ref'

class NowTimeUnitBoundaryUpdateReference(models.Model):
    buid = models.OneToOneField(NowTimeUnitBoundaryUpdate, models.CASCADE, db_column='buid')
    rid = models.ForeignKey(RefReference, models.DO_NOTHING, db_column='rid')

    class Meta:
        db_table = 'now_br'
        unique_together = (('buid', 'rid'),)

class NowCollectingMethodValue(models.Model):
    coll_meth_value = models.CharField(primary_key=True, max_length=21)

    class Meta:
        db_table = 'now_coll_meth_values'

class NowTimeUnitSequence(models.Model):
    sequence = models.CharField(primary_key=True, max_length=30)
    seq_name = models.CharField(max_length=30)

    class Meta:
        db_table = 'now_tu_sequence'

class NowTimeUnit(models.Model):
    tu_name = models.CharField(primary_key=True, max_length=100)
    tu_display_name = models.CharField(max_length=100)
    up_bnd = models.ForeignKey(NowTimeUnitBoundary, models.DO_NOTHING, db_column='up_bnd', related_name='%(class)s_up_bnd')
    low_bnd = models.ForeignKey(NowTimeUnitBoundary, models.DO_NOTHING, db_column='low_bnd', related_name='%(class)s_low_bnd')
    rank = models.CharField(max_length=15, blank=True, null=True)
    sequence = models.ForeignKey(NowTimeUnitSequence, models.DO_NOTHING, db_column='sequence')
    tu_comment = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'now_time_unit'

class NowLocality(models.Model):
    lid = models.AutoField(primary_key=True)
    bfa_max = models.ForeignKey(NowTimeUnit, models.DO_NOTHING, db_column='bfa_max', blank=True, null=True, related_name='%(class)s_bfa_max')
    bfa_min = models.ForeignKey(NowTimeUnit, models.DO_NOTHING, db_column='bfa_min', blank=True, null=True, related_name='%(class)s_bfa_min')
    loc_name = models.CharField(max_length=30)
    date_meth = models.CharField(max_length=9)
    max_age = models.FloatField()
    min_age = models.FloatField()
    bfa_max_abs = models.CharField(max_length=30, blank=True, null=True)
    bfa_min_abs = models.CharField(max_length=30, blank=True, null=True)
    frac_max = models.CharField(max_length=9, blank=True, null=True)
    frac_min = models.CharField(max_length=9, blank=True, null=True)
    chron = models.CharField(max_length=40, blank=True, null=True)
    age_comm = models.CharField(max_length=120, blank=True, null=True)
    basin = models.CharField(max_length=120, blank=True, null=True)
    subbasin = models.CharField(max_length=120, blank=True, null=True)
    dms_lat = models.CharField(max_length=14, blank=True, null=True)
    dms_long = models.CharField(max_length=14, blank=True, null=True)
    dec_lat = models.FloatField()
    dec_long = models.FloatField()
    approx_coord = models.IntegerField(blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    county = models.CharField(max_length=20, blank=True, null=True)
    site_area = models.CharField(max_length=10, blank=True, null=True)
    gen_loc = models.CharField(max_length=1, blank=True, null=True)
    plate = models.CharField(max_length=20, blank=True, null=True)
    loc_detail = models.CharField(max_length=255, blank=True, null=True)
    lgroup = models.CharField(max_length=30, blank=True, null=True)
    formation = models.CharField(max_length=30, blank=True, null=True)
    member = models.CharField(max_length=30, blank=True, null=True)
    bed = models.CharField(max_length=30, blank=True, null=True)
    datum_plane = models.CharField(max_length=50, blank=True, null=True)
    tos = models.FloatField(blank=True, null=True)
    bos = models.FloatField(blank=True, null=True)
    rock_type = models.CharField(max_length=15, blank=True, null=True)
    rt_adj = models.CharField(max_length=30, blank=True, null=True)
    lith_comm = models.CharField(max_length=120, blank=True, null=True)
    depo_context1 = models.CharField(max_length=10, blank=True, null=True)
    depo_context2 = models.CharField(max_length=10, blank=True, null=True)
    depo_context3 = models.CharField(max_length=10, blank=True, null=True)
    depo_context4 = models.CharField(max_length=10, blank=True, null=True)
    depo_comm = models.CharField(max_length=120, blank=True, null=True)
    sed_env_1 = models.CharField(max_length=13, blank=True, null=True)
    sed_env_2 = models.CharField(max_length=15, blank=True, null=True)
    event_circum = models.CharField(max_length=15, blank=True, null=True)
    se_comm = models.CharField(max_length=50, blank=True, null=True)
    climate_type = models.CharField(max_length=15, blank=True, null=True)
    biome = models.CharField(max_length=15, blank=True, null=True)
    v_ht = models.CharField(max_length=4, blank=True, null=True)
    v_struct = models.CharField(max_length=9, blank=True, null=True)
    v_envi_det = models.CharField(max_length=80, blank=True, null=True)
    disturb = models.CharField(max_length=16, blank=True, null=True)
    nutrients = models.CharField(max_length=7, blank=True, null=True)
    water = models.CharField(max_length=8, blank=True, null=True)
    seasonality = models.CharField(max_length=16, blank=True, null=True)
    seas_intens = models.CharField(max_length=3, blank=True, null=True)
    pri_prod = models.CharField(max_length=4, blank=True, null=True)
    moisture = models.CharField(max_length=3, blank=True, null=True)
    temperature = models.CharField(max_length=4, blank=True, null=True)
    assem_fm = models.CharField(max_length=12, blank=True, null=True)
    transport = models.CharField(max_length=15, blank=True, null=True)
    trans_mod = models.CharField(max_length=9, blank=True, null=True)
    weath_trmp = models.CharField(max_length=9, blank=True, null=True)
    pt_conc = models.CharField(max_length=14, blank=True, null=True)
    size_type = models.CharField(max_length=5, blank=True, null=True)
    vert_pres = models.CharField(max_length=12, blank=True, null=True)
    plant_pres = models.CharField(max_length=12, blank=True, null=True)
    invert_pres = models.CharField(max_length=12, blank=True, null=True)
    time_rep = models.CharField(max_length=9, blank=True, null=True)
    appr_num_spm = models.IntegerField(blank=True, null=True)
    num_spm = models.IntegerField(blank=True, null=True)
    true_quant = models.CharField(max_length=1, blank=True, null=True)
    complete = models.CharField(max_length=1, blank=True, null=True)
    num_quad = models.IntegerField(blank=True, null=True)
    taph_comm = models.CharField(max_length=120, blank=True, null=True)
    tax_comm = models.CharField(max_length=255, blank=True, null=True)
    loc_status = models.IntegerField(blank=True, null=True)
    estimate_precip = models.IntegerField(blank=True, null=True)
    estimate_temp = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    estimate_npp = models.IntegerField(blank=True, null=True)
    pers_woody_cover = models.IntegerField(blank=True, null=True)
    pers_pollen_ap = models.IntegerField(blank=True, null=True)
    pers_pollen_nap = models.IntegerField(blank=True, null=True)
    pers_pollen_other = models.IntegerField(blank=True, null=True)
    hominin_skeletal_remains = models.IntegerField()
    bipedal_footprints = models.IntegerField()
    stone_tool_technology = models.IntegerField()
    stone_tool_cut_marks_on_bones = models.IntegerField()
    technological_mode_1 = models.IntegerField(blank=True, null=True)
    technological_mode_2 = models.IntegerField(blank=True, null=True)
    technological_mode_3 = models.IntegerField(blank=True, null=True)
    cultural_stage_1 = models.CharField(max_length=64, blank=True, null=True)
    cultural_stage_2 = models.CharField(max_length=64, blank=True, null=True)
    cultural_stage_3 = models.CharField(max_length=64, blank=True, null=True)
    regional_culture_1 = models.CharField(max_length=64, blank=True, null=True)
    regional_culture_2 = models.CharField(max_length=64, blank=True, null=True)
    regional_culture_3 = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'now_loc'

class NowCollectingMethod(models.Model):
    lid = models.OneToOneField(NowLocality, models.CASCADE, db_column='lid')
    coll_meth = models.CharField(max_length=21)

    class Meta:
        db_table = 'now_coll_meth'
        unique_together = (('lid', 'coll_meth'),)

class NowLocalityUpdate(models.Model):
    luid = models.AutoField(primary_key=True)
    lau_coordinator = models.ForeignKey(ComPeople, models.DO_NOTHING, db_column='lau_coordinator', related_name='%(class)s_lau_coordinator')
    lau_authorizer = models.ForeignKey(ComPeople, models.DO_NOTHING, db_column='lau_authorizer', related_name='%(class)s_lau_authorizer')
    lid = models.ForeignKey(NowLocality, models.CASCADE, db_column='lid')
    lau_date = models.DateField(blank=True, null=True)
    lau_comment = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'now_lau'

class NowLocalityUpdateReference(models.Model):
    luid = models.OneToOneField(NowLocalityUpdate, models.CASCADE, db_column='luid')
    rid = models.ForeignKey(RefReference, models.DO_NOTHING, db_column='rid')

    class Meta:
        db_table = 'now_lr'
        unique_together = (('luid', 'rid'),)


class NowLocalitySpecies(models.Model):
    lid = models.OneToOneField(NowLocality, models.DO_NOTHING, db_column='lid')
    species = models.ForeignKey(ComSpecies, models.DO_NOTHING)
    nis = models.IntegerField(blank=True, null=True)
    pct = models.FloatField(blank=True, null=True)
    quad = models.IntegerField(blank=True, null=True)
    mni = models.IntegerField(blank=True, null=True)
    qua = models.CharField(max_length=1, blank=True, null=True)
    id_status = models.CharField(max_length=20, blank=True, null=True)
    orig_entry = models.CharField(max_length=120, blank=True, null=True)
    source_name = models.CharField(max_length=120, blank=True, null=True)
    body_mass = models.BigIntegerField(blank=True, null=True)
    mesowear = models.CharField(max_length=3, blank=True, null=True)
    mw_or_high = models.IntegerField(blank=True, null=True)
    mw_or_low = models.IntegerField(blank=True, null=True)
    mw_cs_sharp = models.IntegerField(blank=True, null=True)
    mw_cs_round = models.IntegerField(blank=True, null=True)
    mw_cs_blunt = models.IntegerField(blank=True, null=True)
    mw_scale_min = models.IntegerField(blank=True, null=True)
    mw_scale_max = models.IntegerField(blank=True, null=True)
    mw_value = models.IntegerField(blank=True, null=True)
    microwear = models.CharField(max_length=7, blank=True, null=True)
    dc13_mean = models.FloatField(blank=True, null=True)
    dc13_n = models.IntegerField(blank=True, null=True)
    dc13_max = models.FloatField(blank=True, null=True)
    dc13_min = models.FloatField(blank=True, null=True)
    dc13_stdev = models.FloatField(blank=True, null=True)
    do18_mean = models.FloatField(blank=True, null=True)
    do18_n = models.IntegerField(blank=True, null=True)
    do18_max = models.FloatField(blank=True, null=True)
    do18_min = models.FloatField(blank=True, null=True)
    do18_stdev = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'now_ls'
        unique_together = (('lid', 'species'),)


class NowLocalitySpeciesCopy(models.Model):
    lid = models.IntegerField(primary_key=True)
    species_id = models.IntegerField()
    nis = models.IntegerField(blank=True, null=True)
    pct = models.FloatField(blank=True, null=True)
    quad = models.IntegerField(blank=True, null=True)
    mni = models.IntegerField(blank=True, null=True)
    qua = models.CharField(max_length=1, blank=True, null=True)
    id_status = models.CharField(max_length=20, blank=True, null=True)
    orig_entry = models.CharField(max_length=120, blank=True, null=True)
    source_name = models.CharField(max_length=120, blank=True, null=True)
    body_mass = models.BigIntegerField(blank=True, null=True)
    mesowear = models.CharField(max_length=3, blank=True, null=True)
    mw_or_high = models.IntegerField(blank=True, null=True)
    mw_or_low = models.IntegerField(blank=True, null=True)
    mw_cs_sharp = models.IntegerField(blank=True, null=True)
    mw_cs_round = models.IntegerField(blank=True, null=True)
    mw_cs_blunt = models.IntegerField(blank=True, null=True)
    mw_scale_min = models.IntegerField(blank=True, null=True)
    mw_scale_max = models.IntegerField(blank=True, null=True)
    mw_value = models.IntegerField(blank=True, null=True)
    microwear = models.CharField(max_length=7, blank=True, null=True)
    dc13_mean = models.FloatField(blank=True, null=True)
    dc13_n = models.IntegerField(blank=True, null=True)
    dc13_max = models.FloatField(blank=True, null=True)
    dc13_min = models.FloatField(blank=True, null=True)
    dc13_stdev = models.FloatField(blank=True, null=True)
    do18_mean = models.FloatField(blank=True, null=True)
    do18_n = models.IntegerField(blank=True, null=True)
    do18_max = models.FloatField(blank=True, null=True)
    do18_min = models.FloatField(blank=True, null=True)
    do18_stdev = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'now_ls_copy'


class NowMuseum(models.Model):
    """Museum where significant material from the locality is housed"""
    lid = models.OneToOneField(NowLocality, models.CASCADE, db_column='lid')
    museum = models.ForeignKey(ComMuseumList, models.DO_NOTHING, db_column='museum')

    class Meta:
        db_table = 'now_mus'
        unique_together = (('lid', 'museum'),)

class NowProject(models.Model):
    pid = models.AutoField(primary_key=True)
    contact = models.ForeignKey(ComPeople, models.DO_NOTHING, db_column='contact')
    proj_code = models.CharField(max_length=10, blank=True, null=True)
    proj_name = models.CharField(max_length=80, blank=True, null=True)
    proj_status = models.CharField(max_length=10, blank=True, null=True)
    proj_records = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'now_proj'

class NowProjectLocality(models.Model):
    lid = models.OneToOneField(NowLocality, models.CASCADE, db_column='lid')
    pid = models.ForeignKey(NowProject, models.DO_NOTHING, db_column='pid')

    class Meta:
        db_table = 'now_plr'
        unique_together = (('lid', 'pid'),)

class NowProjectPeople(models.Model):
    pid = models.OneToOneField(NowProject, models.DO_NOTHING, db_column='pid')
    initials = models.ForeignKey(ComPeople, models.DO_NOTHING, db_column='initials')

    class Meta:
        db_table = 'now_proj_people'
        unique_together = (('pid', 'initials'),)


class NowProjectSpecies(models.Model):
    pid = models.OneToOneField(NowProject, models.DO_NOTHING, db_column='pid')
    species = models.ForeignKey(ComSpecies, models.DO_NOTHING)

    class Meta:
        db_table = 'now_psr'
        unique_together = (('pid', 'species'),)


class NowRegCoord(models.Model):
    reg_coord_id = models.AutoField(primary_key=True)
    region = models.CharField(max_length=80)

    class Meta:
        db_table = 'now_reg_coord'


class NowRegCoordCountry(models.Model):
    reg_coord = models.OneToOneField(NowRegCoord, models.DO_NOTHING)
    country = models.CharField(max_length=80)

    class Meta:
        db_table = 'now_reg_coord_country'
        unique_together = (('reg_coord', 'country'),)


class NowRegCoordPeople(models.Model):
    reg_coord = models.OneToOneField(NowRegCoord, models.DO_NOTHING)
    initials = models.ForeignKey(ComPeople, models.DO_NOTHING, db_column='initials')

    class Meta:
        db_table = 'now_reg_coord_people'
        unique_together = (('reg_coord', 'initials'),)


class NowRegionalCulture(models.Model):
    regional_culture_id = models.CharField(primary_key=True, max_length=50)
    regional_culture_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'now_regional_culture'


class NowSpeciesUpdate(models.Model):
    suid = models.AutoField(primary_key=True)
    sau_coordinator = models.ForeignKey(ComPeople, models.DO_NOTHING, db_column='sau_coordinator', related_name='%(class)s_sau_coordinator')
    sau_authorizer = models.ForeignKey(ComPeople, models.DO_NOTHING, db_column='sau_authorizer', related_name='%(class)s_sau_authorizer')
    species = models.ForeignKey(ComSpecies, models.DO_NOTHING)
    sau_date = models.DateField(blank=True, null=True)
    sau_comment = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        db_table = 'now_sau'


class NowSpCoord(models.Model):
    sp_coord_id = models.AutoField(primary_key=True)
    tax_group = models.CharField(max_length=80)

    class Meta:
        db_table = 'now_sp_coord'


class NowSpCoordPeople(models.Model):
    sp_coord = models.OneToOneField(NowSpCoord, models.DO_NOTHING)
    initials = models.ForeignKey(ComPeople, models.DO_NOTHING, db_column='initials')

    class Meta:
        db_table = 'now_sp_coord_people'
        unique_together = (('sp_coord', 'initials'),)


class NowSpCoordTaxa(models.Model):
    sp_coord = models.OneToOneField(NowSpCoord, models.DO_NOTHING)
    order_name = models.CharField(max_length=30)
    family_name = models.CharField(max_length=30)

    class Meta:
        db_table = 'now_sp_coord_taxa'
        unique_together = (('sp_coord', 'order_name', 'family_name'),)


class NowSpeciesUpdateReference(models.Model):
    suid = models.OneToOneField(NowSpeciesUpdate, models.DO_NOTHING, db_column='suid', primary_key=True)
    rid = models.ForeignKey(RefReference, models.DO_NOTHING, db_column='rid')

    class Meta:
        db_table = 'now_sr'
        unique_together = (('suid', 'rid'),)


class NowSedimentaryStructure(models.Model):
    lid = models.OneToOneField(NowLocality, models.DO_NOTHING, db_column='lid', primary_key=True)
    sed_struct = models.CharField(max_length=30)

    class Meta:
        db_table = 'now_ss'
        unique_together = (('lid', 'sed_struct'),)


class NowSedimentaryStructureValue(models.Model):
    ss_value = models.CharField(primary_key=True, max_length=30)
    category = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        db_table = 'now_ss_values'


class NowStratCoord(models.Model):
    strat_coord_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=80)

    class Meta:
        db_table = 'now_strat_coord'


class NowStratCoordPeople(models.Model):
    strat_coord = models.OneToOneField(NowStratCoord, models.DO_NOTHING, primary_key=True)
    initials = models.ForeignKey(ComPeople, models.DO_NOTHING, db_column='initials')

    class Meta:
        db_table = 'now_strat_coord_people'
        unique_together = (('strat_coord', 'initials'),)


class NowLocalitySynonym(models.Model):
    syn_id = models.AutoField(primary_key=True)
    lid = models.ForeignKey(NowLocality, models.DO_NOTHING, db_column='lid')
    synonym = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = 'now_syn_loc'


class NowTimeUnitUpdate(models.Model):
    tuid = models.AutoField(primary_key=True)
    tau_coordinator = models.ForeignKey(ComPeople, models.DO_NOTHING, db_column='tau_coordinator', related_name='%(class)s_tau_coordinator')
    tau_authorizer = models.ForeignKey(ComPeople, models.DO_NOTHING, db_column='tau_authorizer', related_name='%(class)s_tau_authorizer')
    tu_name = models.ForeignKey(NowTimeUnit, models.DO_NOTHING, db_column='tu_name')
    tau_date = models.DateField(blank=True, null=True)
    tau_comment = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'now_tau'

class NowTimeUpdate(models.Model):
    time_update_id = models.AutoField(primary_key=True)
    tu_name = models.ForeignKey(NowTimeUnit, models.DO_NOTHING, db_column='tu_name')
    tuid = models.ForeignKey(NowTimeUnitUpdate, models.DO_NOTHING, db_column='tuid', blank=True, null=True)
    lower_buid = models.ForeignKey(NowTimeUnitBoundaryUpdate, models.DO_NOTHING, db_column='lower_buid', blank=True, null=True, related_name='%(class)s_lower_buid')
    upper_buid = models.ForeignKey(NowTimeUnitBoundaryUpdate, models.DO_NOTHING, db_column='upper_buid', blank=True, null=True, related_name='%(class)s_upper_buid')
    coordinator = models.CharField(max_length=10)
    authorizer = models.CharField(max_length=10)
    date = models.DateField(blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'now_time_update'


class NowTimeUnitUpdateReference(models.Model):
    tuid = models.OneToOneField(NowTimeUnitUpdate, models.DO_NOTHING, db_column='tuid', primary_key=True)
    rid = models.ForeignKey(RefReference, models.DO_NOTHING, db_column='rid')

    class Meta:
        db_table = 'now_tr'
        unique_together = (('tuid', 'rid'),)

class NowTimeUnitBoundaryReference(models.Model):
    bid = models.OneToOneField(NowTimeUnitBoundary, models.DO_NOTHING, db_column='bid', primary_key=True)
    rid = models.ForeignKey(RefReference, models.DO_NOTHING, db_column='rid')

    class Meta:
        db_table = 'now_tur'
        unique_together = (('bid', 'rid'),)


class NowVCollMethValuesList(models.Model):
    coll_meth_value = models.CharField(max_length=21, db_collation='utf8mb3_general_ci')

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'now_v_coll_meth_values_list'


class NowVExportLoc(models.Model):
    lid = models.IntegerField()
    loc_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci')
    dms_lat = models.CharField(max_length=14, db_collation='utf8mb3_general_ci', blank=True, null=True)
    dms_long = models.CharField(max_length=14, db_collation='utf8mb3_general_ci', blank=True, null=True)
    dec_lat = models.FloatField()
    dec_long = models.FloatField()
    max_age = models.FloatField()
    bfa_max = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    bfa_max_abs = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    frac_max = models.CharField(max_length=9, db_collation='utf8mb3_general_ci', blank=True, null=True)
    min_age = models.FloatField()
    bfa_min = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    bfa_min_abs = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    frac_min = models.CharField(max_length=9, db_collation='utf8mb3_general_ci', blank=True, null=True)
    chron = models.CharField(max_length=40, db_collation='utf8mb3_general_ci', blank=True, null=True)
    age_comm = models.CharField(max_length=120, db_collation='utf8mb3_general_ci', blank=True, null=True)
    basin = models.CharField(max_length=120, db_collation='utf8mb3_general_ci', blank=True, null=True)
    subbasin = models.CharField(max_length=120, db_collation='utf8mb3_general_ci', blank=True, null=True)
    country = models.CharField(max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)
    state = models.CharField(max_length=20, db_collation='utf8mb3_general_ci', blank=True, null=True)
    county = models.CharField(max_length=20, db_collation='utf8mb3_general_ci', blank=True, null=True)
    appr_num_spm = models.IntegerField(blank=True, null=True)
    gen_loc = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    loc_synonyms = models.TextField(db_collation='utf8mb3_general_ci', blank=True, null=True)
    loc_status = models.IntegerField(blank=True, null=True)
    estimate_precip = models.IntegerField(blank=True, null=True)
    estimate_temp = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    estimate_npp = models.IntegerField(blank=True, null=True)
    pers_woody_cover = models.IntegerField(blank=True, null=True)
    pers_pollen_ap = models.IntegerField(blank=True, null=True)
    pers_pollen_nap = models.IntegerField(blank=True, null=True)
    pers_pollen_other = models.IntegerField(blank=True, null=True)
    hominin_skeletal_remains = models.IntegerField()
    bipedal_footprints = models.IntegerField()
    stone_tool_technology = models.IntegerField()
    stone_tool_cut_marks_on_bones = models.IntegerField()
    technological_mode_1 = models.IntegerField(blank=True, null=True)
    cultural_stage_1 = models.CharField(max_length=64, db_collation='utf8mb3_general_ci', blank=True, null=True)
    regional_culture_1 = models.CharField(max_length=64, db_collation='utf8mb3_general_ci', blank=True, null=True)
    technological_mode_2 = models.IntegerField(blank=True, null=True)
    cultural_stage_2 = models.CharField(max_length=64, db_collation='utf8mb3_general_ci', blank=True, null=True)
    regional_culture_2 = models.CharField(max_length=64, db_collation='utf8mb3_general_ci', blank=True, null=True)
    technological_mode_3 = models.IntegerField(blank=True, null=True)
    cultural_stage_3 = models.CharField(max_length=64, db_collation='utf8mb3_general_ci', blank=True, null=True)
    regional_culture_3 = models.CharField(max_length=64, db_collation='utf8mb3_general_ci', blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'now_v_export_loc'


class NowVExportLocsp(models.Model):
    lid = models.IntegerField(blank=True, null=True)
    loc_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    dms_lat = models.CharField(max_length=14, db_collation='utf8mb3_general_ci', blank=True, null=True)
    dms_long = models.CharField(max_length=14, db_collation='utf8mb3_general_ci', blank=True, null=True)
    dec_lat = models.FloatField(blank=True, null=True)
    dec_long = models.FloatField(blank=True, null=True)
    max_age = models.FloatField(blank=True, null=True)
    bfa_max = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    bfa_max_abs = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    frac_max = models.CharField(max_length=9, db_collation='utf8mb3_general_ci', blank=True, null=True)
    min_age = models.FloatField(blank=True, null=True)
    bfa_min = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    bfa_min_abs = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    frac_min = models.CharField(max_length=9, db_collation='utf8mb3_general_ci', blank=True, null=True)
    chron = models.CharField(max_length=40, db_collation='utf8mb3_general_ci', blank=True, null=True)
    age_comm = models.CharField(max_length=120, db_collation='utf8mb3_general_ci', blank=True, null=True)
    basin = models.CharField(max_length=120, db_collation='utf8mb3_general_ci', blank=True, null=True)
    subbasin = models.CharField(max_length=120, db_collation='utf8mb3_general_ci', blank=True, null=True)
    country = models.CharField(max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)
    state = models.CharField(max_length=20, db_collation='utf8mb3_general_ci', blank=True, null=True)
    county = models.CharField(max_length=20, db_collation='utf8mb3_general_ci', blank=True, null=True)
    appr_num_spm = models.IntegerField(blank=True, null=True)
    gen_loc = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    loc_synonyms = models.TextField(db_collation='utf8mb3_general_ci', blank=True, null=True)
    loc_status = models.IntegerField(blank=True, null=True)
    estimate_precip = models.IntegerField(blank=True, null=True)
    estimate_temp = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    estimate_npp = models.IntegerField(blank=True, null=True)
    pers_woody_cover = models.IntegerField(blank=True, null=True)
    pers_pollen_ap = models.IntegerField(blank=True, null=True)
    pers_pollen_nap = models.IntegerField(blank=True, null=True)
    pers_pollen_other = models.IntegerField(blank=True, null=True)
    hominin_skeletal_remains = models.IntegerField(blank=True, null=True)
    bipedal_footprints = models.IntegerField(blank=True, null=True)
    stone_tool_technology = models.IntegerField(blank=True, null=True)
    stone_tool_cut_marks_on_bones = models.IntegerField(blank=True, null=True)
    technological_mode_1 = models.IntegerField(blank=True, null=True)
    cultural_stage_1 = models.CharField(max_length=64, db_collation='utf8mb3_general_ci', blank=True, null=True)
    regional_culture_1 = models.CharField(max_length=64, db_collation='utf8mb3_general_ci', blank=True, null=True)
    technological_mode_2 = models.IntegerField(blank=True, null=True)
    cultural_stage_2 = models.CharField(max_length=64, db_collation='utf8mb3_general_ci', blank=True, null=True)
    regional_culture_2 = models.CharField(max_length=64, db_collation='utf8mb3_general_ci', blank=True, null=True)
    technological_mode_3 = models.IntegerField(blank=True, null=True)
    cultural_stage_3 = models.CharField(max_length=64, db_collation='utf8mb3_general_ci', blank=True, null=True)
    regional_culture_3 = models.CharField(max_length=64, db_collation='utf8mb3_general_ci', blank=True, null=True)
    species_id = models.IntegerField()
    order_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci')
    family_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci')
    subfamily_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    subclass_or_superorder_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    suborder_or_superfamily_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    genus_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci')
    species_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci')
    unique_identifier = models.CharField(max_length=50, db_collation='utf8mb3_general_ci')
    taxonomic_status = models.CharField(max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)
    sv_length = models.CharField(max_length=7, db_collation='utf8mb3_general_ci', blank=True, null=True)
    body_mass = models.BigIntegerField(blank=True, null=True)
    sd_size = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    sd_display = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    tshm = models.CharField(max_length=3, db_collation='utf8mb3_general_ci', blank=True, null=True)
    tht = models.CharField(max_length=3, db_collation='utf8mb3_general_ci', blank=True, null=True)
    crowntype = models.CharField(max_length=6, db_collation='utf8mb3_general_ci', blank=True, null=True)
    diet1 = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    diet2 = models.CharField(max_length=9, db_collation='utf8mb3_general_ci', blank=True, null=True)
    diet3 = models.CharField(max_length=10, db_collation='utf8mb3_general_ci', blank=True, null=True)
    locomo1 = models.CharField(max_length=2, db_collation='utf8mb3_general_ci', blank=True, null=True)
    locomo2 = models.CharField(max_length=15, db_collation='utf8mb3_general_ci', blank=True, null=True)
    locomo3 = models.CharField(max_length=15, db_collation='utf8mb3_general_ci', blank=True, null=True)
    sp_status = models.IntegerField(blank=True, null=True)
    sp_comment = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    horizodonty = models.CharField(max_length=3, db_collation='utf8mb3_general_ci', blank=True, null=True)
    microwear = models.CharField(max_length=7, db_collation='utf8mb3_general_ci', blank=True, null=True)
    mesowear = models.CharField(max_length=3, db_collation='utf8mb3_general_ci', blank=True, null=True)
    mw_or_high = models.IntegerField(blank=True, null=True)
    mw_or_low = models.IntegerField(blank=True, null=True)
    mw_cs_sharp = models.IntegerField(blank=True, null=True)
    mw_cs_round = models.IntegerField(blank=True, null=True)
    mw_cs_blunt = models.IntegerField(blank=True, null=True)
    mw_scale_min = models.IntegerField(blank=True, null=True)
    mw_scale_max = models.IntegerField(blank=True, null=True)
    mw_value = models.IntegerField(blank=True, null=True)
    cusp_shape = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    cusp_count_buccal = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    cusp_count_lingual = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    loph_count_lon = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    loph_count_trs = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    fct_al = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    fct_ol = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    fct_sf = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    fct_ot = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    fct_cm = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    id_status = models.CharField(max_length=20, db_collation='utf8mb3_general_ci', blank=True, null=True)
    orig_entry = models.CharField(max_length=120, db_collation='utf8mb3_general_ci', blank=True, null=True)
    source_name = models.CharField(max_length=120, db_collation='utf8mb3_general_ci', blank=True, null=True)
    ls_microwear = models.CharField(max_length=7, db_collation='utf8mb3_general_ci', blank=True, null=True)
    ls_mesowear = models.CharField(max_length=3, db_collation='utf8mb3_general_ci', blank=True, null=True)
    ls_mw_or_high = models.IntegerField(blank=True, null=True)
    ls_mw_or_low = models.IntegerField(blank=True, null=True)
    ls_mw_cs_sharp = models.IntegerField(blank=True, null=True)
    ls_mw_cs_round = models.IntegerField(blank=True, null=True)
    ls_mw_cs_blunt = models.IntegerField(blank=True, null=True)
    ls_mw_scale_min = models.IntegerField(blank=True, null=True)
    ls_mw_scale_max = models.IntegerField(blank=True, null=True)
    ls_mw_value = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'now_v_export_locsp'


class NowVExportNaspecies(models.Model):
    lid = models.CharField(max_length=3, db_collation='utf8mb4_general_ci')
    loc_name = models.CharField(max_length=3, db_collation='utf8mb4_general_ci')
    dms_lat = models.CharField(max_length=3, db_collation='utf8mb4_general_ci')
    dms_long = models.CharField(max_length=3, db_collation='utf8mb4_general_ci')
    dec_lat = models.CharField(max_length=3, db_collation='utf8mb4_general_ci')
    dec_long = models.CharField(max_length=3, db_collation='utf8mb4_general_ci')
    max_age = models.CharField(max_length=3, db_collation='utf8mb4_general_ci')
    bfa_max = models.CharField(max_length=3, db_collation='utf8mb4_general_ci')
    bfa_max_abs = models.CharField(max_length=3, db_collation='utf8mb4_general_ci')
    frac_max = models.CharField(max_length=3, db_collation='utf8mb4_general_ci')
    min_age = models.CharField(max_length=3, db_collation='utf8mb4_general_ci')
    bfa_min = models.CharField(max_length=3, db_collation='utf8mb4_general_ci')
    bfa_min_abs = models.CharField(max_length=3, db_collation='utf8mb4_general_ci')
    frac_min = models.CharField(max_length=3, db_collation='utf8mb4_general_ci')
    chron = models.CharField(max_length=3, db_collation='utf8mb4_general_ci')
    age_comm = models.CharField(db_collation='utf8mb4_general_ci', max_length=128)
    basin = models.CharField(db_collation='utf8mb4_general_ci', max_length=128)
    subbasin = models.CharField(db_collation='utf8mb4_general_ci', max_length=128)
    country = models.CharField(max_length=3, db_collation='utf8mb4_general_ci')
    state = models.CharField(max_length=3, db_collation='utf8mb4_general_ci')
    county = models.CharField(max_length=3, db_collation='utf8mb4_general_ci')
    appr_num_spm = models.CharField(max_length=3, db_collation='utf8mb4_general_ci')
    gen_loc = models.CharField(max_length=3, db_collation='utf8mb4_general_ci')
    loc_synonyms = models.CharField(max_length=3, db_collation='utf8mb4_general_ci')
    loc_status = models.CharField(max_length=3, db_collation='utf8mb4_general_ci')
    mean_hypsodonty = models.CharField(max_length=3, db_collation='utf8mb4_general_ci')
    estimate_precip = models.CharField(max_length=3, db_collation='utf8mb4_general_ci')
    estimate_temp = models.CharField(max_length=3, db_collation='utf8mb4_general_ci')
    estimate_npp = models.CharField(max_length=3, db_collation='utf8mb4_general_ci')
    pers_woody_cover = models.CharField(max_length=3, db_collation='utf8mb4_general_ci')
    pers_pollen_ap = models.CharField(max_length=3, db_collation='utf8mb4_general_ci')
    pers_pollen_nap = models.CharField(max_length=3, db_collation='utf8mb4_general_ci')
    pers_pollen_other = models.CharField(max_length=3, db_collation='utf8mb4_general_ci')
    species_id = models.IntegerField()
    order_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci')
    family_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci')
    subfamily_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    subclass_or_superorder_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    suborder_or_superfamily_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    genus_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci')
    species_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci')
    unique_identifier = models.CharField(max_length=50, db_collation='utf8mb3_general_ci')
    taxonomic_status = models.CharField(max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)
    sv_length = models.CharField(max_length=7, db_collation='utf8mb3_general_ci', blank=True, null=True)
    body_mass = models.BigIntegerField(blank=True, null=True)
    sd_size = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    sd_display = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    tshm = models.CharField(max_length=3, db_collation='utf8mb3_general_ci', blank=True, null=True)
    tht = models.CharField(max_length=3, db_collation='utf8mb3_general_ci', blank=True, null=True)
    crowntype = models.CharField(max_length=6, db_collation='utf8mb3_general_ci', blank=True, null=True)
    diet1 = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    diet2 = models.CharField(max_length=9, db_collation='utf8mb3_general_ci', blank=True, null=True)
    diet3 = models.CharField(max_length=10, db_collation='utf8mb3_general_ci', blank=True, null=True)
    locomo1 = models.CharField(max_length=2, db_collation='utf8mb3_general_ci', blank=True, null=True)
    locomo2 = models.CharField(max_length=15, db_collation='utf8mb3_general_ci', blank=True, null=True)
    locomo3 = models.CharField(max_length=15, db_collation='utf8mb3_general_ci', blank=True, null=True)
    sp_status = models.IntegerField(blank=True, null=True)
    sp_comment = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    horizodonty = models.CharField(max_length=3, db_collation='utf8mb3_general_ci', blank=True, null=True)
    microwear = models.CharField(max_length=7, db_collation='utf8mb3_general_ci', blank=True, null=True)
    mesowear = models.CharField(max_length=3, db_collation='utf8mb3_general_ci', blank=True, null=True)
    mw_or_high = models.IntegerField(blank=True, null=True)
    mw_or_low = models.IntegerField(blank=True, null=True)
    mw_cs_sharp = models.IntegerField(blank=True, null=True)
    mw_cs_round = models.IntegerField(blank=True, null=True)
    mw_cs_blunt = models.IntegerField(blank=True, null=True)
    mw_scale_min = models.IntegerField(blank=True, null=True)
    mw_scale_max = models.IntegerField(blank=True, null=True)
    mw_value = models.IntegerField(blank=True, null=True)
    cusp_shape = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    cusp_count_buccal = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    cusp_count_lingual = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    loph_count_lon = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    loph_count_trs = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    fct_al = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    fct_ol = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    fct_sf = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    fct_ot = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    fct_cm = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    id_status = models.CharField(max_length=3, db_collation='utf8mb4_general_ci')
    orig_entry = models.CharField(max_length=3, db_collation='utf8mb4_general_ci')
    source_name = models.CharField(max_length=3, db_collation='utf8mb4_general_ci')
    ls_microwear = models.CharField(max_length=3, db_collation='utf8mb4_general_ci')
    ls_mesowear = models.CharField(max_length=3, db_collation='utf8mb4_general_ci')
    ls_mesowear_score = models.CharField(max_length=3, db_collation='utf8mb4_general_ci')
    ls_mw_or_high = models.CharField(max_length=3, db_collation='utf8mb4_general_ci')
    ls_mw_or_low = models.CharField(max_length=3, db_collation='utf8mb4_general_ci')
    ls_mw_cs_sharp = models.CharField(max_length=3, db_collation='utf8mb4_general_ci')
    ls_mw_cs_round = models.CharField(max_length=3, db_collation='utf8mb4_general_ci')
    ls_mw_cs_blunt = models.CharField(max_length=3, db_collation='utf8mb4_general_ci')
    ls_mw_scale_min = models.CharField(max_length=3, db_collation='utf8mb4_general_ci')
    ls_mw_scale_max = models.CharField(max_length=3, db_collation='utf8mb4_general_ci')
    ls_mw_value = models.CharField(max_length=3, db_collation='utf8mb4_general_ci')

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'now_v_export_naspecies'


class NowVLocalityAge(models.Model):
    lid = models.IntegerField()
    loc_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci')
    country = models.CharField(max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)
    date_meth = models.CharField(max_length=9, db_collation='utf8mb3_general_ci')
    min_age = models.FloatField()
    bfa_min_abs = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    bfa_min = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    frac_min = models.CharField(max_length=9, db_collation='utf8mb3_general_ci', blank=True, null=True)
    max_age = models.FloatField()
    bfa_max_abs = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    bfa_max = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    frac_max = models.CharField(max_length=9, db_collation='utf8mb3_general_ci', blank=True, null=True)
    chron = models.CharField(max_length=40, db_collation='utf8mb3_general_ci', blank=True, null=True)
    age_comm = models.CharField(max_length=120, db_collation='utf8mb3_general_ci', blank=True, null=True)
    basin = models.CharField(max_length=120, db_collation='utf8mb3_general_ci', blank=True, null=True)
    subbasin = models.CharField(max_length=120, db_collation='utf8mb3_general_ci', blank=True, null=True)
    lgroup = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    formation = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    member = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    bed = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    datum_plane = models.CharField(max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)
    tos = models.FloatField(blank=True, null=True)
    bos = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'now_v_locality_age'


class NowVLocalityArchaeology(models.Model):
    lid = models.IntegerField()
    loc_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci')
    hominin_skeletal_remains = models.IntegerField()
    bipedal_footprints = models.IntegerField()
    stone_tool_technology = models.IntegerField()
    stone_tool_cut_marks_on_bones = models.IntegerField()
    technological_mode_1 = models.IntegerField(blank=True, null=True)
    cultural_stage_1 = models.CharField(max_length=64, db_collation='utf8mb3_general_ci', blank=True, null=True)
    regional_culture_1 = models.CharField(max_length=64, db_collation='utf8mb3_general_ci', blank=True, null=True)
    technological_mode_2 = models.IntegerField(blank=True, null=True)
    cultural_stage_2 = models.CharField(max_length=64, db_collation='utf8mb3_general_ci', blank=True, null=True)
    regional_culture_2 = models.CharField(max_length=64, db_collation='utf8mb3_general_ci', blank=True, null=True)
    technological_mode_3 = models.IntegerField(blank=True, null=True)
    cultural_stage_3 = models.CharField(max_length=64, db_collation='utf8mb3_general_ci', blank=True, null=True)
    regional_culture_3 = models.CharField(max_length=64, db_collation='utf8mb3_general_ci', blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'now_v_locality_archaeology'


class NowVLocalityClimate(models.Model):
    lid = models.IntegerField()
    loc_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci')
    country = models.CharField(max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)
    climate_type = models.CharField(max_length=15, db_collation='utf8mb3_general_ci', blank=True, null=True)
    temperature = models.CharField(max_length=4, db_collation='utf8mb3_general_ci', blank=True, null=True)
    moisture = models.CharField(max_length=3, db_collation='utf8mb3_general_ci', blank=True, null=True)
    disturb = models.CharField(max_length=16, db_collation='utf8mb3_general_ci', blank=True, null=True)
    biome = models.CharField(max_length=15, db_collation='utf8mb3_general_ci', blank=True, null=True)
    v_ht = models.CharField(max_length=4, db_collation='utf8mb3_general_ci', blank=True, null=True)
    v_struct = models.CharField(max_length=9, db_collation='utf8mb3_general_ci', blank=True, null=True)
    pri_prod = models.CharField(max_length=4, db_collation='utf8mb3_general_ci', blank=True, null=True)
    v_envi_det = models.CharField(max_length=80, db_collation='utf8mb3_general_ci', blank=True, null=True)
    seasonality = models.CharField(max_length=16, db_collation='utf8mb3_general_ci', blank=True, null=True)
    seas_intens = models.CharField(max_length=3, db_collation='utf8mb3_general_ci', blank=True, null=True)
    nutrients = models.CharField(max_length=7, db_collation='utf8mb3_general_ci', blank=True, null=True)
    water = models.CharField(max_length=8, db_collation='utf8mb3_general_ci', blank=True, null=True)
    pers_pollen_ap = models.IntegerField(blank=True, null=True)
    pers_pollen_nap = models.IntegerField(blank=True, null=True)
    pers_pollen_other = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'now_v_locality_climate'


class NowVLocalityEcometrics(models.Model):
    lid = models.IntegerField()
    estimate_precip = models.IntegerField(blank=True, null=True)
    estimate_temp = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    estimate_npp = models.IntegerField(blank=True, null=True)
    pers_woody_cover = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'now_v_locality_ecometrics'


class NowVLocalityEcometricsMeanHypsodonty(models.Model):
    lid = models.IntegerField()
    mean_hypsodonty = models.DecimalField(max_digits=25, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'now_v_locality_ecometrics_mean_hypsodonty'


class NowVLocalityHeader(models.Model):
    lid = models.IntegerField()
    loc_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci')
    country = models.CharField(max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)
    state = models.CharField(max_length=20, db_collation='utf8mb3_general_ci', blank=True, null=True)
    county = models.CharField(max_length=20, db_collation='utf8mb3_general_ci', blank=True, null=True)
    site_area = models.CharField(max_length=10, db_collation='utf8mb3_general_ci', blank=True, null=True)
    dms_lat = models.CharField(max_length=14, db_collation='utf8mb3_general_ci', blank=True, null=True)
    dms_long = models.CharField(max_length=14, db_collation='utf8mb3_general_ci', blank=True, null=True)
    dec_lat = models.FloatField()
    dec_long = models.FloatField()
    approx_coord = models.IntegerField(blank=True, null=True)
    max_age = models.FloatField()
    bfa_max = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    bfa_max_abs = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    min_age = models.FloatField()
    bfa_min = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    bfa_min_abs = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    date_meth = models.CharField(max_length=9, db_collation='utf8mb3_general_ci')
    frac_max = models.CharField(max_length=9, db_collation='utf8mb3_general_ci', blank=True, null=True)
    frac_min = models.CharField(max_length=9, db_collation='utf8mb3_general_ci', blank=True, null=True)
    age_comm = models.CharField(max_length=120, db_collation='utf8mb3_general_ci', blank=True, null=True)
    chron = models.CharField(max_length=40, db_collation='utf8mb3_general_ci', blank=True, null=True)
    basin = models.CharField(max_length=120, db_collation='utf8mb3_general_ci', blank=True, null=True)
    subbasin = models.CharField(max_length=120, db_collation='utf8mb3_general_ci', blank=True, null=True)
    loc_status = models.IntegerField(blank=True, null=True)
    gen_loc = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    plate = models.CharField(max_length=20, db_collation='utf8mb3_general_ci', blank=True, null=True)
    loc_detail = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    lgroup = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    formation = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    member = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    bed = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    datum_plane = models.CharField(max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)
    tos = models.FloatField(blank=True, null=True)
    bos = models.FloatField(blank=True, null=True)
    rock_type = models.CharField(max_length=15, db_collation='utf8mb3_general_ci', blank=True, null=True)
    rt_adj = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    lith_comm = models.CharField(max_length=120, db_collation='utf8mb3_general_ci', blank=True, null=True)
    depo_context1 = models.CharField(max_length=10, db_collation='utf8mb3_general_ci', blank=True, null=True)
    depo_context2 = models.CharField(max_length=10, db_collation='utf8mb3_general_ci', blank=True, null=True)
    depo_context3 = models.CharField(max_length=10, db_collation='utf8mb3_general_ci', blank=True, null=True)
    depo_context4 = models.CharField(max_length=10, db_collation='utf8mb3_general_ci', blank=True, null=True)
    depo_comm = models.CharField(max_length=120, db_collation='utf8mb3_general_ci', blank=True, null=True)
    sed_env_1 = models.CharField(max_length=13, db_collation='utf8mb3_general_ci', blank=True, null=True)
    sed_env_2 = models.CharField(max_length=15, db_collation='utf8mb3_general_ci', blank=True, null=True)
    event_circum = models.CharField(max_length=15, db_collation='utf8mb3_general_ci', blank=True, null=True)
    se_comm = models.CharField(max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)
    climate_type = models.CharField(max_length=15, db_collation='utf8mb3_general_ci', blank=True, null=True)
    biome = models.CharField(max_length=15, db_collation='utf8mb3_general_ci', blank=True, null=True)
    v_ht = models.CharField(max_length=4, db_collation='utf8mb3_general_ci', blank=True, null=True)
    v_struct = models.CharField(max_length=9, db_collation='utf8mb3_general_ci', blank=True, null=True)
    v_envi_det = models.CharField(max_length=80, db_collation='utf8mb3_general_ci', blank=True, null=True)
    disturb = models.CharField(max_length=16, db_collation='utf8mb3_general_ci', blank=True, null=True)
    nutrients = models.CharField(max_length=7, db_collation='utf8mb3_general_ci', blank=True, null=True)
    water = models.CharField(max_length=8, db_collation='utf8mb3_general_ci', blank=True, null=True)
    seasonality = models.CharField(max_length=16, db_collation='utf8mb3_general_ci', blank=True, null=True)
    seas_intens = models.CharField(max_length=3, db_collation='utf8mb3_general_ci', blank=True, null=True)
    pri_prod = models.CharField(max_length=4, db_collation='utf8mb3_general_ci', blank=True, null=True)
    moisture = models.CharField(max_length=3, db_collation='utf8mb3_general_ci', blank=True, null=True)
    temperature = models.CharField(max_length=4, db_collation='utf8mb3_general_ci', blank=True, null=True)
    assem_fm = models.CharField(max_length=12, db_collation='utf8mb3_general_ci', blank=True, null=True)
    transport = models.CharField(max_length=15, db_collation='utf8mb3_general_ci', blank=True, null=True)
    trans_mod = models.CharField(max_length=9, db_collation='utf8mb3_general_ci', blank=True, null=True)
    weath_trmp = models.CharField(max_length=9, db_collation='utf8mb3_general_ci', blank=True, null=True)
    pt_conc = models.CharField(max_length=14, db_collation='utf8mb3_general_ci', blank=True, null=True)
    size_type = models.CharField(max_length=5, db_collation='utf8mb3_general_ci', blank=True, null=True)
    vert_pres = models.CharField(max_length=12, db_collation='utf8mb3_general_ci', blank=True, null=True)
    plant_pres = models.CharField(max_length=12, db_collation='utf8mb3_general_ci', blank=True, null=True)
    invert_pres = models.CharField(max_length=12, db_collation='utf8mb3_general_ci', blank=True, null=True)
    time_rep = models.CharField(max_length=9, db_collation='utf8mb3_general_ci', blank=True, null=True)
    appr_num_spm = models.IntegerField(blank=True, null=True)
    num_spm = models.IntegerField(blank=True, null=True)
    true_quant = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    complete = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    num_quad = models.IntegerField(blank=True, null=True)
    taph_comm = models.CharField(max_length=120, db_collation='utf8mb3_general_ci', blank=True, null=True)
    tax_comm = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'now_v_locality_header'


class NowVLocalityList(models.Model):
    lid = models.IntegerField()
    loc_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci')
    country = models.CharField(max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)
    max_age = models.FloatField()
    min_age = models.FloatField()
    loc_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'now_v_locality_list'


class NowVLocalityLithology(models.Model):
    lid = models.IntegerField()
    loc_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci')
    country = models.CharField(max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)
    rock_type = models.CharField(max_length=15, db_collation='utf8mb3_general_ci', blank=True, null=True)
    rt_adj = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    lith_comm = models.CharField(max_length=120, db_collation='utf8mb3_general_ci', blank=True, null=True)
    sed_env_1 = models.CharField(max_length=13, db_collation='utf8mb3_general_ci', blank=True, null=True)
    sed_env_2 = models.CharField(max_length=15, db_collation='utf8mb3_general_ci', blank=True, null=True)
    event_circum = models.CharField(max_length=15, db_collation='utf8mb3_general_ci', blank=True, null=True)
    se_comm = models.CharField(max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)
    depo_context1 = models.CharField(max_length=10, db_collation='utf8mb3_general_ci', blank=True, null=True)
    depo_context2 = models.CharField(max_length=10, db_collation='utf8mb3_general_ci', blank=True, null=True)
    depo_context3 = models.CharField(max_length=10, db_collation='utf8mb3_general_ci', blank=True, null=True)
    depo_context4 = models.CharField(max_length=10, db_collation='utf8mb3_general_ci', blank=True, null=True)
    depo_comm = models.CharField(max_length=120, db_collation='utf8mb3_general_ci', blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'now_v_locality_lithology'


class NowVLocalityLocality(models.Model):
    lid = models.IntegerField()
    loc_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci')
    country = models.CharField(max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)
    state = models.CharField(max_length=20, db_collation='utf8mb3_general_ci', blank=True, null=True)
    county = models.CharField(max_length=20, db_collation='utf8mb3_general_ci', blank=True, null=True)
    loc_detail = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    site_area = models.CharField(max_length=10, db_collation='utf8mb3_general_ci', blank=True, null=True)
    gen_loc = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    plate = models.CharField(max_length=20, db_collation='utf8mb3_general_ci', blank=True, null=True)
    dms_lat = models.CharField(max_length=14, db_collation='utf8mb3_general_ci', blank=True, null=True)
    dec_lat = models.FloatField()
    dms_long = models.CharField(max_length=14, db_collation='utf8mb3_general_ci', blank=True, null=True)
    dec_long = models.FloatField()
    approx_coord = models.IntegerField(blank=True, null=True)
    loc_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'now_v_locality_locality'


class NowVLocalityLocalitySynonym(models.Model):
    lid = models.IntegerField(blank=True, null=True)
    loc_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    syn_id = models.IntegerField()
    synonym = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'now_v_locality_locality_synonym'


class NowVLocalityMuseum(models.Model):
    lid = models.IntegerField(blank=True, null=True)
    loc_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    museum = models.CharField(max_length=10, db_collation='utf8mb3_general_ci', blank=True, null=True)
    institution = models.CharField(max_length=120, db_collation='utf8mb3_general_ci', blank=True, null=True)
    city = models.CharField(max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)
    country = models.CharField(max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'now_v_locality_museum'


class NowVLocalityProject(models.Model):
    lid = models.IntegerField(blank=True, null=True)
    loc_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    pid = models.IntegerField()
    proj_code = models.CharField(max_length=10, db_collation='utf8mb3_general_ci', blank=True, null=True)
    proj_name = models.CharField(max_length=80, db_collation='utf8mb3_general_ci', blank=True, null=True)
    contact = models.CharField(max_length=10, db_collation='utf8mb3_general_ci', blank=True, null=True)
    proj_status = models.CharField(max_length=10, db_collation='utf8mb3_general_ci', blank=True, null=True)
    proj_records = models.IntegerField(blank=True, null=True)
    full_name = models.CharField(max_length=80, db_collation='utf8mb3_general_ci', blank=True, null=True)
    email = models.CharField(max_length=120, db_collation='utf8mb3_general_ci', blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'now_v_locality_project'


class NowVLocalitySpecies(models.Model):
    lid = models.IntegerField(blank=True, null=True)
    loc_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    country = models.CharField(max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)
    species_id = models.IntegerField(blank=True, null=True)
    order_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    family_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    subfamily_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    subclass_or_superorder_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    suborder_or_superfamily_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    genus_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    species_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    unique_identifier = models.CharField(max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)
    taxonomic_status = models.CharField(max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)
    id_status = models.CharField(max_length=20, db_collation='utf8mb3_general_ci', blank=True, null=True)
    orig_entry = models.CharField(max_length=120, db_collation='utf8mb3_general_ci', blank=True, null=True)
    nis = models.IntegerField(blank=True, null=True)
    pct = models.FloatField(blank=True, null=True)
    quad = models.IntegerField(blank=True, null=True)
    mni = models.IntegerField(blank=True, null=True)
    qua = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    source_name = models.CharField(max_length=120, db_collation='utf8mb3_general_ci', blank=True, null=True)
    body_mass = models.BigIntegerField(blank=True, null=True)
    dc13_mean = models.FloatField(blank=True, null=True)
    dc13_n = models.IntegerField(blank=True, null=True)
    dc13_max = models.FloatField(blank=True, null=True)
    dc13_min = models.FloatField(blank=True, null=True)
    dc13_stdev = models.FloatField(blank=True, null=True)
    do18_mean = models.FloatField(blank=True, null=True)
    do18_n = models.IntegerField(blank=True, null=True)
    do18_max = models.FloatField(blank=True, null=True)
    do18_min = models.FloatField(blank=True, null=True)
    do18_stdev = models.FloatField(blank=True, null=True)
    mesowear = models.CharField(max_length=3, db_collation='utf8mb3_general_ci', blank=True, null=True)
    mw_or_high = models.IntegerField(blank=True, null=True)
    mw_or_low = models.IntegerField(blank=True, null=True)
    mw_cs_sharp = models.IntegerField(blank=True, null=True)
    mw_cs_round = models.IntegerField(blank=True, null=True)
    mw_cs_blunt = models.IntegerField(blank=True, null=True)
    mw_scale_min = models.IntegerField(blank=True, null=True)
    mw_scale_max = models.IntegerField(blank=True, null=True)
    mw_value = models.IntegerField(blank=True, null=True)
    microwear = models.CharField(max_length=7, db_collation='utf8mb3_general_ci', blank=True, null=True)
    sp_status = models.IntegerField(blank=True, null=True)
    sp_comment = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'now_v_locality_species'


class NowVLocalityStatistics(models.Model):
    year = models.IntegerField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    surname = models.CharField(max_length=80, db_collation='utf8mb3_general_ci', blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'now_v_locality_statistics'


class NowVLocalityTaphonomy(models.Model):
    lid = models.IntegerField()
    loc_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci')
    country = models.CharField(max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)
    assem_fm = models.CharField(max_length=12, db_collation='utf8mb3_general_ci', blank=True, null=True)
    transport = models.CharField(max_length=15, db_collation='utf8mb3_general_ci', blank=True, null=True)
    trans_mod = models.CharField(max_length=9, db_collation='utf8mb3_general_ci', blank=True, null=True)
    weath_trmp = models.CharField(max_length=9, db_collation='utf8mb3_general_ci', blank=True, null=True)
    pt_conc = models.CharField(max_length=14, db_collation='utf8mb3_general_ci', blank=True, null=True)
    size_type = models.CharField(max_length=5, db_collation='utf8mb3_general_ci', blank=True, null=True)
    time_rep = models.CharField(max_length=9, db_collation='utf8mb3_general_ci', blank=True, null=True)
    vert_pres = models.CharField(max_length=12, db_collation='utf8mb3_general_ci', blank=True, null=True)
    appr_num_spm = models.IntegerField(blank=True, null=True)
    num_spm = models.IntegerField(blank=True, null=True)
    num_quad = models.IntegerField(blank=True, null=True)
    true_quant = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    complete = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    taph_comm = models.CharField(max_length=120, db_collation='utf8mb3_general_ci', blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'now_v_locality_taphonomy'


class NowVLocalityUpdateHeader(models.Model):
    luid = models.IntegerField()
    date = models.DateField(blank=True, null=True)
    authorizer = models.CharField(max_length=80, db_collation='utf8mb3_general_ci', blank=True, null=True)
    coordinator = models.CharField(max_length=80, db_collation='utf8mb3_general_ci', blank=True, null=True)
    comment = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    lid = models.IntegerField(blank=True, null=True)
    loc_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    country = models.CharField(max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'now_v_locality_update_header'


class NowVLocalityUpdates(models.Model):
    luid = models.IntegerField()
    lid = models.IntegerField()
    lau_coordinator = models.CharField(max_length=10, db_collation='utf8mb3_general_ci')
    lau_authorizer = models.CharField(max_length=10, db_collation='utf8mb3_general_ci')
    lau_date = models.DateField(blank=True, null=True)
    rids = models.TextField(db_collation='utf8mb4_general_ci', blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'now_v_locality_updates'


class NowVMuseumList(models.Model):
    museum = models.CharField(max_length=10, db_collation='utf8mb3_general_ci')
    institution = models.CharField(max_length=120, db_collation='utf8mb3_general_ci')
    alt_int_name = models.CharField(max_length=120, db_collation='utf8mb3_general_ci', blank=True, null=True)
    city = models.CharField(max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)
    state_code = models.CharField(max_length=5, db_collation='utf8mb3_general_ci', blank=True, null=True)
    state = models.CharField(max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)
    country = models.CharField(max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)
    used_now = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'now_v_museum_list'


class NowVPeopleList(models.Model):
    initials = models.CharField(max_length=10, db_collation='utf8mb3_general_ci')
    first_name = models.CharField(max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)
    surname = models.CharField(max_length=80, db_collation='utf8mb3_general_ci')
    full_name = models.CharField(max_length=80, db_collation='utf8mb3_general_ci')
    format = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    email = models.CharField(max_length=120, db_collation='utf8mb3_general_ci', blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    organization = models.CharField(max_length=80, db_collation='utf8mb3_general_ci', blank=True, null=True)
    country = models.CharField(max_length=80, db_collation='utf8mb3_general_ci', blank=True, null=True)
    password_set = models.DateField(blank=True, null=True)
    used_now = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'now_v_people_list'


class NowVProjectList(models.Model):
    pid = models.IntegerField()
    full_name = models.CharField(max_length=80, db_collation='utf8mb3_general_ci', blank=True, null=True)
    proj_code = models.CharField(max_length=10, db_collation='utf8mb3_general_ci', blank=True, null=True)
    proj_name = models.CharField(max_length=80, db_collation='utf8mb3_general_ci', blank=True, null=True)
    proj_status = models.CharField(max_length=10, db_collation='utf8mb3_general_ci', blank=True, null=True)
    proj_records = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'now_v_project_list'


class NowVProjectListUser(models.Model):
    pid = models.IntegerField()
    full_name = models.CharField(max_length=80, db_collation='utf8mb3_general_ci', blank=True, null=True)
    nppinitials = models.CharField(max_length=10, db_collation='utf8mb3_general_ci')
    proj_code = models.CharField(max_length=10, db_collation='utf8mb3_general_ci', blank=True, null=True)
    proj_name = models.CharField(max_length=80, db_collation='utf8mb3_general_ci', blank=True, null=True)
    proj_status = models.CharField(max_length=10, db_collation='utf8mb3_general_ci', blank=True, null=True)
    proj_records = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'now_v_project_list_user'


class NowVPublicLocalitySpecies(models.Model):
    count = models.BigIntegerField()

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'now_v_public_locality_species'


class NowVRefCit(models.Model):
    rid = models.IntegerField()
    date_primary = models.IntegerField(blank=True, null=True)
    title_primary = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    title_secondary = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    gen_notes = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    volume = models.CharField(max_length=10, db_collation='utf8mb3_general_ci', blank=True, null=True)
    issue = models.CharField(max_length=10, db_collation='utf8mb3_general_ci', blank=True, null=True)
    start_page = models.IntegerField(blank=True, null=True)
    end_page = models.IntegerField(blank=True, null=True)
    publisher = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    pub_place = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    author_surname1 = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    author_surname2 = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    author_surname3 = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    author_surname4 = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    editor_surname1 = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    editor_surname2 = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    editor_surname3 = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    editor_surname4 = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    journal_title = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    ref_type_id = models.IntegerField()
    ref_type = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'now_v_ref_cit'


class NowVReferenceHeader(models.Model):
    rid = models.IntegerField()

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'now_v_reference_header'


class NowVReferenceList(models.Model):
    rid = models.IntegerField()
    date_primary = models.IntegerField(blank=True, null=True)
    date_secondary = models.IntegerField(blank=True, null=True)
    exact_date = models.DateField(blank=True, null=True)
    title_primary = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    title_secondary = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    title_series = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    journal_id = models.IntegerField(blank=True, null=True)
    ref_type_id = models.IntegerField()
    volume = models.CharField(max_length=10, db_collation='utf8mb3_general_ci', blank=True, null=True)
    issue = models.CharField(max_length=10, db_collation='utf8mb3_general_ci', blank=True, null=True)
    start_page = models.IntegerField(blank=True, null=True)
    end_page = models.IntegerField(blank=True, null=True)
    publisher = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    pub_place = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    issn_isbn = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    ref_abstract = models.TextField(db_collation='utf8mb3_general_ci', blank=True, null=True)
    web_url = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    misc_1 = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    misc_2 = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    gen_notes = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    printed_language = models.CharField(max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)
    used_morph = models.IntegerField(blank=True, null=True)
    used_now = models.IntegerField(blank=True, null=True)
    used_gene = models.IntegerField(blank=True, null=True)
    author_surname = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    journal_title = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    ref_type = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    cmb_title = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    cmb_author = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'now_v_reference_list'


class NowVReferenceLocality(models.Model):
    rid = models.IntegerField()
    lid = models.IntegerField(blank=True, null=True)
    loc_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    country = models.CharField(max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)
    max_age = models.FloatField(blank=True, null=True)
    min_age = models.FloatField(blank=True, null=True)
    loc_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'now_v_reference_locality'


class NowVReferenceSpecies(models.Model):
    rid = models.IntegerField()
    species_id = models.IntegerField(blank=True, null=True)
    order_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    family_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    subfamily_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    subclass_or_superorder_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    suborder_or_superfamily_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    genus_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    species_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    unique_identifier = models.CharField(max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)
    sp_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'now_v_reference_species'


class NowVReferenceTubound(models.Model):
    rid = models.IntegerField()
    bid = models.IntegerField(blank=True, null=True)
    b_name = models.CharField(max_length=150, db_collation='utf8mb3_general_ci', blank=True, null=True)
    age = models.FloatField(blank=True, null=True)
    b_comment = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'now_v_reference_tubound'


class NowVSpeciesDiet(models.Model):
    species_id = models.IntegerField()
    genus_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci')
    species_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci')
    unique_identifier = models.CharField(max_length=50, db_collation='utf8mb3_general_ci')
    diet1 = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    diet2 = models.CharField(max_length=9, db_collation='utf8mb3_general_ci', blank=True, null=True)
    diet3 = models.CharField(max_length=10, db_collation='utf8mb3_general_ci', blank=True, null=True)
    rel_fib = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    selectivity = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    digestion = models.CharField(max_length=2, db_collation='utf8mb3_general_ci', blank=True, null=True)
    hunt_forage = models.CharField(max_length=8, db_collation='utf8mb3_general_ci', blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'now_v_species_diet'


class NowVSpeciesHeader(models.Model):
    species_id = models.IntegerField()
    class_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci')
    order_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci')
    family_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci')
    subfamily_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    subclass_or_superorder_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    suborder_or_superfamily_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    genus_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci')
    species_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci')
    unique_identifier = models.CharField(max_length=50, db_collation='utf8mb3_general_ci')
    common_name = models.CharField(max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)
    sp_status = models.IntegerField(blank=True, null=True)
    taxonomic_status = models.CharField(max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)
    sp_author = models.CharField(max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)
    strain = models.CharField(max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)
    gene = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    taxon_status = models.CharField(max_length=10, db_collation='utf8mb3_general_ci', blank=True, null=True)
    diet1 = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    diet2 = models.CharField(max_length=9, db_collation='utf8mb3_general_ci', blank=True, null=True)
    diet3 = models.CharField(max_length=10, db_collation='utf8mb3_general_ci', blank=True, null=True)
    diet_description = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    rel_fib = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    selectivity = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    digestion = models.CharField(max_length=2, db_collation='utf8mb3_general_ci', blank=True, null=True)
    feedinghab1 = models.CharField(max_length=2, db_collation='utf8mb3_general_ci', blank=True, null=True)
    feedinghab2 = models.CharField(max_length=8, db_collation='utf8mb3_general_ci', blank=True, null=True)
    shelterhab1 = models.CharField(max_length=2, db_collation='utf8mb3_general_ci', blank=True, null=True)
    shelterhab2 = models.CharField(max_length=8, db_collation='utf8mb3_general_ci', blank=True, null=True)
    locomo1 = models.CharField(max_length=2, db_collation='utf8mb3_general_ci', blank=True, null=True)
    locomo2 = models.CharField(max_length=15, db_collation='utf8mb3_general_ci', blank=True, null=True)
    locomo3 = models.CharField(max_length=15, db_collation='utf8mb3_general_ci', blank=True, null=True)
    hunt_forage = models.CharField(max_length=8, db_collation='utf8mb3_general_ci', blank=True, null=True)
    body_mass = models.BigIntegerField(blank=True, null=True)
    brain_mass = models.IntegerField(blank=True, null=True)
    sv_length = models.CharField(max_length=7, db_collation='utf8mb3_general_ci', blank=True, null=True)
    activity = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    sd_size = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    sd_display = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    tshm = models.CharField(max_length=3, db_collation='utf8mb3_general_ci', blank=True, null=True)
    symph_mob = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    relative_blade_length = models.FloatField(blank=True, null=True)
    tht = models.CharField(max_length=3, db_collation='utf8mb3_general_ci', blank=True, null=True)
    crowntype = models.CharField(max_length=6, db_collation='utf8mb3_general_ci', blank=True, null=True)
    microwear = models.CharField(max_length=7, db_collation='utf8mb3_general_ci', blank=True, null=True)
    pop_struc = models.CharField(max_length=3, db_collation='utf8mb3_general_ci', blank=True, null=True)
    used_morph = models.IntegerField(blank=True, null=True)
    used_now = models.IntegerField(blank=True, null=True)
    used_gene = models.IntegerField(blank=True, null=True)
    sp_comment = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'now_v_species_header'


class NowVSpeciesList(models.Model):
    species_id = models.IntegerField()
    order_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci')
    family_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci')
    subfamily_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    subclass_or_superorder_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    suborder_or_superfamily_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    genus_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci')
    species_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci')
    unique_identifier = models.CharField(max_length=50, db_collation='utf8mb3_general_ci')
    sp_status = models.IntegerField(blank=True, null=True)
    taxonomic_status = models.CharField(max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)
    sp_comment = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    syncount = models.BigIntegerField()

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'now_v_species_list'


class NowVSpeciesLocality(models.Model):
    species_id = models.IntegerField(blank=True, null=True)
    genus_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    species_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    unique_identifier = models.CharField(max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)
    lid = models.IntegerField(blank=True, null=True)
    loc_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    country = models.CharField(max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)
    max_age = models.FloatField(blank=True, null=True)
    min_age = models.FloatField(blank=True, null=True)
    id_status = models.CharField(max_length=20, db_collation='utf8mb3_general_ci', blank=True, null=True)
    orig_entry = models.CharField(max_length=120, db_collation='utf8mb3_general_ci', blank=True, null=True)
    source_name = models.CharField(max_length=120, db_collation='utf8mb3_general_ci', blank=True, null=True)
    nis = models.IntegerField(blank=True, null=True)
    pct = models.FloatField(blank=True, null=True)
    quad = models.IntegerField(blank=True, null=True)
    mni = models.IntegerField(blank=True, null=True)
    qua = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    body_mass = models.BigIntegerField(blank=True, null=True)
    dc13_mean = models.FloatField(blank=True, null=True)
    dc13_n = models.IntegerField(blank=True, null=True)
    dc13_max = models.FloatField(blank=True, null=True)
    dc13_min = models.FloatField(blank=True, null=True)
    dc13_stdev = models.FloatField(blank=True, null=True)
    do18_mean = models.FloatField(blank=True, null=True)
    do18_n = models.IntegerField(blank=True, null=True)
    do18_max = models.FloatField(blank=True, null=True)
    do18_min = models.FloatField(blank=True, null=True)
    do18_stdev = models.FloatField(blank=True, null=True)
    mesowear = models.CharField(max_length=3, db_collation='utf8mb3_general_ci', blank=True, null=True)
    mw_or_high = models.IntegerField(blank=True, null=True)
    mw_or_low = models.IntegerField(blank=True, null=True)
    mw_cs_sharp = models.IntegerField(blank=True, null=True)
    mw_cs_round = models.IntegerField(blank=True, null=True)
    mw_cs_blunt = models.IntegerField(blank=True, null=True)
    mw_scale_min = models.IntegerField(blank=True, null=True)
    mw_scale_max = models.IntegerField(blank=True, null=True)
    mw_value = models.IntegerField(blank=True, null=True)
    microwear = models.CharField(max_length=7, db_collation='utf8mb3_general_ci', blank=True, null=True)
    loc_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'now_v_species_locality'


class NowVSpeciesLocomotion(models.Model):
    species_id = models.IntegerField()
    genus_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci')
    species_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci')
    unique_identifier = models.CharField(max_length=50, db_collation='utf8mb3_general_ci')
    feedinghab1 = models.CharField(max_length=2, db_collation='utf8mb3_general_ci', blank=True, null=True)
    feedinghab2 = models.CharField(max_length=8, db_collation='utf8mb3_general_ci', blank=True, null=True)
    shelterhab1 = models.CharField(max_length=2, db_collation='utf8mb3_general_ci', blank=True, null=True)
    shelterhab2 = models.CharField(max_length=8, db_collation='utf8mb3_general_ci', blank=True, null=True)
    locomo1 = models.CharField(max_length=2, db_collation='utf8mb3_general_ci', blank=True, null=True)
    locomo2 = models.CharField(max_length=15, db_collation='utf8mb3_general_ci', blank=True, null=True)
    locomo3 = models.CharField(max_length=15, db_collation='utf8mb3_general_ci', blank=True, null=True)
    activity = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'now_v_species_locomotion'


class NowVSpeciesSize(models.Model):
    species_id = models.IntegerField()
    genus_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci')
    species_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci')
    unique_identifier = models.CharField(max_length=50, db_collation='utf8mb3_general_ci')
    body_mass = models.BigIntegerField(blank=True, null=True)
    brain_mass = models.IntegerField(blank=True, null=True)
    sv_length = models.CharField(max_length=7, db_collation='utf8mb3_general_ci', blank=True, null=True)
    sd_size = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    sd_display = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    pop_struc = models.CharField(max_length=3, db_collation='utf8mb3_general_ci', blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'now_v_species_size'


class NowVSpeciesStatistics(models.Model):
    year = models.IntegerField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    surname = models.CharField(max_length=80, db_collation='utf8mb3_general_ci', blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'now_v_species_statistics'


class NowVSpeciesTaxonomy(models.Model):
    species_id = models.IntegerField()
    class_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci')
    order_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci')
    family_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci')
    subfamily_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    subclass_or_superorder_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    suborder_or_superfamily_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    genus_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci')
    species_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci')
    unique_identifier = models.CharField(max_length=50, db_collation='utf8mb3_general_ci')
    taxonomic_status = models.CharField(max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)
    sp_author = models.CharField(max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)
    sp_status = models.IntegerField(blank=True, null=True)
    sp_comment = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'now_v_species_taxonomy'


class NowVSpeciesTeeth(models.Model):
    species_id = models.IntegerField()
    genus_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci')
    species_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci')
    unique_identifier = models.CharField(max_length=50, db_collation='utf8mb3_general_ci')
    tshm = models.CharField(max_length=3, db_collation='utf8mb3_general_ci', blank=True, null=True)
    crowntype = models.CharField(max_length=6, db_collation='utf8mb3_general_ci', blank=True, null=True)
    tht = models.CharField(max_length=3, db_collation='utf8mb3_general_ci', blank=True, null=True)
    microwear = models.CharField(max_length=7, db_collation='utf8mb3_general_ci', blank=True, null=True)
    symph_mob = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    relative_blade_length = models.FloatField(blank=True, null=True)
    horizodonty = models.CharField(max_length=3, db_collation='utf8mb3_general_ci', blank=True, null=True)
    cusp_shape = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    cusp_count_buccal = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    cusp_count_lingual = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    loph_count_lon = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    loph_count_trs = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    fct_al = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    fct_ol = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    fct_sf = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    fct_ot = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    fct_cm = models.CharField(max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)
    mesowear = models.CharField(max_length=3, db_collation='utf8mb3_general_ci', blank=True, null=True)
    mw_or_high = models.IntegerField(blank=True, null=True)
    mw_or_low = models.IntegerField(blank=True, null=True)
    mw_cs_sharp = models.IntegerField(blank=True, null=True)
    mw_cs_round = models.IntegerField(blank=True, null=True)
    mw_cs_blunt = models.IntegerField(blank=True, null=True)
    mw_scale_min = models.IntegerField(blank=True, null=True)
    mw_scale_max = models.IntegerField(blank=True, null=True)
    mw_value = models.IntegerField(blank=True, null=True)
    functional_crown_type = models.CharField(max_length=5, db_collation='utf8mb3_general_ci', blank=True, null=True)
    developmental_crown_type = models.CharField(max_length=5, db_collation='utf8mb3_general_ci', blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'now_v_species_teeth'


class NowVSpeciesUpdateHeader(models.Model):
    suid = models.IntegerField()
    date = models.DateField(blank=True, null=True)
    authorizer = models.CharField(max_length=80, db_collation='utf8mb3_general_ci', blank=True, null=True)
    coordinator = models.CharField(max_length=80, db_collation='utf8mb3_general_ci', blank=True, null=True)
    comment = models.CharField(max_length=1024, db_collation='utf8mb3_general_ci', blank=True, null=True)
    species_id = models.IntegerField(blank=True, null=True)
    genus_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    species_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    unique_identifier = models.CharField(max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'now_v_species_update_header'


class NowVSpeciesUpdates(models.Model):
    suid = models.IntegerField()
    species_id = models.IntegerField()
    sau_coordinator = models.CharField(max_length=10, db_collation='utf8mb3_general_ci')
    sau_authorizer = models.CharField(max_length=10, db_collation='utf8mb3_general_ci')
    sau_date = models.DateField(blank=True, null=True)
    rids = models.TextField(db_collation='utf8mb4_general_ci', blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'now_v_species_updates'


class NowVSsValuesList(models.Model):
    ss_value = models.CharField(max_length=30, db_collation='utf8mb3_general_ci')
    category = models.CharField(max_length=80, db_collation='utf8mb3_general_ci', blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'now_v_ss_values_list'


class NowVTimeBound(models.Model):
    bid = models.IntegerField()
    b_name = models.CharField(max_length=150, db_collation='utf8mb3_general_ci', blank=True, null=True)
    age = models.FloatField(blank=True, null=True)
    b_comment = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'now_v_time_bound'


class NowVTimeBoundHeader(models.Model):
    bid = models.IntegerField()
    b_name = models.CharField(max_length=150, db_collation='utf8mb3_general_ci', blank=True, null=True)
    age = models.FloatField(blank=True, null=True)
    b_comment = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'now_v_time_bound_header'


class NowVTimeBoundList(models.Model):
    bid = models.IntegerField()
    b_name = models.CharField(max_length=150, db_collation='utf8mb3_general_ci', blank=True, null=True)
    age = models.FloatField(blank=True, null=True)
    b_comment = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'now_v_time_bound_list'


class NowVTimeBoundUpdateHeader(models.Model):
    buid = models.IntegerField()
    date = models.DateField(blank=True, null=True)
    authorizer = models.CharField(max_length=80, db_collation='utf8mb3_general_ci', blank=True, null=True)
    coordinator = models.CharField(max_length=80, db_collation='utf8mb3_general_ci', blank=True, null=True)
    comment = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    bid = models.IntegerField(blank=True, null=True)
    b_name = models.CharField(max_length=150, db_collation='utf8mb3_general_ci', blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'now_v_time_bound_update_header'


class NowVTimeBoundUpdates(models.Model):
    buid = models.IntegerField()
    bid = models.IntegerField()
    bau_coordinator = models.CharField(max_length=10, db_collation='utf8mb3_general_ci')
    bau_authorizer = models.CharField(max_length=10, db_collation='utf8mb3_general_ci')
    bau_date = models.DateField(blank=True, null=True)
    rids = models.TextField(db_collation='utf8mb4_general_ci', blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'now_v_time_bound_updates'


class NowVTimeBoundsInTimeUnits(models.Model):
    bid = models.IntegerField(blank=True, null=True)
    tu_name = models.CharField(max_length=100, db_collation='utf8mb3_general_ci')
    tu_display_name = models.CharField(max_length=100, db_collation='utf8mb3_general_ci')
    up_bnd = models.IntegerField()
    low_bnd = models.IntegerField()
    rank = models.CharField(max_length=15, db_collation='utf8mb3_general_ci', blank=True, null=True)
    sequence = models.CharField(max_length=30, db_collation='utf8mb3_general_ci')
    tu_comment = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'now_v_time_bounds_in_time_units'


class NowVTimeUnitAndBoundUpdates(models.Model):
    time_update_id = models.IntegerField()
    tu_name = models.CharField(max_length=100, db_collation='utf8mb3_general_ci')
    tu_display_name = models.CharField(max_length=100, db_collation='utf8mb3_general_ci')
    tuid = models.IntegerField(blank=True, null=True)
    lower_buid = models.IntegerField(blank=True, null=True)
    upper_buid = models.IntegerField(blank=True, null=True)
    coordinator = models.CharField(max_length=10, db_collation='utf8mb3_general_ci')
    authorizer = models.CharField(max_length=10, db_collation='utf8mb3_general_ci')
    date = models.DateField(blank=True, null=True)
    comment = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'now_v_time_unit_and_bound_updates'


class NowVTimeUnitLocalities(models.Model):
    tu_name = models.CharField(max_length=100, db_collation='utf8mb3_general_ci')
    tu_display_name = models.CharField(max_length=100, db_collation='utf8mb3_general_ci')
    lid = models.IntegerField(blank=True, null=True)
    loc_name = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    bfa_min = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    bfa_max = models.CharField(max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)
    loc_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'now_v_time_unit_localities'


class RefAuthors(models.Model):
    rid = models.OneToOneField(RefReference, models.DO_NOTHING, db_column='rid', primary_key=True)
    field_id = models.IntegerField()
    au_num = models.IntegerField()
    author_surname = models.CharField(max_length=255, blank=True, null=True)
    author_initials = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'ref_authors'
        unique_together = (('rid', 'field_id', 'au_num'),)

class RefFieldName(models.Model):
    field_id = models.IntegerField(db_column='field_ID', primary_key=True)  # Field name made lowercase.
    ref_type = models.ForeignKey(RefReferenceType, models.DO_NOTHING)
    ref_field_name = models.CharField(max_length=50, blank=True, null=True)
    display = models.IntegerField(blank=True, null=True)
    label_x = models.IntegerField(blank=True, null=True)
    label_y = models.IntegerField(blank=True, null=True)
    field_x = models.IntegerField(blank=True, null=True)
    field_y = models.IntegerField(blank=True, null=True)
    field_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'ref_field_name'
        unique_together = (('field_id', 'ref_type'),)

class RefKeywords(models.Model):
    keywords_id = models.AutoField(primary_key=True)
    keyword = models.CharField(max_length=50)

    class Meta:
        db_table = 'ref_keywords'


class RefKeywordsReference(models.Model):
    keywords = models.OneToOneField(RefKeywords, models.DO_NOTHING, primary_key=True)
    rid = models.ForeignKey(RefReference, models.DO_NOTHING, db_column='rid')

    class Meta:
        db_table = 'ref_keywords_ref'
        unique_together = (('keywords', 'rid'),)
