from genequery.models import GeneAutoComplete as genetable
from django.core import serializers
from django.db.models import F

def get_genes(lookup, species=None):
        #result = serializers.serialize('json',genetable.objects.filter(display_label__startswith='bra').values(), fields=('species', 'stable_id', 'display_label', 'location'))
        
        result =  genetable.objects.filter(display_label__startswith=lookup)

        if species:
            result =  result.filter(species__exact=species)

        return result.values(species_name = F('species'), 
                ensembl_stable_id = F('stable_id'),  gene_name = F('display_label'), gene_location = F('location'))
