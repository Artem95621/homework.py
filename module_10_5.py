from datetime import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, encoding="utf-8") as file:
        data = file.readline()
        while data:
            data = file.readline()
            all_data.append(data[0:-1])
filenames = [f'./file {number}.txt' for number in range(1, 5)]

#Линейный вызов
start = datetime.now()
for name in filenames:
    read_info(name)
end = datetime.now()
time = end - start
print(f'Линейный вызов: {time}')

# многопроцессный
if __name__ == '__main__':
    start = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
        end = datetime.now()
        time = end - start
        print(f'Многопроцессный вызов: {time}')