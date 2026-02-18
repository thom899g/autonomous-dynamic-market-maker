class RiskManager:
    def __init__(self):
        self.risk_tolerance = None
        self.position_size_limits = {}

    def set_parameters(self, risk_tolerance=0.05, position_limits=None):
        """Sets the risk management parameters."""
        self.risk_tolerance = risk_tolerance
        if not position_limits:
            position_limits = {}
        self.position_size_limits = position_limits

    def is_safe(self, action):
        """Evaluates whether an action is within acceptable risk limits."""
        current_risk = self._calculate_current_risk()
        return (current_risk + self._action_risk(action)) <= self.risk_tolerance

    def _calculate_current_risk(self):
        """Returns the current risk level based on open positions."""
        # Simplified calculation; actual would be more complex
        return 0.03  # Example 3% current risk

    def _action_risk(self, action):
        """Estimates the risk of taking a specific action."""
        if action == 'increase_liquidity':
            return 0.02
        elif action == 'decrease_liquidity':
            return 0.01
        else:
            return 0.0