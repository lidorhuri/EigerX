def priceCheck(products, productPrices, productSold, soldPrice):
    errCount=0
    dictionary_products ={}
    for i in range (len(products)):
        dictionary_products[products[i]] = i
    
     # identify prices and check       
    for i in range (len(productSold)):
        realprice = productPrices[dictionary_products[productSold[i]]]
        priceSoldCheck = soldPrice[i]
        if realprice != priceSoldCheck:
            errCount+=1
            
    
    return errCount


products = ['rice', 'sugar', 'wheat', 'cheese']
productPrices = [16.89, 56.92, 20.89, 345.99]
productSold = ['rice', 'cheese']
soldPrice = [18.99, 400.89]
print(priceCheck(products, productPrices, productSold, soldPrice))