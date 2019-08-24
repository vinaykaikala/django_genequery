from django.shortcuts import render
from genequery.business import get_genes
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods

def index(request):
    return render(request, 'bootstrap.html')
    #return HttpResponse("Gene Search Catalog is Working....")


@require_http_methods(["GET"])
def search(request):
    lookup = request.GET.get('lookup', None)
    species = request.GET.get('species', None)
    if not lookup or len(lookup) < 3:
        return JsonResponse({"errors": {"lookup": "Gene name example: BRAF Missing required parameter in the JSON body or the post body or the query string", "message": "Input payload validation failed lookup value should be gtrater than equal to 3"}}, status=400)
    results = get_genes(lookup, species)
    return JsonResponse(list(results), safe=False)
