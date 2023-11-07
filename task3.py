#from rdflib import URIRef
from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper('https://dbpedia.org/sparql')

query = """
PREFIX dbr: <http://dbpedia.org/resource/>
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX dbp: <http://dbpedia.org/property/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?act1 ?act2
WHERE {
    { 
        ?act1 dbp:occupation "Actor"@en . 
    }
    UNION 
    {
        ?act1 dbp:occupation "Actress"@en . 
    }
    # передбачено одностатеві сімейні пари

    { 
        ?act2 dbp:occupation "Actor"@en . 
    }
    UNION 
    {
        ?act2 dbp:occupation "Actress"@en . 
    }

   ?film dbo:starring ?act1 .
   ?film dbo:starring ?act2  .

  ?act1 dbo:spouse ?act2 .    
}
"""

sparql.setQuery(query)
sparql.setReturnFormat(JSON)
query_res = sparql.query().convert()
#print(query_res)

print('Сімейні акторські пари, які знімалися разом у фільмах:')
for value in query_res['results']['bindings']:
    person1 = value['act1']['value']
    person2 = value['act2']['value']
    print(person1 + '   ' + person2)