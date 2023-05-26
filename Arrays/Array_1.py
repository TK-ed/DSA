# 1. Let us say your expense for every month are listed below,
# 	1. January -  2200
#  	2. February - 2350
#     3. March - 2600
#     4. April - 2130
#     5. May - 2190
#
# Create a list to store these monthly expenses and using that find out,
expenses = [2200, 2350, 2600, 2130, 2190]

# 1. In Feb, how many dollars you spent extra compare to January?
print(expenses[1] - expenses[0])

# 2. Find out your total expense in first quarter (first three months) of the year.
print(expenses[0] + expenses[1] + expenses[2])

# 3. Find out if you spent exactly 2000 dollars in any month
for i in expenses:
    if i == 2000:
        print('YES')
print('NO')

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
expenses.append(1980)
print(expenses)

# 5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list
expenses[3] = expenses[3]-200
print(expenses)
