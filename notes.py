# s  =  'this is a sentence'.capitalize()
# print(s)

# s  =  'ths is a sentence this'
# print(s.count('a'))

# pre = 'unhappy'
# suf = 'quickly'

# print(suf.endswith('ly'))

# s  =  'ths is a sentence this'
# print(s.find('i'))

# s  =  'ths is a sentence this'
# print(s.rfind('i'))
# index = s.rfind('i')
# print(s[s.rfind('i')])

# s  =  'ths is a sentence this'
# s = 'SCREAM'
# print(s.rfind('i'))
# print(s.title())
# print(s)

# s  =  "I'm bad in python"
# print(s.replace(bad, good))
# print(s)
# -------------------------------------------------------------------------

s = 'a12'
print(s.isalnum())

a= 'ab2'
print(a.isalpha())

#
b = '10'
print(b.isdecimal())
z = '10a'
print(z.isdecimal())

# ISDIGIT
c = '5'
print(c.isdigit())
d = 'h'
print(d.isdigit())

# IS NUMERIC
e = '266'
print(e.isnumeric())
f = '266h'
print(f.isnumeric())

# ISTITLE
g = 'jejx'
print(g.istitle())
print(g.title())

# ISSPACE
h = '   '
print(h.isspace())
i = 'jxebwxjwbjx211'
print(i.isspace())

# LSTRIP
j = 'hjjh'
print(j.lstrip())

# SPLIT
k = "1 0 0"
print(k.lstrip())
m = "100"
print(m.lstrip())