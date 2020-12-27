from transitions.extensions import GraphMachine
from linebot.models import ImageCarouselColumn, URITemplateAction, MessageTemplateAction,TextSendMessage,TemplateSendMessage,ButtonsTemplate
from utils import send_text_message, send_button_message, send_image_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

# Gin
    def is_going_to_gin(self, event):
        text = event.message.text
        if text == "琴酒" or text == "Gin" or text == "gin":
            wine = "gin"
            return True
        else: 
            return False
    def on_enter_gin(self, event):
        title = '請選擇您想要的調酒：'
        text = "請從以下三種選一種"
        action = [
            MessageTemplateAction(
                label = '琴通寧 Gin & Tonic',
                text ='琴通寧 Gin & Tonic'
            ),
            MessageTemplateAction(
                label = '馬丁尼 Martini',
                text = '馬丁尼 Martini'
            ),
            MessageTemplateAction(
                label = '內格羅尼 Negroni',
                text = '內格羅尼 Negroni'
            ),
        ]
        url = 'https://i.imgur.com/d7WviyC.jpg'
        send_button_message(event.reply_token, title, text, action, url)
    # https://www.1shot.tw/17332/%E8%AA%BF%E9%85%92%E7%9F%A5%E8%AD%98-51-%E6%AC%BE%E4%B8%80%E5%AE%9A%E8%A6%81%E5%96%9D%E9%81%8E%E7%9A%84%E7%90%B4%E9%85%92%E8%AA%BF%E9%85%92
    # 琴通寧 Gin & Tonic
    def is_going_to_gin_tonic(self, event):
        text = event.message.text
        if text == '琴通寧 Gin & Tonic':
            return True
        return False
    
    def on_enter_gin_tonic(self, event):
        txt = '材料：1. 琴酒 45ml\n2. 檸檬汁 5ml\n3. 通寧水適量\n調製方法：\n在杯中加入琴酒、檸檬汁與冰塊稍加攪拌後，再倒入通寧水即可。琴酒與通寧水的比例約為 1:2 到 1:3 皆可，可看個人喜好調整。檸檬汁也是可加可不加，通寧水偏甜時可以加入一些酸做調整。'
        send_text_message(event.reply_token, txt)
        self.go_back()
    # 馬丁尼 Martini
    def is_going_to_martini(self, event):
        text = event.message.text
        if text == '馬丁尼 Martini':
            return True
        return False

    def on_enter_martini(self, event):
        txt = '材料：1. 琴酒 45ml\n2. 不甜苦艾酒 15ml\n調製方法：\n將兩者與冰塊攪拌冷卻均勻後倒入馬丁尼杯中即可，裝飾可用橄欖或柑橘、檸檬皮噴附皮油。'
        send_text_message(event.reply_token, txt)
        self.go_back()
    # 內格羅尼 Negroni
    def is_going_to_nagroni(self, event):
        text = event.message.text
        if text == '內格羅尼 Negroni':
            return True
        return False

    def on_enter_nagroni(self, event):
        txt = '材料：1. 琴酒 30ml\n2. 金巴利 30ml\n3. 紅色苦艾酒 30ml\n調製方法：\n三種酒以 1:1:1 的比例用攪拌法調製，這就是一杯苦、甜、藥草、重酒感的調酒。'
        send_text_message(event.reply_token, txt)
        self.go_back()


# Vodka
    def is_going_to_vodka(self, event):
        text = event.message.text
        if text == "伏特加" or text == "Vodka" or text == "vodka":
            wine = "vodka"
            return True
        else:
            return False
    def on_enter_vodka(self, event):
        title = '請選擇您想要的調酒：'
        text = "請從以下四種選一種"
        action = [
            MessageTemplateAction(
                label = '螺絲起子 Screwdriver',
                text ='螺絲起子 Screwdriver'
            ),
            MessageTemplateAction(
                label = '伏特加萊姆 Vodka Lime',
                text = '伏特加萊姆 Vodka Lime'
            ),
            MessageTemplateAction(
                label = '莫斯科騾子 Moscow Mule',
                text = '莫斯科騾子 Moscow Mule'
            ),
            MessageTemplateAction(
                label = '伏特加馬丁尼 Vodka Martini',
                text = '伏特加馬丁尼 Vodka Martini'
            ),
        ]
        url = 'https://i.imgur.com/JZIYuN2.jpg'
        send_button_message(event.reply_token, title, text, action, url)
    # https://mf.techbang.com/posts/10662-7-at-home-can-do-ultra-simple-vodka-bartender-wine-fresh-people-can-quickly-get-started
    # 螺絲起子 Screwdriver
    def is_going_to_screwdriver(self, event):
        text = event.message.text
        if text == '螺絲起子 Screwdriver':
            return True
        return False

    def on_enter_screwdriver(self, event):
        txt = '材料：1. 伏特加 50ml\n2. 柳橙汁 100ml（也可按照自己的口味做調整，推薦1:4）\n調製方法：\n將所有材料倒入裝6分滿冰塊的杯中，攪拌均勻。'
        send_text_message(event.reply_token, txt)
        self.go_back()
    # 伏特加萊姆 Vodka Lim
    def is_going_to_vodka_lime(self, event):
        text = event.message.text
        if text == '伏特加萊姆 Vodka Lime':
            return True
        return False

    def on_enter_vodka_lime(self, event):
        txt = '材料：1. 伏特加 30ml\n2. 萊姆汁 15ml\n3. 鹽巴適量\n4. 檸檬片或檸檬角少許\n調製方法：\n1. 切一檸檬薄片沾濕杯口一圈，以滾動方式將杯口均勻沾上一圈鹽巴\n2. 將剛剛的酒杯裝入六分滿冰塊\n3. 將伏特加與萊姆汁倒入後攪拌\n4. 以檸檬片裝飾。'
        send_text_message(event.reply_token, txt)
        self.go_back()
    
    # 莫斯科騾子 Moscow Mule
    def is_going_to_moscow_mule(self, event):
        text = event.message.text
        if text == '莫斯科騾子 Moscow Mule':
            return True
        return False

    def on_enter_moscow_mule(self, event):
        txt = '材料：1. 伏特加 2oz\n2. 檸檬汁 半顆的量\n3. 糖適量\n4. 薑汁啤酒或汽水\n調製方法：\n在雪克杯中加入糖、伏特加、檸檬汁，加冰塊後搖勻，最後倒入薑汁汽水，再放個檸檬片裝飾。'
        send_text_message(event.reply_token, txt)
        self.go_back()

    # 伏特加馬丁尼 Vodka Martini
    def is_going_to_vodka_martini(self, event):
        text = event.message.text
        if text == '伏特加馬丁尼 Vodka Martini':
            return True
        return False

    def on_enter_vodka_martini(self, event):
        txt = '材料：1. 伏特加 45ml\n2. 苦艾酒 15ml\n3. 冰塊適量\n調製方法：\n在雪克杯中加入伏特加、苦艾酒，加冰塊後搖勻，倒入馬丁尼杯，用檸檬皮peal後，最後將檸檬皮沈入杯底。'
        send_text_message(event.reply_token, txt)
        self.go_back()
        
# Rum
    def is_going_to_rum(self, event):
        text = event.message.text
        if text == "萊姆酒" or text == "Rum" or text == "rum":
            wine = "rum"
            return True
        else:
            return False
    def on_enter_rum(self, event):
        title = '請選擇您想要的調酒：'
        text = "請從以下三種選一種"
        action = [
            MessageTemplateAction(
                label = '莫西多 Mojito',
                text ='莫西多 Mojito'
            ),
            MessageTemplateAction(
                label = '自由古巴 Cuba Libre',
                text = '自由古巴 Cuba Libre'
            ),
            MessageTemplateAction(
                label = '藍色夏威夷 Blue Hawaii',
                text = '藍色夏威夷 Blue Hawaii'
            ),
        ]
        url = 'https://i.imgur.com/0yeeYr9.jpg'
        send_button_message(event.reply_token, title, text, action, url)
    # https://mf.techbang.com/posts/11317-a-must-have-drink-for-a-summer-party-7-lamb-bartender-diy-recommendations-at-home-you-can-enjoy-the-tropical-style
    # 莫西多 Mojito
    def is_going_to_mojito(self, event):
        text = event.message.text
        if text == '莫西多 Mojito':
            return True
        return False

    def on_enter_mojito(self, event):
        txt = '材料：1. 薄荷葉 數片\n2. 白萊姆酒 45ml\n3. 檸檬汁 半顆的量\n4. 糖或糖漿 30ml\n5. 蘇打水\n調製方法：\n選一個長玻璃杯或啤酒杯，把薄荷葉、糖、檸檬切片（或檸檸汁）倒入杯中，拿隻搗棒，在不破壞杯子的情況下盡你所能把杯中物品搗爛混合，之後加入大量碎冰填滿杯子、倒入蘭姆酒，再加入一些蘇打水倒至滿杯。'
        send_text_message(event.reply_token, txt)
        self.go_back()
    # 自由古巴 Cuba Libre
    def is_going_to_cuba_libre(self, event):
        text = event.message.text
        if text == '莫西多 Mojito':
            return True
        return False

    def on_enter_cuba_libre(self, event):
        txt = '材料：1. 白萊姆酒 50ml\n2. 可樂 120ml\n3. 新鮮萊姆汁 10ml\n調製方法：\n將蘭姆酒、萊姆汁與冰塊一同放入高球杯中稍加攪拌，再倒入可樂即可。'
        send_text_message(event.reply_token, txt)
        self.go_back()
    # 藍色夏威夷 Blue Hawaii
    def is_going_to_blue_hawaii(self, event):
        text = event.message.text
        if text == '莫西多 Mojito':
            return True
        return False

    def on_enter_blue_hawaii(self, event):
        txt = '材料：1. 白萊姆酒 45ml\n2. 伏特加 15ml\n3. 藍柑橘香甜酒 15ml\n4. 現榨鳳梨汁 45ml\n5. 現榨萊姆汁 15ml\n6. 糖漿 1tsp\n調製方法：\n1. 冰鎮颶風杯。\n2. 雪克杯加入所有材料及冰塊，搖盪均勻。\n3. 將酒液倒入冰鎮過的颶風杯，加入冰塊至滿杯。'
        send_text_message(event.reply_token, txt)
        self.go_back()

# Tequila
    def is_going_to_tequila(self, event):
        text = event.message.text
        if text == "龍舌蘭" or text == "Tequila" or text == 'tequila':
            return True
        else:
            return False
    def on_enter_tequila(self, event):
        title = '請選擇您想要的調酒：'
        text = "請從以下三種選一種"
        action = [
            MessageTemplateAction(
                label = '瑪格麗特 Margarita',
                text ='瑪格麗特 Margarita'
            ),
            MessageTemplateAction(
                label = '龍舌蘭日出 Tequila Sunrise',
                text = '龍舌蘭日出 Tequila Sunrise'
            ),
            MessageTemplateAction(
                label = '迪亞布羅 El Diablo',
                text = '迪亞布羅 El Diablo'
            ),
        ]
        url = 'https://i.imgur.com/fJCTIJs.png'
        send_button_message(event.reply_token, title, text, action, url)
    # https://www.1shot.tw/14069/%E8%AA%BF%E9%85%92%E7%9F%A5%E8%AD%98-%E9%BE%8D%E8%88%8C%E8%98%AD%E5%85%A5%E9%96%80-%E5%9B%9B%E6%AC%BE%E9%BE%8D%E8%88%8C%E8%98%AD%E7%B6%93%E5%85%B8%E8%AA%BF%E9%85%92%E5%9C%A8%E5%AE%B6%E5%81%9A
    # 瑪格麗特 Margarita
    def is_going_to_margarita(self, event):
        text = event.message.text
        if text == '瑪格麗特 Margarita':
            return True
        return False

    def on_enter_margarita(self, event):
        txt = '材料：1. 龍舌蘭 30ml\n2. 橙酒 20ml\n3. 現榨萊姆汁 15ml\n調製方法：\n1. 將材料放入雪克杯搖勻。\n2. 將雞尾酒杯杯沿用檸檬片沾濕並沾上一層薄鹽。\n3. 將酒液倒入杯中。'
        send_text_message(event.reply_token, txt)
        self.go_back()

    # 龍舌蘭日出 Tequila Sunrise
    def is_going_to_tequila_sunrise(self, event):
        text = event.message.text
        if text == '龍舌蘭日出 Tequila Sunrise':
            return True
        return False

    def on_enter_tequila_sunrise(self, event):
        txt = '材料：1. 龍舌蘭 45ml\n2. 橙汁 90ml\n3. 紅石榴糖漿 15ml\n調製方法：\n將 1：2 的龍舌蘭和柳橙汁加入杯中和冰塊攪拌均勻，最後再加入少許紅石榴糖漿即可。'
        send_text_message(event.reply_token, txt)
        self.go_back()
    
    # 迪亞布羅 El Diablo
    def is_going_to_diablo(self, event):
        text = event.message.text
        if text == '迪亞布羅 El Diablo':
            return True
        return False

    def on_enter_diablo(self, event):
        txt = '材料：1. 龍舌蘭 45ml\n2. 檸檬汁 15ml\n3. 黑醋栗利口酒 15ml\n4. 薑汁汽水 60-90ml\n調製方法：\n調製方法是先將除了薑汁汽水外的材料，與冰塊放入雪克杯中搖盪均勻，倒入裝滿冰的高球杯後，補上薑汁汽水即可。'
        send_text_message(event.reply_token, txt)
        self.go_back()

# Brandy
    def is_going_to_brandy(self, event):
        text = event.message.text
        if text == "白蘭地" or text == "Brandy" or text == 'brandy':
            wine = "brandy"
            return True
        else:
            return False
    def on_enter_brandy(self, event):
        title = '請選擇您想要的調酒：'
        text = "請從以下四種選一種"
        action = [
            MessageTemplateAction(
                label = '白蘭地亞歷山大 Brandy Alexander',
                text ='白蘭地亞歷山大 Brandy Alexander'
            ),
            MessageTemplateAction(
                label = '床笫之間 Between the sheets',
                text = '床笫之間 Between the sheets'
            ),
            MessageTemplateAction(
                label = '老廣場 Vieux Carre',
                text = '老廣場 Vieux Carre'
            ),
            MessageTemplateAction(
                label = "馬頸 Horse's Neck",
                text = "馬頸 Horse's Neck"
            ),
        ]
        url = 'https://i.imgur.com/LcvMYQV.png'
        send_button_message(event.reply_token, title, text, action, url)
    # 白蘭地亞歷山大 Brandy Alexander
    def is_going_to_brandy_alexander(self, event):
        text = event.message.text
        if text == '白蘭地亞歷山大 Brandy Alexander':
            return True
        return False

    def on_enter_brandy_alexander(self, event):
        txt = '材料：1. 白蘭地 40ml\n2. 深色可可香甜酒 20ml\n3. 奶水 20ml\n4. 荳蔻粉 少許\n調製方法：\n1. 搖酒器裝入八分滿冰塊，倒入白蘭地、奶水與可可酒後搖勻。\n2. 過濾冰塊後倒入冰鎮好的酒杯。\n3. 撒上一點點荳蔻粉。'
        send_text_message(event.reply_token, txt)
        self.go_back()
    # 床笫之間 Between the sheets
    def is_going_to_between_the_sheets(self, event):
        text = event.message.text
        if text == '床笫之間 Between the sheets':
            return True
        return False

    def on_enter_between_the_sheets(self, event):
        txt = '材料：1. 白蘭地 30ml\n2. 白萊姆酒 30ml\n3. 君度橙酒 30ml\n4. 檸檬汁 15ml\n調製方法：\n加冰塊搖盪均勻，濾掉冰塊將酒液倒入雞尾酒杯中，以檸檬皮捲作為裝飾。'
        send_text_message(event.reply_token, txt)
        self.go_back()
    # 老廣場 Vieux Carre
    def is_going_to_vieux_carre(self, event):
        text = event.message.text
        if text == '老廣場 Vieux Carre':
            return True
        return False

    def on_enter_vieux_carre(self, event):
        txt = '材料：1. 白蘭地 22.5ml\n2. 裸麥威士忌 22.5ml\n3. 紅色苦艾酒 22.5ml\n4. 班尼迪克汀 1匙\n5. 安格仕苦精 1 dash\n6. 裴喬（Peychaud’s）苦精 1 dash\n調製方法：\n以攪拌法調製，倒入裝有冰塊的古典杯中，最後還有加上一點的班尼迪克汀。'
        send_text_message(event.reply_token, txt)
        self.go_back()
    # 馬頸 Horse's Neck
    def is_going_to_horse_neck(self, event):
        text = event.message.text
        if text == "馬頸 Horse's Neck":
            return True
        return False

    def on_enter_horse_neck(self, event):
        txt = '材料：1. 干邑白蘭地 60ml\n2. 薑汁汽水 120ml\n3. 檸檬皮少許\n調製方法：\n事先切削整顆檸檬的外皮，以連續不斷的方式削下形成一旋轉長條的檸檬皮，先放入杯中後，再加入冰塊、倒入白蘭地，最後加入薑汁啤酒，稍微攪拌一下即完成。'
        send_text_message(event.reply_token, txt)
        self.go_back()

# Whisky
    def is_going_to_whisky(self, event):
        text = event.message.text
        if text == "威士忌" or text == "Whisky" or text == "whisky":
            wine = "whisky"
            return True
        else:
            return False
    def on_enter_whisky(self, event):
        title = '請選擇您想要的調酒：'
        text = "請從以下四種選一種"
        action = [
            MessageTemplateAction(
                label = '教父 Godfather',
                text ='教父 Godfather'
            ),
            MessageTemplateAction(
                label = '威士忌蘇打 Highball',
                text = '威士忌蘇打 Highball'
            ),
            MessageTemplateAction(
                label = '曼哈頓 Manhattan',
                text = '曼哈頓 Manhattan'
            ),
            MessageTemplateAction(
                label = "威士忌酸 Whisky Sour",
                text = "威士忌酸 Whisky Sour"
            ),
        ]
        url = 'https://i.imgur.com/mRzjold.jpg'
        send_button_message(event.reply_token, title, text, action, url)
    # 教父 Godfather
    def is_going_to_godfather(self, event):
        text = event.message.text
        if text == "教父 Godfather":
            return True
        return False

    def on_enter_godfather(self, event):
        txt = '材料：1. 蘇格蘭威士忌 35ml\n2. 義大利苦艾酒 35ml\n調製方法：\n將材料倒入已放好冰塊的杯中，攪拌均勻。'
        send_text_message(event.reply_token, txt)  
        self.go_back()
    # 威士忌蘇打 Highball
    def is_going_to_highball(self, event):
        text = event.message.text
        if text == "威士忌蘇打 Highball":
            return True
        return False

    def on_enter_highball(self, event):
        txt = '材料：1. 威士忌 30-45ml\n2. 蘇打水適量\n3. 檸檬角適量\n調製方法：\n將威士忌加入裝滿冰塊的高球杯中，蘇打水加滿後輕輕攪拌即可。（可輕輕擠壓檸檬角後丟入杯中，增添風味）'
        send_text_message(event.reply_token, txt) 
        self.go_back()
    # 曼哈頓 Manhattan
    def is_going_to_manhattan(self, event):
        text = event.message.text
        if text == "曼哈頓 Manhattan":
            return True
        return False

    def on_enter_manhattan(self, event):
        txt = '材料：1. 裸麥威士忌(波本亦可) 50ml\n2. 甜紅威末酒 20ml\n3. 苦精少許\n調製方法：\n材料充分攪拌冰鎮後倒入雞尾酒杯，雞尾酒杯以櫻桃裝飾。'
        send_text_message(event.reply_token, txt)   
        self.go_back() 
    # 威士忌酸 Whisky Sour
    def is_going_to_whisky_sour(self, event):
        text = event.message.text
        if text == "威士忌酸 Whisky Sour":
            return True
        return False

    def on_enter_whisky_sour(self, event):
        txt = '材料：1. 波本威士忌 45ml\n2. 檸檬汁 30ml\n3. 糖漿 15ml\n調製方法：\n在調酒壺中加入冰塊，把所有成份倒入其中，搖勻後倒入冰鎮的雞尾酒杯，再用加以裝飾。'
        send_text_message(event.reply_token, txt)     
        self.go_back()    
     

    
