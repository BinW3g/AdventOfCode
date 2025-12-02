day2_input = "245284-286195,797927-983972,4949410945-4949555758,115-282,8266093206-8266228431,1-21,483873-655838,419252-466133,6190-13590,3876510-4037577,9946738680-9946889090,99954692-100029290,2398820-2469257,142130432-142157371,9797879567-9798085531,209853-240025,85618-110471,35694994-35766376,4395291-4476150,33658388-33694159,680915-772910,4973452995-4973630970,52-104,984439-1009605,19489345-19604283,22-42,154149-204168,7651663-7807184,287903-402052,2244-5558,587557762-587611332,307-1038,16266-85176,422394377-422468141"
# smaller test input
# day2_input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

def part1():
  sumOfInvalid = 0
  ranges = day2_input.split(',')
  for r in ranges:
    tokens = r.split('-')
    for i in range(int(tokens[0]), int(tokens[1])+1):
      str_n = str(i)
      half = len(str_n) // 2
      start = str_n[:half]
      end = str_n[half:]

      if start == end:
        sumOfInvalid += i
  print(sumOfInvalid)

def part2():
  sumOfInvalid = 0
  ranges = day2_input.split(',')
  for r in ranges:
    tokens = r.split('-')
    for i in range(int(tokens[0]), int(tokens[1]) + 1):
      str_n = str(i)
      for clen in range(1, len(str_n)//2+1):
        isValid = True
        for j in range(clen, len(str_n), clen):
          if str_n[:clen] != str_n[j:j+clen]:
            isValid = False
            break

        if(isValid):
          sumOfInvalid += i
          break
  print(sumOfInvalid)



if __name__ == '__main__':
  part1()
  part2()
