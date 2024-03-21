# Import Flask modules
from flask import Flask, render_template, request
# Create an object named app
app = Flask(__name__)


# create a function named "lcm" which calculates a least common multiple values of two numbers. 
def lcm(num1,num2):
    common_multiplications = [] 
    for i in range(max(num1, num2),num1*num2+1):
        if i%num1==0 and i%num2==0:
           common_multiplications.append(i) 
    return min(common_multiplications) #girilen rakamlarin en kucuk ortak katini hesapliyor bu fonksiyonda ekok



# Create a function named `index` which uses template file named `index.html` 
# send two numbers as template variable to the app.py and assign route of no path ('/') 
@app.route("/")
def index():
    return render_template("index.html", methods=["GET"]) 
#GET ve POST metotlarin
#GET ile bir sayfa site uygulama CAGIRMA isleme karsimiza getiriyoruz
#post ise cagirdigimiz uygulamaya degerler girip tekrar gonderdigimiz ve sonuc bekledigimiz durum post metodu
#yukardaki get ile uygulamayi cagirdik index.html deki postlu uygulama



# calculate sum of them using "lcm" function, then sent the result to the 
# "result.hmtl" file and assign route of path ('/calc'). 
# When the user comes directly "/calc" path, "Since this is a GET request, LCM has not been calculated" string returns to them with "result.html" file
@app.route("/calc", methods=["GET", "POST"])
def calculate():
    if request.method == "POST": #post metodu uyguladiysak sonuclari alabilmek icin request uyguluyor
        num1 = request.form.get("number1")
        num2 = request.form.get("number2") #girdigim degerlerden sonra karsima asagidaki html sayfasi donecek
        return render_template("result.html", result1 = num1, result2 = num2, lcm = lcm(int(num1),int(num2)), developer_name = 'aynur') #bundan sonra result.html sayfasi gelir
    else: # eger sayilari girmezsek posta bu uyari geliyor yine result.htmldeki else blogu
        return render_template("result.html", developer_name = "aynur")

# Add a statement to run the Flask application which can be debugged.
if __name__== "__main__":
    # app.run(debug=True)
     app.run(host='0.0.0.0', port=80)