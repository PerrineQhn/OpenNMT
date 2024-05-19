# OpenNMT

Projet pour le cours de Traduction Automatique et Assistée

## Paramètres Entrainement pour les deux runs

- **train_steps** : 10000
- **test_steps** : 5000


## Constuction des vocabulaires

```python
onmt_build_vocab -config fichier.yaml -n_sample -1
```

Voici les différents fichiers `.yaml` utilisés pour la construction des vocabulaires :

`data/clean/run1.yaml` ;
`data/clean/run2.yaml`

`data/clean/run1_lemma.yaml` ;
`data/clean/run2_lemma.yaml`

Exemple :

```python
onmt_build_vocab -config data/clean/run1.yaml -n_sample -1
```

## Entrainement

```python
onmt_train -config fichier.yaml
````

`fichier.yaml` : fichier de configuration pour l'entrainement

- Voici les différents fichiers `.yaml` utilisés pour l'entrainement :

  - `data/clean/run1.yaml`
  - `data/clean/run2.yaml`

  - `data/clean/run1_lemma.yaml`
  - `data/clean/run2_lemma.yaml`

Exemple :

```python
onmt_train -config data/clean/run1.yaml
```

## Prédiction

```python
ontm_translate -model fichier.pt -src fichier_soucrce -output fichier_prediction -verbose
```

`fichier.pt` : modèle entrainé
`fichier_source` : fichier d'entrée contenant les phrases à traduire
`fichier_prediction` : fichier de sortie contenant les phrases traduites

- Voici les différents fichiers `.pt` utilisés pour la prédiction :

  - `data/clean/run1_model/model_step_10000.pt`
  - `data/clean/run2_model/model_step_10000.pt`

  - `data/clean/run1_model_lemma/model_step_10000.pt` 
  - `data/clean/run2_model_lemma/model_step_10000.pt`

- Voici les différents fichiers `.src` utilisés pour la prédiction :

  - `data/clean/Europarl_en_fr_clean/Europarl_test_500.tok.true.clean.en`
  - `data/clean/Emea_en_fr_clean/Emea_test_500.tok.true.clean.en`

  - `data/clean/lemmatised/lemme_Europarl_test_500.tok.true.clean.en`
  - `data/clean/lemmatised/lemme_Emea_test_500.tok.true.clean.en`

Exemple :

```python
onmt_translate -model data/clean/run1_model/model_step_10000.pt -src data/clean/Europarl_en_fr_clean/Europarl_test_500.tok.true.clean.en -output data/clean/run1_model/src_europarl_prediction_10000.txt -verbose
```


## Score BLEU

Le script `compute-bleu.py`provient du dépot suivant : [https://github.com/ymoslem/MT-Evaluation](https://github.com/ymoslem/MT-Evaluation)

```python
python3 src/compute-bleu.py target prediction
```

### Exercice 3

**target** : fichier contenant les phrases cibles

- `data/clean/Europarl_en_fr_clean/Europarl_test_500.tok.true.clean.fr`
- `data/clean/Emea_en_fr_clean/Emea_test_500.tok.true.clean.fr`

**prediction** : fichier contenant les phrases prédites

#### Run 1

- `data/clean/run1_model/src_europarl_prediction_10000.txt`
- `data/clean/run1_model/src_emea_prediction_10000.txt`

#### Run 2

- `data/clean/run2_model/src_europarl_prediction_10000.txt`
- `data/clean/run2_model/src_emea_prediction_10000.txt`

### Exercice 4

**target** : fichier contenant les phrases cibles

- `data/clean/lemmatised/lemme_Europarl_test_500.tok.true.clean.en`
- `data/clean/lemmatised/lemme_Emea_test_500.tok.true.clean.en`

**prediction** : fichier contenant les phrases prédites

#### Run 1

- `data/clean/run1_model_lemma/src_europarl_prediction_10000.txt`
- `data/clean/run1_model_lemma/src_emea_prediction_10000.txt`

#### Run 2

- `data/clean/run2_model_lemma/src_europarl_prediction_10000.txt`
- `data/clean/run2_model_lemma/src_emea_prediction_10000.txt`

## Exemple

```python
python3 src/compute-bleu.py data/clean/Europarl_en_fr_clean/Europarl_test_500.tok.true.clean.en data/clean/run1_model/src_europarl_prediction_10000.txt
```
