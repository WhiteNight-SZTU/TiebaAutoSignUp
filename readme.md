# 使用方式
命令行运行：
```
python main.py
```

## 可选参数
* --log 日志等级，默认info。可选info/debug
* -r --refresh 刷新需要签到的贴吧列表，默认false。第一次运行时会自动将需要签到的贴吧列表保存到tieba_dict.json文件中。只有后续关注了新的贴吧才需要用到该参数。

## 注意事项  
需要在account.json中填入BDUSS和STOKEN。这两个参数可通过浏览器f12抓包获取。
![Snipaste_2024-08-28_17-27-09](https://github.com/user-attachments/assets/2730fa71-cb49-4417-9f81-ad5f74d108cc)

手机端APP显示的关注贴吧数，和脚本获取到的关注贴吧数可能不一致——**这是百度的锅**。如果关注的贴吧有些被“神隐”了，而你随后又取消关注了就会导致这种情况发生。目前无解。  

可通过github action实现每天自动定时签到。需要fork后在repo的**setting-secrets and variables-action**中填入秘密变量BDUSS和STOKEN值。
