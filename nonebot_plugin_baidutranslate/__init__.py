import httpx
import nonebot
from .config import Config
from .consts import *
from .exceptions import EXCEPTIONS
from .data_source import *
from typing import Tuple, Any

from nonebot import on_regex, on_command
from nonebot.params import RegexGroup, CommandArg
from nonebot.plugin import PluginMetadata
from nonebot.exception import FinishedException
from nonebot.adapters.onebot.v11 import GroupMessageEvent, Message

global_config = nonebot.get_driver().config
plugin_config = Config(**global_config.dict())

general_translate = on_regex(r"^([x|\u4e00-\u9fa5])翻([x|\u4e00-\u9fa5])(.*)?$", priority=5)
field_translate = on_regex(r"^([\u4e00-\u9fa5][\u4e00-\u9fa5])领域([\u4e00-\u9fa5])翻([\u4e00-\u9fa5])(.*)?$", priority=5)
language_recognize = on_command("语种识别", priority=5)

@general_translate.handle()
async def _(event: GroupMessageEvent, reg_group: Tuple[Any, ...] = RegexGroup()):
    if event.reply:
        query_ = event.reply.message.extract_plain_text().strip()
    else:
        query_ = reg_group[-1].strip()

    from_, to_ = reg_group[0], reg_group[1]

    if not from_ or not to_:
        await general_translate.finish(f"指令打错啦！请输入“x翻x [内容]”，方括号不需要输入\n其中x可以为: {', '.join(GENERAL_LANGUAGES.keys())}", at_sender=True)

    # 消除指令前缀
    command_start = (global_config.dict())['command_start']
    if from_[0] in command_start:
        from_ = from_[1:]

    if len(query_) > 2000:
        await general_translate.finish("翻译过长！请不要超过2000字", at_sender=True)

    async with httpx.AsyncClient() as client:
        try:
            result = await Translate(client=client).general_translate(
                q=query_, from_=parse_lang(from_), to=parse_lang(to_)
            )
            await general_translate.finish(result, at_sender=True)
        except FinishedException:
            pass
        except KeyError as e:
            await general_translate.finish(f"指令打错啦！\n能翻译的语种只有: {', '.join(GENERAL_LANGUAGES.keys())}", at_sender=True)
        except Exception as e:
            if any((isinstance(e, _) for _ in EXCEPTIONS.values())):
                await general_translate.finish(e.__str__())
            await general_translate.finish(f"百度翻译出错：{e.__str__()}")


@field_translate.handle()
async def _(event: GroupMessageEvent, reg_group: Tuple[Any, ...] = RegexGroup()):
    if event.reply:
        query_ = event.reply.message.extract_plain_text().strip()
    else:
        query_ = reg_group[-1].strip()

    domain_, from_, to_ = reg_group[0], reg_group[1], reg_group[2]

    if not all((domain_, from_, to_)):
        await field_translate.finish(f"指令打错啦！请输入“oo领域x翻x [内容]”，方括号不需要输入\n其中oo可以为{', '.join(DOMAINS_NAMES.keys())}\nx仅能为中, 英", at_sender=True)

    # 消除指令前缀
    command_start = (global_config.dict())['command_start']
    if from_[0] in command_start:
        from_ = from_[1:]

    if len(query_) > 2000:
        await field_translate.finish("翻译过长！请不要超过2000字", at_sender=True)

    async with httpx.AsyncClient() as client:
        try:
            result = await Translate(client=client).field_translate(
                q=query_, from_=parse_lang(from_), to=parse_lang(to_), domain=parse_domain(domain_)
            )
            await field_translate.finish(result, at_sender=True)
        except FinishedException:
            pass
        except KeyError as e:
            await field_translate.finish(f"指令打错啦！\n能翻译的领域只有: {', '.join(DOMAINS_NAMES.keys())}\n能翻译的语种只有: 中, 英", at_sender=True)
        except Exception as e:
            if any((isinstance(e, _) for _ in EXCEPTIONS.values())):
                await field_translate.finish(e.__str__())
            await field_translate.finish(f"百度翻译出错：{e.__str__()}")


@language_recognize.handle()
async def _(event: GroupMessageEvent, args: Message = CommandArg()):
    if event.reply:
        query_ = event.reply.message.extract_plain_text().strip()
    else:
        query_ = args.extract_plain_text().strip()

    if not query_:
        await general_translate.finish(f"指令打错啦！请输入“语种识别 [内容]”，方括号不需要输入\n其中能识别的语种只有{', '.join(RECOGNIZABLE_LANGUAGES.values())}", at_sender=True)

    # 消除指令前缀
    command_start = (global_config.dict())['command_start']
    if query_ in command_start:
        query_ = query_[1:]

    if len(query_) > 2000:
        await language_recognize.finish("翻译过长！请不要超过2000字", at_sender=True)

    async with httpx.AsyncClient() as client:
        try:
            result = await Translate(client=client).language_recognize(
                q=query_
            )
            await language_recognize.finish(result, at_sender=True)
        except FinishedException:
            pass
        except Exception as e:
            if any((isinstance(e, _) for _ in EXCEPTIONS.values())):
                await field_translate.finish(e.__str__())
            await language_recognize.finish(f"百度翻译出错：{e.__str__()}")


__plugin_meta__ = PluginMetadata(
    name="百度翻译",
    description="调用百度翻译API进行常用语种互译",
    usage=(
        "1. 通用翻译："
        "\n\tx翻x [内容]"
        f"\n\t其中x可以为: {', '.join(GENERAL_LANGUAGES.keys())}"
        "\n2. 领域翻译："
        "\n\too领域x翻x [内容]"
        f"\n\t其中oo可以为{', '.join(DOMAINS_NAMES.keys())}"
        f"\n\tx仅能为中, 英"
        f"\n3. 语种识别："
        f"\n\t语种识别 [内容]"
    ),
    extra={
        "author": "Number_Sir<number_sir@126.com>",
        "version": "0.3.0"
    }
)
