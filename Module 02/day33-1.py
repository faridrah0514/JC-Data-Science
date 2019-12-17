from flask import Flask, render_template, jsonify, abort, send_from_directory

server = Flask(__name__)

karyawan=[
    {"id":1 , "nama": "Andi", "usia":20, "kota":"Jakarta"},
    {"id":2 , "nama": "Budi", "usia":22, "kota":"Bandung"},
    {"id":3 , "nama": "Caca", "usia":24, "kota":"Surabaya"}
]

@server.errorhandler(404)
def notFound(error):
    # return "<h1>sorry, not Found</h1>"
    return render_template("error.html")

@server.route('/karyawan/<int:kid>')
def emp(kid):
    print(kid)
    if (kid - 1) not in list(range(len(karyawan))) or (kid - 1) < 0:
        abort(404)
    else:
        return jsonify(karyawan[kid-1])

#render static file
@server.route('/file/<path:namaFile>')
def myFile(namaFile):
    return send_from_directory('storage', namaFile)

@server.route('/')
def home():
    return "<h1>Hallo Semuanya</h1>"

@server.route('/hello')
def hello():
    return "makan nasi"

@server.route('/index')
def index():
    return render_template('index.html')

@server.route('/data')
def data():
    nama = "Andi"
    kota = "Jakarta"
    return render_template("data.html", 
        data ={'name':nama, 'city': kota}
    )

if __name__ == '__main__':
    server.run(debug = True)


#FLASK
#bikin CV yang jalan di HTML, jalan di flask, route pertama yang di bikin
# - HOME
# - aboud
# - education
# - skills
# - experience

# digi dbwebscrape
# /table => HTML table data digidb
# /json => JSON data digimon