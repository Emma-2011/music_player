import pygame
pygame.init()
sc = pygame.display.set_mode((300,250))
class Player():
    def __init__(self):
        self.bg = pygame.image.load("/Users/huangshitong/mxcmaterials/音乐播放器-bg-9d9442c2-e229-4f58-a160-77c824c2a620.png")
        self.pre_img = pygame.image.load("/Users/huangshitong/mxcmaterials/pre-b94007ff-262b-4882-b5af-298ba3150120.png")
        self.start_img = pygame.image.load("/Users/huangshitong/mxcmaterials/start-ba0eb1eb-4b72-4d98-b54c-32e4d36c8d9f.png")
        self.pause_img = pygame.image.load("/Users/huangshitong/mxcmaterials/pause-c8353465-701a-4885-8ac7-cfd292d7bef9.png")
        self.next_img = pygame.image.load("/Users/huangshitong/mxcmaterials/next-b91bef6d-2621-40f9-a92d-31d7f74364c4.png")
        self.ff_img = pygame.image.load("/Users/huangshitong/mxcmaterials/音乐播放器-ff-9520d735-916d-48f9-b8b0-d36d9d62e418.png")
        self.res_img = pygame.image.load("/Users/huangshitong/mxcmaterials/音乐播放器-res-49a9c2b8-bc24-40d1-95ba-53e1253ff241.png")
        self.rand_img = pygame.image.load("/Users/huangshitong/mxcmaterials/音乐播放器-rand-a87fe4b3-3bc5-497b-bf84-9200154199d7.png")
        
        self.song_list=["/Users/huangshitong/mxcmaterials/TheSpectre-82d10991-95bc-41f8-b069-a98c0d626625.mp3",
        "/Users/huangshitong/mxcmaterials/第一次告白-20552acb-f9db-4583-b898-007697c79b22.mp3",
        "/Users/huangshitong/mxcmaterials/勋章-5845618c-e81f-4247-b662-441858948529.mp3",
        "/Users/huangshitong/mxcmaterials/王者荣耀-1-6f7a8268-a768-47e0-9bef-4b906d020429.mp3"]
        self.index=0
        self.is_pause = True
        self.time=0
    def draw_player(self):
        sc.blit(self.bg,(0,0))
        sc.blit(self.pre_img,(20,90))
        sc.blit(self.next_img,(210,90))
        sc.blit(self.ff_img,(210,170))
        sc.blit(self.rand_img,(115,170))
        sc.blit(self.res_img,(20,170))
        if self.is_pause== True:
            sc.blit(self.start_img,(115,90))
        else:
            sc.blit(self.pause_img,(115,90))
        pygame.display.update()
    def unpause(self):
        self.is_pause = False
        song=self.song_list[self.index]
        pygame.mixer.music.load(song)
        pygame.mixer.music.set_volume(0.3)
        self.time+=pygame.mixer.music.get_pos()/1000
        pygame.mixer.music.play(1,0)
        pygame.mixer.music.unpause()
    def pause(self):
        self.is_pause = True
        pygame.mixer.music.pause()
    def next_song(self):
        self.index+=1
        if self.index >3:
            self.index=0
        self.unpause()
    def pre_song(self):
        self.index-=1
        if self.index <0:
            self.index=3
        self.unpause()
    def rand(self):
        self.index=random.randint(0,3)
        self.unpause()
    def res(self):
        self.time=0
        pygame.mixer.music.play(1,self.time)
    def ff(self):
        self.time+=10
        pygame.mixer.music.play(1,self.time)
        
player = Player()
while True:
    player.draw_player()
    mouse_x,mouse_y= pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            if 115<mouse_x<185 and 90<mouse_y<160:
                if player.is_pause==True:
                    player.unpause()
                else:
                    player.pause()
            if 20 <mouse_x<90 and 90<mouse_y<160:
                player.pre_song()
            if 210 <mouse_x<280 and 90<mouse_y<160:
                player.pre_song()
            if 115 <mouse_x<185 and 170<mouse_y<240:
                player.rand()
            if 210 <mouse_x<280 and 170<mouse_y<240:
                player.ff()
            if 20 <mouse_x<90 and 170<mouse_y<240:
                player.res()

input()
        
