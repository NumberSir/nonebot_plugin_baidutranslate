import hashlib

import httpx
from .exceptions import EXCEPTIONS, BaiduBaseException
from .consts import *
from nonebot import get_driver
from .config import Config
baidu_config = Config.parse_obj(get_driver().config.dict())


class Translate:
    """百度翻译的多种翻译功能"""
    def __init__(self, client: httpx.AsyncClient, appid: str = baidu_config.appid, salt: str = baidu_config.salt, key: str = baidu_config.key):
        self._client = client
        self._appid = appid
        self._salt = salt
        self._key = key

    async def _request(self, url: str, headers: dict = None, files: dict = None, **params):
        headers = headers or {"Content-Type": "application/x-www-form-urlencoded"}
        for _ in range(5):
            try:
                if files:
                    return await self._client.post(url=url, headers=headers, files=files, data=params)
                return await self._client.post(url=url, headers=headers, data=params)
            except httpx.TimeoutException as e:
                continue
        raise BaiduBaseException(code="-1", msg="请求超时，请检查网络或稍后再试……")

    async def _process_response(self, response: httpx.Response):
        json_data = response.json()
        if "error_code" not in json_data.keys():  # 通用翻译
            _result = json_data['trans_result'][0]
            res = f"\n原文：{_result['src']}\n译文：{_result['dst']}"
            return "QAQ，翻译出来太长了，请发的短一些吧..." if len(res) > 2000 else res

        if json_data["error_code"] == 0:  # 语种识别
            return f"\n语种：{RECOGNIZABLE_LANGUAGES[json_data['data']['src']]}"

        if json_data['error_code'] != "52000":
            raise EXCEPTIONS[json_data['error_code']]

    async def general_translate(self, q: str, from_: str, to: str):
        """通用文本翻译"""
        sign = hashlib.md5(bytes(f"{self._appid}{q}{self._salt}{self._key}", 'utf-8')).hexdigest()
        url = "https://fanyi-api.baidu.com/api/trans/vip/translate"
        params = {
            "q": q,
            "from": from_,
            "to": to,
            "appid": self._appid,
            "salt": self._salt,
            "sign": sign,
        }
        response = await self._request(url, **params)
        return await self._process_response(response)

    async def field_translate(self, q: str, from_: str, to: str, domain: str):
        # sourcery skip: raise-specific-error
        """垂直领域翻译"""
        if domain not in DOMAINS.keys() or f"{from_}-{to}" not in DOMAINS[domain]:
            raise BaiduBaseException(code="-1", msg="领域或语言填写出错，领域及对应语言仅能为：" + ", ".join(f"{k}({', '.join(v)})" for k, v in DOMAINS.items()))

        sign = hashlib.md5(bytes(f"{self._appid}{q}{self._salt}{domain}{self._key}", 'utf-8')).hexdigest()
        url = "https://fanyi-api.baidu.com/api/trans/vip/fieldtranslate"
        params = {
            "q": q,
            "from": from_,
            "to": to,
            "appid": self._appid,
            "salt": self._salt,
            "domain": domain,
            "sign": sign,
        }
        response = await self._request(url, **params)
        return await self._process_response(response)

    # async def document_count(self, file: Path, from_: str, to: str, type_: str):
    #     """文档统计校验"""
    #     file = file.absolute()
    #     if all(_ not in file.__str__() for _ in DOCUMENT_TYPES):
    #         raise BaiduInvalidFileTypeException
    #     async with aopen(file, "rb") as fp:
    #         file_bytes = await fp.read()
    #
    #     _sign = (
    #         f"appid={self._appid}&"
    #         f"from={from_}&"
    #         f"timestamp={int(time.time())}&"
    #         f"to={to}&"
    #         f"type={type_}&"
    #     )
    #     _sign = (
    #         f"{_sign}"
    #         f"{hashlib.md5(file_bytes).hexdigest()}"
    #     )
    #     sign = hashlib.md5(bytes(f"{_sign}{self._key}", "utf-8")).hexdigest()
    #
    #     url = "https://fanyi-api.baidu.com/api/trans/vip/doccount"
    #     params = {
    #         "appid": self._appid,
    #         "from": from_,
    #         "timestamp": int(time.time()),
    #         "to": to,
    #         "type": type_,
    #
    #         "file": os.path.basename(file),
    #         "sign": sign,
    #     }
    #     files = {"file": (os.path.basename(file), file_bytes, "multipart/form-data")}
    #     headers = {"Content-Type": "Content-Type=mutipart/form-data"}
    #     response = await self._request(url, headers=headers, files=files, **params)
    #     return await self._process_response(response)

    # async def document_translate(self, file: Path, from_: str, to: str, type_: str, output_type: str):
    #     """文档翻译"""
    #     file = file.absolute()
    #     async with aopen(file, "rb") as fp:
    #         file_bytes = await fp.read()
    #
    #     _sign = (
    #         f"appid={self._appid}&"
    #         f"from={from_}&"
    #         f"outPutType={output_type}&"
    #         f"timestamp={int(time.time())}&"
    #         f"to={to}&"
    #         f"type={type_}&"
    #     )
    #     _sign = (
    #         f"{_sign}"
    #         f"{hashlib.md5(file_bytes).hexdigest()}"
    #     )
    #     sign = hashlib.md5(bytes(f"{_sign}{self._key}", "utf-8")).hexdigest()
    #
    #     url = "https://fanyi-api.baidu.com/api/trans/vip/doctrans"
    #     params = {
    #         "appid": self._appid,
    #         "from": from_,
    #         "outPutType": output_type,
    #         "timestamp": int(time.time()),
    #         "to": to,
    #         "type": type_,
    #
    #         "file": os.path.basename(file),
    #         "sign": sign,
    #     }
    #     files = {"file": (os.path.basename(file), file_bytes, "multipart/form-data")}
    #     headers = {"Content-Type": "Content-Type=mutipart/form-data"}
    #     response = await self._request(url, headers=headers, files=files, **params)
    #     return await self._process_response(response)

    async def language_recognize(self, q: str):
        """语种识别"""
        sign = hashlib.md5(bytes(f"{self._appid}{q}{self._salt}{self._key}", 'utf-8')).hexdigest()
        url = "https://fanyi-api.baidu.com/api/trans/vip/language"
        params = {
            "q": q,
            "appid": self._appid,
            "salt": self._salt,
            "sign": sign,
        }
        response = await self._request(url, **params)
        return await self._process_response(response)

    # async def picture_translate(self, image: Path, from_: str, to: str, paste: int = 0):
    #     """图片翻译"""
    #     file = image.absolute()
    #     if all(_ not in file.__str__() for _ in IMAGE_TYPES):
    #         raise BaiduInvalidImageTypeException
    #     async with aopen(file, "rb") as fp:
    #         file_bytes = await fp.read()
    #     _sign = hashlib.md5(file_bytes).hexdigest()
    #     sign = hashlib.md5(bytes(f"{self._appid}{_sign}{self._salt}APICUIDmac{self._key}", "utf-8")).hexdigest()
    #     url = "https://fanyi-api.baidu.com/api/trans/sdk/picture"
    #     params = {
    #         "image": os.path.basename(file),
    #         "from": from_,
    #         "to": to,
    #         "appid": self._appid,
    #         "salt": self._salt,
    #         "cuid": "APICUID",
    #         "mac": "mac",
    #         "version": 3,
    #         "paste": paste,
    #         "sign": sign,
    #     }
    #     files = {"file": (os.path.basename(file), file_bytes, "multipart/form-data")}
    #     headers = {"Content-Type": "Content-Type=mutipart/form-data"}
    #     response = await self._request(url, headers=headers, files=files, **params)
    #     return await self._process_response(response)

    # async def voice_translate(self, from_: str, to: str, voice: str, format: str = "pcm"):
    #     """语音翻译"""
    #
    #     url = "https://fanyi-api.baidu.com/api/trans/v2/voicetrans"
    #     params = {
    #         "from": from_,
    #         "to": to,
    #         "voice": voice,
    #         "format": format
    #     }
    #     response = await self._request(
    #         url,
    #         headers={
    #             "Content-Type": "application/json",
    #             "X-Appid": params['appid'],
    #             "X-Timestamp": int(time.time()),
    #             "X-Sign": params['sign']
    #         },
    #         **params
    #     )
    #     return await self._process_response(response)


def parse_lang(lang_zh: str):
    try:
        return GENERAL_LANGUAGES[lang_zh]
    except KeyError:
        raise


def parse_domain(domain_zh: str):
    try:
        return DOMAINS_NAMES[domain_zh]
    except KeyError:
        raise


__all__ = [
    "Translate",
    "parse_lang",
    "parse_domain"
]
