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
    return all_data


if __name__ == '__main__':
    filenames = [f'./file_{number}.txt' for number in range(1, 5)]

    # Linear
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    linear_duration = time.time() - start_time
    print(f'Linear execution time: {linear_duration:.4f} seconds')

    # Multiprocessing
    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    multiprocessing_duration = time.time() - start_time
    print(f'Multiprocessing execution time: {multiprocessing_duration:.4f} seconds')
