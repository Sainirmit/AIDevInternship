def main():
    user_input = input("Enter your input here (eg: 2 + 2): ")
    result = math_operation(user_input)

    if result is not None:
        result_output(result)

def math_operation(user_input):
    try:
        result = eval(user_input)
        return result
    except Exception as e:
        print(f"error: {e}")
        return None

def result_output(result):
    print(f"result: {result}")

if __name__ == "__main__":
    main()
    

