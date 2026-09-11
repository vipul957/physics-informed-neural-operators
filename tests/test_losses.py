from physics_informed_neural_operators.losses import physics_loss
def test_loss(): assert physics_loss([0],[0],[0]) == 0
