---
tags:
  - écran
  - gaming
  - technologie
  - OLED
  - LCD
  - hardware
---
# La Science Cachée de la Netteté en Jeu

> **L'OLED.** Le mot est sur toutes les lèvres, synonyme du progrès ultime pour nos écrans. 

Mais si le marketing nous vend une supériorité absolue, la réalité physique et neuro-sensorielle est – comme souvent – plus complexe. Aujourd'hui, on plonge dans la technique pure pour comprendre pourquoi, pour un certain type de gaming, la solution la plus récente n'est pas encore la solution optimale.

---

## Anatomie des technologies d'affichage

### Le LCD : un modulateur de lumière sophistiqué

Commençons par la technologie dominante : le **LCD** (affichage à cristaux liquides). Son principe de base ? Celui d'un modulateur de lumière. 

Imaginez : une source lumineuse constante – le rétroéclairage – émet une lumière blanche. Cette lumière est ensuite filtrée par une matrice de cellules (les cristaux liquides) dont l'orientation, contrôlée électriquement, va bloquer plus ou moins la lumière pour chaque sous-pixel rouge, vert et bleu. Un peu comme la lumière du soleil qui change de couleur en traversant des vitraux.

De cette base découlent plusieurs technologies de dalles, chacune avec ses forces :

**Les dalles TN** (Twisted Nematic) → Des temps de réponse quasi-instantanés, au détriment des couleurs et des angles de vision. Destination : le jeu compétitif pur.

**Les dalles VA** (Vertical Alignment) → Des contrastes statiques très élevés grâce à un excellent blocage de la lumière. Parfaites pour le cinéma.

**Les dalles IPS** (In-Plane Switching) → Le couteau suisse technologique. Un compromis remarquable entre justesse des couleurs, angles de vision et une réactivité devenue excellente.

### L'OLED : le changement de paradigme

L'**OLED** (Diode Électroluminescente Organique) change radicalement la donne. 

C'est une technologie **auto-émissive**. Plus de filtre – chaque sous-pixel est une source de lumière indépendante. Pour du noir ? La diode est simplement mise hors tension. C'est ce qui permet un contraste *théoriquement infini* et un temps de réponse mesuré en microsecondes (pas d'inertie mécanique comme avec les cristaux liquides). 

Pensez à une mosaïque dont chaque pierre serait en fait une LED miniature.

#### Le piège du PWM

Mais. (Il y a toujours un "mais".)

Cette indépendance des pixels introduit une contrainte : la gestion de la luminosité. Réduire la tension d'une diode organique peut altérer sa colorimétrie et sa stabilité. La solution industrielle ? Le **PWM** (Pulse Width Modulation).

Pour varier l'intensité, l'écran allume et éteint les pixels des centaines – voire des milliers – de fois par seconde. La luminosité perçue dépend du ratio entre le temps "allumé" et le temps "éteint". 

Efficace, certes. Mais ce scintillement, même imperceptible, peut induire une fatigue visuelle chez les personnes sensibles, surtout à bas niveau de luminosité où la durée de la phase "éteinte" augmente.

---

## Le flou perçu : un problème neuro-visuel

On pourrait se dire que le débat est clos. Le temps de réponse quasi nul de l'OLED devrait, en théorie, éliminer toute forme de flou.

**C'est exact pour le ghosting** – l'artefact de traînée dû à la latence de transition des pixels. 

Cependant. Ça ne résout pas le *flou de mouvement perçu*, qui émane non pas des limites de l'écran, mais de l'interaction fondamentale entre le principe d'affichage moderne et notre propre système neuro-visuel.

Ce flou ? C'est l'enfant de deux phénomènes : le **sample-and-hold** et la **persistance rétinienne**.

### Le sample-and-hold : des images figées qui sautent

Le principe d'échantillonnage-blocage est inhérent à la quasi-totalité des écrans plats actuels. 

L'écran affiche une série d'images fixes discrètes. Durant l'intervalle de rafraîchissement (par exemple, 4,16 millisecondes pour un écran 240Hz), l'image d'un objet en mouvement est maintenue *parfaitement statique* avant d'être instantanément actualisée à sa nouvelle position.

Il n'y a pas de transition. Juste une succession de positions figées.

### La dissonance œil-écran

Or, pour suivre cet objet, notre œil engage un mouvement de poursuite oculaire lisse (*smooth pursuit*), anticipant une trajectoire continue. 

Il se crée alors une **dissonance fondamentale** : notre œil suit un chemin continu, tandis que la source lumineuse qu'il traque effectue des sauts discrets d'une position statique à une autre.

C'est là qu'intervient la persistance rétinienne. Votre perception du mouvement y est fondamentalement liée. Même si la source de lumière a disparu, votre système visuel retient une image pendant environ 40 millisecondes. 

Grâce à ça, nous percevons un film comme un mouvement continu (alors qu'il n'est qu'une succession rapide d'images fixes, comme un flip book). Ou que nous percevons les lumières comme constamment allumées, bien qu'elles alternent à un rythme effréné entre "on" et "off".

---

## La contre-attaque du LCD : technologies MBR

C'est pour combattre ce flou neuro-visuel que les technologies de réduction de flou de mouvement (**MBR** – Motion Blur Reduction) ont été créées, principalement sur LCD.

### L'ULMB (2015) : le pionnier imparfait

Son principe ? Imiter les anciens écrans à tube cathodique en insérant une image noire entre chaque image affichée. Ce "flash" noir réinitialise la persistance rétinienne et force notre cerveau à percevoir une image nette.

La technique était efficace mais... imparfaite :
- Luminosité drastiquement réduite
- Apparition de *crosstalk* (images fantômes dues à une synchronisation imparfaite)

### L'ULMB 2 (2023) : le game changer

En 2023, l'**ULMB 2** a changé la donne. 

Grâce à une gestion bien plus fine du rétroéclairage (Vertical Dependent Overdrive), il parvient à synchroniser l'impulsion lumineuse au moment *exact* où les pixels ont fini leur transition.

Résultat :
- Le crosstalk est quasi éliminé
- La luminosité effective est 2 à 3 fois supérieure à celle de l'ULMB 1
- On atteint une résolution de mouvement perçue (MPRT) qui, sur un moniteur 360Hz, peut dépasser l'équivalent d'un écran théorique à 1440Hz

Du lourd.

### G-Sync Pulsar (2024) : le Saint-Graal

Le conflit historique : impossible de combiner le rafraîchissement variable (VRR) du G-Sync – essentiel pour éliminer le tearing et le stutter – avec le strobing de l'ULMB, qui exigeait une fréquence fixe.

**Pulsar découple les deux.**

Vous obtenez la fluidité parfaite du VRR ET la netteté absolue du strobing. Simultanément. C'était impensable il y a deux ans.

---

## L'horizon de l'OLED : la prochaine révolution

Alors, le LCD a-t-il définitivement gagné la guerre de la netteté ? 

...Pas si vite.

Si ces technologies de pointe sont aujourd'hui l'apanage du LCD, il ne faut pas sous-estimer l'OLED. Cette technologie est déjà mature – elle nous accompagne dans nos poches depuis des années – et elle n'est pas étrangère à l'univers du gaming.

### Le BFI actuel : encore perfectible

Les moniteurs OLED actuels sont déjà compatibles G-Sync et possèdent leur propre version de réduction de flou : le **BFI** (Black Frame Insertion). Le principe est identique à l'ULMB.

Mais pour l'instant, il souffre des mêmes défauts que les premières générations de MBR :
- Baisse de luminosité significative
- Scintillement parfois perceptible  
- Impossibilité de l'utiliser avec le VRR

Bon. À quoi ressemblera l'étape d'après ?

### Le "BFI AI" : spéculation éclairée

Entrons dans la prospective. Imaginons une évolution que l'on pourrait nommer, pour le concept, le **"BFI AI"**.

L'idée fondamentale est d'une élégance redoutable : **découpler la fréquence de fonctionnement de la dalle de la fréquence du signal qu'elle reçoit**.

Imaginez : votre carte graphique produit 480 images par seconde (déjà phénoménal). Le moniteur, lui, opère en interne à **960Hz**.

Pour chaque image unique reçue du PC, l'électronique du moniteur exécute un cycle en deux temps à une vitesse folle :
1. Affichage de l'image du jeu (1/960s)
2. Affichage d'une image noire (1/960s)
3. Image de jeu suivante (1/960s)
4. Image noire (1/960s)

Le bénéfice ? Colossal.

Vous obtenez la clarté de mouvement d'un écran 960Hz, éliminant presque totalement le flou de persistance rétinienne, *sans demander à votre PC l'effort herculéen de calculer 960 images par seconde*.

De plus, à une telle fréquence de strobing, le scintillement devient totalement imperceptible pour l'œil humain. C'est le meilleur des deux mondes : fluidité extrême + netteté parfaite.

### Les défis techniques

Le défi est évidemment technique. Il faut :
- Des dalles capables d'un temps de réponse quasi nul (ce pour quoi l'OLED est le candidat idéal)
- Une électronique interne surpuissante

Et l'étape ultime de cette évolution ?

### Le "G-Sync Quantum" : l'équivalent Pulsar pour OLED

Ce serait une technologie qui fusionnerait la fluidité adaptative du G-Sync avec cette netteté absolue du BFI à très haute fréquence.

Appelons-le **"G-Sync Quantum"** (pour le concept).

Ce n'est plus une question de "si", mais de "quand".

---

## Choisir aujourd'hui, anticiper demain

Nous voilà donc face à un arbitrage technique clair.

### Le présent (2024-2025)

**OLED** → Roi pour l'expérience cinématographique, la profondeur des noirs dans un RPG, la justesse des couleurs en création.

**LCD + ULMB 2/Pulsar** → Avantage mesurable pour la performance brute et la clarté de mouvement absolue dans un jeu compétitif.

### Le futur (proche)

La prochaine révolution de la netteté sera très certainement menée par l'OLED, lorsque sa vitesse de pixel intrinsèque sera combinée à ces nouvelles techniques de traitement d'image.

Le choix vous appartient. Mais il doit se faire en toute connaissance du présent... et de l'avenir.

---

*Et vous ? Comment voyez-vous cette évolution ? Êtes-vous prêts à sacrifier les noirs profonds pour la netteté absolue, ou attendez-vous patiemment que l'OLED récupère son trône ?*
