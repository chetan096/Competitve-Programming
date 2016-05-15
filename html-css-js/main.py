import sys
#in = sys.stdin
#sys.stdin = open('IP.txt', 'r')
#sys.stdin = in

dict={'punjab': [{'state': 'punjab', 'literacy_rate': 0.809, 'district': 'sangrur', 'village': 'c', 'country': 'India', 'panchayat': 'C', 'block': '132', 'population': 1236}], 'up': [{'state': 'up', 'literacy_rate': 0.489, 'district': 'agra', 'village': 'd', 'country': 'India', 'panchayat': 'D', 'block': '1332', 'population': 1226}], 'mp': [{'state': 'mp', 'literacy_rate': 0.689, 'district': 'sagar', 'village': 'e', 'country': 'India', 'panchayat': 'E', 'block': '123', 'population': 12263}], 'uk': [{'state': 'uk', 'literacy_rate': 0.789, 'district': 'dehradun', 'village': 'f', 'country': 'India', 'panchayat': 'F', 'block': '13', 'population': 1236}], 'jk': [{'state': 'jk', 'literacy_rate': 0.75, 'district': 'doda', 'village': 'a', 'country': 'India', 'panchayat': 'A', 'block': '101', 'population': 123}, {'state': 'jk', 'literacy_rate': 0.89, 'district': 'doda', 'village': 'b', 'country': 'India', 'panchayat': 'B', 'block': '101', 'population': 126}], 'hp': [{'state': 'hp', 'literacy_rate': 0.819, 'district': 'shimla', 'village': 'g', 'country': 'India', 'panchayat': 'G', 'block': '11', 'population': 1236}]}
state=[]
for key,val in dict.items():#val is a list
    state_name=key
    temp={}
    temp["state"]=state_name
    temp["literacy_rate"]=0
    population=0
    for i in val:#i is a dictionary
        population+=i["population"]
        temp["literacy_rate"]+=i["population"]*i["literacy_rate"]
    temp["literacy_rate"]/=population
    state.append(temp)

print state
        
    
   


