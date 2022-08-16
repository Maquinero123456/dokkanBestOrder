import requests
import json

class characterSearch:
    def __init__(self):
        self.url = "https://dokkan.fyi/characters/"


    def buscarPersonaje(self, id : int):

        try:
            url = self.url+str(id)
        except TypeError:
            print("Id debe ser tipo int")

        querystring = {"":""}

        headers = {
            "cookie": "_ga=GA1.1.571519870.1660659359; XSRF-TOKEN=eyJpdiI6IlFRdDJHL0tsbzBpMDQxcWhLRU96dkE9PSIsInZhbHVlIjoiNktSSDdzSXZ4UmJOM21KbGZXZllaZXFZQTFKZEJQRHNXQXhFamxiaHp3eS9HQnJoaTAvVVhZUmI2T2lnNk1mR3hQSjRoRHR6UjdwVnVkS0NjNnhNWkJhNVBCRVVhUnoyUm9lNGFpcUdEWVFIQmxoTldnQisyTm9BeVplSmhtL1YiLCJtYWMiOiJmN2EyMzdkZmJjNzQ1YmU1M2M2NDZhMWM2NzY2ODljZDA3Mjk4NzJmMGUyZDI2Y2JmZGVkYTY5N2Q1NzVhMTgxIiwidGFnIjoiIn0%3D; dokkanfyi_session=eyJpdiI6Ikl6bFN2L2pLUWhFMFFzR3RXSzZWcWc9PSIsInZhbHVlIjoiY1Z5SFlraDJnME9rNDE5bHJRV3V6bjhBOWM4U3hZQU1zU1RPRlJTRUt0VVgvQ3F6dWZqMnIzRDk4RzJGeE9yZktycXlYWG9TZXRzVFlJNHZJcFlyV1hqY0E2SFpwNDJ6amF6WllhUlNTNVhVc2hGNkFUb05LRGJqdC9IZ2J1TGEiLCJtYWMiOiI0M2RkOTU5YWQ4OGIwMzhkN2ExY2ZkNTM0ZDNmZGNhYjMxYjQ5MTQzYjZjNTk3NDhkODQzZDEzMGM1ZWU1ODFhIiwidGFnIjoiIn0%3D; _ga_CW9XGRYJ3X=GS1.1.1660659359.1.1.1660659750.0; _iub_cs-77725586=%7B%22timestamp%22%3A%222022-08-16T14%3A16%3A05.754Z%22%2C%22version%22%3A%221.40.1%22%2C%22purposes%22%3A%7B%221%22%3Atrue%2C%224%22%3Atrue%2C%225%22%3Atrue%7D%2C%22id%22%3A77725586%7D; euconsent-v2=CPdzKwAPdzKwAB7EUBENCcCsAP_AAH_AAAAAI8Nd_X__bW9j-_5_aft0eY1P9_r37uQzDhfNk-8F3L_W_LwX52E7NF36pq4KmR4Eu1LBIQNlHMHUDUmwaokVrzHsak2cpyNKJ7JEknMZOydYGF9Pn1tjuYKY7_5_9_bx2D-t_9_-39T378Xf3_dp_2_-_vCfV599jfn9fV_789KP9_78v-_8__________3_7BHYAkw1biALsyxwZtAwigRAjCsJCqBQAQUAwtEFgA4OCnZWAT6whYAIBQhGBECHEFGDAIABBIAkIgAkCLBAIgCIBAACABEAhAAxMAgsALAwCAAEA0LFEKAAQJCDIgIjlMCAqBIKCWysQSgr0NMIA6zwAoNEbFQAIkkBFICAkLBwDBEgJWLJA0xRvkAIwQoBRKgAAAAA; _iub_cs-77725586-granular=%7B%22gac%22%3A%22MX4mAQMBAgEIAQUBCAEMAQUBAwEOAQgBBAEBAQYBAwIGAgIBAQEJAQIBBAEDARQBAwEFAQgBBgEJAQEBCAEBAREBBgEFAQ0BBAETAQUBBAICAgoBHAEDAQ0BAwEEAQIBCQEFAQEBCAEFAQUBAwEEAQMBAwEcAQMBBAECAgUBAQEBARACEAEJAQgCBwEFAQEBBwECAQMBwo0BAwEHASkBDgINAQICBwEJARgBAgEGARgBBAERAQgBBgEoAQEBAwERARQBAgEDAQEBBgEFAQQBAQENAREBBgECAQEBAQEHARMBBwEHAQUBAgEJAQMBEwEBAQwBAwEFAQMBCgICARUBDwEBAQUBBwEBAQMBCgEFAQQBIAEKAQcCCQEbAQsCAgEUAQEBBgEFAggBHQEQAQMBCAEOAQcBBgECAQUBBQEGAQEBAwIGAQsBDAEVAQwBAQELAQEBCQEEAQ4BAQEDAQgBAwEEAQMBBgEMAQQBDgEDAQwBAwENAQcBAQEOAQEBBAEEAgEBAQIBAQ0BBgEDAQcBAQEIAQkBEQELAQwBAQERAwIDCAEYAQMCEgEHAQMBBAECAQQBAwEHAQMBAQEBAQEBDQEBAQwBAwEBAQUBCAEFAQIBAwECAQQBAQECAQUBCQEKAQUBAgEPAQIBCgECAgEBAgEIARIBCgEOAQIBCQEGAQUBAwECAQMBBQECAQIBAgECBAUBCgECAwoBBQIJAQQBAQEFAQIBAQEBAQMBAgEBAQEBBgEOAQYBCwEBAgIBAgEDAQQBAwECAQEBAQEEAQIEAQEIAgUBCAIEAQECBgEJAQoCAgMBAgIBAQEFAgsBBAECAgIDAQEBAQYBBgIDAgEBBQIBAwIDAwMBAgcCBgEDAQIBAQICAQQBAgEIAQUCDgEJARsCAQEBAQsBAgEDAgUBAgEDAQYCAgMCAgQBAgICAQEBAQMDAQECAQIBAQEBAQEDAQECAQEBAQEBAwQBAQEFAQQBAQEDAQIBAgYCAQQBBQEDAgEBAwcEBAEBAgUBBAYBAQEBAgMDAwEBAQMDAQICAQEBAgECAQECAwEBAwQEAgIBBQECAgQBAQECAQMCAQECAgMBAQIBAQEBAQcKAgIDAQEBAQQBAQECAQIBBAQDAQEDAQEEAggBAwMCAgYCAwEEAgYBAQQBBAMBAQILAwICAQEBAQICAQQBAwEFAQICAgQCAQEDAQIBBwEBAQEBCAEGAQEBAQIBAgMBBQMFAw%3D%3D%22%7D",
            "authority": "dokkan.fyi",
            "accept": "text/html, application/xhtml+xml",
            "accept-language": "es-ES,es;q=0.9",
            "content-type": "application/json;charset=utf-8",
            "referer": "https://dokkan.fyi/characters/1023091",
            "sec-ch-ua": "'Opera GX';v='89', 'Chromium';v='103', '_Not:A-Brand';v=¡24¡",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "'Windows'",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 OPR/89.0.4447.64",
            "x-inertia": "true",
            "x-inertia-version": "aa6e2214730f2161a1f77c9fa9074052",
            "x-requested-with": "XMLHttpRequest",
            "x-xsrf-token": "eyJpdiI6IlFRdDJHL0tsbzBpMDQxcWhLRU96dkE9PSIsInZhbHVlIjoiNktSSDdzSXZ4UmJOM21KbGZXZllaZXFZQTFKZEJQRHNXQXhFamxiaHp3eS9HQnJoaTAvVVhZUmI2T2lnNk1mR3hQSjRoRHR6UjdwVnVkS0NjNnhNWkJhNVBCRVVhUnoyUm9lNGFpcUdEWVFIQmxoTldnQisyTm9BeVplSmhtL1YiLCJtYWMiOiJmN2EyMzdkZmJjNzQ1YmU1M2M2NDZhMWM2NzY2ODljZDA3Mjk4NzJmMGUyZDI2Y2JmZGVkYTY5N2Q1NzVhMTgxIiwidGFnIjoiIn0="
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        nombre = response.json()["props"]["card"]["name"]
        dict = [nombre]

        x = True
        i = 1
        a = "link_skill"
        b = "_id"
        links = []
        while x :
            try:
                c = a+str(i)+b
                links.append(response.json()["props"]["card"][c])
                i+=1
            except KeyError:
                x = False
        dict.append(links)
        return dict