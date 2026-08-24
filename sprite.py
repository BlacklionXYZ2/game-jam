import pygame

class Sprite:
    def __init__(self, sheet, width, height, animation_frame_lengths, animation_time_periods, start_animation):
        self.frame_count=0
        self.animation_num=start_animation
        self.animations=[]
        self.sheet=pygame.image.load("textures/"+sheet).convert_alpha()
        self.width=width
        self.height=height
        self.animation_frame_lengths=animation_frame_lengths
        self.animation_time_periods=animation_time_periods
        self.count=0
        self.load()

    def load_frame(self, x, y):
        img=pygame.Surface((self.width, self.height)).convert_alpha()
        img.blit(self.sheet, (0, 0), (x*self.width, y*self.height, self.width, self.height))
        return img

    def load_animation(self, num):
        length=self.animation_frame_lengths[num]
        animation=[]
        for i in range(length):
            animation.append(self.load_frame(i, num))
        return animation

    def load(self):
        for i in range(len(self.animation_frame_lengths)):
            if self.animation_frame_lengths[i]!=0:
                self.animations.append(self.load_animation(i))
    
    def next_frame(self):
        self.frame_count+=1
        self.frame_count%=len(self.animations[self.animation_num])

    def change_animation(self, new_animation_num):
        self.animation_num=new_animation_num%len(self.animations)
        self.count=0
        self.frame_count=0

    def change_frame(self, new_frame_num):
        self.frame_count=new_frame_num

    def update(self):
        if self.animation_time_periods[self.animation_num]-1==self.count:
            self.next_frame()
        self.count+=1
        self.count%=self.animation_time_periods[self.animation_num]

    def draw(self, screen, pos, scale):
        img=self.animations[self.animation_num][self.frame_count]
        img=pygame.transform.scale(img, (self.width*scale, self.height*scale))
        img.set_colorkey((0, 0, 0))
        screen.blit(img, pos)
