class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.__remaining_budget = allocated_budget

    # Getter for category name
    def get_category_name(self):
        return self.__category_name

    # Setter for category name
    def set_category_name(self, category_name):
        self.__category_name = category_name

    # Getter for allocated budget
    def get_allocated_budget(self):
        return self.__allocated_budget

    # Setter for allocated budget with validation
    def set_allocated_budget(self, allocated_budget):
        if allocated_budget >= 0:
            self.__allocated_budget = allocated_budget
            self.__remaining_budget = allocated_budget
        else:
            print("Budget must be a positive number.")

    # Method to add an expense
    def add_expense(self, amount):
        if amount > 0 and amount <= self.__remaining_budget:
            self.__remaining_budget -= amount
            print(f"Expense of {amount} added to {self.__category_name}. Remaining budget: {self.__remaining_budget}")
        else:
            print("Invalid expense amount or insufficient budget.")

# Example usage
food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
