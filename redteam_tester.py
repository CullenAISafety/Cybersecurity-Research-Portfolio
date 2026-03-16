import json

with open("prompt_tests.json") as f:

    tests = json.load(f)

for test in tests:

    print("\nTesting prompt:")

    print(test["prompt"])

    print("Category:", test["category"])

    print("Result: manual evaluation required")
