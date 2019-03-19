import random
import PIL
from Stack import *
from PIL import Image
from PIL import ImageDraw


class cell:
    
    def __init__(self,coords):
        self.x = coords[0]
        self.y = coords[1]
        self.walls = [1,1,1,1]
        self.neighbours = []
        self.visited = False
        self.not_visited_neighbours = 0
    
    def __repr__(self):
        coords = str(self.x)+','+str(self.y)
        return repr(coords)
    
    def c(self):
        return (self.x,self.y)

class maze:
    
    def __init__(self):
        self.width = 0
        self.height = 0
        self.cells = []
        self.not_visited = -1
        
    def make_grid(self):
        for y in range(self.height):
            self.cells.append([])
            for x in range(self.width):
                temp = cell((x,y))
                if x-1>=0:
                    temp.neighbours.append((x-1, y))
                    temp.not_visited_neighbours += 1
                else:
                    temp.neighbours.append(None)
                if y-1>=0:
                    temp.neighbours.append((x, y-1))
                    temp.not_visited_neighbours += 1
                else:
                    temp.neighbours.append(None)
                if x+1<self.width:
                    temp.neighbours.append((x+1, y))
                    temp.not_visited_neighbours += 1
                else:
                    temp.neighbours.append(None)
                if y+1<self.height:
                    temp.neighbours.append((x, y+1))
                    temp.not_visited_neighbours += 1
                else:
                    temp.neighbours.append(None)
                self.cells[y].append(temp)
        self.not_visited = self.width*self.height
    
    def make_paths(self):
        path = Stack()
        current = self.cells[0][0]
        self.visit(0,0)
        path.push(current)
        while self.not_visited > 0:
            index = random.randint(0,3)
            if current.not_visited_neighbours>0:
                coords = current.neighbours[index]
                if coords is not None:
                    x = coords[0]
                    y = coords[1]
                    sequent = self.cells[y][x]
                    if not sequent.visited:
                        
                        if index>1:
                            other_index = index-2
                        else:
                            other_index = index+2
                        
                        current.walls[index] = 0
                        sequent.walls[other_index] = 0
                        self.visit(x,y)
                        path.push(current)
                        current = sequent
                    else:
                        continue
                else:
                    continue
            while current.not_visited_neighbours == 0 and self.not_visited > 0:
                current = path.pop().data
            continue
            
    def visit(self,x,y):
        cell = self.cells[y][x]
        cell.visited = True
        self.not_visited -= 1
        for x in cell.neighbours:
            if x is not None:
                neighbour = self.cells[x[1]][x[0]]
                neighbour.not_visited_neighbours -= 1
                
    def draw(self,name='new'):
        unit = 10
        img = Image.new('1',(self.width*unit+2,self.height*unit+2),color='white')
        for a in self.cells:
            for b in a:
                newx = b.x*unit
                newy = b.y*unit
                draw = ImageDraw.Draw(img)
                draw.rectangle((newx,newy,newx+unit,newy+unit))
                for index,wall in enumerate(b.walls):
                    if wall == 0:
                        if index == 0:
                            draw.line((newx,newy+1,newx,newy+unit-1), fill = 'white')
                        if index == 1:
                            draw.line((newx+1,newy,newx+unit-1,newy), fill = 'white')
                        if index == 2:
                            draw.line((newx+unit,newy+1,newx+unit,newy+unit-1), fill = 'white')
                        if index == 3:
                            draw.line((newx+1,newy+unit+1,newx+unit-1,newy+unit), fill = 'white')
        draw.line((1,0,unit-1,0),fill='white')
        draw.line((self.width*unit-9,self.height*unit,self.width*unit,self.height*unit),fill='white')
        img.save('{}.png'.format(name),'png')

    def generate(self, name = 'new', width = 0, height = 0):
        self.width = width
        self.height = height
        self.cells = []
        self.not_visited = -1
        print("Generating grid...")
        self.make_grid()
        print("Making paths...")
        self.make_paths()
        print("Drawing...")
        self.draw(name)
        print("Done! File \"{}.png\" is ready!".format(name))

