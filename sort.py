from settings import *
import time
import random

pygame.mixer.init(44100,-16,2,4096)

testArray = [2,5,4,3,6,1]
class Sorts():
    def __init__(self,size):
        self.sortType = ""
        self.size = size
        self.barSize = WIDTH // self.size
        self.sound = pygame.mixer.Sound("audio/blipSelect.wav")
        self.sound.set_volume(0.3)
        self.text = font.render("Choose Sort", True, "#ecf0f1")
        self.textRect = self.text.get_rect(center = (WIDTH//2,HEIGHT + BOTMARGIN // 2))
        self.pause = False


    def changeText(self,text):
        self.text = font.render(text, True, "#ecf0f1")
        self.textRect = self.text.get_rect(center = (WIDTH//2,HEIGHT + BOTMARGIN // 2))

    def createRandomArray(self):
        array = []
        for i in range(self.size):
            array.append(i + 1)

        random.shuffle(array)
        return array

    def display(self):
        screen.blit(self.text,self.textRect)
        selectionSort.display()
        insertionSort.display()
        shellSort.display()
        bubbleSort.display()

class SelectionSort(Sorts):
    def __init__(self,type):
        super().__init__(size)
        self.type = type
        self.array = self.createRandomArray()
        self.i = 0
        self.j = 0
        self.minIndex = None

    def reset(self):
        self.array = self.createRandomArray()
        self.i = 0
        self.j = 0
        self.minIndex = self.i
        self.sound.play()


    def update(self):
        if self.i < len(self.array) - 1:
            if self.array[self.j] < self.array[self.minIndex]:
                self.minIndex = self.j

            if self.j >= len(self.array) - 1:
                (self.array[self.i], self.array[self.minIndex]) = (self.array[self.minIndex], self.array[self.i])
                self.sound.play()
                self.i += 1
                self.minIndex = self.i
                self.j = self.i

            self.j += 1

        else:
            self.i += 1
            self.minIndex = None
            if self.i > len(self.array) + FPS:
                sort.changeText("Choose Sort")
                sort.sortType = ""


    def display(self):
        if sort.sortType == self.type:
            self.update()
            for i in range(len(self.array)):
                if i == self.i:
                    pygame.draw.rect(screen, "#e74c3c", (
                    i * self.barSize, HEIGHT - self.barSize * self.array[i], self.barSize,
                    self.barSize * self.array[i]))
                elif i == self.j:
                    pygame.draw.rect(screen, "#2ecc71", (
                    i * self.barSize, HEIGHT - self.barSize * self.array[i], self.barSize,
                    self.barSize * self.array[i]))
                elif i == self.minIndex:
                    pygame.draw.rect(screen, "#3498db", (
                        i * self.barSize, HEIGHT - self.barSize * self.array[i], self.barSize,
                        self.barSize * self.array[i]))
                else:
                    pygame.draw.rect(screen,"#b2bec3",(i * self.barSize,HEIGHT - self.barSize * self.array[i],self.barSize,self.barSize * self.array[i]))

class InsertionSort(Sorts):
    def __init__(self,type):
        super().__init__(size)
        self.type = type
        self.array = self.createRandomArray()
        self.i = 1
        self.j = 0
        self.temp = 0

    def reset(self):
        self.array = self.createRandomArray()
        self.i = 1
        self.j = self.i - 1
        self.temp = self.array[self.i]

    def update(self):
        if self.i < len(self.array):
            if self.j >= 0 and self.temp < self.array[self.j]:
                self.array[self.j + 1] = self.array[self.j]
                self.j -= 1
            else:
                self.sound.play()
                self.array[self.j + 1] = self.temp
                self.i += 1
                self.j = self.i - 1
                if self.i < len(self.array):
                    self.temp = self.array[self.i]
        else:
            self.i += 1
            self.j = None
            if self.i > len(self.array) + FPS:
                sort.changeText("Choose Sort")
                sort.sortType = ""

    def display(self):
        if sort.sortType == self.type:
            self.update()
            for i in range(len(self.array)):
                if i == self.i:
                    pygame.draw.rect(screen, "#e74c3c", (
                    i * self.barSize, HEIGHT - self.barSize * self.array[i], self.barSize,
                    self.barSize * self.array[i]))
                elif i == self.j:
                    pygame.draw.rect(screen, "#2ecc71", (
                    i * self.barSize, HEIGHT - self.barSize * self.array[i], self.barSize,
                    self.barSize * self.array[i]))
                else:
                    pygame.draw.rect(screen,"#b2bec3",(i * self.barSize,HEIGHT - self.barSize * self.array[i],self.barSize,self.barSize * self.array[i]))

class ShellSort(Sorts):
    def __init__(self,type):
        super().__init__(size)
        self.type = type
        self.array = self.createRandomArray()
        self.array = testArray
        self.gap = len(self.array) // 2
        self.i = self.gap
        self.j = self.i
        self.temp = self.array[self.i]

    def reset(self):
        self.array = self.createRandomArray()
        self.gap = len(self.array) // 2
        self.i = self.gap
        self.j = self.i
        self.temp = self.array[self.i]

    def update(self):
        if self.gap > 0:
            if self.i < len(self.array):
                if self.j >= self.gap and self.array[self.j - self.gap] > self.temp:
                    self.sound.play()
                    self.array[self.j] = self.array[self.j - self.gap]
                    self.j -= self.gap

                else:
                    self.array[self.j] = self.temp
                    self.i += 1
                    self.j = self.i
                    if self.i < len(self.array):
                        self.temp = self.array[self.i]
            else:
                self.gap = self.gap // 2
                self.i = self.gap
                self.j = self.i
                self.temp = self.array[self.i]

        else:
            self.i -= 1
            self.j = None
            self.temp = None
            if self.i < -(len(self.array) + FPS):
                sort.changeText("Choose Sort")
                sort.sortType = ""

    def display(self):
        if sort.sortType == self.type:
            if not sort.pause:
                self.update()
            for i in range(len(self.array)):
                if i == self.i:
                    pygame.draw.rect(screen, "#e74c3c", (
                    i * self.barSize, HEIGHT - self.barSize * self.array[i], self.barSize,
                    self.barSize * self.array[i]))
                elif i == self.j:
                    pygame.draw.rect(screen, "#2ecc71", (
                    i * self.barSize, HEIGHT - self.barSize * self.array[i], self.barSize,
                    self.barSize * self.array[i]))
                elif i == self.temp:
                    pygame.draw.rect(screen, "#3498db", (
                    i * self.barSize, HEIGHT - self.barSize * self.array[i], self.barSize,
                    self.barSize * self.array[i]))
                else:
                    pygame.draw.rect(screen,"#b2bec3",(i * self.barSize,HEIGHT - self.barSize * self.array[i],self.barSize,self.barSize * self.array[i]))

class BubbleSort(Sorts):
    def __init__(self,type):
        super().__init__(size)
        self.type = type
        self.array = self.createRandomArray()
        self.i = 0
        self.j = 0
        self.swapped = False

    def reset(self):
        self.array = self.createRandomArray()
        self.i = 0
        self.j = 0
        self.swapped = False
        self.sound.play()

    def update(self):
        if self.i < len(self.array) - 1:
            if self.j < len(self.array)-self.i-1:
                if self.array[self.j] > self.array[self.j + 1]:
                    self.array[self.j], self.array[self.j + 1] = self.array[self.j + 1], self.array[self.j]
                    self.sound.play()
                    self.swapped = True
                self.j += 1
            else:
                if self.swapped == False:
                    self.i = len(self.array)

                else:
                    self.swapped = False
                    self.j = 0
                    self.i += 1
        else:
            self.i += 1
            self.j = None
            self.swapped = False
            if self.i > len(self.array) + FPS:
                sort.changeText("Choose Sort")
                sort.sortType = ""

    def display(self):
        if sort.sortType == self.type:
            self.update()
            for i in range(len(self.array)):
                if i == self.j:
                    pygame.draw.rect(screen, "#2ecc71", (
                    i * self.barSize, HEIGHT - self.barSize * self.array[i], self.barSize,
                    self.barSize * self.array[i]))
                else:
                    pygame.draw.rect(screen,"#b2bec3",(i * self.barSize,HEIGHT - self.barSize * self.array[i],self.barSize,self.barSize * self.array[i]))

def bubbleSort(array):
    for i in range(len(array)-1):
        swapped = False
        for j in range(len(array)-i-1):
            if array[j] > array[j + 1]:
                swapped = True
                array[j],array[j+1] = array[j+1],array[j]

        if not swapped:
            return array

    return array


size = 50
sort = Sorts(size)
selectionSort = SelectionSort("selectionSort")
insertionSort = InsertionSort("insertionSort")
shellSort = ShellSort("shellSort")
bubbleSort = BubbleSort("bubbleSort")

