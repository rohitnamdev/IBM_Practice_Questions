def sol(products, product_price, product_sold, sold_price):
    count = 0
    products_dict = {}
    for i in range(len(products)):
        products_dict[products[i]] = product_price[i] 

    for i in range(len(product_sold)):
        if sold_price[i] != products_dict[product_sold[i]]:
            count +=1
    return count

products = ['eggs', 'milk', 'cheese']
productPrices = [2.89, 3.29, 5.79]
productSold = ['eggs', 'eggs', 'cheese', 'milk']
soldPrice = [2.89, 2.99, 5.90, 3.29]

# Count the number of pricing errors
result = sol(products, productPrices, productSold, soldPrice)

print(result)  # Output: 2