import unittest
from calculate_the_profit import calculate_the_profit

class Test(unittest.TestCase):
    def test_calculate_the_profit(self):
        self.assertEqual(calculate_the_profit({
            "cost_price": 32.67,
            "sell_price": 45.00,
            "inventory": 1200,
        }), 14796)
        self.assertEqual(calculate_the_profit({
            "cost_price": 225.89,
            "sell_price": 550.00,
            "inventory": 100,
        }), 32411)
        self.assertEqual(calculate_the_profit({
            "cost_price": 2.77,
            "sell_price": 7.95,
            "inventory": 8500,
        }), 44030)
        
if __name__ == "__main__":
    unittest.main()