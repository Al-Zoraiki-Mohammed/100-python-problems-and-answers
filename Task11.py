"""Task11"""

def read_data(n=0):
    data=[]
    names=[]
    scores=[]
    for i in range(n):
        name = input(f'Enter the name of studet number{i+1}:  ')
        score = float(input(f'Enter the score of studet number{i+1}:  '))
        names.append(name)
        scores.append(score)
        data.append([score,name])
    return data

def find_second_lowest(sorted_data):
    first= sorted_data[0][0]
    second = False
    last = sorted_data[0][0]
    for i,j in sorted_data:
        if i>first and not second:
            second = True 
            return(j)                 
        elif i ==last and second:
             return(j)
        elif i> first and second:
            break
                
        last = i


if __name__ == '__main__':
    no_of_students = int(input('Enter Number of Studets N: '))
    data = read_data(no_of_students)
    sorted_data = sorted(data)
    print(sorted_data)
    second_lowest = find_second_lowest(sorted_data)
    print(second_lowest)
