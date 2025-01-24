from flask import Flask, request, jsonify
from mira_sdk import MiraClient

app = Flask(__name__)
client = MiraClient(config={"API_KEY": "YOUR_API_KEY"})

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    input_data = {
        "inputcode": data['inputcode'],
        "outputlanguage": data['outputlanguage']
    }
    flow_name = "@nitishgb/code-translator/1.0.0"
    result = client.flow.execute(flow_name, input_data)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
