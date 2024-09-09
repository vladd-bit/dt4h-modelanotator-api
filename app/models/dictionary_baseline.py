
import csv
from app.models.model_annotation import ModelAnnotation

class DictionaryLookupModel(ModelAnnotation):
    def __init__(self, csv_path):
        import csv
        import spacy
        from spacy.tokens import Doc, Span
        from spacy.language import Language

        self.nlp = spacy.load("en_core_web_sm")
        self.entities = self.load_entities_from_csv(csv_path)

        @Language.component("dictionary_entity_recognizer")
        def dictionary_entity_recognizer(doc):
            matches = []
            for token in doc:
                if token.lower_ in self.entities:
                    start = token.i
                    end = token.i + 1
                    matches.append(Span(doc, start, end, label=self.entities[token.lower_]))

            new_ents = []
            for span in matches:
                overlap = False
                for ent in doc.ents:
                    if span.start < ent.end and span.end > ent.start:
                        overlap = True
                        break
                if not overlap:
                    new_ents.append(span)

            doc.ents = list(doc.ents) + new_ents
            return doc

        self.nlp.add_pipe("dictionary_entity_recognizer", last=True)

    def load_entities_from_csv(self, file_path):
        entities = {}
        with open(file_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) >= 2:
                    entities[row[0].lower()] = row[1]  # Word: Label
        return entities

    def predict(self, text, app):
        doc = self.nlp(text)
        annotations = []
        for ent in doc.ents:
            annotation = {
                "concept_class": ent.label_,
                "start_offset": ent.start_char,
                "end_offset": ent.end_char,
                "concept_mention_string": ent.text,
                "concept_confidence": 0.95,  # Example value
                "ner_component_type": "dictionary lookup",
                "ner_component_version": self.nlp.meta["version"],
                "negation": "no",  # Simplified
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
            annotations.append(annotation)
        return self.serialize(text, annotations)
