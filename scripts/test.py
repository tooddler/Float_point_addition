import numpy as np

def main2():
    """ fp32 test. """
    data1 = np.float32(10 * np.random.rand())
    data2 = np.float32(10 * np.random.rand())
    rlst0 = data2 * data1

    data3 = np.float32(10 * np.random.rand())
    data4 = np.float32(10 * np.random.rand())
    rlst1 = data3 * data4

    value = [data1, data2, data3, data4, rlst0, rlst1]
    weight_bin_data = np.stack(value)
    weight_bin_data = weight_bin_data.reshape(-1)
    file = open('fp32_test.bin', 'wb')
    for i in range(len(weight_bin_data)):
        file.write(weight_bin_data[i].tobytes())
    file.close()
    print(1)

if __name__ == '__main__':
    main2()
