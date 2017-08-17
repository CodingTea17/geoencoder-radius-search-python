import geocoder
from haversine import haversine

addresses_to_convert = ['3500 NE Francis Ave,Gresham, OR 97030', '3427 NE Francis Ave, Gresham, OR 97030', '2106 NE 34th St, Gresham, OR 97030', '2030 NE 36th Ct,Gresham, OR 97030', '2312 NW 217th Ave, Gresham, OR 97030', '1207 SE 217th Ave,Gresham, OR 97030']

converted_addresses = []

for address in addresses_to_convert:
    encode = geocoder.google(address)
    converted_addresses.append(encode.latlng)

for coordinates in converted_addresses:
    print(coordinates)

home = converted_addresses[0]

for coordinates in converted_addresses:
    distance = haversine(home, coordinates, miles=True)
    if(distance <= 1):
        print(str(distance) + " " + str(coordinates))
