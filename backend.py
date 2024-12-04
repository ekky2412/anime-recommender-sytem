from flask import Flask,jsonify,request
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/')
def hello_world():
    data = { 
            "Modules" : 15, 
            "Subject" : "Data Structures and Algorithms", 
        } 
    return jsonify(data)

@app.route('/rating', methods=['POST'])
def add_rating():
    data = request.form
    return data

@app.route('/recommendations/<id>')
def get_top_ten_recommendation(id):
    data = {
        "user_id" : id,
        "result": "ini hasilnya"
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run()