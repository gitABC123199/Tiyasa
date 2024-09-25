import string
def remove_punctuation(input_string):
  translator=str.maketrans('',"",string.punctuation)
  return input_string.translate(translator)
input_string="Hello,tiyasa this side!"
result=remove_punctuation(input_string)
print(result)
  
