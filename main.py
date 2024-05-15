import json
from functions import state_executed,sort_operations, output_format
def main():
    with open("operations.json", "r", encoding='utf-8') as file:
        data = json.load(file)
        items = state_executed(data)
        sort_items = sort_operations(items)

        for i in range(5):
            print(output_format(sort_items[i]))
            print()


if __name__ == "__main__":
    main()