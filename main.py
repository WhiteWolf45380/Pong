
# ======================================== IMPORTS ========================================
import pygame_manager as pm
from .selection.state import GameModeState
from .modifiers_menu.state import GameModifiersState
from .game.state import GameState

# ======================================== CLASSE PRINCIPALE ========================================
class Main:
    """
    Jeu entier
    """
    def __init__(self):
        # Initialisation du framework modulable
        pm.init()

        # Instanciation des états
        self.selection = GameModeState().init()
        self.modifiers = GameModifiersSate().init()
        self.game = GameState().init()

    def update(self):
        """
        Actualisation de la frame
        """
        pm.screen.fill((80, 80, 90))

# ======================================== INSTANCE PRINCIPALE ========================================
if __name__ == '__main__':
    main = Main()
    pm.run(main.update)