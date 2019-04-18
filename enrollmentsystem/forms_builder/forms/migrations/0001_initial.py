# Generated by Django 2.0.1 on 2019-04-15 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('enrollment', '0001_initial'),
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=200, verbose_name='Label')),
                ('slug', models.SlugField(blank=True, default='', max_length=2000, verbose_name='Slug')),
                ('field_type', models.IntegerField(choices=[(1, 'Single line text'), (2, 'Multi line text'), (3, 'Email'), (13, 'Number'), (14, 'URL'), (4, 'Check box'), (5, 'Check boxes'), (6, 'Drop down'), (7, 'Multi select'), (8, 'Radio buttons'), (9, 'File upload'), (10, 'Date'), (11, 'Date/time'), (15, 'Date of birth'), (12, 'Hidden')], verbose_name='Type')),
                ('required', models.BooleanField(default=True, verbose_name='Required')),
                ('visible', models.BooleanField(default=True, verbose_name='Visible')),
                ('choices', models.CharField(blank=True, help_text='Comma separated options where applicable. If an option itself contains commas, surround the option starting with the `character and ending with the ` character.', max_length=1000, verbose_name='Choices')),
                ('default', models.CharField(blank=True, max_length=2000, verbose_name='Default value')),
                ('placeholder_text', models.CharField(blank=True, max_length=100, null=True, verbose_name='Placeholder Text')),
                ('help_text', models.CharField(blank=True, max_length=100, verbose_name='Help text')),
                ('order', models.IntegerField(blank=True, null=True, verbose_name='Order')),
            ],
            options={
                'verbose_name': 'Field',
                'verbose_name_plural': 'Fields',
                'ordering': ('order',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FieldEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_id', models.IntegerField()),
                ('value', models.CharField(max_length=2000, null=True)),
            ],
            options={
                'verbose_name': 'Form field entry',
                'verbose_name_plural': 'Form field entries',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('slug', models.SlugField(editable=False, max_length=100, unique=True, verbose_name='Slug')),
                ('intro', models.TextField(blank=True, verbose_name='Intro')),
                ('button_text', models.CharField(default='Submit', max_length=50, verbose_name='Button text')),
                ('response', models.TextField(blank=True, verbose_name='Response')),
                ('redirect_url', models.CharField(blank=True, help_text='An alternate URL to redirect to after form submission', max_length=200, null=True, verbose_name='Redirect url')),
                ('status', models.IntegerField(choices=[(1, 'Draft'), (2, 'Published')], default=2, verbose_name='Status')),
                ('publish_date', models.DateTimeField(blank=True, help_text="With published selected, won't be shown until this time", null=True, verbose_name='Published from')),
                ('expiry_date', models.DateTimeField(blank=True, help_text="With published selected, won't be shown after this time", null=True, verbose_name='Expires on')),
                ('login_required', models.BooleanField(default=False, help_text='If checked, only logged in users can view the form', verbose_name='Login required')),
                ('send_email', models.BooleanField(default=True, help_text='If checked, the person entering the form will be sent an email', verbose_name='Send email')),
                ('email_from', models.EmailField(blank=True, help_text='The address the email will be sent from', max_length=254, verbose_name='From address')),
                ('email_copies', models.CharField(blank=True, help_text='One or more email addresses, separated by commas', max_length=200, verbose_name='Send copies to')),
                ('email_subject', models.CharField(blank=True, max_length=200, verbose_name='Subject')),
                ('email_message', models.TextField(blank=True, verbose_name='Message')),
                ('sites', models.ManyToManyField(default=[1], related_name='forms_form_forms', to='sites.Site')),
            ],
            options={
                'verbose_name': 'Form',
                'verbose_name_plural': 'Forms',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FormEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_time', models.DateTimeField(verbose_name='Date/time')),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='enrollment.Child')),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='forms.Form')),
            ],
            options={
                'verbose_name': 'Form entry',
                'verbose_name_plural': 'Form entries',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='fieldentry',
            name='entry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fields', to='forms.FormEntry'),
        ),
        migrations.AddField(
            model_name='field',
            name='form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fields', to='forms.Form'),
        ),
    ]