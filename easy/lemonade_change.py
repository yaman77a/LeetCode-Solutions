class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        # Dictionary to store the count of 5 and 10 dollar bills.
        box = {"five": 0, "ten": 0}
        
        # Iterate over each bill.
        for bill in bills:
            if bill == 5:
                # If the customer pays with 5 dollar, add it to the box.
                box["five"] += 1
            elif bill == 10:
                # If the customer pays with 10 dollar,we should give 5 dollar as change.
                if box["five"] != 0:
                    box["ten"] += 1 # Add 10 dollar bill to the box. 
                    box["five"] -= 1 # Give 1 of 5 dollar(s) for change.
                else:
                    return False # If no 5 dollar bill is available, return False
            else: # If the customer pays with 20 dollar
                # We prefer to give one 10 dollar and one 5 dollar as change
                if box["five"] >= 1 and box["ten"] >= 1:
                    box["five"] -= 1
                    box["ten"] -= 1
                # If no 10 dollar is available, give three 5 dollar bills as change
                elif box["five"] >= 3:
                    box["five"] -= 3
                else:
                    return False # If we cannot give the change, return False
        # If all customers received correct charge, return True
        return True
    