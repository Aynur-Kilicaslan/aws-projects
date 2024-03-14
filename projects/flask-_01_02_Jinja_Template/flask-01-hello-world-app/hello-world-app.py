from flask import Flask 
app = Flask(__name__)

@app.route('/') #ana sayfayi olusturuyoruz. dekorasyon satirlari denir app route satirlarina
def head(): #ana sayfaya ne istiyorsak buraya ekliyoruz
     return 'Hello word Aynur'

@app.route('/secondpage') #ikinci sayfayi ekliyoruz
def second():
     return 'This is second World'
@app.route('/third')
def third():
     return 'This is third page'
@app.route('/fourth/<string:id>')
def fourth(id):
     return f'Id of this page is {id}'







if __name__ == '__main__':

     #app.run(debug=True) #hatalari görmek istiyorsak debug i  aktif birakacaz
      app.run(host= '0.0.0.0/0', port=80) #farkli port istersek onu yazabilirz port bildirmessen 500 portunda calisir