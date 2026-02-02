# ======================================== IMPORTS ========================================
import pygame_manager as pm

# ======================================== ETAT ========================================
class ModesMenuState(pm.states.State):
    """
    Modification du mode de jeu
    """
    def __init__(self):
        super().__init__('modes_menu')

    def init(self):
        """Chargement de l'état"""

    def update(self):
        """Actualisation par frame"""