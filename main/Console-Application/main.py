import json
import math
import random
import matplotlib.colors as colors
import folium.vector_layers
import webbrowser
import time

def open_file_json(filename):
    with open(filename , encoding='utf-8') as f:
        cities_json = json.load(f)
    cities_names = []
    cities_coords = {}
    for city in cities_json:
        if not(city['city'] in cities_names):
            cities_names.append(city['city'])
            cities_coords[city['city']] = (float(city['lat']), float(city['lng']))
    print("Loaded " + str(len(cities_names)) + " nodes")
    return cities_names, cities_coords


def distance_calculator(c1, c2, cities_coords):
    city_1 = cities_coords[c1]
    city_2 = cities_coords[c2]
    diff = (city_1[0] - city_2[0], city_1[1] - city_2[1])
    return math.sqrt(diff[0] * diff[0] + diff[1] * diff[1])


def distance_matrix_generator(cities_names, cities_coords):
    distance_matrix = {}
    for city_1 in cities_names:
        for city_2 in cities_names:
            if city_1 != city_2:
                distance_matrix[(city_1, city_2)] = distance_calculator(city_1, city_2, cities_coords)
            else:
                distance_matrix[(city_1, city_2)] = 0.0
    return distance_matrix


def fun_obj(cities_names, distance_matrix, medians):
    min_distances = []
    for i in cities_names:
        distances = []
        if not(i in medians):
            for j in medians:
                distances.append(distance_matrix[i, j])
            min_distances.append(min(distances))
    res = sum(min_distances)
    return res


def tb_heuristic(cities_names, distance_matrix, p):

    start_time = time.perf_counter()
    medians = random.sample(cities_names, p)
    z = fun_obj(cities_names, distance_matrix, medians)

    print("Start random solution => Z: " + str(z) + " P-Medians: " + str(medians))

    bad_medians = []
    end_loop = False
    k = 0
    while not end_loop:
        savings = {}
        max_val = -1
        cont_negative = 0
        for j in cities_names:
            if not (j in medians) and not (j in bad_medians):
                cont = 0
                for i in medians:
                    tmp_median = medians.copy()
                    tmp_median[tmp_median.index(i)] = j
                    z_new = fun_obj(cities_names, distance_matrix, tmp_median)
                    savings[(i, j)] = z - z_new
                    if savings[(i, j)] < 0:
                        cont_negative = cont_negative + 1
                        cont = cont + 1
                    else:
                        if savings[(i, j)] > max_val:
                            max_val = savings[(i, j)]
                            best_z = z_new
                            best_medians = tmp_median.copy()
                if cont == p:
                    bad_medians.append(j)

        if cont_negative != len(savings):
            medians = best_medians.copy()
            z = best_z
            print("Solution " + str(k) + " => Z: " + str(z) + " P-Medians: " + str(medians))
            k = k + 1
        else:
            print("Best solution at " + str(k-1) + " => Z: " + str(z) + " P-Medians: " + str(medians))
            end_time = time.perf_counter()
            print("Best solution in " + str(round(end_time - start_time, 2)) + "s")
            end_loop = True
    return z, medians


def assegnamento(distance_matrix, cities_names, centroids):

    cluster_matrix = {}
    for i in cities_names:
        if not(i in centroids):
            min_val = 100000000
            for j in centroids:
                if distance_matrix[(i, j)] < min_val:
                    min_val = distance_matrix[(i, j)]
                    centroid = j
            cluster_matrix[(i, centroid)] = min_val
    return cluster_matrix


def map_generator(cluster_matrix, centroids, cities_coords):

    lat, lng = cities_coords[centroids[0]]
    colors_array = []
    for i in range(len(centroids)):
        colors_array.append([random.random(), random.random(), random.random()])
    map_clusters = folium.Map(location=[lat, lng], zoom_start=4)
    cont = 0
    for k in centroids:
        for i, j in cluster_matrix:
            if j == k:
                lat, lng = cities_coords[i]
                folium.vector_layers.CircleMarker(
                    [lat, lng],
                    radius=10,
                    tooltip='Node: ' + str(i) + ' Lat: ' + str(lat) + ' Lng: ' + str(lng),
                    color=colors.to_hex(colors_array[cont]),
                    fill=True,
                    fill_color=colors.to_hex(colors_array[cont]),
                    fill_opacity=0.9
                ).add_to(map_clusters)
        cont = cont + 1
        lat, lng = cities_coords[k]
        folium.vector_layers.Marker(
            [lat, lng],
            radius=10,
            tooltip='Centroids: ' + str(k) + ' Lat: ' + str(lat) + ' Lng: ' + str(lng)
        ).add_to(map_clusters)
    return map_clusters


if __name__ == "__main__":

    errore = 1
    while errore == 1:
        try:
            print("Insert json file path included file name and file type (like C:/Folder/filename.json)")
            filename = str(input())
            cities_names, cities_coords = open_file_json(filename)
            errore = 0
        except():
            print("Error!")
            print("Check that path is correct!")
            print("The elements of file json must have")
            print("\"city\":\"CityName\"")
            print("\"lat\": (float)lat")
            print("\"lng\": (float)lng")

    errore_1 = 1
    while errore_1 == 1:
        try:
            print("Insert the P variable: ")
            p = int(input())
            distance_matrix = distance_matrix_generator(cities_names, cities_coords)
            z, centroids = tb_heuristic(cities_names, distance_matrix, p)
            errore_1 = 0
        except(ValueError):
            print("P must be a number > 0!")

    print("Creating clusters...")
    cluster_matrix = assegnamento(distance_matrix, cities_names, centroids)
    map_clusters = map_generator(cluster_matrix, centroids, cities_coords)
    map_clusters.save('./map.html')
    print("Clusters generated!")
    print("Do you want show clusters on your browser? (y/N)")
    x = str(input())
    if x == "Y" or x == "y":
        webbrowser.open("map.html")
        print("Goodbye!")
    else:
        print("Goodbye!")

    input()
