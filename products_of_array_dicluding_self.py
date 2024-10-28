
def productExceptSelf( nums):
    accumelated_product=[]
    product_of_ahead=[]
    product_total = 1
    reverse_product=1
    result_list=[]
    for i in range(len(nums)):
        product_total*= nums[i]
        if (i !=0):
            reverse_product*=nums[-(i)]
        accumelated_product.append(product_total)
        product_of_ahead.append(reverse_product)
    print(accumelated_product,product_of_ahead)
    result_list.append(product_of_ahead.pop())
    accumelated_product.pop()
    for i in range(len(accumelated_product)):
        result_list.append(accumelated_product[i]*product_of_ahead[-(i+1)])
    print(result_list)

productExceptSelf([1,2,3,4])