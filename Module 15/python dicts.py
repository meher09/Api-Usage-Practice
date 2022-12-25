import os
person = {'name': 'aouwal', 'age':'21'}
# print(person.items())

from dotenv import load_dotenv
load_dotenv()
name = os.getenv('MY_NAME')
print(name)