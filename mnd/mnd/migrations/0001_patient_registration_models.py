# Generated by Django 2.1.9 on 2019-07-11 02:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patients', '0038_patient_consent_upload_to_change'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientInsurance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicare_number', models.BigIntegerField(blank=True, null=True)),
                ('pension_number', models.BigIntegerField(blank=True, null=True)),
                ('private_health_fund_name', models.CharField(blank=True, choices=[('', 'Private Health Fund'), ('ACA', 'ACA Health Benefits Fund'), ('AHM', 'ahm health insurance'), ('AUF', 'Australian Unity Health Limited'), ('BUP', 'Bupa HI Pty Ltd'), ('CBC', 'CBHS Corporate Health Pty Ltd'), ('CBH', 'CBHS Health Fund Limited'), ('CDH', 'CDH Benefits Fund'), ('CPS', 'CUA Health Limited'), ('AHB', 'Defence Health Limited'), ('AMA', "Doctors' Health Fund"), ('ESH', 'Emergency Services Health'), ('GMH', 'GMHBA Limited'), ('FAI', 'Grand United Corporate Health'), ('HBF', 'HBF Health Limited'), ('HCF', 'HCF'), ('HCI', 'Health Care Insurance Limited'), ('HIF', 'Health Insurance Fund of Australia Limited'), ('SPS', 'Health Partners'), ('HEA', 'health.com.au'), ('LHS', 'Latrobe Health Services'), ('MBP', 'Medibank Private Limited'), ('MDH', 'Mildura Health Fund'), ('MYO', 'MO Health'), ('OMF', 'National Health Benefits Australia Pty Ltd (onemedifund)'), ('NHB', 'Navy Health Ltd'), ('NIB', 'nib Health Funds Ltd.'), ('NMW', 'Nurses & Midwives Health'), ('LHM', 'Peoplecare Health Insurance'), ('PWA', 'Phoenix Health Fund Limited'), ('SPE', 'Police Health'), ('QCH', 'Queensland Country Health Fund Ltd'), ('RTE', 'Railway and Transport Health Fund Limited'), ('RBH', 'Reserve Bank Health Society Ltd'), ('SLM', 'St.Lukes Health'), ('NTF', 'Teachers Health'), ('TFS', 'Transport Health Pty Ltd'), ('QTU', 'TUH Health Fund'), ('WFD', 'Westfund Limited')], max_length=10)),
                ('private_health_fund_number', models.BigIntegerField(blank=True, null=True)),
                ('ndis_number', models.CharField(max_length=30)),
                ('ndis_plan_manager', models.CharField(choices=[('', 'NDIS Plan Manager'), ('self', 'Self'), ('agency', 'Agency'), ('other', 'Other')], max_length=30)),
                ('ndis_coordinator_first_name', models.CharField(blank=True, max_length=30, null=True)),
                ('ndis_coordinator_last_name', models.CharField(blank=True, max_length=30, null=True)),
                ('ndis_coordinator_phone', models.CharField(blank=True, max_length=30, null=True)),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='insurance_data', to='patients.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='PreferredContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('contact_method', models.CharField(choices=[('', 'Preferred contact method'), ('phone', 'Phone'), ('sms', 'SMS'), ('person', 'Nominated person below'), ('email', 'Email')], max_length=30)),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='preferred_contact', to='patients.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='PrimaryCarer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('relationship', models.CharField(choices=[('', 'Primary carer relationship'), ('spouse', 'Spouse'), ('child', 'Child'), ('sibling', 'Sibling'), ('friend', 'Friend'), ('other', 'Other(specify)')], max_length=30)),
                ('relationship_info', models.CharField(blank=True, max_length=30, null=True)),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='primary_carer', to='patients.Patient')),
            ],
        ),
        migrations.AddField(
            model_name='preferredcontact',
            name='primary_carer',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='preferred_contact', to='mnd.PrimaryCarer'),
        ),
    ]
