<p align="center">
  <a href="https://v2.nonebot.dev/"><img src="https://v2.nonebot.dev/logo.png" width="200" height="200" alt="nonebot"></a>
</p>

<div align="center">
  
# Nonebot_Plugin_BaiduTranslate
  
_✨ 基于OneBot适配器的[NoneBot2](https://v2.nonebot.dev/)百度翻译插件 ✨_
  
</div>

## 功能

- 可以调用百度翻译 API 实现常用语种之间的互译

## 安装

- 使用 nb-cli

```
nb plugin install nonebot_plugin_baidutranslate
```

- 使用 pip

```
pip install -U nonebot_plugin_baidutranslate
```

## 如何使用

### .env 配置项

```ini
# 以下均为百度翻译配置，见 https://fanyi-api.baidu.com/doc/21
appid = "xxx"  # 你的 APP ID，在百度翻译的开发者中心里可以找到
key = "xxx"    # 你的密钥，在百度翻译的开发者中心里可以找到
salt = "xxx"   # 随机字符串
```

各配置项的含义如上。

### 指令

使用以下指令触发，需加上指令前缀

```
通用文本翻译：
    x翻x [内容]
    (回复消息)x翻x
   
垂直领域翻译：
    oo领域x翻x [内容]
    (回复消息)oo领域x翻x
    
语种识别：
    语种识别 [内容]
    (回复消息)语种识别
```

## 图片示例
<div align="left">
  <img src="https://user-images.githubusercontent.com/52584526/169519990-df4402d1-8b5e-4c88-8582-f64485e0e702.png" width="500" />
</div>

<div align="left">
  <img src="https://user-images.githubusercontent.com/52584526/169520252-71343d82-b3fc-477f-a7d7-714405e160ba.png" width="500" />
</div>

<div align="left">
  <img src="https://user-images.githubusercontent.com/52584526/215271556-2b800b02-298f-44f1-af1b-bda0a2d3653b.png" width="500" />
</div>

<div align="left">
  <img src="https://user-images.githubusercontent.com/52584526/215284148-93d94ee7-d04a-4834-9ce1-4e0aeacaa4b6.png" width="500" />
</div>

<div align="left">
  <img src="https://user-images.githubusercontent.com/52584526/215284152-8a0506fa-7719-4c86-a30e-c65d8f84db26.png" width="500" />
</div>

## 更新日志
> 2023-04-04 v0.3.2
> - 修复回复时的空行[@issue/13](https://github.com/NumberSir/nonebot_plugin_baidutranslate/issues/13)
> 
> 2023-03-29 v0.3.1
> - 现在私聊也可用（但不推荐）
> 
> 2023-01-29 v0.3.0
> - 添加“垂直领域翻译”与“语种识别”功能
> 
> 2023-01-28 v0.2.0
> - 修改最低兼容版本为 Python 3.8, 与 nonebot2.0.0rc3 一致
> - 增加回复消息翻译功能
> - 修改匹配翻译文本的bug
> - 错误信息以聊天信息的方式发送
> - 修复命令前缀引起参数缺少，判断翻译后的文本长度[@pull/5](https://github.com/NumberSir/nonebot_plugin_baidutranslate/pull/5)
>
> 2022-05-30 v0.1.1
> - 修改最低兼容版本到 Python 3.7.3 版本
> 
> 2022-05-27 v0.1.0
> - 添加了基础翻译功能
>
