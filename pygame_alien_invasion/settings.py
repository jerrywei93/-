class Settings:
    """
    存储游戏《外星人入侵》中所有设置的类
    """
    def __init__(self):
        """
        初始化游戏设置
        """
        # 屏幕设置
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (248, 248, 248)

        # 飞船移动速度
        self.ship_speed = 1.5

        # 子弹设置
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

        # 最大子弹数量
        self.bullets_allowed = 6
        
        # 外星人设置
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction为1表示向右移，为-1表示向左移
        self.fleet_direction = 1