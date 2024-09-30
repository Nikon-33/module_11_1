import requests
import pandas
import numpy

# 1. requests - запросить данные с сайта и вывести их в консоль.
for i in range(1, 10):
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{i}')
    if response.status_code == 200:
        post = response.json()
        print(f"Post ID: {post['id']}")
        print(f"Title: {post['title']}")
        print(f"Body: {post['body']}")
        print("-" * 20)
    else:
        print("Error:", response.status_code)

for i in range(1, 10):
    data = {
        'id': i,
        'title': f'Updated Title {i}',
        'body': f'Updated Body {i}',
        'userId': 1
    }
    response = requests.put(f'https://jsonplaceholder.typicode.com/posts/{i}', json=data)

    if response.status_code == 200:
        print(f"Post {i} updated:", response.json())
    else:
        print(f"Error updating post {i}: {response.status_code}")

for i in range(1, 10):
    response = requests.delete(f'https://jsonplaceholder.typicode.com/posts/{i}')
    if response.status_code == 200:
        print("Post deleted successfully")
    else:
        print("Error:", response.status_code)


# 2. pandas - считать данные из файла, выполнить простой анализ данных (на своё усмотрение) и вывести результаты в консоль.
data = {
    'Имя': ['Илья', 'Евгений', 'Игорь', 'Антон'],
    'Возраст': [25, 26, 27, 28],
    'Город': ['Санкт-Петербург', 'Владимир', 'Новосибирск', 'Магнитогорск']
}

df = pandas.DataFrame(data)
print(df)
print("-" * 20)

df['Возраст через 5 лет'] = df['Возраст'] + 5
print(df)
print("-" * 20)

filtered_df = df[df['Возраст'] > 27]
print(filtered_df)
print("-" * 20)

df.to_csv('Сотрудники.csv')
df.to_csv('Сотрудники (без нумерации строк).csv', index=False)

df = pandas.read_csv('Сотрудники (без нумерации строк).csv')
print(df)

# 3. numpy - создать массив чисел, выполнить математические операции с массивом и вывести результаты в консоль.
array_1d = numpy.array([1, 2, 3, 4, 5])
print(array_1d)
print("-" * 20)

array_2d = numpy.array([[1, 2, 3], [4, 5, 6]])
print(array_2d)
print("-" * 20)

array_a = numpy.array([1, 2, 3])
array_b = numpy.array([4, 5, 6])
result = array_a + array_b
print(result)  # [5 7 9]
print("-" * 20)

result = result * 2
print(result)
print("-" * 20)

array = numpy.array([25, 79, 153])
print(f'Сумма элементов = {numpy.sum(array)}')
print(f'Среднее значение = {numpy.mean(array)}')
print(f'Стандартное отклонение = {numpy.std(array)}')
print("-" * 20)

zeros_array = numpy.zeros((2, 3))
ones_array = numpy.ones((4, 7))
print(f'Массив из нулей:\n {zeros_array}')
print(f'Массив из единиц:\n {ones_array}')
print("-" * 20)

array_3d = numpy.random.rand(4, 2, 3)
print(array_3d)