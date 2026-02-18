class ExchangeAdapter:
    def __init__(self):
        self.adapters = {}

    def connect(self, exchange_name):
        """Connects to the specified exchange using its adapter."""
        if exchange_name not in self.adapters:
            raise ValueError(f"Exchange {exchange_name} is not supported.")
        
        # Initialize API connection
        adapter = self._get_adapter(exchange_name)
        adapter.connect()
        return adapter

    def _get_adapter(self, exchange_name):
        """Returns the appropriate adapter for the exchange."""
        if exchange_name == "binance":
            return BinanceAdapter()
        elif exchange_name == "coinbase":
            return CoinbaseAdapter()
        else:
            raise ValueError("Unsupported exchange")

class BinanceAdapter:
    def __init__(self):
        self.api_key = None
        self.secret_key = None

    def connect(self):
        """Establishes connection to Binance."""
        if not self.api_key or not self.secret_key:
            raise ValueError("API keys not set for Binance.")
        
        # Simulated connection logic
        print("Connected to Binance.")

class CoinbaseAdapter:
    def __init__(self):
        self.api_key = None
        self.token = None

    def connect(self):
        """Establishes connection to Coinbase."""
        if not self.api_key or not self.token:
            raise ValueError("API credentials not set for Coinbase.")
        
        # Simulated connection logic
        print("Connected to Coinbase.")