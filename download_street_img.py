# rotatory angle downloadimport requestsGOOGLE_KEY = "AIzaSyBYlPO30E34zPkUG5MQAY2I-d2MhZlVR8g"IMG_WIDTH, IMG_HEIGHT = (600, 600)ANGLE_SHIFT = 4 # 360 / 90PITCH_ANG = -60 # should stay constantgeo1 = {  "addr"  : "W Post Rd, White Plains, NY",   "geoloc": (41.0176417,-73.7772902)  }geo2 = {  "addr"  : "W Post Rd, White Plains, NY",   "geoloc": (41.020012, -73.776141)  }geo3 = {  "addr"  : "W Post Rd, White Plains, NY",   "geoloc": (41.022670, -73.774865)  }geo4 = {  "addr"  : "W Post Rd, White Plains, NY",   "geoloc": (41.024367, -73.772952)  }geo5 = {  "addr"  : "E Post Rd, White Plains, NY",   "geoloc": (41.026623, -73.769262)  }geo6 = {  "addr"  : "E Post Rd, White Plains, NY",   "geoloc": (41.029930, -73.763814)  }geo7 = {  "addr"  : "E Post Rd, White Plains, NY",   "geoloc": (41.029816, -73.764083)  }geo7 = {  "addr"  : "E Post Rd, White Plains, NY",   "geoloc": (41.031143, -73.762136)  }geo8 = {  "addr"  : "N Broadway, White Plains, NY",   "geoloc": (41.034627, -73.763780)  }geo9 = {  "addr"  : "N Broadway, White Plains, NY",   "geoloc": (41.040754, -73.767644)  }geo10 = {  "addr"  : "N Broadway, White Plains, NY",   "geoloc": (41.043902, -73.768910)  }geo_list = [geo1, geo2, geo3, geo4, geo5,            geo6, geo7, geo8, geo9, geo10]def get_image(loc_lat, loc_long , heading):    image_url = f"https://maps.googleapis.com/maps/api/streetview?size={IMG_WIDTH}x{IMG_HEIGHT}&location={loc_lat},{loc_long}&heading={heading}&pitch={PITCH_ANG}&key={GOOGLE_KEY}"  img_data = requests.get(image_url).content    return img_data  for c in range(len(geo_list)):  for i_ang in range (ANGLE_SHIFT):    loc_lat, loc_long = geo_list[c]['geoloc']    heading = 360 / ANGLE_SHIFT  * i_ang # to cover 360 degree    img_data = get_image(loc_lat, loc_long , heading)    image_name = f'image{4*c +i_ang}.jpg'    with open(f'./street_dataset/{image_name}', 'wb') as handler:        handler.write(img_data)"""# one angle image downloadimport requestsgkey = "AIzaSyBYlPO30E34zPkUG5MQAY2I-d2MhZlVR8g"img_w, img_h = (600, 600)loc_lat, loc_long = (41.0176417,-73.7772902)heading = 180pitch = -60         # should stay constantimage_url = f"https://maps.googleapis.com/maps/api/streetview?size={img_w}x{img_h}&location={loc_lat},{loc_long}&heading={heading}&pitch={pitch}&key={gkey}"img_data = requests.get(image_url).contenti = 0image_name = f'image{i}'with open(f'./street_dataset/change{image_name}', 'wb') as handler:    handler.write(img_data)"""