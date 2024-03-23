from settings import *
from sort import *

def display():
    screen.fill("#636e72")
    sort.display()
    pygame.display.update()
    clock.tick(FPS)

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    sort.sortType = ""
                    sort.changeText("Choose Sort")
                if event.key == pygame.K_1 and sort.sortType == "":
                    selectionSort.reset()
                    sort.sortType = "selectionSort"
                    sort.changeText("Selection Sort")
                if event.key == pygame.K_2 and sort.sortType == "":
                    insertionSort.reset()
                    sort.sortType = "insertionSort"
                    sort.changeText("Insertion Sort")
                if event.key == pygame.K_3 and sort.sortType == "":
                    shellSort.reset()
                    sort.sortType = "shellSort"
                    sort.changeText("Shell Sort")
                if event.key == pygame.K_4 and sort.sortType == "":
                    bubbleSort.reset()
                    sort.sortType = "bubbleSort"
                    sort.changeText("Bubble Sort")
                if event.key == pygame.K_p:
                    sort.pause = not sort.pause


        display()
    pygame.quit()

main()