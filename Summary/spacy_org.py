# import spacy
# from spacy.language import Language
# from spacy.tokens import Span
#
# nlp = spacy.load("en_core_web_sm")
#
# @Language.component("expand_person_entities")
# def expand_person_entities(doc):
#     new_ents = []
#     for ent in doc.ents:
#         if ent.label_ == "ORG" and ent.start != 0:
#             prev_token = doc[ent.start - 1]
#             if prev_token.text in ("Medical Center", "Health Center", "University", "PLANO", "LLP", "Inc."):
#                 new_ent = Span(doc, ent.start - 1, ent.end, label=ent.label)
#                 new_ents.append(new_ent)
#         else:
#             new_ents.append(ent)
#     doc.ents = new_ents
#     return doc
#
# # Add the component after the named entity recognizer
# nlp.add_pipe("expand_person_entities", after="ner")
#
# doc = nlp("Dr. Alex Smith chaired first board meeting of Acme Corp Inc.")
# print([(ent.text, ent.label_) for ent in doc.ents])

# import spacy
# from spacy.matcher import Matcher
# nlp = spacy.load("en_core_web_sm")
# matcher = Matcher(nlp.vocab)
# nlp.add_pipe("merge_entities", after="ner")
#
# text2 = 'All is done by Emily Muller, the leaf MRI Center of Texas is burned by fire. we were not happy, so we cut relations by saying bye bye'
#
# doc = nlp(text2)
#
# pattern = [{"TEXT": "Center of"}, {"ENT_TYPE": "ORG"}]
#
# matcher = Matcher(nlp.vocab)
#
# matcher.add('person_only', [pattern])
# matches = matcher(doc)
# for match_id, start, end in matches:
#     print(doc[start:end])

import spacy
import re

nlp = spacy.load("en_core_web_sm")
content = "The United States of America (USA)  are commonly John Medical Center known as the United TEXAS HEALTH PLANO States Vijay Hospital (U.S. or US) Manu Health Center or America CERM Associates"
doc = nlp("The United States of America (USA)  are commonly John Medical Center known as the United TEXAS HEALTH PLANO States Vijay Hospital (U.S. or US) Manu Health Center or America. CERM Associates")
keywords = ['Hospital','Medical Center','Health Center','University','PLANO','Associates','Centers Of','Farmers Branch','CLINICS']
for i in keywords:
    if i in content:
       expression = r"\w+ "+i
       for match in re.finditer(expression,doc.text):
          start, end = match.span()
          span = doc.char_span(start, end)
        # This is a Span object or None if match doesn't map to valid token sequence
          if span is not None:
             print("Found match:", span.text)