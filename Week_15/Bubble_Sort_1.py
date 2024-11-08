def bubble_sort(list_n):
    
    n = len(list_n)

    for i in range(n): # Repeat n times 
        for j in range(0, n - 1 - i): # Comparing numbers 

            current_element = list_n[j]
            next_element = list_n[j + 1]

            print(f"-- Iteration {i}, {j}. Current element: {current_element}, Next element: {next_element}")

            if current_element > next_element:
                print("The current element is greater than next element. Switching elements...")
                list_n[j], list_n[j + 1] = list_n[j + 1], list_n[j] 
    
my_list = [100, 55, -15, -66, 10, 30, 23]
bubble_sort(my_list)
print(my_list)