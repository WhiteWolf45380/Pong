# ======================================== IMPORTS ========================================
from ..._core import ctx, pm, pygame
from .._objects import Ball, Paddle

# ======================================== MODE DE JEU ========================================
class Local:
    """Mode de jeu : 2 Joueurs"""
    def __init__(self, view: pm.panels.Panel): # type: ignore
        # Panel de vue
        self.view = view
        
        # Balle
        self.ball = Ball(self.view, ctx.modifiers.ball_radius)

        # raquettes
        self.paddle1 = Paddle(self.view, Paddle.OFFSET, view.centery, up=pygame.K_z, down=pygame.K_s)
        self.paddle2 = Paddle(self.view, self.surface_rect.width - Paddle.OFFSET, self.surface_rect.height / 2, up=pygame.K_UP, down=pygame.K_DOWN)

    # ======================================== ACTUALISATION ======================================== 
    def update(self):
        """Actualisation par frame"""

    def end(self, winner: int = 0):
        """
        Fint de partie

        Args:
            winner (int) : joueur gagnant (1 pour gauche et 2 pour droit)
        """
        print(f"La partie est terminée !\nLe gagnant est le joueur {winner}")
        pm.stop()