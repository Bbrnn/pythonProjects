def string_compare(s1,s2):
    if len(s1) != len(s2):
        return False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True 
    
s1="hello"
s2="hello"

print("Output for equal strings:",string_compare("hello","hello"))
print("Output for unequal strings:",string_compare("hello","helo"))

