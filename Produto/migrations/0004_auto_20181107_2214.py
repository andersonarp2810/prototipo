# Generated by Django 2.1.1 on 2018-11-08 00:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Produto', '0003_produto_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foto',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fotos', to='Produto.Produto'),
        ),
    ]