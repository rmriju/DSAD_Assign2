# Knapsack Problem - Crypto currency
fout = None  # global variable to handle file; avoiding additional libs import


class Currency:

    ################################################################
    # Constructor method to instantiate class variables
    ################################################################
    def __init__(self, curr, quant, price, profit):
        self.curr = curr
        self.quant = quant
        self.price = price
        self.profit = profit
        self.cost = profit / price
        self.sold = 0
        self.ratio = 0


# Greedy Approach
class FractionalKnapSack:
    """Time Complexity O(n log n)"""

    ######################################################################
    # Method will do whole calculation to identify list of coins, quantity
    # and ratio that satisfies the maxSell criteria to give more profit
    ######################################################################
    @staticmethod
    def getMaxProfit(crypto, maxSell):
        """function to get maximum value """
        totalProfit = 0
        for i in crypto:
            # todo check if enough coins can be purchased for example maxsell is .1 and min price is 1000
            if i.quant > 0:  # Handle div by zero
                i.sold = min(i.quant, maxSell / i.price)
                i.ratio = i.sold / i.quant
                maxSell = maxSell - (i.sold * i.price)
                totalProfit = totalProfit + i.sold * i.profit
            if maxSell <= 0:
                break

        crypto = sorted(crypto, key=lambda x: x.curr)
        print("Max Profit =", round(totalProfit, 2), file=fout)
        print("Quantity selection Ratio:", file=fout)
        for i in crypto:
            print(i.curr, ": ", round(i.ratio, 2), file=fout)

        print("Total Quantity of each coin sold:", file=fout)
        for i in crypto:
            print(i.curr, ": ", round(i.sold, 2), file=fout)

    ######################################################################
    # Read input file and consider all input file entry errors/warnings
    # process the file if all good.
    ######################################################################
    def processCurrencyInput(self):
        file = open("inputPS1.txt")
        content = file.read()
        lines = content.split('\n')
        crypto = []
        curr_list = []
        global fout

        # Recreate the output file; avoiding additional libs
        self.createOutputFile()
        try:
            for line in lines:
                currency_head = line.split(':')
                if len(currency_head) == 2:
                    if currency_head[0] == 'Type of Crypto coins':
                        type_of_curr = int(currency_head[1])
                    if currency_head[0].strip() == 'Maximum spend':
                        maxSell = float(currency_head[1])
                        if maxSell < 1:
                            print("Error: Maximum spend should be more than 0 value !")
                            return
                else:
                    currency = line.split('/')
                    if len(currency) == 4:
                        qty = float(currency[1])
                        price = float(currency[2])
                        # Handle div by zero
                        if price < 1:
                            print("Error: For all currency, price should be more than 0")
                            return
                        profit = float(currency[3])
                        if profit < 0:
                            print("Error: Profit can't be negative, please check your input file")
                            return
                        curr = currency[0].strip()
                        if curr in curr_list:
                            print("Error: Duplicates are not allowed in currency type !")
                            return
                        else:
                            crypto.append(Currency(curr, qty, price, profit))
                            curr_list.append(curr)

        except ValueError:
            print("Error: Program expect maximum spend, quantity, price, and profit as numeric")
            return
        except:
            print("Error: Invalid input !")
            return
        finally:
            no_of_curr = len(crypto)
            if no_of_curr <= 0:
                print("Warning: No currency entered, please check your input file")
                return
            if no_of_curr != type_of_curr:
                print("Warning: Type of currency do not match with list of currencies in the input file")
                # Give warning, but continue pgm execution for entered currency list

        # sorting items by cost benefit
        cryptoSorted = sorted(crypto, key=lambda x: x.cost, reverse=True)
        self.getMaxProfit(cryptoSorted, maxSell)

    ################################################################
    # Method will invalidate file content and reopen in append mode
    ################################################################
    @staticmethod
    def createOutputFile() -> object:
        global fout
        fout = open("outputPS1.txt", "w")
        fout.close()
        fout = open("outputPS1.txt", "a")


# Driver Code
if __name__ == "__main__":
    greedy = FractionalKnapSack()
    greedy.processCurrencyInput()
