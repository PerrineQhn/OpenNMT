# Structure de la commande : python3 meteor_score.py data/valid.fr data/valid.pred

import os
import subprocess
import sys

# Chemin vers le fichier JAR de METEOR
METEOR_JAR = "src/meteor-1.5/meteor-1.5.jar"


# Fonction pour appeler METEOR et calculer le score
def calculate_meteor_score(reference_file: str, candidate_file: str) -> str:
    """
    Calcule le score METEOR entre un fichier de référence et un fichier de prédiction.

    Parameters:
    reference_file (str): Chemin du fichier de référence.
    candidate_file (str): Chemin du fichier de prédiction.

    Returns:
    meteor_score (str): Score METEOR.
    """
    command = [
        "java",
        "-jar",
        METEOR_JAR,
        candidate_file,
        reference_file,
        "-l",
        "fr",
        "-norm",
    ]
    print(f"Executing command: {' '.join(command)}")

    result = subprocess.run(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )

    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        return None

    # Extraire le score METEOR de la sortie
    output_lines = result.stdout.strip().split("\n")
    meteor_score = output_lines[-1]

    return meteor_score


def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <reference_file_path> <candidate_file_path>")
        sys.exit(1)

    reference_path = sys.argv[1]
    candidate_path = sys.argv[2]

    # Calculer et afficher le score METEOR
    meteor_score = calculate_meteor_score(reference_path, candidate_path)

    if meteor_score is not None:
        print(f"METEOR Score: {meteor_score}")
    else:
        print("Failed to calculate METEOR score")


if __name__ == "__main__":
    main()
