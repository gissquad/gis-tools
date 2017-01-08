import requests
import json
import psycopg2

USER = "bogdancandrea"
PASSWORD = "fdr2016!"

SEARCH_AREA = 'POLYGON((20.221856546292585 46.1306374626826,21.531040079759293 46.74517759075221,22.46075012526464 47.838996032701424,24.54785430905215 47.991596247529756,26.19856398168409 48.04236299017992,26.7867478880242 48.29544716088847,27.9251683519083 47.08215962168433,28.26669449107353 46.327520363994815,28.247720816675464 45.45595144993119,29.499983326947962 45.41600964158927,29.97432518689967 45.10884983859369,28.58924695584069 43.71292477616252,27.62158956153921 43.972931548226526,26.767774213626137 44.0684378364689,25.705248447334316 43.65804212610262,24.054538774702372 43.72663759278493,22.859197287624074 43.863593131200716,22.53664482285691 44.394719819641466,21.436171707768953 44.74615039735866,20.734145755040426 45.46925910361986,20.221856546292585 46.1306374626826))'
START_DATE = "2017-01-02T00:00:00.000Z"
RECORDS_LIMIT = 100

COUNT_URL = 'https://scihub.copernicus.eu/dhus/api/stub/products/count?filter=(footprint:"Intersects({0})") AND ( beginPosition:[{1} TO NOW] AND endPosition:[{1} TO NOW] ) AND (platformname:Sentinel-2)'
SEARCH_URL = 'https://scihub.copernicus.eu/dhus/api/stub/products?filter=(footprint:"Intersects({0})") AND ( beginPosition:[{1} TO NOW] AND endPosition:[{1} TO NOW] ) AND (platformname:Sentinel-2)&offset={2}&limit={3}&sortedby=beginposition&order=asc'

conn = psycopg2.connect("dbname='sentinel' user='postgres' host='localhost' password='ils121wk'")
cur = conn.cursor()

def extract_node_info(node, node_name):
        for index in node:
                if index["name"] == node_name:
                        return index
        return None

def get_utm_grid(foot_print):
	query = "select name from geo_sentinel_caroiaj_utm where st_intersects(the_geom, st_centroid(st_geometryFromText('{0}', 4326)))".format(foot_print)
	cur.execute(query)
	rows = cur.fetchall()
	return rows

r = requests.get(COUNT_URL.format(SEARCH_AREA, START_DATE), auth=(USER, PASSWORD))

number_of_records = int(r.text)
print "Url folosit: ", COUNT_URL.format(SEARCH_AREA, START_DATE)
print "Sau gasit: ", number_of_records
j = 1
for i in xrange(0,number_of_records,100):
	r = requests.get(SEARCH_URL.format(SEARCH_AREA, START_DATE, i, RECORDS_LIMIT), auth=(USER, PASSWORD))
	content = r.json()
	for record in content:
		uuid = record['uuid']
		_product_info = extract_node_info(record["indexes"], "product")
		_jsts_footprint = extract_node_info(_product_info["children"], "JTS footprint")["value"]
		generation_time = extract_node_info(_product_info["children"], "Generation time")["value"]
		_utm_grid_list = get_utm_grid(_jsts_footprint)
		careuri = ""
		for row in _utm_grid_list:
			careuri = careuri + ' ' + row[0]
		print j, uuid, generation_time, careuri
		j = j + 1

conn.close()
