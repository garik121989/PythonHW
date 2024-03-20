

transactions = [
('Կարապետ', 'Կարապետյան', 11000, 'aperitivo'),
('Կարապետ', 'Կարապետյան', 13700, 'zangakbookstore'),
('Կարապետ', 'Կարապետյան', 7200, 'aperitivo'),
('Կարապետ', 'Կարապետյան', 10900, 'zangakbookstore'),
('Կարապետ', 'Կարապետյան', 6200, 'sassupermarket'),
('Կարապետ', 'Կարապետյան', 5000, 'sassupermarket'),
('Կարապետ', 'Կարապետյան', 4500, 'aperitivo'),
('Կարապետ', 'Կարապետյան', 2800, 'sassupermarket'),
('Կարապետ', 'Կարապետյան', 9430, 'sassupermarket'),
('Կարապետ', 'Կարապետյան', 1700, 'aperitivo'),
]

spent_money = max([j for i in transactions for j in i if isinstance(j,int)])
print(spent_money)
merchan_id = [i[-1] for i in transactions if spent_money in i]
print(merchan_id[0])

