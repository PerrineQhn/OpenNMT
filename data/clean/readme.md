# La composition des modèles

run1_model : 
- train : 100K (Europarl)
- dev (référence) : 3,75K (Europarl)
- test (prédiction) : 500 (Europarl) & 500 (EMEA)

run2_model : 
- train : 100K (Europarl) + 10K (EMEA)
- dev (référence) : 3,75K (Europarl)
- test (prédiction) : 500 (Europarl) & 500 (EMEA)

run1_model_lemma : 
- train : 100K (Europarl lemmatisés)
- dev (référence) : 3,75K (Europarl lemmatisés)
- test (prédiction) : 500 (Europarl lemmatisés) & 500 (EMEA lemmatisés)

run2_model_lemma : 
- train : 100K (Europarl lemmatisés) + 10K (EMEA lemmatisés)
- dev (référence) : 3,75K (Europarl lemmatisés)
- test (prédiction) : 500 (Europarl lemmatisés) & 500 (EMEA lemmatisés)