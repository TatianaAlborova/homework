
import numpy as np

# Создаем массив чисел от 0 до 9
array = np.arange(10)

# Выводим исходный массив
print("Исходный массив:")
print(array)

# Увеличиваем все элементы на 5
increased_array = array + 5
print("\nМассив после увеличения на 5:")
print(increased_array)

# Умножаем все элементы на 2
multiplied_array = array * 2
print("\nМассив после умножения на 2:")
print(multiplied_array)

# Находим квадрат каждого элемента
squared_array = np.square(array)
print("\nКвадрат каждого элемента:")
print(squared_array)

# Находим среднее значение элементов массива
mean_value = np.mean(array)
print("\nСреднее значение элементов массива:")
print(mean_value)

# Находим стандартное отклонение
std_deviation = np.std(array)
print("\nСтандартное отклонение элементов массива:")
print(std_deviation)


from PIL import Image, ImageDraw, ImageFont

# Создаем новое изображение
width, height = 300, 200
image = Image.new('RGB', (width, height), color='lightblue')

# Инициализируем объект для рисования
draw = ImageDraw.Draw(image)

# Рисуем текст на изображении
text = "Hello!"
font_size = 20
font = ImageFont.load_default()

# Получаем размеры текста
bbox = draw.textbbox((0, 0), text, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]

draw.text(((width - text_width) / 2, (height - text_height) / 2), text, fill='black', font=font)

image.save('output_image.png')

image.show()








