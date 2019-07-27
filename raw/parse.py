import xml.etree.ElementTree as ET
root = ET.parse('aixm_ls.xml').getroot()
#for child in root:
    #if child.tag == "Ahp":
    #    print(child.tag, child.attrib)

f = open("apt.geojson","w")
f.write('{\r')
f.write('  "type": "FeatureCollection",\r')
f.write('  "features": [\r')

      
txt = ""
for neighbor in root.iter('Ahp'):
    print(neighbor.find('codeIcao').text, neighbor.find("geoLat").text, neighbor.find("geoLong").text,)
    txt += '    {\r'
    txt += '    "type": "Feature",\r'
    txt += '    "geometry": {\r'
    txt += '      "type": "Point",\r'
    txt += '      "coordinates": ['+neighbor.find("geoLong").text[:-1]+', '+neighbor.find("geoLat").text[:-1]+']\r'
    txt += '    },\r'
    txt += '    "properties": {\r'
    txt += '      "title": "'+neighbor.find('codeIcao').text+'",\r'
    txt += '      "icon": "airport",\r'
    txt += '      "name": "<strong>'+neighbor.find('txtName').text.encode('utf-8').replace('"','')+'</strong>"\r'
    txt += '    }\r'
    txt += "},"

f.write(txt[:-1])
f.write("\r")
f.write(' ]\r')
f.write('}')
f.close()

f = open("nav.geojson","w")
f.write('{\r')
f.write('  "type": "FeatureCollection",\r')
f.write('  "features": [\r')

txt = ""
for neighbor in root.iter('Vor'):
    uid = neighbor.find("VorUid")
    print(uid.find('codeId').text, uid.find("geoLat").text, uid.find("geoLong").text,neighbor.find('txtName').text, neighbor.find("codeType").text, neighbor.find("valFreq").text,)
    txt += '    {\r'
    txt += '    "type": "Feature",\r'
    txt += '    "geometry": {\r'
    txt += '      "type": "Point",\r'
    txt += '      "coordinates": ['+uid.find("geoLong").text[:-1]+', '+uid.find("geoLat").text[:-1]+']\r'
    txt += '    },\r'
    txt += '    "properties": {\r' 
    txt += '      "title": "'+uid.find('codeId').text+'",\r'
    txt += '      "info": "'+neighbor.find('codeType').text+' '+neighbor.find('valFreq').text+'",\r'
    txt += '      "icon": "airport",\r'
    txt += '      "name": "<strong>'+neighbor.find('txtName').text.encode('utf-8').replace('"','')+'</strong>"\r'
    txt += '    }\r'
    txt += "},"

f.write(txt[:-1])
f.write("\r")

for neighbor in root.iter('Ndb'):
    uid = neighbor.find("NdbUid")
    print(uid.find('codeId').text, uid.find("geoLat").text, uid.find("geoLong").text,neighbor.find('txtName').text, neighbor.find("valFreq").text,)

f.write(' ]\r')
f.write('}')
f.close()