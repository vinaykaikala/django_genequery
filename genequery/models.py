from django.db import models as mysql


class GeneAutoComplete(mysql.Model):
    class Meta:
        db_table = 'gene_autocomplete'

    species = mysql.CharField(max_length=255) #mysql.Column(mysql.String(255), nullable=False)
    stable_id = mysql.CharField(max_length=128, primary_key=True) #mysql.Column(mysql.String(128), nullable=False , primary_key=True)
    display_label = mysql.CharField(max_length=128) #mysql.Column(mysql.String(128), nullable=False)
    location = mysql.CharField(max_length=60) #mysql.Column(mysql.String(60), nullable=False)
    db = mysql.CharField(max_length=128) #mysql.Column(mysql.String(128), nullable=False)

