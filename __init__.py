from flask import Flask, request, jsonify
from flasgger import Swagger
from model_annotation import DictionaryLookupModel

app = Flask(__name__)
swagger = Swagger(app)

# Initialize the model
model = DictionaryLookupModel("path/to/your/english_entities.csv")

@app.route('/process_text', methods=['POST'])
def process_text():
    """
    Process text using NER Dictionary Lookup
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          id: text_input
          required:
            - text
            - patient_id
          properties:
            text:
              type: string
              description: The text to process
            patient_id:
              type: string
              description: The patient ID
    responses:
      200:
        description: Processed text with NER annotations
    """
    data = request.json
    text = data.get('text')
    patient_id = data.get('patient_id')
    
    if not text or not patient_id:
        return jsonify({"error": "Both 'text' and 'patient_id' are required"}), 400

    result = model.predict(text, patient_id)
    return jsonify(result)

@app.route('/process_bulk', methods=['POST'])
def process_bulk():
    """
    Process multiple texts using NER Dictionary Lookup
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          id: bulk_input
          type: array
          items:
            type: object
            required:
              - text
              - patient_id
            properties:
              text:
                type: string
                description: The text to process
              patient_id:
                type: string
                description: The patient ID
    responses:
      200:
        description: Processed texts with NER annotations
    """
    data = request.json
    
    if not isinstance(data, list):
        return jsonify({"error": "Input must be a list of objects"}), 400

    results = []
    for item in data:
        text = item.get('text')
        patient_id = item.get('patient_id')
        
        if not text or not patient_id:
            return jsonify({"error": "Each item must contain 'text' and 'patient_id'"}), 400
        
        result = model.predict(text, patient_id)
        results.append(result)

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)