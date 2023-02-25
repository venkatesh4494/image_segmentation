from flask import Flask,request,jsonify,render_template
from flask_cors import CORS,cross_origin
from predict import shapeAnalysis
from utils.decode import decodeimage



app = Flask(__name__)
CORS(app)



class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = shapeAnalysis(self.filename)



@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')
    


@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    image = request.json['image']
    decodeimage(image, clApp.filename)
    result = clApp.classifier.prediction()
    return jsonify(result)


#port = int(os.getenv("PORT"))
if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host='127.0.0.1', port=8000, debug=True)
