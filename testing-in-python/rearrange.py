#!/usr/bin/env python3

import re

def rearrange_name(name):
  result = re.search(r"^([\w .]*), ([\w .]*)$", name)
  if result is None:
    return name
  return "{} {}".format(result[2], result[1])

  
my_txt = ""

def LetterCompiler(txt):
    result = re.findall(r'([a-c]).', txt)
    return result

print("Resultado: ", LetterCompiler(my_txt))