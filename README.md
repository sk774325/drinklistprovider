# LINE BOT BARTENDER

## 前言
有鑒於近期新冠病毒的肆虐，在酒吧喝酒可能面臨病毒感染的風險，因此，在眾人的熱烈矚目下，推出了即將風靡全球的--Bartender。

## 功能
將會提供國際調酒師協會（International Bartenders Association）以六種基酒為基底所調的調酒配方。

## 環境
* Python 3.6
* Line bot
* Heroku
* Mac os 13.0

## 使用教學
QR-code:
![加好友](https://i.imgur.com/uD3u7VF.png)
### Step1:加好友
![剛加好友](https://i.imgur.com/Nx3ZVnc.png)
### Step2:選擇基酒
![選擇基酒](https://i.imgur.com/mbj5ClI.png)
### Step3:選擇想喝的配方
![選擇酒類](https://i.imgur.com/dC0rZLE.png)
### Step4:顯示材料與方法
![顯示配方](https://i.imgur.com/26jkwgf.png)


## Finite State Machine
![fsm](https://i.imgur.com/P70n52V.png)

## State 說明：
1. 先分出六大基酒
2. 每一種基酒會再分出各種調酒
3. 調酒會再回到"user"


## Reference
[Gin 琴酒](https://www.1shot.tw/17332/%E8%AA%BF%E9%85%92%E7%9F%A5%E8%AD%98-51-%E6%AC%BE%E4%B8%80%E5%AE%9A%E8%A6%81%E5%96%9D%E9%81%8E%E7%9A%84%E7%90%B4%E9%85%92%E8%AA%BF%E9%85%92) 

[Vodka 伏特加](https://mf.techbang.com/posts/10662-7-at-home-can-do-ultra-simple-vodka-bartender-wine-fresh-people-can-quickly-get-started)

[Rum 萊姆酒](https://mf.techbang.com/posts/11317-a-must-have-drink-for-a-summer-party-7-lamb-bartender-diy-recommendations-at-home-you-can-enjoy-the-tropical-style)

[Tequila 龍舌蘭](https://www.1shot.tw/14069/%E8%AA%BF%E9%85%92%E7%9F%A5%E8%AD%98-%E9%BE%8D%E8%88%8C%E8%98%AD%E5%85%A5%E9%96%80-%E5%9B%9B%E6%AC%BE%E9%BE%8D%E8%88%8C%E8%98%AD%E7%B6%93%E5%85%B8%E8%AA%BF%E9%85%92%E5%9C%A8%E5%AE%B6%E5%81%9A)
