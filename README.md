# OpenNMT

Projet pour le cours de Traduction Automatique et Assistée

## Paramètres Entrainement pour les deux runs

- **train_steps** : 10000
- **test_steps** : 5000

## Score BLEU

```python
python3 src/compute-bleu.py target prediction
```

### Exercice 3

**target** : fichier contenant les phrases cibles

- data/clean/Europarl_en_fr_clean/Europarl_test_500.tok.true.clean.fr
- data/clean/Emea_en_fr_clean/Emea_test_500.tok.true.clean.fr

**prediction** : fichier contenant les phrases prédites

#### Run 1

- data/clean/run1_model/src_europarl_prediction_10000.txt
- data/clean/run1_model/src_emea_prediction_10000.txt

#### Run 2

- data/clean/run2_model/src_europarl_prediction_10000.txt
- data/clean/run2_model/src_emea_prediction_10000.txt

### Exercice 4

**target** : fichier contenant les phrases cibles

- data/clean/lemmatised/lemme_Europarl_test_500.tok.true.clean.en
- data/clean/lemmatised/lemme_Emea_test_500.tok.true.clean.en

**prediction** : fichier contenant les phrases prédites

#### Run 1

- data/clean/run1_model_lemma/src_europarl_prediction_10000.txt
- data/clean/run1_model_lemma/src_emea_prediction_10000.txt

#### Run 2

- data/clean/run2_model_lemma/src_europarl_prediction_10000.txt
- data/clean/run2_model_lemma/src_emea_prediction_10000.txt

## Exemple

```python
python3 src/compute-bleu.py data/clean/Europarl_en_fr_clean/Europarl_test_500.tok.true.clean.en data/clean/run1_model/src_europarl_prediction_10000.txt
```
