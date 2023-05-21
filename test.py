python
import pygame

pygame.init()

# Создаем окно размером 600 на 100 пикселей
size = (600, 100)
screen = pygame.display.set_mode(size)

# Создаем кнопки
button1 = pygame.Rect(50, 25, 100, 50)
button2 = pygame.Rect(200, 25, 100, 50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Проверяем, была ли нажата кнопка 1
            if button1.collidepoint(event.pos):
                print("Кнопка 1 нажата")
                # Здесь можно добавить код для управления комбайном
            # Проверяем, была ли нажата кнопка 2
            elif button2.collidepoint(event.pos):
                print("Кнопка 2 нажата")
                # Здесь можно добавить код для управления комбайном

    # Отрисовываем кнопки на экране
    pygame.draw.rect(screen, (255, 0, 0), button1)
    pygame.draw.rect(screen, (0, 255, 0), button2)

    # Обновляем экран
    pygame.display.flip()