RANKFLOW - AUTO UPDATE

Dépôt GitHub configuré :
https://github.com/jojobougere-maker/rankflow

Ce patch ajoute :
- version centralisée dans src/core/version.py
- vérification GitHub Releases au démarrage
- téléchargement du Setup de la release
- lancement du Setup et fermeture de RankFlow
- workflow GitHub Actions pour construire un Setup lors d'un tag vX.Y.Z

IMPORTANT
1. Ta V1.0.0 stable reste la base de sauvegarde.
2. Copie ces fichiers dans une copie de ton projet.
3. Pour une future version, modifie APP_VERSION et MyAppVersion.
4. Crée un tag GitHub correspondant (ex. v1.1.0).
5. Le workflow construira le Setup et le publiera dans Releases.
6. L'auto-update cherchera la dernière release publique.

ATTENTION
Le dépôt GitHub actuel ne contient pas encore le projet complet RankFlow.
Il faut d'abord y pousser le projet source complet et le workflow avant que
l'auto-update puisse fonctionner pour les utilisateurs.
