import arithmetic
import string_ops

a= float(input("Enter the first number: "))
b= float(input("Enter the second number: "))
print(f"{a}+{b} = {arithmetic.add(a,b)}")
print(f"{a}*{b} = {arithmetic.add(a,b)}")

s=input("Enter the string:")
print("Reversed string:", string_ops.reverse_string(s))
print("Vowel count:", string_ops.count_vowels(s))