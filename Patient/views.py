from django.shortcuts import render
import requests

# Create your views here.
def patient(request):
    try:
        nam = request.GET['name']
        gen = request.GET['gender']
    except:
        nam = ""
        gen = ""

    print(nam)
    print(gen)

    if nam == "" and gen =="" :
        url = "http://localhost:8888/Patient"
        payload = {}
        headers = {
          'Authorization': 'Basic cm9vdDpzZWNyZXQ='
        }

        response = requests.request("GET", url, headers=headers, data = payload)
        d = response.json()
        print(type(d))
        op = len(d['entry'])
        print(op)
        print('-----------------------------')
        dict1 = {}
        for j in range(0,op):
        	for i,m in d['entry'][j]['resource'].items():
        		if i == "id":
        			jk = m

        	try:
        		for i in d['entry'][j]['resource']['name']:
        			kk = i['given'][0]

        	except:
        		kk ='Name Unknow'

        	dict1[jk] = kk
        #	print(jk)
        #	print('{} ---- {} ---- {}'.format(j,kk, jk))

        print(dict1)
        ls = [1,2,3,4,5]
        return render(request,'patient.html',{'key1':dict1})
    else:
        url = "http://localhost:8888/Patient?name="+nam+"&gender="+gen
        payload = {}
        headers = {
          'Authorization': 'Basic cm9vdDpzZWNyZXQ='
        }

        response = requests.request("GET", url, headers=headers, data = payload)
        d = response.json()
        print(type(d))
        op = len(d['entry'])
        print(op)
        print('-----------------------------')
        dict1 = {}
        for j in range(0,op):
        	for i,m in d['entry'][j]['resource'].items():
        		if i == "id":
        			jk = m

        	try:
        		for i in d['entry'][j]['resource']['name']:
        			kk = i['given'][0]

        	except:
        		kk ='Name Unknow'

        	dict1[jk] = kk
        #	print(jk)
        #	print('{} ---- {} ---- {}'.format(j,kk, jk))

        print(dict1)
        ls = [1,2,3,4,5]
        return render(request,'patient.html',{'key1':dict1})




def patientrecord(request, id):
    import requests
    url = "http://localhost:8888/Patient?id="+id

    payload = {}
    headers = {
      'Authorization': 'Basic cm9vdDpzZWNyZXQ='
    }

    response = requests.request("GET", url, headers=headers, data = payload)
    d = response.json()
    print(type(d))
    op = len(d['entry'])
    print(op)
    print('-----------------------------')
    dictpatientrecord = {}
    for j in range(0,op):
    	#------------------------Taking the Name-----------------------
    	try:
    		for i in d['entry'][j]['resource']['name']:
    			nam = i['given'][0]
    	except:
    		nam ='Name Unknow'

    	#--------------Taking the City[Address]--------------
    	try:
    		for i in d['entry'][j]['resource']['address']:
    			for e,r in i.items():
    				if e == 'city':
    					city = r
    	except:
    		city = 'Not given'
    	#--------------Taking the Date Of Birth--------------
    	for i,m in d['entry'][j]['resource'].items():
    		if i == "birthDate":
    			dob = m
    			break
    		else:
    			dob = "DOB Not Given"
    	#--------------Taking the Date Of gender--------------
    	for i,m in d['entry'][j]['resource'].items():
    		if i == "gender":
    			gnr=m
    			break
    		else:
    			gnr = "Not Given"

    	print('Name : ',nam)
    	print(id)
    	print(city)
    	print(dob)
    	print(gnr)
    # 	dictpatientrecord['name'] = nam
    # 	dictpatientrecord['id'] = id
    # 	dictpatientrecord['city'] = city
    # 	dictpatientrecord['dob'] = dob
    # 	dictpatientrecord['gnr'] = gnr
    #
    # print(dictpatientrecord)
    return render(request,'Patientrecord.html',{'key1':nam,'key2':id,'key3':gnr,'key4':city,'key5':dob})
