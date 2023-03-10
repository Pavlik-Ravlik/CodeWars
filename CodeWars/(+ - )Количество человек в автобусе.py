# https://www.codewars.com/kata/5648b12ce68d9daa6b000099/train/python
# По городу движется автобус, который забирает и высаживает несколько человек
# на каждой остановке.
# Вам предоставляется список (или массив) целочисленных пар. Элементы каждой пары
# представляют количество людей, садящихся в автобус (первый элемент), и количество
# людей, выходящих из автобуса (второй элемент) на автобусной остановке.
# Ваша задача — вернуть количество людей, которые еще находятся в автобусе после
# последней автобусной остановки (после последнего массива). Несмотря на то, что это
# последняя автобусная остановка, автобус может быть не пустым, и некоторые люди все еще
# могут быть внутри автобуса, они, вероятно, спят там :D
# Взгляните на тест-кейсы.
# Имейте в виду, что тестовые примеры гарантируют, что количество людей в автобусе
# всегда >= 0. Таким образом, возвращаемое целое число не может быть отрицательным.
# Второе значение в первой паре массива равно 0, так как на первой остановке автобус пустой.
# test.assert_equals(number([[10, 0], [3, 5], [5, 8]]), 5)
# test.assert_equals(number([[3, 0], [9, 1], [4, 10], [12, 2], [6, 1], [7, 10]]), 17)
# bus_stops = [[10, 0], [3, 5], [5, 8]]
# ([[3, 0], [9, 1], [4, 10], [12, 2], [6, 1], [7, 10]])
def number(bus_stops):
    return sum([stop[0] - stop[1] for stop in bus_stops])


# assert number ([[10,0],[3,5],[5,8]])
assert number([[3, 0], [9, 1], [4, 10], [12, 2], [6, 1], [7, 10]]) == 17
