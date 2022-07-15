from modules import *
from main import App
import folium
import folium.vector_layers
import matplotlib.colors as colors

def open_file_json(filename):
    with open(filename, encoding='utf-8') as f:
        cities_json = json.load(f)
    cities_names = []
    cities_coords = {}
    for city in cities_json:
        if not(city['city'] in cities_names):
            cities_names.append(city['city'])
            cities_coords[city['city']] = (float(city['lat']), float(city['lng']))
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
                    tooltip='Nodo: ' + str(i) + ' Lat: ' + str(lat) + ' Lng: ' + str(lng),
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
            tooltip='Centroide: ' + str(k) + ' Lat: ' + str(lat) + ' Lng: ' + str(lng)
        ).add_to(map_clusters)
    return map_clusters