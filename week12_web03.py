from bs4 import BeautifulSoup

html = """
<html>
<head>
<title>스크레이핑 실습</title>
</head>
<body>
<h1 id = "univ">대림대학교</h1>
<p>웹스크레이핑</p>
<p id = "contents">파이썬, 판다스, 넘파이, 맷플롯립, GUI...</p>
</body>
</html>
"""
soup = BeautifulSoup(html, 'html.parser')
t = soup.html.head.title
print(t)
print(t.string)

h1 = soup.html.body.h1.string
print(h1)

p1 = soup.html.body.p.string
print(p1)

p2 = p1.next_sibling.next_sibling
print(p2)