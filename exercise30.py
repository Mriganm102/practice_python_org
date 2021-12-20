import random
class exercise30(object):
  def exercise_30(self):
    list1 = []
    with open('hi1', 'r') as f:
      line = f.readline()
      while line:
        line = f.readline().strip()
        list1.append(line)
    x = random.choice(list1)
    self.x = x
  def __init__(self):
    self.exercise_30()
def main():
  e30 = exercise30()
  print(e30.x)
if __name__ == '__main__':
    main()
