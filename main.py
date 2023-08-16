import requests


def main():
    r = requests.get("https://httpbin.org/")
    print(
        f"{r.status_code=}\n"
        f"{r.content=}"
    )
    with open ("page1.html", "wb") as file:
        file.write(r.content)

def post():
    data = {"key1": 1, "key2": 2}
    r = requests.post("https://httpbin.org/post", data=data)
    print(
        f"{r.status_code=}\n"
        f"{r.text=}\n"
        f"{r.headers=}\n"
        f"{r.content=}"
    )
    with open("response.txt", "w") as file:
        file.write(r.text)


if __name__ == '__main__':
    main()
    post()
