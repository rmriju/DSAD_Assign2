# Python3 program to solve fractional
# Knapsack Problem

class CurrenyDetails:
    """Item Value DataClass"""

    def __init__(self, curr, quant, price, profit, ind):
        self.cost = profit // price
        self.ratio = 0
        self.curr = curr
        self.quant = quant
        self.price = price
        self.profit = profit
        self.ind = ind
        self.sold = 0

    def __lt__(self, other):
        return self.cost < other.cost


# Greedy Approach

class FractionalKnapSack:
    """Time Complexity O(n log n)"""

    @staticmethod
    def getMaxProfit(curr, quant, price, profit, maxsell):
        """function to get maximum value """
        iCurrency = []
        for i in range(len(curr)):
            iCurrency.append(CurrenyDetails(curr[i], quant[i], price[i], profit[i], i))

        TotalProfit = 0
        for i in iCurrency:
            # todo check if enough coins can be purchased for example maxsell is .1 and min price is 1000
            i.sold = min(i.quant, maxsell / i.price)
            i.ratio = i.sold / i.quant
            maxsell = maxsell - (i.sold * i.price)
            TotalProfit = TotalProfit + i.sold * i.profit
            if maxsell <= 0:
                break
        print("Profit =", TotalProfit)
        return iCurrency


# Driver Code
if __name__ == "__main__":
    # curr = ['c9', 'c2', 'c3', 'c4', 'c5', 'c6']
    # quant = [1, 2, 3, 4, 5, 6]
    # price = [60, 40, 10, 10, 400, 500]
    # profit = [5, 2, 3, 4, 5, 6]
    # maxsell = 50

    curr = ['c1', 'c2', 'c3', 'c4', 'c5', 'c6']
    quant = [6, 8, 1, 2, 2, 2]
    price = [50, 60, 400, 100, 15, 200]
    profit = [45, 50, 90, 70, 4, 24]
    maxsell = 1000

    # sorting items by cost benifit
    for i in range(len(curr)):
        # to do validations check if quant is zero , price is zero
        # to do handle profit is zero
        # to do check if maxsell is zero
        # to do should we check for duplicates
        j = i + 1
        while j < len(curr):
            if (profit[i] / price[i]) < (profit[j] / price[j]):
                temp = curr[j]
                curr[j] = curr[i]
                curr[i] = temp
                temp = quant[j]
                quant[j] = quant[i]
                quant[i] = temp
                temp = price[j]
                price[j] = price[i]
                price[i] = temp
                temp = profit[j]
                profit[j] = profit[i]
                profit[i] = temp
            j = j + 1

    # Function call
    maxProfit = FractionalKnapSack.getMaxProfit(curr, quant, price, profit, maxsell)
    for i in maxProfit:
        print("Currency:", i.curr)
        print("Ratio:", i.ratio)
    for i in maxProfit:
        print("Currency:", i.curr)
        print("Sold:", i.sold)
    #    print("Maximum value in Knapsack =", maxValue)



