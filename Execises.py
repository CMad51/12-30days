'''#first exercise
import string
import random
def random_user_id(size=6,chars=string.ascii_lowercase+string.digits):
 feedback=''.join(random.choice(chars) for _ in range(size) )
 return feedback

print(random_user_id(3,'jdhkjfvnk494903lldfhdljjv'))'''


#6 random generate rgb and hexa color
import random
import string
def generate_random_color():
 rang=[3,5,6,74,2]
 color = list(random.choice(rang))
 return color
 print(color)
 

print(generate_random_color())

