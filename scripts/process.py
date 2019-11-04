import pandas as pd
from pathlib import Path

root = Path(__file__).parents[1]

annex_a = pd.read_csv(root / "archive/annex_a.csv")
annex_a["Formula"] = annex_a["Group"]
annex_a["Group"] = annex_a["Group"].apply(lambda x: x if x.startswith("Group") else None)
annex_a["Group"] = annex_a["Group"].ffill()
annex_a = annex_a[~annex_a["Substance"].isnull()]
annex_a["Substance"] = annex_a["Substance"].str.replace('(', ' ')
annex_a["Substance"] = annex_a["Substance"].str.replace(')', ' ')
annex_a.columns = ['Group', 'Substance', 'Ozone-Depleting Potential', '100-Year Global Warming Potential', 'Formula']
annex_a["Annex"] = "Annex A"
annex_a = annex_a[['Annex', 'Group', 'Formula', 'Substance', 'Ozone-Depleting Potential', '100-Year Global Warming Potential']]

annex_b = pd.read_csv(root / "archive/annex_b.csv")
annex_b["Formula"] = annex_b["Group"]
annex_b["Group"] = annex_b["Group"].apply(lambda x: x if x.startswith("Group") else None)
annex_b["Group"] = annex_b["Group"].ffill()
annex_b = annex_b[~annex_b["Substance"].isnull()]
annex_b["Formula"] = annex_b["Formula"].str.replace('*', '')
annex_b["Substance"] = annex_b["Substance"].str.replace('*', '')
annex_b["Substance"] = annex_b["Substance"].str.replace('\r', ' ')
annex_b["Substance"] = annex_b["Substance"].str.replace('(', ' ')
annex_b["Substance"] = annex_b["Substance"].str.replace(')', ' ')
annex_b["Annex"] = "Annex B"
annex_b = annex_b[['Annex', 'Group', "Formula", "Substance", "Ozone-Depleting Potential"]]
annex_b["100-Year Global Warming Potential"] = pd.np.NaN

annex_c_group_1 = pd.read_csv(root / "archive/annex_c_group_1.csv", na_values="–")
annex_c_group_1.columns = ['Group', 'Substance', 'Number of isomers', 'Ozone-Depleting Potential*', '100-Year Global Warming Potential']
annex_c_group_1["Formula"] = annex_c_group_1["Group"]
annex_c_group_1["Group"] = annex_c_group_1["Group"].apply(lambda x: x if x.startswith("Group") else None)
annex_c_group_1["Group"] = annex_c_group_1["Group"].ffill()
annex_c_group_1["Substance"] = annex_c_group_1["Substance"].str.replace('*', '')
annex_c_group_1 = annex_c_group_1[~annex_c_group_1["Substance"].isnull()]
annex_c_group_1["Number of isomers"] = annex_c_group_1["Number of isomers"].astype(pd.Int64Dtype())
annex_c_group_1.columns = ['Group', 'Substance', 'Number of isomers', 'Ozone-Depleting Potential', '100-Year Global Warming Potential', 'Formula']
annex_c_group_1["Annex"] = "Annex C"

annex_c_group_2_3 = pd.read_csv(root / "archive/annex_c_group_2_3.csv")
annex_c_group_2_3.columns = ['Group', 'Substance', 'Number of isomers', 'Ozone-Depleting Potential']
annex_c_group_2_3["Formula"] = annex_c_group_2_3["Group"]
annex_c_group_2_3["Group"] = annex_c_group_2_3["Group"].apply(lambda x: x if x.startswith("Group") else None)
annex_c_group_2_3["Group"] = annex_c_group_2_3["Group"].ffill()
annex_c_group_2_3 = annex_c_group_2_3[~annex_c_group_2_3["Ozone-Depleting Potential"].isnull()]
annex_c_group_2_3["Number of isomers"] = annex_c_group_2_3["Number of isomers"].astype(pd.Int64Dtype())
annex_c_group_2_3["Annex"] = "Annex C"

annex_f = pd.read_csv(root / "archive/annex_f.csv")
annex_f["Formula"] = annex_f["Group"]
annex_f["Group"] = annex_f["Group"].apply(lambda x: x if x.startswith("Group") else None)
annex_f["Group"] = annex_f["Group"].ffill()
annex_f = annex_f.dropna()
annex_f["Annex"] = "Annex F"

annex_e = pd.read_csv(root / "archive/annex_e.csv", skiprows=1)
annex_e.columns = ["Formula", "Substance", "Ozone-Depleting Potential"]
annex_e["Annex"] = "Annex E"
annex_e["Group"] = "Group I"

annex = pd.concat([annex_a, annex_b, annex_c_group_1, annex_c_group_2_3, annex_f, annex_e], sort=False)
annex["Substance"] = annex["Substance"].str.replace('(', ' ')
annex["Substance"] = annex["Substance"].str.replace(')', ' ')
annex["Substance"] = annex["Substance"].str.strip()
annex["100-Year Global Warming Potential"] = annex["100-Year Global Warming Potential"].str.replace(" ", "")

assert len(annex[annex["Annex"] == "Annex A"]) == 8
assert len(annex[annex["Annex"] == "Annex B"]) == 12
assert len(annex[(annex["Annex"] == "Annex C") & (annex["Group"] == "Group I")]) == 40
assert len(annex[(annex["Annex"] == "Annex C") & (annex["Group"] == "Group II")]) == 34
assert len(annex[(annex["Annex"] == "Annex C") & (annex["Group"] == "Group III")]) == 1
assert len(annex[annex["Annex"] == "Annex E"]) == 1
assert len(annex[annex["Annex"] == "Annex F"]) == 18

annex.to_csv(root / "montreal-protocol-controlled-substances.csv", index=False)

