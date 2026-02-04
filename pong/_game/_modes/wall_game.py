# ======================================== IMPORTS ========================================
from ..._core import ctx, pm, pygame
from .._objects import Ball
from .._objects import Paddle

# ======================================== MODE DE JEU ========================================
class WallGame:
    """Mode de jeu : Wall Game"""
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

    def end(self, score: int = 0):
        """
        Fin de partie

        Args:
            score (int) : le score du joueur
        """
        print(f"La partie est terminée !\n Score : {score}")
        pm.stop()