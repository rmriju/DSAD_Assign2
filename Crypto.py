# Knapsack Problem - Crypto currency

class CurrenyDetails:

    def __init__(self, curr, quant, price, profit):
        self.curr = curr
        self.quant = quant
        self.price = price
        self.profit = profit
        self.cost = profit / price
        self.sold = 0
        self.ratio = 0

    def __lt__(self, other):
        return self.cost < other.cost

# Greedy Approach
class FractionalKnapSack:
    """Time Complexity O(n log n)"""
    def getMaxProfit(self, crypto, maxsell):
        """function to get maximum value """
        totalProfit = 0
        for i in crypto:
            # todo check if enough coins can be purchased for example maxsell is .1 and min price is 1000
            if i.quant > 0:  # Handle div by zero
                i.sold = min(i.quant, maxsell / i.price)
                i.ratio = i.sold / i.quant
                maxsell = maxsell - (i.sold * i.price)
                totalProfit = totalProfit + i.sold * i.profit
            if maxsell <= 0:
                break

        crypto = sorted(crypto, key=lambda x: x.curr)

        print("Max Profit =", round(totalProfit, 2))
        print("Quantity selection Ratio:")
        for i in crypto:
            print(i.curr, ": ", round(i.ratio, 2))

        print("Total Quantity of each coin sold:")
        for i in crypto:
            print(i.curr, ": ", round(i.sold, 2))

    def readFileInput(self):
        file = open("inputPS1.txt")
        content = file.read()
        lines = content.split('\n')
        crypto = []
        curr_list = []
        try:
            for line in lines:
                currency_head = line.split(':')
                if len(currency_head) == 2:
                    # if currency_head[0] == 'Type of Crypto coins':
                    #     type_of_curr =  currency_head[1]
                    if currency_head[0].strip() == 'Maximum spend':
                        maxsell = float(currency_head[1])
                        if maxsell < 1:
                            print("Maximum spend should be more than 0 value !")
                            return
                else:
                    currency = line.split('/')
                    if len(currency) == 4:
                        qty = float(currency[1])
                        price = float(currency[2])
                        # Handle div by zero
                        if price < 1:
                            print("For all currency, price should be more than 0")
                            return
                        profit = float(currency[3])
                        curr = currency[0].strip()
                        if curr in curr_list:
                            print("Duplicates are not allowed in currency type !")
                            return
                        else:
                            crypto.append(CurrenyDetails(curr, qty, price, profit))
                            curr_list.append(curr)

        except ValueError:
            print("Program expect maximum spend, quantity, price, and profit as numeric")
            return
        # except :
        #     print("Invalid input !")
        #     return

        # sorting items by cost benefit
        cryptoSorted = sorted(crypto, key=lambda x: x.cost, reverse=True)
        self.getMaxProfit(cryptoSorted, maxsell)


# Driver Code
if __name__ == "__main__":
    greedy = FractionalKnapSack()
    greedy.readFileInput()
