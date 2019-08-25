Django gene_queryh application
=============

- Instal
--
``` 
    - git clone  https://github.com/vinaykaikala/django_genequery.git
    - cd django_genequery
    - conda env create -f environment.yml
    - conda activate django
```
 - Run application
    --
```
    -python manage.py runserver
```

 - Example
--
```
    -UI  : http://localhost:8000
```
    ![alt text](https://raw.githubusercontent.com/vinaykaikala/django_genequery/master/ui.png)
```
    -API : http://localhost:8000/genequery/search?lookup=brap
    -API : http://localhost:8000/genequery/search?lookup=bra&species=amphilophus_citrinellus 
```


