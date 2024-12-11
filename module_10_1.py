# Потоковая запись в файлы
from time import sleep, time
import threading

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range (1, word_count + 1):
            file.write(f'Какое-то слово № {i}\n')
            sleep(0.1)
    print(f'Завершилась запись файла {file_name}')

if __name__=='__main__':
    start_time = time()

    write_words(10, 'example1.txt')
    write_words(30, 'example2.txt')
    write_words(200, 'example3.txt')
    write_words(100, 'example4.txt')

    end_time = time()
    print(f"Время выполнения функций: {end_time - start_time} секунд")

    threads = []
    thread_args = [
        (10, 'example5.txt'),
        (30, 'example6.txt'),
        (200, 'example7.txt'),
        (100, 'example8.txt'),
    ]
    start_time_1 = time()
    for args in thread_args:
        thread = threading.Thread(target=write_words, args=args)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

    end_time_1 = time()
    print(f"Время работы потоков: {end_time_1 - start_time_1:.6f} секунд")