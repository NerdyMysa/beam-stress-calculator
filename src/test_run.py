import sys
sys.path.append("src")

import beam

print("=== Beam Stress Calculator ===")
print("Entrez les valeurs demandées :\n")

force = float(input("Force appliquée (N) : "))
length = float(input("Longueur de la poutre (m) : "))
width = float(input("Largeur de la section (m) : "))
height = float(input("Hauteur de la section (m) : "))
yield_stress = float(input("Limite élastique du matériau (Pa) : "))

results = beam.analyze_beam(
    force=force,
    length=length,
    width=width,
    height=height,
    yield_stress=yield_stress
)

print("\n=== Résultats ===")
print(f"Moment max : {results['moment']} Nm")
print(f"Contrainte max : {results['stress']} Pa")
print(f"Facteur de sécurité : {results['safety_factor']}")
