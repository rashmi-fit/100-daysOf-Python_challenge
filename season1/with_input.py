def compute_avg_output(numbers):
    try:
        count=len(numbers)
        total=0
        for num in numbers:
            total+=num
        avg=total/count
        return avg
    except Exception as e:
        print("Something went wrong! Please check your input", e)

'''function with input and and return'''