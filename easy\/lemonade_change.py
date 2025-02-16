class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        box = {"five": 0, "ten": 0}
        for bill in bills:
            if bill == 5:
                box["five"] += 1
            elif bill == 10:
                if box["five"] != 0:
                    box["ten"] += 1
                    box["five"] -= 1
                else:
                    return False
            else:
                if box["five"] >= 1 and box["ten"] >= 1:
                    box["five"] -= 1
                    box["ten"] -= 1
                elif box["five"] >= 3:
                    box["five"] -= 3
                else:
                    return False
        return True