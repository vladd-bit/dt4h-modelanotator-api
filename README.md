# Dictionary Lookup NER API

This is a Flask API that performs Named Entity Recognition (NER) using a dictionary-based approach. The model relies on a CSV file containing entities and their corresponding labels.

## Prerequisites

Before starting, make sure you have Docker and Docker Compose installed on your system.

* Docker
* Docker Compose
## Instructions to Start the Service

1. Clone the repository
First, clone the repository to your local machine:

```bash
git clone <repository-url>
cd <repository-directory>
```

2. Create the Entity CSV File
Make sure the english_entities.csv file exists in the root directory of the project. The file should follow this format:

```csv
word,label
heart attack,Condition
aspirin,Medication
fever,Symptom
diabetes,Condition
acetaminophen,Medication
This CSV file is used by the model to recognize entities in the text.
```

3. Build and Run the Docker Container
Build and run the service using Docker Compose:

```bash
docker-compose up --build
```
This will start the service on port 8000.

4. Verify the Service is Running
You can open your browser or run a curl request to http://localhost:8000 to ensure the service is up and running.

## Available Endpoints

1. /process_text - Process a Single Text
Method: POST

This endpoint processes a single text and applies NER using the dictionary model.

Example Request

```bash
curl -X POST "http://localhost:8000/process_text" \
-H "Content-Type: application/json" \
-d '{
  "text": "The patient was diagnosed with diabetes and prescribed aspirin."
}'
```
Example Response

```json
{
  "text": "The patient was diagnosed with diabetes and prescribed aspirin.",
  "patient_id": null,
  "annotations": [
    {
      "concept_class": "Condition",
      "start_offset": 30,
      "end_offset": 38,
      "concept_mention_string": "diabetes",
      "concept_confidence": 0.95,
      "ner_component_type": "dictionary lookup",
      "ner_component_version": "3.1.0",
      "negation": "no",
      "negation_confidence": 1.0,
      "qualifier_negation": "",
      "qualifier_temporal": "",
      "dt4h_concept_identifier": "",
      "nel_component_type": "",
      "nel_component_version": "",
      "controlled_vocabulary_namespace": "none",
      "controlled_vocabulary_version": "",
      "controlled_vocabulary_concept_identifier": "",
      "controlled_vocabulary_concept_official_term": "",
      "controlled_vocabulary_source": "original"
    },
    {
      "concept_class": "Medication",
      "start_offset": 56,
      "end_offset": 63,
      "concept_mention_string": "aspirin",
      "concept_confidence": 0.95,
      "ner_component_type": "dictionary lookup",
      "ner_component_version": "3.1.0",
      "negation": "no",
      "negation_confidence": 1.0,
      "qualifier_negation": "",
      "qualifier_temporal": "",
      "dt4h_concept_identifier": "",
      "nel_component_type": "",
      "nel_component_version": "",
      "controlled_vocabulary_namespace": "none",
      "controlled_vocabulary_version": "",
      "controlled_vocabulary_concept_identifier": "",
      "controlled_vocabulary_concept_official_term": "",
      "controlled_vocabulary_source": "original"
    }
  ]
}
```
2. /process_bulk - Process Multiple Texts
Method: POST

This endpoint processes multiple texts at once, applying NER using the dictionary model to each text.

Example Request

```bash
curl -X POST "http://localhost:8000/process_bulk" \
-H "Content-Type: application/json" \
-d '[
  {"text": "The patient was diagnosed with diabetes."},
  {"text": "The doctor prescribed acetaminophen."}
]'
```
Example Response

```json
[
  {
    "text": "The patient was diagnosed with diabetes.",
    "patient_id": null,
    "annotations": [
      {
        "concept_class": "Condition",
        "start_offset": 30,
        "end_offset": 38,
        "concept_mention_string": "diabetes",
        "concept_confidence": 0.95,
        "ner_component_type": "dictionary lookup",
        "ner_component_version": "3.1.0",
        "negation": "no",
        "negation_confidence": 1.0,
        "qualifier_negation": "",
        "qualifier_temporal": "",
        "dt4h_concept_identifier": "",
        "nel_component_type": "",
        "nel_component_version": "",
        "controlled_vocabulary_namespace": "none",
        "controlled_vocabulary_version": "",
        "controlled_vocabulary_concept_identifier": "",
        "controlled_vocabulary_concept_official_term": "",
        "controlled_vocabulary_source": "original"
      }
    ]
  },
  {
    "text": "The doctor prescribed acetaminophen.",
    "patient_id": null,
    "annotations": [
      {
        "concept_class": "Medication",
        "start_offset": 22,
        "end_offset": 35,
        "concept_mention_string": "acetaminophen",
        "concept_confidence": 0.95,
        "ner_component_type": "dictionary lookup",
        "ner_component_version": "3.1.0",
        "negation": "no",
        "negation_confidence": 1.0,
        "qualifier_negation": "",
        "qualifier_temporal": "",
        "dt4h_concept_identifier": "",
        "nel_component_type": "",
        "nel_component_version": "",
        "controlled_vocabulary_namespace": "none",
        "controlled_vocabulary_version": "",
        "controlled_vocabulary_concept_identifier": "",
        "controlled_vocabulary_concept_official_term": "",
        "controlled_vocabulary_source": "original"
      }
    ]
  }
]
```
## Environment Variables

You can configure the following environment variables in the Docker Compose file:

DICTIONARY_FILE: Path to the CSV file with dictionary entities (optional if using default ./english_entities.csv).
LANGUAGE: Language model to use (default: en).
Stopping the Service

## To stop the service, use:

```bash
docker-compose down
```
