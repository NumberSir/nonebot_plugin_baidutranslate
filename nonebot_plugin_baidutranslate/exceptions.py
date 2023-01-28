"""
这里定义一些百度翻译返回的异常类型
API 参考：https://fanyi-api.baidu.com/doc/21
"""


class BaiduBaseException(Exception):
    """基类，代码 52000 是成功代码"""
    def __init__(self, code: str = "52000", msg: str = "发生未知错误..."):
        self.code = code
        self.msg = msg

    def __str__(self):
        return f"百度翻译出错：\n错误代码：{self.code}\t错误信息：{self.msg}"


class BaiduVoiceWrongParamsException(BaiduBaseException):
    """必填参数为空或固定参数有误"""
    def __init__(self, code: str = "10001", msg: str = "必填参数为空或固定参数有误，请检查参数是否误传 ..."):
        super().__init__(code, msg)


class BaiduVoiceFrequencyLimitException(BaiduBaseException):
    """访问频率受限"""
    def __init__(self, code: str = "10004", msg: str = "访问频率受限，请降低您的调用频率 ..."):
        super().__init__(code, msg)


class BaiduVoiceWrongSignException(BaiduBaseException):
    """签名错误"""
    def __init__(self, code: str = "10005", msg: str = "签名错误，请检查您的签名生成方法 ..."):
        super().__init__(code, msg)


class BaiduVoiceUnauthorizedException(BaiduBaseException):
    """未授权用户"""
    def __init__(self, code: str = "10006", msg: str = "请检查 APP ID 是否正确或者短语音翻译服务是否开通 ..."):
        super().__init__(code, msg)


class BaiduVoiceIllegalClientIPException(BaiduBaseException):
    """客户端IP非法"""
    def __init__(self, code: str = "10007", msg: str = "客户端IP非法，请检查个人资料里填写的IP地址是否正确 ..."):
        super().__init__(code, msg)


class BaiduVoiceUnsupportedLangException(BaiduBaseException):
    """语言方向不支持"""
    def __init__(self, code: str = "20000", msg: str = "语言方向不支持，请检查源语种或目标语种是否在语言列表里 ..."):
        super().__init__(code, msg)


class BaiduFailedVoiceTranslateException(BaiduBaseException):
    """语音翻译请求失败"""
    def __init__(self, code: str = "20200", msg: str = "语音翻译请求失败，请重试 ..."):
        super().__init__(code, msg)


class BaiduVoiceTooLargeException(BaiduBaseException):
    """音频数据大小超过限制"""
    def __init__(self, code: str = "20201", msg: str = "音频数据大小超过限制，请上传符合大小要求的音频数据 ..."):
        super().__init__(code, msg)


class BaiduInvalidVoiceTypeException(BaiduBaseException):
    """文件格式不支持"""
    def __init__(self, code: str = "20202", msg: str = "文件格式不支持，请上传符合格式要求的音频数据 ..."):
        super().__init__(code, msg)


class BaiduTimeoutException(BaiduBaseException):
    """请求超时"""
    def __init__(self, code: str = "52001", msg: str = "请求超时，请重试 ..."):
        super().__init__(code, msg)


class BaiduInternalError(BaiduBaseException):
    """系统错误"""
    def __init__(self, code: str = "52002", msg: str = "系统错误，请重试 ..."):
        super().__init__(code, msg)


class BaiduUnauthorizedException(BaiduBaseException):
    """未授权用户"""
    def __init__(self, code: str = "52003", msg: str = "请检查 appid 是否正确或者服务是否开通 ..."):
        super().__init__(code, msg)


class BaiduMissingArgException(BaiduBaseException):
    """缺少必填参数"""
    def __init__(self, code: str = "54000", msg: str = "请检查是否少传参数 ..."):
        super().__init__(code, msg)


class BaiduWrongSignException(BaiduBaseException):
    """签名错误"""
    def __init__(self, code: str = "54001", msg: str = "请检查您的签名生成方法 ..."):
        super().__init__(code, msg)


class BaiduFrequencyLimitException(BaiduBaseException):
    """访问频率受限"""
    def __init__(self, code: str = "54003", msg: str = "请降低您的调用频率，或进行身份认证后切换为高级版/尊享版 ..."):
        super().__init__(code, msg)


class BaiduNoBalanceException(BaiduBaseException):
    """账户余额不足"""
    def __init__(self, code: str = "54004", msg: str = "请前往 https://api.fanyi.baidu.com/api/trans/product/desktop 为账户充值 ..."):
        super().__init__(code, msg)


class BaiduLongQueryException(BaiduBaseException):
    """长 query 请求频繁"""
    def __init__(self, code: str = "54005", msg: str = "请降低长query的发送频率，3s后再试 ..."):
        super().__init__(code, msg)


class BaiduLangRecognizeFailedException(BaiduBaseException):
    """语种检测失败"""
    def __init__(self, code: str = "54009", msg: str = "不在支持检测的语种范围内 ..."):
        super().__init__(code, msg)


class BaiduBudgetNotEnoughException(BaiduBaseException):
    """预扣金额不足"""
    def __init__(self, code: str = "54010", msg: str = "余额不足以支付本次翻译费用，请前往管理控制台为账户充值 ..."):
        super().__init__(code, msg)


class BaiduIllegalClientIPException(BaiduBaseException):
    """客户端IP非法"""
    def __init__(self, code: str = "58000", msg: str = "检查个人资料里填写的IP地址是否正确，可前往 https://api.fanyi.baidu.com/access/0/3 修改 ..."):
        super().__init__(code, msg)


class BaiduUnsupportedLangException(BaiduBaseException):
    """译文语言方向不支持"""
    def __init__(self, code: str = "58001", msg: str = "检查译文语言是否在语言列表里 ..."):
        super().__init__(code, msg)


class BaiduServiceClosedException(BaiduBaseException):
    """服务当前已关闭"""
    def __init__(self, code: str = "58002", msg: str = "请前往 https://api.fanyi.baidu.com/choose 开启服务 ..."):
        super().__init__(code, msg)


class BaiduWrongParamsException(BaiduBaseException):
    """参数错误"""
    def __init__(self, code: str = "66000", msg: str = "参数错误，请检查传递参数 ..."):
        super().__init__(code, msg)


class BaiduInvalidImageDataException(BaiduBaseException):
    """上传图片数据有误"""
    def __init__(self, code: str = "69001", msg: str = "上传图片数据有误，请检查图片是否有问题 ..."):
        super().__init__(code, msg)


class BaiduOCRTimeOutException(BaiduBaseException):
    """图片识别超时"""
    def __init__(self, code: str = "69002", msg: str = "图片识别超时，请重试 ..."):
        super().__init__(code, msg)


class BaiduOCRFailedException(BaiduBaseException):
    """内容识别失败"""
    def __init__(self, code: str = "69003", msg: str = "内容识别失败，请检查图片是否存在内容后重试 ..."):
        super().__init__(code, msg)


class BaiduEmptyImageException(BaiduBaseException):
    """识别内容为空"""
    def __init__(self, code: str = "69004", msg: str = "识别内容为空，请检查图片是否存在内容后重试 ..."):
        super().__init__(code, msg)


class BaiduImageTooLargeException(BaiduBaseException):
    """图片大小超限（超过4M）"""
    def __init__(self, code: str = "69005", msg: str = "图片大小超限（超过4M），请上传符合图片大小要求的图片 ..."):
        super().__init__(code, msg)


class BaiduInvalidImageSizeException(BaiduBaseException):
    """图片尺寸不符合标准（最短边至少30px，最长边最大4096px）"""
    def __init__(self, code: str = "69006", msg: str = "图片尺寸不符合标准（最短边至少30px，最长边最大4096px），请上传符合图片大小要求的图片 ..."):
        super().__init__(code, msg)


class BaiduInvalidImageTypeException(BaiduBaseException):
    """图片格式不支持（png/jpg）"""
    def __init__(self, code: str = "69007", msg: str = "请上传png或jpg格式的图片"):
        super().__init__(code, msg)


class BaiduEmptyCUIDException(BaiduBaseException):
    """设备号为空"""
    def __init__(self, code: str = "69008", msg: str = "请检查 cuid 参数(正常情况下应为 APICUID) ..."):
        super().__init__(code, msg)


class BaiduInvalidImagePasteException(BaiduBaseException):
    """文字贴合参数异常"""
    def __init__(self, code: str = "69012", msg: str = "请检查 paste 参数(正常情况下应为0, 1, 2)"):
        super().__init__(code, msg)


class BaiduFileInfoNotFoundException(BaiduBaseException):
    """找不到文件信息"""
    def __init__(self, code: str = "70201", msg: str = "请检查是否上传文件 ..."):
        super().__init__(code, msg)


class BaiduCreateRemoteFileFailedException(BaiduBaseException):
    """生成远程文件失败"""
    def __init__(self, code: str = "70202", msg: str = "生成远程文件失败，请重试 ..."):
        super().__init__(code, msg)


class BaiduFileTooLargeException(BaiduBaseException):
    """上传文件大小超限"""
    def __init__(self, code: str = "70203", msg: str = "上传文件大小超限，请拆分文件后重试 ..."):
        super().__init__(code, msg)


class BaiduFileCacheExpiredException(BaiduBaseException):
    """缓存文件失效"""
    def __init__(self, code: str = "70204", msg: str = "缓存文件失效，请重新提交翻译文件 ..."):
        super().__init__(code, msg)


class BaiduDocTranslateFailedException(BaiduBaseException):
    """文档翻译失败"""
    def __init__(self, code: str = "70205", msg: str = "文档翻译失败，请重试 ..."):
        super().__init__(code, msg)


class BaiduInvalidFileTypeException(BaiduBaseException):
    """文件类型不支持"""
    def __init__(self, code: str = "70206", msg: str = "文件类型不支持，请检查文件 ..."):
        super().__init__(code, msg)


class BaiduFileTranslateUnableException(BaiduBaseException):
    """文件内容无法翻译"""
    def __init__(self, code: str = "70207", msg: str = "文件内容无法翻译，请检查文件 ..."):
        super().__init__(code, msg)


class BaiduServiceUnavailableException(BaiduBaseException):
    """认证未通过或未生效"""
    def __init__(self, code: str = "90107", msg: str = "请前往 https://api.fanyi.baidu.com/myIdentify 开启服务 ..."):
        super().__init__(code, msg)


EXCEPTIONS = {
    "10001": BaiduVoiceWrongParamsException,
    "10004": BaiduVoiceFrequencyLimitException,
    "10005": BaiduVoiceWrongSignException,
    "10006": BaiduVoiceUnauthorizedException,
    "10007": BaiduVoiceIllegalClientIPException,
    "20000": BaiduVoiceUnsupportedLangException,
    "20200": BaiduFailedVoiceTranslateException,
    "20201": BaiduVoiceTooLargeException,
    "20202": BaiduInvalidVoiceTypeException,
    "52000": BaiduBaseException,
    "52001": BaiduTimeoutException,
    "52002": BaiduInternalError,
    "52003": BaiduUnauthorizedException,
    "54000": BaiduMissingArgException,
    "54001": BaiduWrongSignException,
    "54003": BaiduFrequencyLimitException,
    "54004": BaiduNoBalanceException,
    "54009": BaiduLangRecognizeFailedException,
    "54010": BaiduBudgetNotEnoughException,
    "54005": BaiduLongQueryException,
    "58000": BaiduIllegalClientIPException,
    "58001": BaiduUnsupportedLangException,
    "58002": BaiduServiceClosedException,
    "66000": BaiduWrongParamsException,
    "69001": BaiduInvalidImageDataException,
    "69002": BaiduOCRTimeOutException,
    "69003": BaiduOCRFailedException,
    "69004": BaiduEmptyImageException,
    "69005": BaiduImageTooLargeException,
    "69006": BaiduInvalidImageSizeException,
    "69007": BaiduInvalidImageTypeException,
    "69008": BaiduEmptyCUIDException,
    "69012": BaiduInvalidImagePasteException,
    "70201": BaiduFileInfoNotFoundException,
    "70202": BaiduCreateRemoteFileFailedException,
    "70203": BaiduFileTooLargeException,
    "70204": BaiduFileCacheExpiredException,
    "70205": BaiduDocTranslateFailedException,
    "70206": BaiduInvalidFileTypeException,
    "70207": BaiduFileTranslateUnableException,
    "90107": BaiduServiceUnavailableException,
}