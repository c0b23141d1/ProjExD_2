import os
import random
import sys
import pygame as pg


WIDTH, HEIGHT = 1100, 650
DELTA ={
    pg.K_UP: (0.-5),
    pg.K_DOWN: (0,+5),
    pg.K_LEFT: (-5,0),
    pg.K_RIGHT: (+5,0),
    }
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("fig/pg_bg.jpg") #背景画像read
    kk_img = pg.transform.rotozoom(pg.image.load("fig/3.png"), 0, 0.9)
    kk_rct = kk_img.get_rect() 
    kk_rct.center = 300, 200
    bd_img = pg.Surface((20,20))
    bd_img.set_colorkey((0,0,0))  #四隅の四角を取り除く
    pg.draw.circle(bd_img,(255,0,0),(10,10),10)
    bd_rct = bd_img.get_rect()  #爆弾rectの抽出
    bd_rct.centerx = random.randint(0,WIDTH)
    bd_rct.centery = random.randint(0,HEIGHT)
    vx,vy = +5,+5  #爆弾の速度
    #bd_img.set_colorkey((0,0,0))


    clock = pg.time.Clock()
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        screen.blit(bg_img, [0, 0])  # 背景画像貼り付け

        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]  # 横、縦
        # if key_lst[pg.K_UP]:
        #     sum_mv[1] -= 5
        # if key_lst[pg.K_DOWN]:
        #     sum_mv[1] += 5
        # if key_lst[pg.K_LEFT]:
        #     sum_mv[0] -= 5
        # if key_lst[pg.K_RIGHT]:
        #     sum_mv[0] += 5
        for key,tpl in DELTA.items():
            if key_lst[key]:
                sum_mv[0] += tpl[0]  # 横方向
                sum_mv[1] += tpl[1]  # 縦方向
        kk_rct.move_ip(sum_mv)
        screen.blit(kk_img, kk_rct)  # kk_retに基づいた場所に
        bd_rct.move_ip(vx,vy)
        screen.blit(bd_img, bd_rct)  # kk_retに基づいた場所に
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
