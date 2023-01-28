import nonebot
from .config import Config
from .data_source import translate_msg, LANGUAGES
from .utils import EXCEPTIONS
from typing import Tuple, Any

from nonebot import on_regex
from nonebot.params import RegexGroup
from nonebot.plugin import PluginMetadata
from nonebot.adapters.onebot.v11 import GroupMessageEvent

global_config = nonebot.get_driver().config
plugin_config = Config(**global_config.dict())

translate = on_regex(r"^(.*)?翻([\u4e00-\u9fa5]+?)(.*)?$", priority=5, block=True)


@translate.handle()
async def _(event: GroupMessageEvent, reg_group: Tuple[Any, ...] = RegexGroup()):
    if event.reply:
        _query = event.reply.message.extract_plain_text().strip()
    else:
        _query = reg_group[-1].strip()

    _from, _to = reg_group[0], reg_group[1]

    # 消除指令前缀
    command_start = (global_config.dict())['command_start']
    if len(_from) > 1 and _from[0] in command_start:
        _from = _from[1:]

    if _from and _to:
        _from_to = [_from, _to]
    else:
        await translate.finish(f"指令打错啦！请输入“x翻x 内容”\n其中x可以为: {', '.join(LANGUAGES.keys())}", at_sender=True)

    if len(_query) > 2000:
        await translate.finish("翻译过长！请不要超过2000字", at_sender=True)
    try:
        await translate.finish(await translate_msg(_from_to, _query), at_sender=True)
    except Exception as e:
        if e in EXCEPTIONS.values():
            await translate.finish(e.__str__())
        await translate.finish(f"百度翻译出错：{e.__str__()}")

__plugin_meta__ = PluginMetadata(
    name="百度翻译",
    description="调用百度翻译API进行常用语种互译",
    usage=(
        "x翻x [内容]"
        f"\n其中x可以为: {', '.join(LANGUAGES.keys())}"
    ),
    extra={
        "author": "Number_Sir<number_sir@126.com>",
        "version": "0.2.0"
    }
)
