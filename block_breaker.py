from typing import Any
import pygame as pg
import sys
WIDTH, HEIGHT = 1600, 900
class Block(pg.sprite.Sprite):
    """
    ブロックに関するクラス
    """
    def __init__(self,width:int,height:int,x:int,y:int):
        super().__init__()
        self.img = pg.Surface((width, height))
        self.img.fill((255, 255, 255))  # 白色で塗りつぶす
        self.rect = self.img.get_rect()
        self.rect.center = x,y
    def update(self,screen: pg.Surface):
        screen.blit(self.img,self.rect)


class Bar(pg.sprite.Sprite):
    """
    バーに関するクラス
    """
    delta = {
        pg.K_LEFT: -1,
        pg.K_RIGHT: +1,
    }
    def __init__(self, xy: tuple[int, int]) -> None:
        """
        プレイヤーが操作するバーを描画
        引数1 x: バーのx座標
        引数2 y: バーのy座標
        """
        self.width = WIDTH/5
        self.height = HEIGHT/20
        self.wid_dec = 0
        self.width -= self.wid_dec
        self.speed = 10
        color = (255, 255, 255)
        self.rect = self.image.get_rect()
        self.image = pg.Surface((self.width, self.height))
        pg.draw.rect(self.image, color, (xy[0], xy[1], self.width, self.height))
    
    def update(self, key_lst: list[bool], screen: pg.Surface):
        """
        押下キーに応じてバーを移動させる
        引数1 key_lst：押下キーの真理値リスト
        引数2 screen：画面Surface
        """
        if self.rect.left >= 0 or WIDTH > self.rect.right:
            for k, mv in __class__.delta.items():
                if key_lst[k]:
                    self.rect.move_ip(+self.speed*mv, 0)


def main():
    pg.display.set_caption("ブロック崩し改")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    blocks = pg.sprite.Group()
    ball = pg.sprite.Group()
    
    # 初期ブロックの追加
    for i in range(1,10):
        for j in range(1,10):
            blocks.add(Block(100, 25,200+(110*i),100+(30*j)))
    
    while True:
        key_lst = pg.key.get_pressed()
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return 0

        # ブロックの更新と描画
        blocks.update(screen)
        
        # 画面の更新
        pg.display.flip()
if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()