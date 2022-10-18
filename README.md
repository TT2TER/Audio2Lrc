# Audio2Lrc
A tool helps people generate lrcs from audio with the help of whisper

# 安装：
## 本项目需要依赖openAI的whisper模型转录
请先行安装该项目([地址](https://github.com/openai/whisper))

可以参考博客:[whisper实时转录](https://blog.1314171.xyz/post/221018whisper.html)
## 下载解压本项目

# 使用：
使用方法
```
python audio2lrc <参数1：audio path (with suffix name)> <参数2：reserve srt or not (blank for remove)>
```
例子：保留srt文件，如不保留请缺省参数2
```
python audio2lrc example.mp3 1
```

# 引用项目链接
[openai/whisper](https://github.com/openai/whisper)

[cybytess/swapsub](https://github.com/cybytess/swapsub)

其中swapsub本可以用`pip`安装但作者打包有问题

# 题外话：这是本人第一个有实际作用的项目，欢迎star
比如可以转录播客