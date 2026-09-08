def print_lis(list,idx=0):
    if idx == len(list):
        return
    print(list[idx])
    print_lis(list,idx+1)
print_lis(["Delhi", "Solapur", "Noida", "Mumbai", "Pune"])