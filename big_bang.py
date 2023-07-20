import json

def generate_array():
    result = []
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            result.append("BIG BANG")
        elif num % 3 == 0:
            result.append("BIG")
        elif num % 5 == 0:
            result.append("BANG")
        else:
            result.append(str(num))
    return result

if __name__ == "__main__":
    array_result = generate_array()
    with open('output.json', 'w') as output_file:
        json.dump(array_result, output_file)