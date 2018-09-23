from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Availstatic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row_date', models.DateField(blank=True, null=True)),
                ('Customer', models.CharField(blank=True, db_column='Customer', max_length=50, null=True)),
                ('Age', models.CharField(blank=True, db_column='Age', max_length=50, null=True)),
                ('N_Child', models.CharField(blank=True, db_column='N_Child', max_length=101, null=True)),
                ('sessid', models.CharField(blank=True, max_length=15, null=True)),
                ('starttime_utc', models.BigIntegerField(blank=True, null=True)),
                ('scheduled_start', models.CharField(blank=True, db_column='Scheduled Start', max_length=50, null=True)),
                ('scheduled_stop', models.CharField(blank=True, db_column='Scheduled Stop', max_length=50, null=True)),
                ('interval_time', models.CharField(blank=True, db_column='Interval Time', max_length=8, null=True)),
                ('duration', models.TimeField(blank=True, null=True)),
                ('total_interval_time', models.BigIntegerField(blank=True, db_column='Total Interval Time', null=True)),
                ('total_productive_status', models.TimeField(blank=True, db_column='Total Productive Status', null=True)),
                ('availability', models.DecimalField(blank=True, db_column='Availability', decimal_places=4, max_digits=41, null=True)),
                ('total_acd_time', models.TimeField(blank=True, db_column='Total ACD Time', null=True)),
                ('appt_call', models.TimeField(blank=True, db_column='appt', null=True)),
                ('hld_time', models.TimeField(blank=True, db_column='Hold Time', null=True)),
                ('total_acw_time', models.TimeField(blank=True, db_column='Total ACW Time', null=True)),
                ('user1_time', models.TimeField(blank=True, db_column='user1 Time', null=True)),
                ('user1_time', models.TimeField(blank=True, db_column='user2 Time', null=True)),
                ('staffed_time', models.TimeField(blank=True, db_column='Staffed Time', null=True)),
                ('internal_aux_time', models.TimeField(blank=True, db_column='Internal AUX Time', null=True)),
                ('aux_default', models.TimeField(blank=True, db_column='AUX Default', null=True)),
                ('first_rep', models.TimeField(blank=True, db_column='First Rep', null=True)),
                ('second_rep', models.TimeField(blank=True, db_column='Second Rep', null=True)),
                ('train', models.TimeField(blank=True, db_column='Train', null=True)),
                ('lunchen', models.TimeField(blank=True, db_column='Lunchen', null=True)),
                ('meetin', models.TimeField(blank=True, db_column='Meetin', null=True)),
                ('personal', models.TimeField(blank=True, db_column='Personal1', null=True)),
                ('project', models.TimeField(blank=True, db_column='Project1', null=True)),
                ('case_management', models.TimeField(blank=True, db_column='Case Management', null=True)),
                ('third_breakeven', models.TimeField(blank=True, db_column='Third Breakeven', null=True)),
                ('coaching1', models.TimeField(blank=True, db_column='Coaching1', null=True)),
                ('outbound_voice1', models.TimeField(blank=True, db_column='Outbound Voice2', null=True)),
                ('get_next1', models.TimeField(blank=True, db_column='Get Next1', null=True)),
                ('vip_escalationen', models.TimeField(blank=True, db_column='VIP Escalationen', null=True)),
                ('handling_escalationens', models.TimeField(blank=True, db_column='Handling Escalationen', null=True)),
                ('acdcalls', models.SmallIntegerField(blank=True, null=True)),
                ('da_acdcalls', models.SmallIntegerField(blank=True, null=True)),
                ('total_acd_other_time', models.TimeField(blank=True, db_column='Total ACD Other Time', null=True)),
                ('total_acd_aux_out_time', models.TimeField(blank=True, db_column='Total ACD/AUX Out Time', null=True)),
                ('total_acd_aux_in_time', models.TimeField(blank=True, db_column='total ACD/AUX In Time', null=True)),
                ('total_aux_in_time', models.TimeField(blank=True, db_column='Total AUX in Time', null=True)),
                ('modfied', models.DateTimeField(blank=True, db_column='Modfied', null=True)),
            ],
            options={
                'db_table': 'availstatic_copy',
                'managed': False,
            },
        ),
    ]
