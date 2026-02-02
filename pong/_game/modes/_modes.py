# ======================================== 1 PLAYER ========================================
class OnePlayer:
    """Mode de jeu : 1 Player"""
    def __init__(self):
        pass
    
    def update(self):
        """Actualisation par frame"""
    
    def end(self, won: int = 0):
        """
        Fint de partie

        Args:
            won (int) : joueur gagnant (0 pour robot et 1 pour joueur)
        """
        print(f"La partie est terminée !\nVous avez {'gagné' if won == 1 else 'perdu'}")

# ======================================== 2 PLAYERS ========================================
class TwoPlayers:
    """Mode de jeu : 2 Players"""
    def __init__(self):
        pass

    def update(self):
        """Actualisation par frame"""

    def end(self, winner: int = 0):
        """
        Fint de partie

        Args:
            winner (int) : joueur gagnant (1 pour gauche et 2 pour droit)
        """
        print(f"La partie est terminée !\nLe gagnant est le joueur {winner}")