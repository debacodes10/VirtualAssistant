from flask import Flask, request, jsonify
import numpy as np
import pickle

model = pickle.load(open('D:\\Test Software\\VirtualAssistant\\.venv\\model.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def display():
    return jsonify("Hello world!")

@app.route('/intent', methods=['POST'])
def predict():
    text = request.form.get('text')
    inp_q = np.array([text])
    result = model.predict(inp_q)[0]
    return jsonify({'intent': str(result)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, ssl_context=('certificate.pem','key.pem'))
