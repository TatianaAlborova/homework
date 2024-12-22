import time
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())

filenames = [f'./file {number}.txt' for number in range(1, 5)]

file_names = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']
start_time = time.time()
for i in file_names:
    f = read_info(i)
end_time = time.time()

print(f"{end_time - start_time} секунд")


if __name__ == '__main__':
    start_time = time.time()
    with Pool() as pool:
        results = pool.map(read_info, file_names)
    end_time = time.time()

    print(f" {end_time - start_time} секунд")
