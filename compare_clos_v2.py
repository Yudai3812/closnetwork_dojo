import math
import matplotlib.pyplot as plt
import time
import numpy as np

# N != 3 mod 6 の場合, 3UF >= 2TFの可能性あり
N_values = [32, 63, 64, 123, 128, 256]

process_time = []
for N in N_values:
    start = time.time()
    a_values = []
    max_nk_3uf_list = []
    max_nk_2tf_list = []
    max_nk_2f_list = []
    # ----------------------- 3UF ----------------------------------
    for a in range(0, 2 * N + 1, math.floor(2 * N / 20)):
        max_nk_3uf = 0
        max_nk_2tf = 0
        max_nk_2f = 0
        
        found = False
        for nk in range(N * a, 0, -1):  # 大きい順にnkを探す
            for n in range(1, N + 1):
                if nk % n != 0:
                    continue  # kは整数じゃないとダメ
                k = nk // n
                if k > a:
                    continue
                for v in range(1, a + 1):
                    if v * k > N:
                        break
                    for m in range(1, a + 1):
                        if v * m > N or 2 * k + m > a:
                            break
                        if 2 * math.floor((n - 1) / v) + 1 <= m:
                            max_nk_3uf = nk
                            found = True
                            break
                    if found:
                        break
                if found:
                    break
            if found:
                break

    # ----------------------- 2TF ----------------------------------
        found = False
        for nk in range(N * a, 0, -1):  # 大きい順にnkを探す
            for n in range(1, N + 1):
                if nk % n != 0:
                    continue  # kは整数じゃないとダメ
                k = nk // n
                if k > a:
                    continue
                for v in range(1, a + 1):
                    if v * k > N:
                        break
                    for m in range(1, a + 1):
                        if n + v * m > N or k + m > a:
                            break
                        if 2 * math.floor((n - 1) / v) + 1 <= m:
                            max_nk_2tf = nk
                            found = True
                            break
                    if found:
                        break
                if found:
                    break
            if found:
                break

    # ----------------------- 2F ----------------------------------
        found = False
        for nk in range(N * a, 0, -1):
            for n in range(1, math.floor(N/2) + 1):
                if nk % n != 0:
                    continue 
                k = nk // n
                if k > a:
                    continue
                for v in range(1, a + 1):
                    if v * k > N:
                        break
                    for m in range(1, a + 1):
                        if 2 * v * m > N or k + m > a:
                            break
                        if 2 * math.floor((n - 1) / v) + 1 <= m:
                            max_nk_2f = nk
                            found = True
                            break
                    if found:
                        break
                if found:
                    break
            if found:
                break
        
        a_values.append(a)
        max_nk_3uf_list.append(max_nk_3uf)
        max_nk_2tf_list.append(max_nk_2tf)
        max_nk_2f_list.append(max_nk_2f)

    
                                    
    end = time.time()
    print(f'N={N} done')
    print(f"実行時間: {end - start:.4f} 秒")
    process_time.append(end - start)

    # a vs max(nk) for each N
    plt.figure(figsize=(8,6))
    plt.plot(a_values, max_nk_3uf_list, label="3UF", marker='o')
    plt.plot(a_values, max_nk_2tf_list, label="2TF", marker='x')
    plt.plot(a_values, max_nk_2f_list, label="2F", marker='x')
    plt.xlabel('a')
    plt.ylabel('Max n*k')
    plt.title(f'Max n*k vs a (N={N})')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    # a_values = np.array(a_values) 
    # max_nk_2tf_list = np.array(max_nk_2tf_list)
    # max_nk_3uf_list = np.array(max_nk_3uf_list)

    # # a/N (relative no of available switches) vs relative capacity(f_P/f_U)
    # plt.figure(figsize=(8,6))
    # plt.plot(a_values/N, max_nk_2tf_list / max_nk_3uf_list, label="relative", marker='o')
    # plt.axhline(y=1, color='black', linestyle='--')  #
    # plt.xlabel('Relative number of available switches, a/N')
    # plt.ylabel('Max n*k')
    # plt.title(f'Relative capacity, 2TF/3UF')
    # plt.legend()
    # plt.grid(True)
    # plt.show()


plt.figure(figsize=(8,6))
plt.plot(N_values, process_time, marker='o')
plt.xlabel('N')
plt.ylabel('Processing time')
plt.title('Processing time with N')
plt.grid(True)
plt.show()

                            