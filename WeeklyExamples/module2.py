import module1

print("This is the main script.")

# Calling the helper function from module1
module1.helper_function()

# Calling the main function from module1
module1.main()

print("--------------------")
print(f"Module2's name is: {__name__}")
print(f"Module1's name is: {module1.__name__}")