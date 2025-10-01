import os
import pandas as pd

# Fichier d'entrée
file_path = r"C:\Users\chaym\Desktop\NasaProject\data\raw\TESS.csv"

# Dossier de sortie
output_dir = r"C:\Users\chaym\Desktop\NasaProject\data\processed"
output_path = os.path.join(output_dir, "TESS_filtered.csv")
os.makedirs(output_dir, exist_ok=True)

# Colonnes à garder
columns_to_keep = [
    "toi", "tid", "tfopwg_disp",
    "pl_orbper", "pl_orbpererr1", "pl_orbpererr2",
    "pl_trandurh", "pl_trandurherr1", "pl_trandurherr2",
    "pl_trandep", "pl_trandeperr1", "pl_trandeperr2",
    "pl_rade", "pl_radeerr1", "pl_radeerr2",
    "pl_insol", "pl_insolerr1", "pl_insolerr2",
    "pl_eqt", "pl_eqterr1", "pl_eqterr2",
    "st_tmag", "st_tmagerr1", "st_tmagerr2",
    "st_teff", "st_tefferr1", "st_tefferr2",
    "st_logg", "st_loggerr1", "st_loggerr2",
    "st_rad", "st_raderr1", "st_raderr2"
]

# Charger le CSV en ignorant les commentaires
df = pd.read_csv(file_path, sep=",", comment="#", on_bad_lines="skip")

# Vérifier les colonnes disponibles
available_cols = [col for col in columns_to_keep if col in df.columns]
missing_cols = [col for col in columns_to_keep if col not in df.columns]

print("✅ Colonnes conservées :", available_cols)
print("⚠️ Colonnes manquantes :", missing_cols)

# Garder seulement les colonnes valides
df_selected = df[available_cols]

# Sauvegarde
df_selected.to_csv(output_path, index=False)
print(f"✅ Fichier filtré sauvegardé dans : {output_path}")
