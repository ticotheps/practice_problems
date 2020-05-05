"""
CALCULATE THE PROFIT

You work for a manufacturer, and have been asked to calculate the total profit
made on the sales of product. You are given a dictionary containing the cost
price per unit (in dollars), the sell price per unit (in dollars), and the
starting inventory. Return the total profit made, rounded to the nearest dollar.
Assume all inventory has been sold.
        
Examples:
    - calculate_the_profit({
        "cost_price": 32.67,
        "sell_price": 45.00,
        "inventory": 1200,
    }) -> 14796
    
    - calculate_the_profit({
        "cost_price": 225.89,
        "sell_price": 550.00,
        "inventory": 100,
    }) -> 32411
    
    - calculate_the_profit({
        "cost_price": 2.77,
        "sell_price": 7.95,
        "inventory": 8500,
    }) -> 44030
    
Notes:
    - Profit = Total Sales - Total Cost
"""

"""
UNDERSTAND PHASE

Objective:
    - Write an algorithm that will take in a single Python dictionary and
        return a single integer, which will represent the number of dollars 
        made in profit after all the inventory has been sold.
        
Expected Inputs & Outputs:
    - Inputs:
        - Number: 1
        - Data Type: Python dictionary
        - Variable Name: 'sales_info'
    - Outputs:
        - Number: 1
        - Data Type: integer
        - Variable Name: 'total_profit'
        
Constraints:
    - Can the input contain negative values?
        - No, because anything but positive values in the input will denote a loss,
            not a gain.
    - Can the input contain floating point values?
        - Yes, they currently do.
    - Can the input be empty?
        - No.
"""

# PLAN PHASE + EXECUTION PHASE

def calculate_the_profit(sales_info):
    # Create a var that will store the total cost of the inventory
    total_cost = sales_info["cost_price"] * sales_info["inventory"]
    
    # Create a var that will store the total sales from the inventory
    total_sales = sales_info["sell_price"] * sales_info["inventory"]
    
    # Calculate the total profit from the given total sales and the total cost
    #   of inventory, rounded to the nearest dollar.
    profit = round(total_sales - total_cost)
    
    return profit

"""
REFLECT/REFACTOR PHASE

Asymptotic Analysis:
    - Time Complexity:
        - O(1) -> "constant"
    - Space Complexity:
        - O(1) -> "constant"
"""