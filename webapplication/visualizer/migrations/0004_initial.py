# Generated by Django 4.2 on 2023-04-18 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("visualizer", "0003_delete_company_delete_stockprice"),
    ]

    operations = [
        migrations.CreateModel(
            name="Company",
            fields=[
                (
                    "ticker",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
                ("company_name", models.CharField(max_length=255)),
                ("exchange", models.CharField(max_length=255)),
                ("industry", models.CharField(max_length=255)),
            ],
            options={
                "db_table": "companies",
            },
        ),
        migrations.CreateModel(
            name="StockPrice",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ticker", models.CharField(max_length=10)),
                ("date", models.DateField()),
                ("open_price", models.FloatField()),
                ("high_price", models.FloatField()),
                ("low_price", models.FloatField()),
                ("close_price", models.FloatField()),
                ("volume", models.FloatField()),
            ],
            options={
                "db_table": "stock_prices",
                "unique_together": {("ticker", "date")},
            },
        ),
    ]
