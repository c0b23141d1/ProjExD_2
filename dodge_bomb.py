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


def check_bound(obj_rct: pg.Rect) -> tuple[bool,bool]:
    """
    引数：こうかとん　または爆弾のRect
    戻り値：真理値タプル　（横判定結果、縦判定結果)
    画面内ならTrue ,画面外ならFalse
    """
    yoko,tate = True,True
    if obj_rct.left < 0 or WIDTH < obj_rct.right:
        yoko = False
    if obj_rct.top < 0 or HEIGHT < obj_rct.bottom:
        tate = False
    return yoko,tate


def gameover(screen):
    ko_img = pg.transform.rotozoom(pg.image.load("fig/6.png"), 0, 0.9)
    ko_rct = ko_img.get_rect() 
    ko_rct.center = 300, 200
    go_img = pg.Surface((WIDTH,HEIGHT)) #　game overの四角
    pg.draw.rect(go_img, (0, 0, 0), pg.Rect(0,0,WIDTH,HEIGHT))
    go_rct = go_img.get_rect()  # 爆弾rectの抽出
    go_img.set_alpha(150)  # 0から255
    go_fonto = pg.font.Font(None,80) # フォント
    go_txt = go_fonto.render("GAME OVER",True,(255,255,255))
    #　こうかとんと爆弾が重なっていたら
    screen.blit(go_img,go_rct) 
    screen.blit(go_txt,[250,200])
    screen.blit(ko_img,ko_rct)
    pg.display.update()
    pg.time.wait(5000)
    return


def kakudai(tmr):
    avx = vx*bd_accs[min(tmr//500,9)]
    bd_img = bd_imgs[min(tmr//500,9)]
    return


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("fig/pg_bg.jpg") #背景画像read
    kk_img = pg.transform.rotozoom(pg.image.load("fig/3.png"), 0, 0.9)
    kk_rct = kk_img.get_rect() 
    kk_rct.center = 300, 200
    bd_img = pg.Surface((20,20))
    bd_img.set_colorkey((0,0,0))  # 四隅の四角を取り除く
    pg.draw.circle(bd_img,(255,0,0),(10,10),10)
    bd_rct = bd_img.get_rect()  # 爆弾rectの抽出
    bd_rct.centerx = random.randint(0, WIDTH)
    bd_rct.centery = random.randint(0, HEIGHT)
    vx,vy = +5,+5  # 爆弾の速度
    accs = [a for a in range(1,11)]  # 加速度のリスト
    clock = pg.time.Clock()
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
            
        screen.blit(bg_img, [0, 0])  # 背景画像貼り付け
        if kk_rct.colliderect(bd_rct):  
            gameover(screen)
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
        if check_bound(kk_rct) != (True,True):
            kk_rct.move_ip(-sum_mv[0], -sum_mv[1])
        screen.blit(kk_img, kk_rct)  # kk_retに基づいた場所に
        bd_rct.move_ip(vx,vy)
        yoko,tate = check_bound(bd_rct)
        if not yoko:
            vx *= -1
        if not tate:
            vy *= -1
        for r in range(1,11):  # 爆弾拡大,加速 
            bd_img = pg.Surface((20*r, 20*r))
            pg.draw.circle(bd_img,(255,0,0),(10*r, 10*r), 10*r)
            kakudai()

        screen.blit(bd_img, bd_rct)
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
