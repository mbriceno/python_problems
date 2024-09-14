import requests


some_list = [3, 6, 7, 12, 8, 11, 20]


# It's not the best solution, then I can review and refactor with a generator and xrange
def random_list():
    return [i for i in range(1, 21)]


rand_list = random_list()

print(rand_list)


def filter_below_10(number_list):
    return [e for e in number_list if e < 10]


list_comprehension_below_10 = filter_below_10(some_list)


print("With list comprehention")
print(list_comprehension_below_10)


def filter_below_10_with_filter(number_list):
    return filter(lambda e: e < 10,  number_list)


filter_below_10 = list(filter_below_10_with_filter(some_list))


print("With filter")
print(filter_below_10)


def get_coodinates(addresses):
    list_coordinates = []

    for address in addresses:        
        payload = {
            "key": "AIzaSyDbsIgLoRKjR6INwR3dSkVdw-XVuCRc88I",
            "address": address
        }

        response = requests.get(
            "https://maps.googleapis.com/maps/api/geocode/json", 
            params=payload
        )
        json_rq = response.json()

        if response.status_code in [200, 201]:
            list_coordinates.append(
                {
                    "lat": json_rq["results"][0]["geometry"]["location"]["lat"],
                    "lng": json_rq["results"][0]["geometry"]["location"]["lng"]
                }
            )

    return list_coordinates


addresses = [
    "8525 west verde way las vegas",
    "442 west 44th street new york",
    "1917 mckinley ave atlantic city new jersey"
]

list_coord = get_coodinates(addresses)

for coord in list_coord:
    print("Latitude: {}, Longuitude: {}".format(coord["lat"], coord["lng"]))
