import geopy

geocoder = geopy.ArcGIS()
lugar = input("Introduce un lugar: ")

direccion = geocoder.geocode(lugar)
p = direccion.point

print("ArcGIS: \t" + str(round(p.latitude,4))+"\t"+str(round(p.longitude,4)))

geocoder = geopy.GeoNames(username="aitorcalero")

direccion = geocoder.geocode(lugar)
p = direccion.point

print("GeoNames: \t"+ str(round(p.latitude,4)) + "\t"+str(round(p.longitude,4)))

