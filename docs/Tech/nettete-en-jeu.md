---
tags:
  - écran
  - gaming
  - technologie
  - OLED
  - LCD
  - hardware
---

## Introduction

L'**OLED** est souvent présenté comme le nec plus ultra des technologies d'affichage. Pourtant, quand on creuse les **mécanismes neuro-visuels** et les **limites physiques**, la réalité est bien plus nuancée.

Pour le **gaming compétitif**, un écran récent n'est pas forcément le meilleur choix. Plongeons dans les détails techniques pour comprendre pourquoi.

---

## 1. Anatomie des Technologies d'Affichage

### 1.1 LCD : Le Modulateur de Lumière
Le **LCD (Liquid Crystal Display)** fonctionne comme un filtre sophistiqué :
- **Source lumineuse** (rétroéclairage) → **Polariseurs** → **Couche TFT** → **Cristaux liquides** → **Filtres couleurs (RGB)**.
- Les cristaux liquides s'orientent pour bloquer ou laisser passer la lumière → création des pixels.

#### Variantes de dalles LCD :
| Type  | Avantages                          | Inconvénients                     | Usage Typique               |
|-------|------------------------------------|-----------------------------------|-----------------------------|
| **TN** | Temps de réponse ultra-rapide (~1ms) | Couleurs médiocres, angles étroits | Gaming compétitif (FPS, etc.) |
| **VA** | Contraste élevé                   | Réactivité moyenne, ghosting      | Cinéma, jeux immersifs      |
| **IPS**| Équilibre couleurs/angles/vitesse | Légèrement plus lent que TN       | Usage polyvalent            |

>  *Analogie* : Comme la lumière du soleil traversant des vitraux, les cristaux liquides "teintent" la lumière blanche en couleurs.

---

### 1.2 OLED : L'Auto-Émission Révolutionnaire
L'**OLED (Organic Light-Emitting Diode)** change de paradigme :
- **Chaque sous-pixel est une source de lumière indépendante** → **noirs parfaits** (contraste "infini").
- **Temps de réponse quasi-instantané** (~0.1ms) → pas d'inertie mécanique.
- *Métaphore* : Une mosaïque où chaque pierre est une LED miniature.

#### Le défi du PWM (Pulse Width Modulation)
Pour gérer la luminosité, les OLED utilisent le **PWM** :
- Les pixels **clignotent** des centaines de fois par seconde.
- La luminosité perçue dépend du **ratio temps allumé/éteint**.
- **Problème** : Scintillement à basse luminosité → **fatigue visuelle** pour les personnes sensibles.

---

## 2. Le Flou Perçu : Un Problème Neuro-Visuel

### 2.1 Ghosting vs. Motion Blur
| Phénomène      | Cause                          | Solution Possible               |
|----------------|--------------------------------|----------------------------------|
| **Ghosting**   | Latence des pixels (LCD)       | Temps de réponse ultra-rapide   |
| **Motion Blur**| **Persistance rétinienne** + **Sample-and-Hold** | ULMB, BFI, Strobing |

#### Pourquoi le Motion Blur persiste-t-il même sur OLED ?
1. **Sample-and-Hold** :
   - Les écrans modernes affichent des images **statiques** pendant un intervalle fixe (ex. 4.16ms à 240Hz).
   - Notre œil suit le mouvement de manière **fluide** (*smooth pursuit*).
   - *Dissonance* : L’œil perçoit une trajectoire continue, mais la source lumineuse "saute" → **superposition mentale** = flou.

2. **Persistance rétinienne** :
   - Notre système visuel retient une image pendant ~40ms.
   - Même si un pixel s’éteint, nous continuons à "voir" sa trace → **renforcement du flou**.

>  **Conséquence** : Même un écran OLED à 0.1ms de temps de réponse **ne résout pas ce problème** – car il est *neurobiologique*.

---

## 3. La Contre-Attaque du LCD : ULMB et G-Sync Pulsar

### 3.1 ULMB (Ultra Low Motion Blur)
Inspiré des écrans **CRT**, l’ULMB insère une **image noire** entre chaque frame :
- **Effet** : Réinitialise la persistance rétinienne → **netteté accrue**.
- **Défauts** (ULMB 1) :
  - Baisse drastique de luminosité.
  - *Crosstalk* (images fantômes).

### 3.2 ULMB 2 (2023) : La Révolution
- **Vertical Dependent Overdrive** : Synchronise l’impulsion du rétroéclairage avec la transition des pixels.
  - **Résultats** :
    - *Crosstalk* quasi éliminé.
    - Luminosité **2-3x supérieure** à l’ULMB 1.
    - **MPRT** équivalent à un écran **1440Hz** sur un 360Hz.

### 3.3 G-Sync Pulsar (2024) : Le Saint-Graal
- **Problème historique** : Impossible de combiner **VRR** (rafraîchissement variable) et **strobing** (ULMB).
- **Solution** : Découplage des deux technologies → **fluidité parfaite + netteté absolue**.

> *Analogie* : Comme conduire une voiture avec une boîte automatique **et** un limiteur de vitesse intelligent qui s’adapte à chaque virage.

---

## 4. L’Horizon de l’OLED : La Prochaine Révolution

### 4.1 BFI (Black Frame Insertion) sur OLED
Les OLED actuels intègrent le **BFI**, mais avec des limites :
- Baisse de luminosité.
- Scintillement perceptible.
- Incompatibilité avec le VRR.

### 4.2 Le Futur : "BFI AI" et G-Sync Quantum
**Hypothèse** : Découpler la fréquence de la dalle de celle du signal entrant.
- **Exemple** :
  - La carte graphique envoie **480 images/seconde**.
  - Le moniteur OLED fonctionne en interne à **960Hz** :
    - Affiche **1 image de jeu → 1 image noire → image suivante → noire**, etc.
- **Avantages** :
  - Netteté équivalente à un **960Hz** sans exiger cette cadence à la source.
  - Scintillement imperceptible (fréquence trop élevée).
  - **Pas de surcharge GPU**.

#### Défis techniques :
- Dalles OLED **ultra-rapides** (temps de réponse ~0ms).
- Électronique de traitement **surpuissante**.

> **Quand ?** Une question de temps – l’OLED a déjà prouvé sa capacité à évoluer (ex. : smartphones).

---

## 5. Conclusion : Choisir Aujourd’hui, Anticiper Demain

| Technologie        | Avantages                          | Inconvénients                      |                               |
| ------------------ | ---------------------------------- | ---------------------------------- | ----------------------------- |
| **OLED (2024)**    | Noirs parfaits, couleurs sublimes  | Motion Blur persistant, BFI limité | Cinéma, RPG, création         |
| **LCD + Pulsar**   | Netteté absolue, MPRT ultra-faible | Contraste inférieur à l’OLED       | Gaming compétitif (FPS, etc.) |
| **OLED "Quantum"** | Netteté + couleurs + VRR           | Pas encore disponible              | Futur du gaming haut de gamme |

### Verdict :
- **Aujourd’hui** :
  - **OLED** → Immersion et qualité d’image (RPG, films, création).
  - **LCD (ULMB 2 / Pulsar)** → Performance pure (FPS, *esport*).
- **Demain** : L’OLED combinera **vitesse, netteté et fluidité** – quand la technologie sera mûre.

---
### Discussion
- Quel écran utilisez-vous pour le gaming ?
- Préférez-vous sacrifier la netteté pour des couleurs parfaites, ou l’inverse ?
- Pensez-vous que l’OLED finira par dominer aussi le gaming compétitif ?

