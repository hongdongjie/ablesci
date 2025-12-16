from ablesci import ablesci

Cookie = "ablesci-serial=6e517b5928cf30d49be347a9f7754187; _identity-frontend=cc2cde3ea2f6f28b644cf66d03799fe1035062562bf47087dbfe28104382a1e5a%3A2%3A%7Bi%3A0%3Bs%3A18%3A%22_identity-frontend%22%3Bi%3A1%3Bs%3A52%3A%22%5B1061893%2C%220uKz-Cw2fsqwVPuqfUoFRIH_aEv66vzT%22%2C2592000%5D%22%3B%7D; Hm_lvt_21ea3daf4a17e94a98a483d3d810f41a=1762394424,1762908724,1764030752; advanced-frontend=4696gqn7v6m5215adb4knu8dr5; _csrf=35cfd53fc90c94caee5391acdad1b0c410941d4cadb08c8213b3868ebb90784ca%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%229tIULiXR_E3237vu2VjitU5Tddfh0o-W%22%3B%7D; security_session_verify=5c31613ef9714d7479f527296e2e7266" # 替换自己在浏览器中的Cookie

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": f"{Cookie}",
    "DNT": "1",
    "Referer": "https://www.ablesci.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}

def main():
    ablesci(headers=headers)

if __name__ == "__main__":
    main()
