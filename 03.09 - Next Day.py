m = int(input("Enter a month 1-12: "))
y = int(input("Enter a day 1-31: "))

if m in (1, 3, 5, 7, 8, 10, 12):
    m_length = 31
elif m == 2:
    m_length = 28
else:
    m_length = 30

if y < m_length:
    y += 1
else:
    y = 1
    if m == 12:
        m = 1
    else:
        m += 1

print ("Next Day: " + str(m) + "/" + str(y))