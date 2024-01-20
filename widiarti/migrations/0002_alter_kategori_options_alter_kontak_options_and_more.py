# Generated by Django 4.2.7 on 2023-11-30 03:35

import ckeditor.fields
from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('widiarti', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kategori',
            options={'verbose_name_plural': 'Data Kategori'},
        ),
        migrations.AlterModelOptions(
            name='kontak',
            options={'verbose_name_plural': 'Data Kontak'},
        ),
        migrations.AlterModelOptions(
            name='produk',
            options={'verbose_name_plural': 'Data Produk'},
        ),
        migrations.AlterModelOptions(
            name='profil',
            options={'verbose_name_plural': 'Data Profil'},
        ),
        migrations.AlterModelOptions(
            name='slide',
            options={'verbose_name_plural': 'Data Slide'},
        ),
        migrations.AlterModelOptions(
            name='statis',
            options={'verbose_name_plural': 'Data Statis'},
        ),
        migrations.RenameField(
            model_name='produk',
            old_name='no_whatsup',
            new_name='no_whatsApp',
        ),
        migrations.AlterField(
            model_name='kategori',
            name='banner_dua',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format=None, keep_meta=True, null=True, quality=80, scale=None, size=[575, 200], upload_to='gambar/banner', verbose_name='Gambar (575 x 200 pixel)'),
        ),
        migrations.AlterField(
            model_name='kategori',
            name='banner_satu',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format=None, keep_meta=True, null=True, quality=80, scale=None, size=[575, 200], upload_to='gambar/banner', verbose_name='Gambar (575 x 200 pixel)'),
        ),
        migrations.AlterField(
            model_name='produk',
            name='keterangan',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profil',
            name='keterangan',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
