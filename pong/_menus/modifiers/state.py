# ======================================== IMPORTS ========================================
from ..._core import pm

# ======================================== ETAT ========================================
class Modifiers(pm.states.State):
    """
    Modification des paramètres de la partie
    """
    def __init__(self):
        super().__init__('modifiers_menu')

        # modifiers
        self.modifiers_init = {
            "ball_radius": 20,
            "ball_celerity_min": 600,
            "ball_celerity_max": 2000,
            "ball_acceleration_duration": 120,
            "ball_trail": True,
            "paddle_size": 100,
            "paddle_celerity": 500,
            "player_1_side": "left",
        }
    
    def init(self):
        """Chargement de l'état"""

    def update(self):
        """Actualisation par frame"""