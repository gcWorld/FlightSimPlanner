import xml.etree.ElementTree as ET
root = ET.parse('aixm_ls.xml').getroot()
#for child in root:
    #if child.tag == "Ahp":
    #    print(child.tag, child.attrib)

f = open("apt.geojson","w")
f.write('{\r')
f.write('  "type": "FeatureCollection",\r')
f.write('  "features": [\r')

      

for neighbor in root.iter('Ahp'):
    print(neighbor.find('codeIcao').text, neighbor.find("geoLat").text, neighbor.find("geoLong").text,)
    f.write('    {\r')
    f.write('    "type": "Feature",\r')
    f.write('    "geometry": {\r')
    f.write('      "type": "Point",\r')
    f.write('      "coordinates": ['+neighbor.find("geoLong").text[:-1]+', '+neighbor.find("geoLat").text[:-1]+']\r')
    f.write('    },\r')
    f.write('    "properties": {\r')  
    f.write('      "title": "'+neighbor.find('codeIcao').text+'",\r')  
    f.write('      "icon": "airport",\r')
    f.write('      "name": "<strong>'+neighbor.find('txtName').text.encode('utf-8')+'</strong>"\r')
    f.write('    }\r')
    f.write("},\r")
f.write(' ]\r')
f.write('}')
f.close()

for neighbor in root.iter('Vor'):
    uid = neighbor.find("VorUid")
    print(uid.find('codeId').text, uid.find("geoLat").text, uid.find("geoLong").text,neighbor.find('txtName').text, neighbor.find("codeType").text, neighbor.find("valFreq").text,)

for neighbor in root.iter('Ndb'):
    uid = neighbor.find("NdbUid")
    print(uid.find('codeId').text, uid.find("geoLat").text, uid.find("geoLong").text,neighbor.find('txtName').text, neighbor.find("valFreq").text,)