import os
import json
import requests
import tornado.web
import tornado.ioloop
import tornado.autoreload
import sys
import asyncio
#import psycopg2
import time



#import matplotlib.pyplot as plt

# On IBM Cloud Cloud Foundry, get the port number from the environment variable PORT



# When running this app on the local machine, default the port to 8000
port = int(os.getenv('PORT', 8000))
#port=8000
class landingPage(tornado.web.RequestHandler):
    def get(self):
        self.render("static/index.html")
        
class HomePage(tornado.web.RequestHandler):
    def get(self):
        self.render("static/index.html")

class Login(tornado.web.RequestHandler):
    def post(self):
        #base_url = 'https://api.eu-gb.apiconnect.appdomain.cloud/m1ganeshtcscom1543928228162-dev/sb/payments/custReg?acctId='
        # 100000001001 is the only working answer
        #headers = {'Content-Type': 'application/json'}
        print("inside login")
        username = str(self.get_body_argument("uname"))
        print(username)
        pwd = str(self.get_body_argument("pass"))
        print(pwd)
        #end_url= base_url+str(self.get_body_argument("accnt")) 
        #req = requests.get(end_url, headers=headers, auth=('701e3938-c7c7-4568-9e3b-d474bfb39700', ''), verify=False)
        #json_out = req.json()
        print("json")
        if username =="admin" and pwd == "adminpass":
            print("success")
            self.render("static/indexx.html")
        else:
            print("no")
            self.render("static/trial.html")
        #print(json_out)
        #self.render("static/genericresp.html",msg=json_out['CSRGRES']['CSRGRES']['MESSAGES'],cname=json_out['CSRGRES']['CSRGRES']['CUSTOMER_NAME'],cid=json_out['CSRGRES']['CSRGRES']['CUSTOMER_ID'],date=json_out['CSRGRES']['CSRGRES']['SYS_DATE'],time=json_out['CSRGRES']['CSRGRES']['SYS_TIME'],bloc="regreq")



class basicRevHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("static/reversal.html")

class predictScore(tornado.web.RequestHandler):
    def post(self):
        
        headers={'Content-Type': 'application/json', 'Control' : 'no-cache',}
        #json_data={'USERNAME':os.getenv("USERNAME"),'PASSWORD':os.getenv("PASSWORD"),}  
        #print(json_data)
        json_data={'username' : 'ibmuser', 'password' : 'tcs2044',}
        #print(json_data)
        response=requests.post('https://192.86.32.113:9888/auth/generateToken', headers=headers,json=json_data,verify=False)
        token=json.loads(response.text)['token']
        print(token)
        #token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImlibXVzZXIiLCJyb2xlIjoic3lzYWRtIiwidWlkIjoiNTAwMCIsImlhdCI6MTY4MDUwNDkzNywiZXhwIjoxNjgwNTUxNzM3fQ.inI8sfW2HHKRv8sklsFBYx6IxupKF5rpro1cm3IlSLfxknEZ-PjscDCwOEg1cF8M7LPDlNiFfMwccjBij8qBFlYEEOAQiq_Pc11UrCQJ0iHfpt1bXLyOYu1cieVgqe4NFqqA6HhuzJj-0qWbjdAREkw_C9pHYggreU656w0WqLpTABtq6cmIeuQ1xyTU1HvvfXHJzKe6FWRUQsm4s_EIgf4WzbhrGw34nr9gdaG_pcH30eqflA6wrYB5dVD4HKFzwEtYaVCO_xhZT_39PRRA9tFa8N5KNb2lR7Ttx-oEP3fpipMyrYgAeAeqoxtjQsTKXVOVw_iBu38h2qU1H2IkpA"
        #print(token)
        #base_url = 'http://192.86.32.113:5001/iml/v2/scoring/online/86118501-fc26-4a19-8451-e54b95acae8b'
        #base_url = 'https://gateway.aipc1.cp4i-b2e73aa4eddf9dc566faa4f42ccdd306-0001.us-east.containers.appdomain.cloud/sachinsorg/sandbox/payments/pymntRev?acctId='
        #base_url = 'https://api.eu-gb.apiconnect.appdomain.cloud/m1ganeshtcscom1543928228162-dev/sb/payments/pymntRev?acctId='
        # 100000001001 is the only working answer
        header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token}
        #end_url= base_url+str(self.get_body_argument("accnt"))+"&transId="+str(self.get_body_argument("trans"))+"&revAmt="+str(self.get_body_argument("debit_amt"))
        amt=str(self.get_body_argument("amt"))
        cnt_children=str(self.get_body_argument("cnt_children"))
        gender=str(self.get_body_argument("gender"))
        birth=str(self.get_body_argument("birth"))
        ext_source_1=str(self.get_body_argument("ext_source_1"))
        ext_source_2=str(self.get_body_argument("ext_source_2"))
        graduate=str(self.get_body_argument("graduate"))
        postgraduate=str(self.get_body_argument("postgraduate"))
        income_type=str(self.get_body_argument("income_type"))
        occupation_type=str(self.get_body_argument("occupation_type"))
        #end_url= base_url+amt+"&user1="+cnt_children+"&amount="+gender+"&merchantxstate="+birth+"&usexchip="+ext_source_1+"&errorsx="+ext_source_2+"&mcc="+graduate+"&merchantxcity="+postgraduate+"&card="+income_type+"&Occupational"+occupaton_type
        #req = requests.get(end_url, headers=headers, auth=('ibmuser', 'ibmuser'), verify=False)
        payload_scoring = [{"EXT_SOURCE_2":ext_source_1,"EXT_SOURCE_3":ext_source_2,"DAYS_BIRTH":birth,"CODE_GENDER_M":gender,"NAME_EDUCATION_TYPE_Higher education":graduate,"NAME_EDUCATION_TYPE_Secondary / secondary special":postgraduate,"NAME_INCOME_TYPE_Working":income_type,"AMT_CREDIT":amt,"CNT_CHILDREN":cnt_children,"OCCUPATION_TYPE_Sales staff":occupation_type}]
        print(payload_scoring)
        response_scoring = requests.post('http://192.86.32.113:5001/iml/v2/scoring/online/74d51bb6-8831-49a0-bd75-0d3e8d1e5058', json=payload_scoring, headers=header,verify=False)

        json_out = (json.loads(response_scoring.text))

        print("before")
        #print(json_out)
        jsonstruct=json_out
        #print(jsonstruct)
        
        jsonstruct=json.dumps(jsonstruct)
        json_load=json.loads(jsonstruct)
        #print(json_load["MODELOUT"]["MODELOUP"]["PROBABILITYX1X"])
        print("df")
        print(json_load)
        
        val1=json_load[0]['probability'][0]
        val2=json_load[0]['probability'][1]
        #print(val1)
        val1=round(val1,16)
        val2=round(val2,16)
        #print (val1)
        val1=round((val1*100),2)
        val2=round((val2*100),2)
        #print(val1)
        #val1=round(val1,2)
        #print(val1)
        #percent1=val1
        #percent2=int(json_load['MODELOUT']['MODELOUP']['PROBABILITYX0X'])*100
        print(val1,val2)
        labels= ['Risk for transfer', 'Non-risk for transfer']
        colors=['#14213d','#e63946']
        sizes= [val1,val2]

        if json_load[0]['prediction']:
            outVal = 'No'
        else:
            outVal = 'Yes'
        #plt.pie(sizes,labels=labels, colors=colors, startangle=90, autopct='%1.1f%%')
        #plt.axis('equal')
        #plt.show()

        x1x = round(json_load[0]['probability'][1],12)*100
        x0x = round(json_load[0]['probability'][0],12)*100


        self.render("static/result.html",label=labels,color=colors,size=sizes,x1x=x1x,xox=x0x,bloc="predictScore", jsonstruct=jsonstruct,
                    amt=amt,
                    cnt_children=cnt_children,
                    gender=gender,birth=birth,
                    ext_source_1=ext_source_1,
                    ext_source_2=ext_source_2,graduate=graduate,
                    postgraduate=postgraduate,
                    income_type=income_type,
                    occupation_type=occupation_type,
                    outVal=outVal)
        



if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", landingPage),
        (r"/predictScore", predictScore),

    ])
    print("commit")
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    app.listen(port)
    # TODO remove in prod
    #print("inside win")
    #server=HTTPServer(app)
    tornado.autoreload.start()
    print("I'm listening on port specified")
    print(port)
    tornado.ioloop.IOLoop.current().start()




