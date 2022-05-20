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
pip install nonebot_plugin_baidutranslate
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
x翻x [内容]
```

## 图片示例
<div align="left">
  <img src="https://user-images.githubusercontent.com/52584526/169519990-df4402d1-8b5e-4c88-8582-f64485e0e702.png" width="500" />
</div>

<div align="left">
  <img src="https://user-images.githubusercontent.com/52584526/169520252-71343d82-b3fc-477f-a7d7-714405e160ba.png" width="500" />
</div>
