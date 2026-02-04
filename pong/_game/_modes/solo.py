# ======================================== IMPORTS ========================================
from ..._core import ctx, pm, pygame
from .._objects import Ball, Paddle

# ======================================== MODE DE JEU ========================================
class Solo:
    """Mode de jeu : Seul contre un IA"""
    def __init__(self, view: pm.panels.Panel): # type: ignore
        # Pannel de vue
        self.view = view

        # Balle
        self.ball = Ball(self.view, ctx.modifiers.ball_radius)

        # Raquette
        self.paddle = Paddle(self.view, Paddle.OFFSET, view.centery, up=pygame.K_z, down=pygame.K_s)
    
    # ======================================== ACTUALISATION ========================================
    def update(self):
        """Actualisation par frame"""
        pass
    
    def end(self, won: int = 0):
        """
        Fint de partie

        Args:
            won (int) : joueur gagnant (0 pour robot et 1 pour joueur)
        """
        print(f"La partie est terminée !\nVous avez {'gagné' if won == 1 else 'perdu'}")
        pm.stop()