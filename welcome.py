"""
generate random keys for django
"""
import random

result = "".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for i in range(50)])

print("""



             WELCOME GEEK! 🐍 + 💻 = 😀

Please copy the collowing key and paste it as the SECRET_KEY variable value on the example-project/settings.py:

\033[94m SECRET_KEY = \033[93m""" + result + """\033[0m

Afterwards you need to run the following commands to start coding:

- Carefully read the project instructions to make sure you understand what needs to be done
- \033[94m$ pipenv run start\033[0m start django
- \033[94m$ pipenv run tests\033[0m to run unit testing on the API

""")
