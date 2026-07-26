import re

# the * means match 0 or more repetitions of the preceding RE
print(re.search(r"Py.*n", "Pygmalion"))
print(re.search(r"Py.*n", "Python Programming"))
print(re.search(r"Py[a-z]*n", "Python Programming"))
print(re.search(r"Py[a-z]*n", "Pyn"))

# the + means match 1 or more repetitions of the preceding RE
print(re.search(r"o+l+", "goldfish"))
print(re.search(r"o+l+", "woolly"))
print(re.search(r"o+l+", "boil"))

# the ? means match 0 or 1 repetition of the preceding RE
print(re.search(r"p?each", "To each their own"))
print(re.search(r"p?each", "I like peaches"))

def repeating_letter_a(text):
  result = re.search(r"[Aa]+.+[Aa]+", text)
  return result != None

print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True

pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
print(re.search(pattern, "_this_is_a_valid_variable_name"))
print(re.search(pattern, "this isn't a valid variable"))
print(re.search(pattern, "my_variable1"))
print(re.search(pattern, "2my_variable1"))

#check if sentence starts with capital letter, followed by lower-case letters and/or white spaces and ends with a period, question mark or exclamation point
def check_sentence(text):
  result = re.search(r"^[A-Z][a-z ]*[.?!]$", text)
  return result != None

print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True

# the {m,n} quantifier means match from m to n repetitions of the preceding RE
pattern_number = r"\d{3}-\d{3}-\d{4}"
print(re.search(pattern_number, "123-456-7890"))

#this pattern matches a string that is a number, which can be negative and/or decimal
pattern_numbers = r"^-?\d*(\.\d+)?$"
print(re.search(pattern_numbers, "123.45"))
print(re.search(pattern_numbers, "-123.45"))
print(re.search(pattern_numbers, "123"))
print(re.search(pattern_numbers, "-123"))


def check_web_address(text):
  pattern = r"^[A-Za-z_.\-+]+\.[A-Za-z]+$"
  result = re.search(pattern, text)
  return result != None

print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # True

def check_time(text):
  pattern = r"^([1-9]|1[0-2]):[0-5][0-9]\s?(AM|PM)?$"
  result = re.search(pattern, text, re.IGNORECASE)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False
print(check_time("6:02 am")) # True
print(check_time("6:02km")) # False

def correct_function(text):
  result = re.search(r" \d{5}(-\d{4})?", text)  # Corrected regex pattern with space
  return result is not None

def check_zip_code(text):
  return correct_function(text)  # Call the correct_function

# Call the check_zip_code function with test cases
print(check_zip_code("The zip codes for New York are 10001 thru 11104."))  # True
print(check_zip_code("90210 is a TV show"))  # False (no space before 90210)
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001."))  # True
print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9."))  # False


print(re.search(r"[a-zA-Z]{5}", "a ghost")) #a word with 5 letters
print(re.search(r"[a-zA-Z]{5}", "a scary ghost appeared")) 
print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared")) #find all words with 5 letters
print(re.findall(r"\b[a-zA-Z]{5}\b", "A scary ghost appeared")) #find all whole words with 5 letters
print(re.findall(r"\w{5,10}", "I really like strawberries")) #find all words with 5 to 10 letters
print(re.findall(r"\w{5,}", "I really like strawberries")) #find all words with 5 or more letters
print(re.search(r"s\w{,20}", "I really like strawberries")) #find a word that starts with s and has 20 or fewer letters