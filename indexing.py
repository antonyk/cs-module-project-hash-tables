'''
what are all the employees in a certain department

'''

records = [
    ("Alice", "Engineering"),
    ("Bob", "Sales"),
    ("Carol", "Sales"),
    ("Dave", "Engineering"),
    ("Erin", "Engineering"),
    ("Frank", "Engineering"),
    ("Grace", "Marketing")
]


cache = {}

def indexit():
  for r in records:
    dept = r[1].lower()
    if dept not in cache:
      cache[dept] = []
    
    cache[dept].append(r)

indexit()

while True:
  dept = input("Enter department: ").lower()
  print(cache[dept])

'''
for r in records:
  if r[1].lower() == dept.lower():
    print(r)
'''
