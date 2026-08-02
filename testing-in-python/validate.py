def validate_user(username, minlen):
  assert type(username) == str, "username must be a string"
  if minlen < 1:
    raise ValueError("minlen must be at least 1")

  if len(username) < minlen:
    return False
  if not username.isalnum():
    return False
  return True

try:
  validate_user("", -1)
except ValueError as e:
    print("Error:", e)
validate_user("", 1)
validate_user("myuser", 1)

try:
    validate_user(88, 1)
except AssertionError as e:
    print("Error:", e)

try:
    validate_user([], 1)
except AssertionError as e:
    print("Error:", e)

try:
    validate_user(["name"], 1)
except AssertionError as e:
    print("Error:", e)

