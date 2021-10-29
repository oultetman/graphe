class Pile(list):
   def empile(self,valeur:any):
       self.append(valeur)

   def depile(self):
       return self.pop()


class File(list):
   def enfile(self, valeur: any):
       self.append(valeur)

   def defile(self):
       return self.pop(0)

if __name__ == '__main__':
   p = Pile()
   print(p)
   p.empile(10)
   p.empile(20)
   print(p)
   print(p.depile())

   f = File()
   print(f)
   f.enfile(10)
   f.enfile(20)
   print(f)
   print(f.defile())

