no_of_test_cases=int(input())
min_cost_list=[]
for i in range(0,no_of_test_cases):
    cost_of_green_baloon, cost_of_purple_baloon=map(int,input().split())
    no_of_users=int(input())
    cost=0
    list1=[]
    list1.clear()
    count_right=0
    count_left=0
    for j in range(0,no_of_users):
        first, second=map(int,input().split())
        list1.append(first)
        list1.append(second)

    
    for l in range(0,len(list1)):
        if l%2==0:
            if list1[l]==1:
                count_left+=1
            else:
                count_left+=0
        else:
            if list1[l]==1:
                count_right+=1
            else:
                count_right+=0
    
    if count_right>count_left:
        cost+=count_right*min(cost_of_green_baloon,cost_of_purple_baloon)
        cost+=count_left*max(cost_of_green_baloon,cost_of_purple_baloon)
    elif count_right<count_left:
        cost+=count_right*max(cost_of_green_baloon,cost_of_purple_baloon)
        cost+=count_left*min(cost_of_green_baloon,cost_of_purple_baloon)
    else:
        cost+=count_right*min(cost_of_green_baloon,cost_of_purple_baloon)
        cost+=count_left*max(cost_of_green_baloon,cost_of_purple_baloon)

   
    min_cost_list.append(cost)
for k in range(0,len(min_cost_list)):
    print(min_cost_list[k])