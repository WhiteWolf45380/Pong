# ======================================== IMPORTS ========================================
import pygame_manager as pm

# ======================================== WALL GAME ========================================
class WallGame:
    """Mode de jeu : Wall Game"""
    def __init__(self):
        pass

    def update(self):
        """Actualisation par frame"""

    def end(self, score: int = 0):
        """
        Fin de partie

        Args:
            score (int) : le score du joueur
        """
        print(f"La partie est terminée !\n Score : {score}")
        pm.stop()