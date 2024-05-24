import sys
from bert_score import score


def calcul_bert_score(candidate_text, reference_text, lang="fr", verbose=False):
    # Calculer les scores Bert
    P, R, F1 = score(candidate_text, reference_text, lang=lang, verbose=verbose)

    # Afficher les scores
    print(f"Précision moyenne: {P.mean():.4f}")
    print(f"Rappel moyen: {R.mean():.4f}")
    print(f"F1 moyen: {F1.mean():.4f}")

    return P, R, F1


def main():
    reference_path = sys.argv[1]
    candidate_path = sys.argv[2]

    # Charger les fichiers
    with open(reference_path, "r") as file:
        reference_text = file.readlines()

    with open(candidate_path, "r") as file:
        candidate_text = file.readlines()

    # Assurez-vous que les deux listes de textes ont la même longueur
    assert len(reference_text) == len(
        candidate_text
    ), "Les fichiers doivent contenir le même nombre de lignes."

    # Calculer les scores Bert
    P, R, F1 = calcul_bert_score(
        candidate_text, reference_text, lang="fr", verbose=True
    )


if __name__ == "__main__":
    main()
