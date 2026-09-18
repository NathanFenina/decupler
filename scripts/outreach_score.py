#!/usr/bin/env python3
"""Classe les cibles de netlinking par score, à partir de content/outreach/cibles.json.

Le score n'est pas un DA déguisé. Un DA 76 injoignable vaut moins qu'un DA 15
qui dit oui la semaine prochaine : on pondère l'autorité par la probabilité
réelle d'obtenir le lien.

    python3 scripts/outreach_score.py [--json] [--offre barometre]
"""
import argparse, json, math, pathlib, sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
CIBLES = RACINE / "content" / "outreach" / "cibles.json"

# Poids max de chaque axe. Total 100.
AXES = {"pertinence": 40, "autorite": 25, "accessibilite": 20, "trafic": 15}


def note_autorite(da):
    """DA Ubersuggest (1-100) → 0-25, en log.

    Passer de 10 à 30 de DA change la vie ; passer de 70 à 90, beaucoup moins.
    Une échelle linéaire écraserait tout le bas du classement, qui est
    justement là où sont les liens qu'on peut décrocher sans budget.
    """
    da = max(int(da or 1), 1)
    return round(AXES["autorite"] * math.log10(da) / 2.0, 1)


def note_trafic(trafic):
    """Trafic organique estimé → 0-15, en log. None = inconnu, on ne devine pas."""
    if trafic is None:
        return 0.0
    t = max(int(trafic), 1)
    return round(min(AXES["trafic"], AXES["trafic"] * math.log10(t) / 4.0), 1)


def score(c):
    detail = {
        "pertinence": float(c.get("pertinence", 0)),
        "autorite": note_autorite(c.get("da")),
        "accessibilite": float(c.get("accessibilite", 0)),
        "trafic": note_trafic(c.get("trafic")),
    }
    return round(sum(detail.values()), 1), detail


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true", help="sortie machine")
    ap.add_argument("--offre", help="ne garder que les cibles de cette offre")
    ap.add_argument("--fichier", default=str(CIBLES))
    a = ap.parse_args()

    doc = json.loads(pathlib.Path(a.fichier).read_text(encoding="utf-8"))
    cibles = doc["cibles"]
    if a.offre:
        cibles = [c for c in cibles if c.get("offre") == a.offre]
    if not cibles:
        sys.exit("Aucune cible ne correspond.")

    classees = []
    for c in cibles:
        s, detail = score(c)
        classees.append({**c, "score": s, "detail": detail})
    classees.sort(key=lambda c: -c["score"])

    if a.json:
        print(json.dumps({"mesure": doc.get("mesure"), "cibles": classees},
                         ensure_ascii=False, indent=2))
        return

    print(f"\n  Cibles netlinking — mesures du {doc.get('mesure')}")
    print(f"  {doc.get('source_metriques')}\n")
    print(f"  {'#':>2}  {'Domaine':<26} {'Score':>5}  {'DA':>3} {'Trafic':>7}  "
          f"{'Coût':<22} Demande")
    print("  " + "-" * 108)
    for i, c in enumerate(classees, 1):
        tr = "?" if c.get("trafic") is None else f"{c['trafic']:,}".replace(",", " ")
        print(f"  {i:>2}  {c['domaine']:<26} {c['score']:>5}  {c['da']:>3} {tr:>7}  "
              f"{c['cout']:<22} {c['demande']}")

    print("\n  Détail du score (pertinence 40 · autorité 25 · accessibilité 20 · trafic 15)\n")
    for c in classees[:5]:
        d = c["detail"]
        print(f"  {c['domaine']:<26} pert {d['pertinence']:>4}  aut {d['autorite']:>4}  "
              f"acc {d['accessibilite']:>4}  traf {d['trafic']:>4}")

    ecartes = doc.get("ecartes", [])
    if ecartes:
        print(f"\n  Écartées ({len(ecartes)}) :")
        for e in ecartes:
            print(f"    · {e['domaine']} — {e['raison']}")
    print()


if __name__ == "__main__":
    main()
