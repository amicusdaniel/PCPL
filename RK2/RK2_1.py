# используется для сортировки
from operator import itemgetter
"""
1. «Компьютер» и «Операционная система» связаны соотношением один-ко-многим. Выведите список всех компьютеров, 
у которых в названии процессора присутствует слово «Ryzen», и список работающих их операционных систем.

2. «Компьютер» и «Операционная система» связаны соотношением один-ко-многим. Выведите список операционных
систем со средним объемом памяти компьютеров, использующих эту операционную систему,
отсортированный по объемом памяти компьютера

3. «Компьютер» и «Операционная система» связаны соотношением многие-ко-многим. Выведите список всех операционных
систем, у которых название начинается с буквы «W» и список компьютеров на которых они установлены.
"""


class PC:
    """Компьютер"""
    def __init__(self, id, user, firm, cpu, memory, os_id):
      self.id = id
      self.user = user
      self.firm = firm
      self.cpu = cpu
      self.memory = memory
      self.os_id = os_id


class OS:
   """Операционная система"""
   def __init__(self, id, name, year):
      self.id = id
      self.name = name
      self.year = year

class PC_OS:
   def __init__(self, os_id, pc_id):
      self.os_id = os_id
      self.pc_id = pc_id

def getData():
   # Операционные системы
   OSs = [
      OS(1, "Windows 10", 2015),
      OS(2, "Linux", 1991),
      OS(3, "Windows 11", 2021),
      OS(4, "Windows 7", 2009),
      OS(5, "FreeDOS", 2006),
   ]
   
   
   # Компьютеры
   PCs = [
      PC(1, "Андрейкин", "Lenovo", "Intel Core i3", 1024, 1),
      PC(2, "Карлсон", "ASUS", "Intel Core i5", 2048, 1),
      PC(3, "Грищук","Dell", "Intel Core i7", 1536, 2),
      PC(4, "Каспаров", "hp", "Intel Core i9", 4096, 3),
      PC(5, "Каруана","Dell", "AMD Ryzen 3", 512, 2),
      PC(6, "Накамура","ASUS", "AMD Ryzen 7", 1024, 4),
      PC(7, "Нородинский", "Lenovo", "AMD Ryzen 9", 2048, 4),
      PC(8, "Омариев", "Colorful", "AMD Ryzen 5", 3072, 5)
   ]
   
   PC_OSs = [
      PC_OS(1,1),
      PC_OS(1,6),
      PC_OS(2,2),
      PC_OS(2,7),
      PC_OS(3,3),
      PC_OS(3,4),
      PC_OS(3,6),
      PC_OS(3,8),
      PC_OS(4,5),
      PC_OS(5,2),
      PC_OS(5,3),
      PC_OS(5,8)
   ]
   return PCs, OSs, PC_OSs

def sred_r(mas): # среднее округл. значение
    return round(sum(mas) / len(mas), 2)

def t1(PCs, OSs, PC_OSs):
    task1 = [(pc.firm, os.name) 
        for pc in PCs 
        for os in OSs 
        if "Ryzen" in pc.cpu and pc.os_id == os.id]
    task1 = sorted(task1)
    return task1
    
def t2(PCs, OSs, PC_OSs):
       task2 = [(os.name, sred_r([pc.memory for pc in PCs if pc.os_id == os.id])) for os in OSs]
       task2.sort(key = lambda x: x[1])
       return task2
       
def t3(PCs, OSs, PC_OSs):
       def pcsearch(pc_id):
           for pc in PCs:
               if pc.id == pc_id:
                   return pc.firm
               
       task3 = {os.name:
                [pcsearch(pc_os.pc_id) for pc_os in PC_OSs if pc_os.os_id == os.id]
                for os in OSs if os.name[0]
                if os.name[0] == 'W'}
       return task3
                
def main():
    """Основная функция"""
    PCs, OSs, PC_OSs = getData()
    
    print('Задание E1')
    print(t1(PCs, OSs, PC_OSs))
    
    print('\nЗадание E2')
    print(t2(PCs, OSs, PC_OSs))

    print('\nЗадание E3')
    print(t3(PCs, OSs, PC_OSs))

if __name__ == '__main__':
    main()

