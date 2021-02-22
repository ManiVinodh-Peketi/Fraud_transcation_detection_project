from flask import *

app = Flask(__name__)

import pickle
def pred(l):
    m2=open(r"ohno.plk","rb")
    m1=pickle.load(m2)
    result1=m1.predict([l])
    return result1[0]

    #print("pickle",result1)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/", methods=['POST','GET'])
def Predict():
    if len(request.form)>0 :
        cred = request.form['cred']
        merchant = request.form['merchant']
        amount = request.form['amount']
        pincode = request.form['pincode']
        lat = request.form['lat']
        longe = request.form['longe']
        dob = request.form['dob']
        trans = request.form['trans']
        city = request.form['city']
        job = request.form['job']
        mer_lat= request.form['mer_lat']
        mer_long= request.form['mer_long']
        gender= request.form['gender']
        category= request.form['category']
        dot=request.form['dot']
        #print(amount,cred,merchant,amount,pincode,lat,longe,dob,trans,city,251.09355,mer_lat,mer_long,gender,category)
       
        year=int(dob[0:4])
        mon=int(dob[5:7])
        day=int(dob[8:])
        year1=int(dot[0:4])
        mon1=int(dot[5:7])
        day1=int(dot[8:])
        #print(year,mon,day)
        
        a=pred([year,mon,day,int(cred),342.96,int(category),float(amount),int(gender),int(pincode),float(lat),float(longe),int(city),243.06,524287,float(mer_lat),float(mer_long),year1,mon1,day1])
        #print("sdhakjd",a)
        if a==0:
            data="Fraud"

        else:
            data="Genuine"
        return render_template("home1.html",data=data)
if __name__ == "__main__":
    app.run(debug=True)
