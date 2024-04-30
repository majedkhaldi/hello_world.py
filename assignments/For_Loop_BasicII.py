# 1. Biggie Size 

def positive_big(li):
    for x in range(len(li)):
        if li[x] > 0:
            li[x] = "big"
    return li
print (positive_big([-9, 2, 15, -25, 8]))


# 2. Count Positives 
def count_positives (list):
    count = 0
    for x in range (len(list)):
        if list[x]>0:
            count = count + 1
    list[len(list) - 1] = count
    return list
print(count_positives([1,5,7,-96,8,2,-7,2,-6,-4,-8,4,5,3]))
    

# 3. Sum Total

def sum_total(list):
    sum = 0
    for i in range (len(list)):
        sum = sum + list[i]
    return sum
print (sum_total([2,8,9,6,-7]))

# 4. avrage 

def avg_(list):
    sum = 0
    avg = 0
    for r in range (len(list)):
        sum = sum + list[r]
    avg = sum / len(list)
    return avg
print(avg_([2,8,9,7,3,6,2,1,4,5]))

# 5. Length 
def length(list):
    counter = 0
    for i in list:
        counter += 1
    return counter
print (length([1,2,3,4,5,2,1]))


# 6. minimum
def mini(li):
    min = 0
    if len(li) == 0:
        return False
    else:
        for i in range(len(li)):
            if li[i] < min:
                min = li[i]
        return min
print (mini([2,5,9,1,-92,4,8]))


# 7. Maximum
def maxi(li):
    max = 0
    if len(li) == 0:
        return False
    else:
        for i in range(len(li)):
            if li[i] > max:
                max = li[i]
        return max
print (maxi([2,5,9,1,-92,4,8]))


# 8. Ultimate Analysis
def ulti_ana(li):
    list = li
    def sum_total(list):
        sum = 0
        for i in range (len(list)):
            sum = sum + list[i]
        return sum


    def avg_(list):
        sum = 0
        avg = 0
        for r in range (len(list)):
            sum = sum + list[r]
        avg = sum / len(list)
        return avg

    def length(list):
        counter = 0
        for i in list:
            counter += 1
        return counter

    def mini(list):
        min = 0
        if len(list) == 0:
            return False
        else:
            for i in range(len(list)):
                if list[i] < min:
                    min = list[i]
            return min

    def maxi(list):
        max = 0
        if len(list) == 0:
            return False
        else:
            for i in range(len(list)):
                if list[i] > max:
                    max = list[i]
            return max
    ulti_dictionary = {'sumTotal': sum_total(list), 'average': avg_(list), 'minimum': mini(list), 'maximum': maxi(list), 'length': length(list)}
    return ulti_dictionary

print (ulti_ana([2,5,9,8,7,4,-6,2,5]))

# 9. Reverse List
def reverse(list):
    n = len(list)-1
    i = 0
    while i < n:
        temp = list[i]
        list[i] = list[n]
        list[n] = temp
        n = n-1
        i = i+1
    return list
print (reverse([1,5,8,9,4]))