import pygame, random, re
str_mensagem = ''
str_bolo = ''
user_text = ''
bolo_text = []

def gerar_bolo():
    #  [ Massa, Recheio, Cobertura ]
    global str_bolo
    global str_mensagem
    global user_text
    global bolo_text
    bolo_text = []
    str_mensagem = ''
    user_text = ''
    bolo = []
    bolo.append(random.randint(1, 4))
    bolo.append(random.randint(1, 4))
    bolo.append(random.randint(1, 4))
    str_bolo = 'M'+str(bolo[0])+'R'+str(bolo[1])+'C'+str(bolo[2])
    return bolo

def desenhar_bolo_text():
    global bolo_text
    str_end = 'sprites/'
    box = (114, 418)
    for i in range(0,len(user_text)-1,2):
        sub = user_text[i:i+2]
        print(sub)
        # print(len(user_text))
        match sub[0]:
            case 'M':
                str_end = str_end + 'Massas/' + str(sub[1]) + '.png'
            case 'R':
                str_end = str_end + 'Recheios/' + str(sub[1]) + '.png'
            case 'C':
                str_end = str_end + 'Coberturas/' + str(sub[1]) + '.png'
        image = pygame.image.load(str_end)
        bolo_text.append((image, box))
        str_end = 'sprites/'


def desenhar_bolo(surface, bolo):
    str_end = 'sprites/'  
    str_massa = str_end + 'Massas/' + str(bolo[0]) + '.png'
    str_recheio = str_end + 'Recheios/' + str(bolo[1]) + '.png'
    str_cobertura = str_end + 'Coberturas/' + str(bolo[2]) + '.png'
    
    massa = pygame.image.load(str_massa)
    recheio = pygame.image.load(str_recheio)
    cobertura = pygame.image.load(str_cobertura)
    surface.blits(((massa, (114,133)),(recheio, (114,133)),(cobertura, (114,133))))

def checar_bolo(surface):
    global user_text
    global str_mensagem
    global str_bolo
    str_mensagem = ""
    pattern = re.compile('([MCR][1-4])+')
    if(bool(pattern.fullmatch(user_text.replace(" ", "")))):
        desenhar_bolo_text()
        if(user_text.replace(" ", "")==str_bolo):
            str_mensagem = "Parabéns, você acertou!"
        else:
            str_mensagem = "Você errou. Tente novamente"
    else:
        str_mensagem = "Inválido. Observe os valores na tabela."

def main():
    global str_bolo
    global str_mensagem
    global user_text
    global bolo_text
    bolo = gerar_bolo()
    pygame.init() 
    
    width = 1000
    height = 900
    dimensions = [width,height] 
    screen_display = pygame.display 
    screen_display.set_caption('CakeBuilder') 
    
    surface = screen_display.set_mode(dimensions)
    background = pygame.image.load('sprites/UI/background.png')
    grid = pygame.image.load('sprites/UI/grid.png')
    button_gerar = pygame.image.load('sprites/UI/gerar.png')
    button_pronto = pygame.image.load('sprites/UI/pronto.png')
    
    base_font = pygame.font.Font('RetroGaming.ttf', 32) 
    small_font = pygame.font.Font('RetroGaming.ttf', 16) 
    running = True
    while running: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if pygame.Rect(100, 80, 95, 40).collidepoint(pos):
                    bolo = gerar_bolo()
                    print(str_bolo)
                if pygame.Rect(870, 842, 95, 40).collidepoint(pos):
                    checar_bolo(surface)
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_BACKSPACE: 
                    user_text = user_text[:-1] 
                elif event.key != pygame.K_ESCAPE and event.key != pygame.K_SPACE and event.key != pygame.K_RETURN : 
                    user_text += event.unicode
                    
        text_surface = base_font.render(user_text, True, (0, 0, 0)) 
        msg_surface = small_font.render(str_mensagem, True, (0, 0, 0)) 
        surface.blit(background,(0,0)) 
        surface.blit(grid, (450,100))
        surface.blit(button_gerar, (100,80))
        surface.blit(button_pronto, (870,842))
        desenhar_bolo(surface, bolo)
        surface.blit(text_surface, (30, 843))            
        surface.blit(msg_surface, (30, 790))       
        if len(bolo_text)!=0:     
            surface.blits(bolo_text)   
        screen_display.update() 
    
    pygame.quit() 

if __name__ == "__main__":
    main()