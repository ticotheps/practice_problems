if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    lst = list(arr)
    highest_score = max(lst)
    sorted_lst = sorted(lst)    
    runner_up = 0
    
    for i in range((len(sorted_lst)-1), -1, -1):
        if sorted_lst[i] != highest_score:
            runner_up = sorted_lst[i]
            break

    print(runner_up)