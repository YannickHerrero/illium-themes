# Winarchy theme packs

Collection locale indépendante du dépôt Winarchy. Chaque dossier est un pack installable : palette Winarchy, wallpapers, attribution et provenance des sources.

| Pack | Mode | Wallpapers | Preview |
|---|---|---:|---|
| `pissarro` | Clair — crème, olive, lavande | 5 peintures | Capture Omarchy amont |
| `akane` | Sombre — bleu-violet, vermillon, or | 8 paysages | Illustration de preview amont |
| `dracula` | Sombre — palette Dracula | 3 images | `screenshot.png` amont renommé |
| `snow` | Clair — monochrome blanc, noir et gris | 3 images | Capture Omarchy amont |
| `synthwave84` | Sombre — violet, magenta et cyan néon | 1 image | Capture liée dans le README amont |
| `mechanoonna` | Sombre — ambre et crème, Mecha no Onna V2 | 3 images | Capture Omarchy amont |
| `aamis` | Sombre : noir profond, texte crème et ambre chaud, accent rouge unique | 1 image | Capture Omarchy amont (`assets/homescreen.png` renommée) |
| `sakura` | Sombre : prune quasi noir, or, rose et corail | 6 images | Capture Omarchy amont |
| `frost` | Sombre : bleu nuit et bleu-gris givré désaturés | 3 images | Capture Omarchy amont |
| `futurism` | Sombre : bleu nuit, texte bleu glacier, accent rose néon et cyan électrique | 4 images | Capture Omarchy amont |

## Installer

Avec une version de Winarchy prenant en charge `theme install` :

```powershell
winarchyctl theme install "C:\Downloads\pissarro"
winarchyctl theme set pissarro
```

Sur cette machine, les sources sont aussi accessibles depuis Windows :

```powershell
winarchyctl theme install "\\wsl.localhost\Debian\home\yannick\dev\winarchy-themes\pissarro"
```

Les dix packs sont déjà installés sous `%USERPROFILE%\.config\winarchy\themes`. Une nouvelle installation du même nom est volontairement refusée pour préserver les réglages existants.

L'installation conserve le format compatible avec WezTerm : `themes/pissarro.toml` pour les couleurs et `themes/pissarro/wallpapers/` pour les images. Aucune modification de l'intégration WezTerm n'est nécessaire.

## Utiliser

- **Alt+Shift+Space → Theme** ou **Ctrl+Alt+Shift+Space** : ouvrir le carrousel, taper pour filtrer, parcourir avec les flèches et valider avec Entrée.
- **Alt+Shift+Space → Wallpaper** : choisir une image ou le fond uni.
- **Ctrl+Alt+Shift+W** : image suivante du thème actif.
- `winarchyctl wallpaper next`, `wallpaper set "nom du fichier.jpg"`, `wallpaper clear` : commandes équivalentes.

Les choix sont mémorisés par thème dans `wallpapers.json`. Les images remplissent chaque écran, avec recadrage centré et proportions conservées ; la préférence de wallpaper Windows n'est pas modifiée.

Chaque pack inclut désormais `preview.png`, récupéré sans recompression depuis la même révision amont que sa palette ou depuis l'image référencée par son README figé. Pour Synthwave84, la capture est une pièce jointe GitHub externe : sa propre somme SHA-256 fixe son contenu, sans prétendre qu'elle est un fichier du commit Git. Le nouveau sélecteur utilise ce fichier plutôt qu'un wallpaper de secours. Ces visuels représentent les thèmes Omarchy, pas les applications Winarchy. Le renommage Dracula et les sommes SHA-256 sont documentés dans les `SOURCES.md`.

Pour compléter une installation existante, copier seulement le `preview.png` manquant dans `themes/<identifiant>/`, sans réinstaller le pack ni écraser ses fichiers. Les previews ont été ajoutées à l'installation locale sans changer le thème actif ni les choix de wallpaper ; `PREVIEW-SOURCES.md` accompagne ces ajouts pour ne pas écraser les documents existants. Akane, Snow, Synthwave84, Futurism, Frost et Sakura restent réservés à l'adaptation locale personnelle, faute de licence explicite.

## Créer un autre pack

Copier l'un des dossiers, lui donner un identifiant en minuscules (`a-z`, `0-9`, `-`, `_`), puis modifier `theme.toml` et remplacer les fichiers de `wallpapers/`. Mettre à jour l'attribution et les licences : ne pas conserver celles d'un thème sans rapport. Installer le nouveau dossier avec `winarchyctl theme install`.

Pour ajouter simplement une image à un thème déjà installé, la copier dans son dossier `themes/<identifiant>/wallpapers/` : la découverte est automatique. JPEG et PNG sont pris en charge, avec au plus 64 images par thème, 32 MiB et 64 megapixels par image, dimension maximale 16384, 512 MiB d'images par pack.

## Skill de conversion Omarchy → Winarchy

Le skill versionné dans [`skills/omarchy-to-winarchy`](skills/omarchy-to-winarchy/SKILL.md) guide la conversion d'une URL GitHub ou d'un dossier local : révision source figée, palette adaptée, previews et wallpapers préservés, attribution, validation et installation sans toucher au dépôt Winarchy. Le guide [assets](skills/omarchy-to-winarchy/references/assets.md) couvre aussi les captures liées dans les README, les pièces jointes GitHub, la conversion des formats et l'ajout sans écrasement à un pack existant.

Il est installé sur cette machine via un lien dans `~/.agents/skills/omarchy-to-winarchy`. Dans pi, exécuter `/reload` pour le découvrir dans une session déjà ouverte, puis :

```text
/skill:omarchy-to-winarchy https://github.com/bjarneo/omarchy-snow-theme
```

On peut aussi demander naturellement « ajoute ce thème Omarchy à Winarchy » avec l'URL. Le skill ne change pas le thème actif sans demande explicite et ne publie pas les ressources tierces.

Son helper Python 3.11+ génère uniquement la palette depuis des fichiers locaux ; le skill conserve une étape de revue visuelle et de vérification des droits. Tests :

```bash
python3 -B -m unittest discover -s skills/omarchy-to-winarchy/tests -v
```

Pour installer le skill sur une autre machine, copier son dossier dans `~/.agents/skills/` ou y créer un lien vers cette collection, puis adapter les chemins locaux indiqués dans le workflow.

## Sources et droits

Chaque pack contient un `SOURCES.md` avec la révision amont exacte et les sommes SHA-256 des fichiers sources. Les palettes terminal préservent les 16 couleurs du fichier Alacritty d'origine ou, pour les thèmes Quattro comme Snow, celles définies par `colors.toml` et le template Alacritty officiel d'Omarchy. Les images sont conservées sans recompression.

Pissarro, Dracula, Mechanoonna et Aamis conservent leurs licences MIT amont ; pour Aamis, le wallpaper hébergé sur Wallhaven reste une illustration tierce non couverte par cette licence ; les droits propres aux illustrations restent à respecter. **Akane, Snow, Synthwave84, Futurism, Frost et Sakura ne fournissent pas de licence explicite dans les révisions consultées : ces packs restent des adaptations locales personnelles, et leur redistribution publique doit être clarifiée avec les auteurs et les ayants droit des images.** Il n'y a pas de licence globale qui réattribuerait les droits des ressources tierces.
