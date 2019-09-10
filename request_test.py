import requests


def foo10():
    files = {"file": open("../Python-Demo/README.md", "rb")}
    response = requests.post("http://httpbin.org/post", files=files)
    print(response.status_code)
    print(response.text)


def foo13():
    session = requests.Session()
    response = session.get("http://httpbin.org/cookies/set/number/123456789")
    print(response.text)
    # "number": "123456789"

    response = session.get("http://httpbin.org/cookies")
    print(response.text)
    # "number": "123456789"


def foo14():
    response = requests.get("https://bitbucket.org/aronxu/merchant-guide-to-the-galaxy/src/master/")
    # CERTIFICATE_VERIFY_FAILED
    print(response.status_code)
    print(response.text)


# 取消验证
def foo15():
    from requests.packages import urllib3
    urllib3.disable_warnings()  # 消除 warning

    response = requests.get("https://bitbucket.org/", verify=False)
    # InsecureRequestWarning
    print(response.status_code)  # 200
    # print(response.text)


# 指定cert证书
def foo16():
    response = requests.get("https://www.12306.cn/", cert=("path"))
    print(response.status_code)  # 200


def foo21():
    from requests.auth import HTTPBasicAuth
    response = requests.get("https://bitbucket.org/aronxu/merchant-guide-to-the-galaxy/src/master/",
                            auth=HTTPBasicAuth("asd", "asd"))
    print(response.status_code)
    print(response.text)


# 也可以
def foo22():
    response = requests.get("http://www.goole.com/",
                            auth=("user", "password"))
    print(response.status_code)
    print(response.text)


def main():
    # payload = {'key1': 'value1', 'key2': 'value2'}
    # ret = requests.get("http://www.baidu.com", params=payload)
    # print(ret)
    # print(ret.url)
    # print(ret.text)
    foo14()
    foo21()


if __name__ == '__main__':
    main()
