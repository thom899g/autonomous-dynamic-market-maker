from exchange_interface import ExchangeAdapter
from rl_engine import RLEngine
from risk_management import RiskManager
from monitoring import Monitor

class AutonomousDynamicMarketMaker:
    def __init__(self):
        self.exchange = ExchangeAdapter()
        self.rl_engine = RLEngine()
        self.risk_manager = RiskManager()
        self.monitor = Monitor()

    def initialize(self):
        """Initializes the ADMM with exchange connections and risk parameters."""
        self.exchange.connect("binance")
        self.exchange.connect("coinbase")
        self.risk_manager.set_parameters(risk_tolerance=0.05)
        self.monitor.start_tracking()

    def run_strategy(self, market_pair):
        """Executes the market making strategy using RL and risk management."""
        while True:
            state = self.exchange.get_market_state(market_pair)
            action = self.rl_engine.decide_action(state)
            if self.risk_manager.is_safe(action):
                self.exchange.execute_order(market_pair, action)
                self.monitor.log_activity("Executed order based on RL decision.")
            else:
                self.monitor.log_activity("Risk check failed; aborted order execution.")

if __name__ == "__main__":
    admm = AutonomousDynamicMarketMaker()
    admm.initialize()
    admm.run_strategy("BTC/USDT")