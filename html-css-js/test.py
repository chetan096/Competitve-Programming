import sys

#in = sys.stdin
#sys.stdin = open('IP.txt', 'r')
#sys.stdin = in

lst=[{"country":"India","state":"jk","district":"doda","block":"101","panchayat":"A","village":"a","population":123,"literacy_rate":0.75},
    {"country":"India","state":"jk","district":"doda","block":"101","panchayat":"B","village":"b","population":126,"literacy_rate":0.89},
     {"country":"India","state":"punjab","district":"sangrur","block":"132","panchayat":"C","village":"c","population":1236,"literacy_rate":0.809},
     {"country":"India","state":"up","district":"agra","block":"1332","panchayat":"D","village":"d","population":1226,"literacy_rate":0.489},
     {"country":"India","state":"mp","district":"sagar","block":"123","panchayat":"E","village":"e","population":12263,"literacy_rate":0.689},
     {"country":"India","state":"uk","district":"dehradun","block":"13","panchayat":"F","village":"f","population":1236,"literacy_rate":0.789},
     {"country":"India","state":"hp","district":"shimla","block":"11","panchayat":"G","village":"g","population":1236,"literacy_rate":0.819}]

state={}
district={}
block={}
panchayat={}
village={}

for i in lst:
    state_name=i["state"]
    district_name=i["district"]
    block_name=i["block"]
    panchayat_name=i["panchayat"]
    village_name=i["village"]
    
    if state.get(state_name,"none")=="none":
        state[state_name]=[]
        state[state_name].append(i)
    else:
        state[state_name].append(i)

    if district.get(district_name,"none")=="none":
        district[district_name]=[]
        district[district_name].append(i)
    else:
        district[district_name].append(i)
        
    if block.get(block_name,"none")=="none":
        block[block_name]=[]
        block[block_name].append(i)
    else:
        block[block_name].append(i)

    if panchayat.get(panchayat_name,"none")=="none":
        panchayat[panchayat_name]=[]
        panchayat[panchayat_name].append(i)
    else:
        panchayat[panchayat_name].append(i)

#Outputting data to different files
out = sys.stdout
sys.stdout = open('state.txt', 'w')
print state
sys.stdout = out

out = sys.stdout
sys.stdout = open('district.txt', 'w')
print district
sys.stdout = out

out = sys.stdout
sys.stdout = open('block.txt', 'w')
print block
sys.stdout = out

out = sys.stdout
sys.stdout = open('panchayat.txt', 'w')
print panchayat
sys.stdout = out





