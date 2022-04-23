'''
Given an array of integers where the ith integer represents the price of the 
stock on day i, return the largest possible profit from completing one 
transaction (i.e. buying 1 share and selling 1 share).
Examples: Given the following prices...

// Buy on day 1 and sell on day 5 for a profit of 5 - 1 = 4. 
prices = [1, 2, 3, 4, 5], return 4. 
// Buy on day 4 and sell on day 9 for a profit of 11 - 1 = 10. 
prices = [4, 5, 2, 1, 6, 10, 4, 9, 11], return 10. 
// Buying and selling the stock at any point would yield a negative profit. 
prices = [33, 18, 8, 2], return 0 

'''
profit=0

days=5

def sellbuy(price_list:list,days:int):
    for i in range(1,days):
    
        if price_list[i]<price_list[i-1]:
            profit+=price_list[i]-price_list[i-1]
        else:
            print("Loss")
    return profit

price_list=[1,2,3,4,5]
profit=sellbuy(price_list,len(price_list))
print(profit)