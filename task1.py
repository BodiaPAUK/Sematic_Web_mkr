from rdflib import URIRef, Literal, Namespace, Graph

graph = Graph()
graph.parse('countrues_info.ttl')

EX = Namespace("http://example.com/demo/")


countries = []
result_neighbour = []
for subj, pred, obj in graph:
    if (pred == URIRef("http://example.com/demo/part_of_continent") and
            obj == URIRef("http://example.com/demo/Continent/EU")):
        countries.append(subj)
        #print(subj, pred, obj)

for i in range(len(countries)):
    temp_neighbours = []
    for subj, pred, obj in graph.triples((countries[i], URIRef("http://example.com/demo/has_country_neighbour"), None)):
        #neighbour_0 = obj
        for subj1, pred1, obj1 in graph.triples((obj, URIRef("http://example.com/demo/country_neighbour_value"), None)):
            temp_neighbours.append(obj1) # довжина 1

    #print(temp_neighbours)

    temp_neighbours_areas = []
    max_area_country = ''
    max_area = -1
    for j in range(len(temp_neighbours)):

        for subj, pred, obj in graph.triples((temp_neighbours[j], URIRef("http://example.com/demo/area_in_sq_km"), None)):
            # довжина 1
            if float(obj)> max_area:
                max_area = float(obj)
                max_area_country = temp_neighbours[j]

    result_neighbour.append(max_area_country)


#print(len(countries))
#print(len(result_neighbour))
for i in range(len(countries)):
    if str(result_neighbour[i]) == '':
        neighbour = 'відсутній'
    else:
        neighbour = str(result_neighbour[i])
    print('Для країни ' + str(countries[i]) + ' сусід з найбільшою площею - ' + neighbour)
