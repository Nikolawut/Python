string = "Hi Mr. Rober53. How are you today? Today is 08.10.2019"
novi_string = ''.join(char for char in string if not char.isdigit())
print(novi_string) 