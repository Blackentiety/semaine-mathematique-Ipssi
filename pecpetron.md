## Analyse des résultats

### 1. Succès : Cas AND et OR
Pour les fonctions **AND** et **OR**, le perceptron (qu'il soit "from scratch" ou via Scikit-Learn) parvient à trouver une droite qui sépare parfaitement les 0 des 1. 
- Les points sont dits **linéairement séparables**.
- La frontière de décision laisse d'un côté le point (1,1) pour le AND, ou isole le point (0,0) pour le OR.

### 2. Échec : Le cas XOR
Le graphique du **XOR** montre l'impuissance du perceptron simple :
- Les points "1" (0,1 et 1,0) sont situés en diagonale.
- Il est **mathématiquement impossible** de tracer une seule ligne droite qui sépare les points rouges des points bleus.
- **Observation :** Le perceptron finit par choisir une ligne qui laisse 2 points sur 4 du mauvais côté, ou qui n'en sépare qu'un seul. La perte (loss) ne tombe jamais à zéro.

### 3. Comparaison avec Scikit-Learn
L'implémentation de `sklearn.linear_model.Perceptron` confirme nos résultats :
- Sur **AND/OR**, les poids sont quasi identiques à notre version manuelle.
- Sur **XOR**, Scikit-Learn échoue également.
- **Conclusion technique :** Pour résoudre le XOR, il faudrait passer à un **Perceptron Multicouche (MLP)** avec au moins une couche cachée, permettant de créer des frontières non-linéaires.
