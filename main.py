l1=[1961,
1986,1958,1983,1986,1974,1978,1981,1982,1975,1979,1971,1979,
1981,1977,1975,1978,1977,1958,1981,1988,1980,1973,1975,1973,
1959,1970,1969,1979,1983,1966]

l=['Еремеев',
"Дедюхин","Дементьев",'Кутузов',    'Степанова',
'Давыдова','Тен', 'Матвеев', 'Седова', 'Романенко',
'Ястребова','Кузнецова','Иванов','Козорезов','Борисов',
'Костенко','Зраев','Филоненко','Иванов','Ковалёва',
'Кузнецова','Степанова','Соловей','Тен','Воробьева','Степанова','Щербаков',
'Ли Евгений',
'Романенко',
'Ляшук',
'Кузнецов',]

n=len(l1)
for i in range(n):
    if l1[i] < 1978:
        print(l1[i],l[i])

