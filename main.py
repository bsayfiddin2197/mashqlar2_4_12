# 7
roy = ["Sayfiddin"]
tes = list(map(lambda x: x[::-1], roy))
print(tes)

# 8
roy = [1, 2, 3, 4, 5]
kub = list(map(lambda x: x ** 4, roy))
print(kub)

# 9
roy = ["Sayfiddin"]
harf = list(map(lambda x: x[0], roy))
print(harf)

# 10
roy = [1, 2, 3, 4, 5, 6]
jt = list(map(lambda x: "juft" if x % 2 == 0 else "toq", roy ))
print(jt)

# 11
roy1, roy2 = [1, 2, 3], [4, 5, 6]
kop = list(map(lambda x, y: x * y, roy1, roy2))
print(kop)
