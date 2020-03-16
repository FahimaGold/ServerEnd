# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    last_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Condition(models.Model):
    conditionguid = models.CharField(db_column='ConditionGuid', unique=True, max_length=36, blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=50, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'condition'


class DiabetesInfo(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    taille = models.CharField(max_length=10)
    poids = models.CharField(max_length=10)
    tourdetaille = models.CharField(db_column='tourDeTaille', max_length=10)  # Field name made lowercase.
    idinfo = models.IntegerField(db_column='idInfo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'diabetes_info'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Smokingstatus(models.Model):
    smokingstatusguid = models.CharField(db_column='SmokingStatusGuid', unique=True, max_length=36, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nistcode = models.IntegerField(db_column='NISTcode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'smokingStatus'


class TestAllmeds(models.Model):
    medicationguid = models.TextField(db_column='MedicationGuid', blank=True, null=True)  # Field name made lowercase.
    patientguid = models.TextField(db_column='PatientGuid', blank=True, null=True)  # Field name made lowercase.
    medicationndccode = models.TextField(db_column='MedicationNdcCode', blank=True, null=True)  # Field name made lowercase.
    medicationname = models.TextField(db_column='MedicationName', blank=True, null=True)  # Field name made lowercase.
    medicationstrength = models.TextField(db_column='MedicationStrength', blank=True, null=True)  # Field name made lowercase.
    schedule = models.TextField(db_column='Schedule', blank=True, null=True)  # Field name made lowercase.
    diagnosisguid = models.TextField(db_column='DiagnosisGuid', blank=True, null=True)  # Field name made lowercase.
    userguid = models.TextField(db_column='UserGuid', blank=True, null=True)  # Field name made lowercase.
    prescriptionguid = models.TextField(db_column='PrescriptionGuid', blank=True, null=True)  # Field name made lowercase.
    patientguid_1 = models.TextField(db_column='PatientGuid:1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    medicationguid_1 = models.TextField(db_column='MedicationGuid:1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    prescriptionyear = models.IntegerField(db_column='PrescriptionYear', blank=True, null=True)  # Field name made lowercase.
    quantity = models.TextField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    numberofrefills = models.TextField(db_column='NumberOfRefills', blank=True, null=True)  # Field name made lowercase.
    refillasneeded = models.IntegerField(db_column='RefillAsNeeded', blank=True, null=True)  # Field name made lowercase.
    genericallowed = models.IntegerField(db_column='GenericAllowed', blank=True, null=True)  # Field name made lowercase.
    userguid_1 = models.TextField(db_column='UserGuid:1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    allergyguid = models.TextField(db_column='AllergyGuid', blank=True, null=True)  # Field name made lowercase.
    patientguid_2 = models.TextField(db_column='PatientGuid:2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    allergytype = models.TextField(db_column='AllergyType', blank=True, null=True)  # Field name made lowercase.
    startyear = models.IntegerField(db_column='StartYear', blank=True, null=True)  # Field name made lowercase.
    reactionname = models.TextField(db_column='ReactionName', blank=True, null=True)  # Field name made lowercase.
    severityname = models.TextField(db_column='SeverityName', blank=True, null=True)  # Field name made lowercase.
    medicationndccode_1 = models.TextField(db_column='MedicationNDCCode:1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    medicationname_1 = models.TextField(db_column='MedicationName:1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    userguid_2 = models.TextField(db_column='UserGuid:2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'test_allMeds'
# Unable to inspect table 'test_allergy'
# The error was: list index out of range
# Unable to inspect table 'test_diagnosis'
# The error was: list index out of range
# Unable to inspect table 'test_immunization'
# The error was: list index out of range
# Unable to inspect table 'test_labObservation'
# The error was: list index out of range
# Unable to inspect table 'test_labPanel'
# The error was: list index out of range
# Unable to inspect table 'test_labResult'
# The error was: list index out of range


class TestLabs(models.Model):
    labresultguid = models.TextField(db_column='LabResultGuid', blank=True, null=True)  # Field name made lowercase.
    userguid = models.TextField(db_column='UserGuid', blank=True, null=True)  # Field name made lowercase.
    patientguid = models.TextField(db_column='PatientGuid', blank=True, null=True)  # Field name made lowercase.
    transcriptguid = models.TextField(db_column='TranscriptGuid', blank=True, null=True)  # Field name made lowercase.
    practiceguid = models.TextField(db_column='PracticeGuid', blank=True, null=True)  # Field name made lowercase.
    facilityguid = models.TextField(db_column='FacilityGuid', blank=True, null=True)  # Field name made lowercase.
    reportyear = models.IntegerField(db_column='ReportYear', blank=True, null=True)  # Field name made lowercase.
    ancestorlabresultguid = models.TextField(db_column='AncestorLabResultGuid', blank=True, null=True)  # Field name made lowercase.
    panelname = models.TextField(db_column='PanelName', blank=True, null=True)  # Field name made lowercase.
    labpanelguid = models.TextField(db_column='LabPanelGuid', blank=True, null=True)  # Field name made lowercase.
    labresultguid_1 = models.TextField(db_column='LabResultGuid:1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    observationyear = models.IntegerField(db_column='ObservationYear', blank=True, null=True)  # Field name made lowercase.
    status = models.TextField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    hl7identifier = models.TextField(db_column='HL7Identifier', blank=True, null=True)  # Field name made lowercase.
    hl7text = models.TextField(db_column='HL7Text', blank=True, null=True)  # Field name made lowercase.
    labobservationguid = models.TextField(db_column='LabObservationGuid', blank=True, null=True)  # Field name made lowercase.
    labpanelguid_1 = models.TextField(db_column='LabPanelGuid:1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hl7codingsystem = models.TextField(db_column='HL7Codingsystem', blank=True, null=True)  # Field name made lowercase.
    observationvalue = models.TextField(db_column='ObservationValue', blank=True, null=True)  # Field name made lowercase.
    units = models.TextField(db_column='Units', blank=True, null=True)  # Field name made lowercase.
    referencerange = models.TextField(db_column='ReferenceRange', blank=True, null=True)  # Field name made lowercase.
    abnormalflags = models.TextField(db_column='AbnormalFlags', blank=True, null=True)  # Field name made lowercase.
    resultstatus = models.TextField(db_column='ResultStatus', blank=True, null=True)  # Field name made lowercase.
    observationyear_1 = models.IntegerField(db_column='ObservationYear:1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    userguid_1 = models.TextField(db_column='UserGuid:1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ssabnormalvalue = models.IntegerField(db_column='SsAbnormalValue', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'test_labs'
# Unable to inspect table 'test_medication'
# The error was: list index out of range


class TestPatient(models.Model):
    patientguid = models.CharField(db_column='PatientGuid', unique=True, max_length=36, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=1, blank=True, null=True)  # Field name made lowercase.
    yearofbirth = models.IntegerField(db_column='YearOfBirth', blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=2, blank=True, null=True)  # Field name made lowercase.
    practiceguid = models.CharField(db_column='PracticeGuid', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'test_patient'
# Unable to inspect table 'test_patientCondition'
# The error was: list index out of range
# Unable to inspect table 'test_patientSmokingStatus'
# The error was: list index out of range


class TestPatienttranscript(models.Model):
    patientguid = models.TextField(db_column='PatientGuid', blank=True, null=True)  # Field name made lowercase.
    gender = models.TextField(db_column='Gender', blank=True, null=True)  # Field name made lowercase.
    yearofbirth = models.IntegerField(db_column='YearOfBirth', blank=True, null=True)  # Field name made lowercase.
    state = models.TextField(db_column='State', blank=True, null=True)  # Field name made lowercase.
    practiceguid = models.TextField(db_column='PracticeGuid', blank=True, null=True)  # Field name made lowercase.
    transcriptguid = models.TextField(db_column='TranscriptGuid', blank=True, null=True)  # Field name made lowercase.
    patientguid_1 = models.TextField(db_column='PatientGuid:1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    visityear = models.IntegerField(db_column='VisitYear', blank=True, null=True)  # Field name made lowercase.
    height = models.TextField(db_column='Height', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    weight = models.FloatField(db_column='Weight', blank=True, null=True)  # Field name made lowercase.
    bmi = models.FloatField(db_column='BMI', blank=True, null=True)  # Field name made lowercase.
    systolicbp = models.IntegerField(db_column='SystolicBP', blank=True, null=True)  # Field name made lowercase.
    diastolicbp = models.IntegerField(db_column='DiastolicBP', blank=True, null=True)  # Field name made lowercase.
    respiratoryrate = models.IntegerField(db_column='RespiratoryRate', blank=True, null=True)  # Field name made lowercase.
    heartrate = models.IntegerField(db_column='HeartRate', blank=True, null=True)  # Field name made lowercase.
    temperature = models.FloatField(db_column='Temperature', blank=True, null=True)  # Field name made lowercase.
    physicianspecialty = models.TextField(db_column='PhysicianSpecialty', blank=True, null=True)  # Field name made lowercase.
    userguid = models.TextField(db_column='UserGuid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'test_patientTranscript'
# Unable to inspect table 'test_prescription'
# The error was: list index out of range


class TestSmoke(models.Model):
    patientguid = models.TextField(db_column='PatientGuid', blank=True, null=True)  # Field name made lowercase.
    gender = models.TextField(db_column='Gender', blank=True, null=True)  # Field name made lowercase.
    yearofbirth = models.IntegerField(db_column='YearOfBirth', blank=True, null=True)  # Field name made lowercase.
    state = models.TextField(db_column='State', blank=True, null=True)  # Field name made lowercase.
    practiceguid = models.TextField(db_column='PracticeGuid', blank=True, null=True)  # Field name made lowercase.
    smokeeffectiveyear = models.IntegerField(db_column='SmokeEffectiveYear', blank=True, null=True)  # Field name made lowercase.
    smokingstatus_description = models.TextField(db_column='SmokingStatus_Description', blank=True, null=True)  # Field name made lowercase.
    smokingstatus_nistcode = models.IntegerField(db_column='SmokingStatus_NISTCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'test_smoke'
# Unable to inspect table 'test_transcript'
# The error was: list index out of range
# Unable to inspect table 'test_transcriptAllergy'
# The error was: list index out of range
# Unable to inspect table 'test_transcriptDiagnosis'
# The error was: list index out of range
# Unable to inspect table 'test_transcriptMedication'
# The error was: list index out of range


class TrainingAllmeds(models.Model):
    medicationguid = models.TextField(db_column='MedicationGuid', blank=True, null=True)  # Field name made lowercase.
    patientguid = models.TextField(db_column='PatientGuid', blank=True, null=True)  # Field name made lowercase.
    medicationndccode = models.TextField(db_column='MedicationNdcCode', blank=True, null=True)  # Field name made lowercase.
    medicationname = models.TextField(db_column='MedicationName', blank=True, null=True)  # Field name made lowercase.
    medicationstrength = models.TextField(db_column='MedicationStrength', blank=True, null=True)  # Field name made lowercase.
    schedule = models.TextField(db_column='Schedule', blank=True, null=True)  # Field name made lowercase.
    diagnosisguid = models.TextField(db_column='DiagnosisGuid', blank=True, null=True)  # Field name made lowercase.
    userguid = models.TextField(db_column='UserGuid', blank=True, null=True)  # Field name made lowercase.
    prescriptionguid = models.TextField(db_column='PrescriptionGuid', blank=True, null=True)  # Field name made lowercase.
    patientguid_1 = models.TextField(db_column='PatientGuid:1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    medicationguid_1 = models.TextField(db_column='MedicationGuid:1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    prescriptionyear = models.IntegerField(db_column='PrescriptionYear', blank=True, null=True)  # Field name made lowercase.
    quantity = models.TextField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    numberofrefills = models.TextField(db_column='NumberOfRefills', blank=True, null=True)  # Field name made lowercase.
    refillasneeded = models.IntegerField(db_column='RefillAsNeeded', blank=True, null=True)  # Field name made lowercase.
    genericallowed = models.IntegerField(db_column='GenericAllowed', blank=True, null=True)  # Field name made lowercase.
    userguid_1 = models.TextField(db_column='UserGuid:1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    allergyguid = models.TextField(db_column='AllergyGuid', blank=True, null=True)  # Field name made lowercase.
    patientguid_2 = models.TextField(db_column='PatientGuid:2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    allergytype = models.TextField(db_column='AllergyType', blank=True, null=True)  # Field name made lowercase.
    startyear = models.IntegerField(db_column='StartYear', blank=True, null=True)  # Field name made lowercase.
    reactionname = models.TextField(db_column='ReactionName', blank=True, null=True)  # Field name made lowercase.
    severityname = models.TextField(db_column='SeverityName', blank=True, null=True)  # Field name made lowercase.
    medicationndccode_1 = models.TextField(db_column='MedicationNdcCode:1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    medicationname_1 = models.TextField(db_column='MedicationName:1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    userguid_2 = models.TextField(db_column='UserGuid:2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'training_allMeds'
# Unable to inspect table 'training_allergy'
# The error was: list index out of range
# Unable to inspect table 'training_diagnosis'
# The error was: list index out of range
# Unable to inspect table 'training_immunization'
# The error was: list index out of range
# Unable to inspect table 'training_labObservation'
# The error was: list index out of range
# Unable to inspect table 'training_labPanel'
# The error was: list index out of range
# Unable to inspect table 'training_labResult'
# The error was: list index out of range


class TrainingLabs(models.Model):
    labresultguid = models.TextField(db_column='LabResultGuid', blank=True, null=True)  # Field name made lowercase.
    userguid = models.TextField(db_column='UserGuid', blank=True, null=True)  # Field name made lowercase.
    patientguid = models.TextField(db_column='PatientGuid', blank=True, null=True)  # Field name made lowercase.
    transcriptguid = models.TextField(db_column='TranscriptGuid', blank=True, null=True)  # Field name made lowercase.
    practiceguid = models.TextField(db_column='PracticeGuid', blank=True, null=True)  # Field name made lowercase.
    facilityguid = models.TextField(db_column='FacilityGuid', blank=True, null=True)  # Field name made lowercase.
    reportyear = models.IntegerField(db_column='ReportYear', blank=True, null=True)  # Field name made lowercase.
    ancestorlabresultguid = models.TextField(db_column='AncestorLabResultGuid', blank=True, null=True)  # Field name made lowercase.
    panelname = models.TextField(db_column='PanelName', blank=True, null=True)  # Field name made lowercase.
    labpanelguid = models.TextField(db_column='LabPanelGuid', blank=True, null=True)  # Field name made lowercase.
    labresultguid_1 = models.TextField(db_column='LabResultGuid:1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    observationyear = models.IntegerField(db_column='ObservationYear', blank=True, null=True)  # Field name made lowercase.
    status = models.TextField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    hl7identifier = models.TextField(db_column='HL7Identifier', blank=True, null=True)  # Field name made lowercase.
    hl7text = models.TextField(db_column='HL7Text', blank=True, null=True)  # Field name made lowercase.
    labobservationguid = models.TextField(db_column='LabObservationGuid', blank=True, null=True)  # Field name made lowercase.
    labpanelguid_1 = models.TextField(db_column='LabPanelGuid:1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hl7codingsystem = models.TextField(db_column='HL7CodingSystem', blank=True, null=True)  # Field name made lowercase.
    observationvalue = models.TextField(db_column='ObservationValue', blank=True, null=True)  # Field name made lowercase.
    units = models.TextField(db_column='Units', blank=True, null=True)  # Field name made lowercase.
    referencerange = models.TextField(db_column='ReferenceRange', blank=True, null=True)  # Field name made lowercase.
    abnormalflags = models.TextField(db_column='AbnormalFlags', blank=True, null=True)  # Field name made lowercase.
    resultstatus = models.TextField(db_column='ResultStatus', blank=True, null=True)  # Field name made lowercase.
    observationyear_1 = models.IntegerField(db_column='ObservationYear:1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    userguid_1 = models.TextField(db_column='UserGuid:1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    isabnormalvalue = models.IntegerField(db_column='IsAbnormalValue', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'training_labs'
# Unable to inspect table 'training_medication'
# The error was: list index out of range


class TrainingPatient(models.Model):
    patientguid = models.CharField(db_column='PatientGuid', unique=True, max_length=36, blank=True, null=True)  # Field name made lowercase.
    dmindicator = models.IntegerField(db_column='dmIndicator', blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=1, blank=True, null=True)  # Field name made lowercase.
    yearofbirth = models.IntegerField(db_column='YearOfBirth', blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=2, blank=True, null=True)  # Field name made lowercase.
    practiceguid = models.CharField(db_column='PracticeGuid', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'training_patient'
# Unable to inspect table 'training_patientCondition'
# The error was: list index out of range
# Unable to inspect table 'training_patientSmokingStatus'
# The error was: list index out of range


class TrainingPatienttranscript(models.Model):
    patientguid = models.TextField(db_column='PatientGuid', blank=True, null=True)  # Field name made lowercase.
    dmindicator = models.IntegerField(db_column='dmIndicator', blank=True, null=True)  # Field name made lowercase.
    gender = models.TextField(db_column='Gender', blank=True, null=True)  # Field name made lowercase.
    yearofbirth = models.IntegerField(db_column='YearOfBirth', blank=True, null=True)  # Field name made lowercase.
    state = models.TextField(db_column='State', blank=True, null=True)  # Field name made lowercase.
    practiceguid = models.TextField(db_column='PracticeGuid', blank=True, null=True)  # Field name made lowercase.
    transcriptguid = models.TextField(db_column='TranscriptGuid', blank=True, null=True)  # Field name made lowercase.
    patientguid_1 = models.TextField(db_column='PatientGuid:1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    visityear = models.IntegerField(db_column='VisitYear', blank=True, null=True)  # Field name made lowercase.
    height = models.TextField(db_column='Height', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    weight = models.FloatField(db_column='Weight', blank=True, null=True)  # Field name made lowercase.
    bmi = models.FloatField(db_column='BMI', blank=True, null=True)  # Field name made lowercase.
    systolicbp = models.IntegerField(db_column='SystolicBP', blank=True, null=True)  # Field name made lowercase.
    diastolicbp = models.IntegerField(db_column='DiastolicBP', blank=True, null=True)  # Field name made lowercase.
    respiratoryrate = models.IntegerField(db_column='RespiratoryRate', blank=True, null=True)  # Field name made lowercase.
    heartrate = models.IntegerField(db_column='HeartRate', blank=True, null=True)  # Field name made lowercase.
    temperature = models.FloatField(db_column='Temperature', blank=True, null=True)  # Field name made lowercase.
    physicianspecialty = models.TextField(db_column='PhysicianSpecialty', blank=True, null=True)  # Field name made lowercase.
    userguid = models.TextField(db_column='UserGuid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'training_patientTranscript'
# Unable to inspect table 'training_prescription'
# The error was: list index out of range


class TrainingSmoke(models.Model):
    patientguid = models.TextField(db_column='PatientGuid', blank=True, null=True)  # Field name made lowercase.
    gender = models.TextField(db_column='Gender', blank=True, null=True)  # Field name made lowercase.
    yearofbirth = models.IntegerField(db_column='YearOfBirth', blank=True, null=True)  # Field name made lowercase.
    state = models.TextField(db_column='State', blank=True, null=True)  # Field name made lowercase.
    practiceguid = models.TextField(db_column='PracticeGuid', blank=True, null=True)  # Field name made lowercase.
    smokeeffectiveyear = models.IntegerField(db_column='SmokeEffectiveYear', blank=True, null=True)  # Field name made lowercase.
    smokingstatus_description = models.TextField(db_column='SmokingStatus_Description', blank=True, null=True)  # Field name made lowercase.
    smokingstatus_nistcode = models.IntegerField(db_column='SmokingStatus_NISTCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'training_smoke'
# Unable to inspect table 'training_transcript'
# The error was: list index out of range
# Unable to inspect table 'training_transcriptAllergy'
# The error was: list index out of range
# Unable to inspect table 'training_transcriptDiagnosis'
# The error was: list index out of range
# Unable to inspect table 'training_transcriptMedication'
# The error was: list index out of range
