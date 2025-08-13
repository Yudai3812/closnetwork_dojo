import math
import matplotlib.pyplot as plt
import time

start = time.time()

# N_values = [64, 128, 256, 512, 1024]   # ポート数
N_values = [32, 64, 128, 2048]

for N in N_values:
    a_values = []
    max_nk_3uf_list = []
    max_nk_2tf_list = []
    max_nk_2f_list = []
    # ----------------------- 3UF ----------------------------------
    for a in range(0, 2 * N + 1, math.floor(2 * N / 10)):
        max_nk_3uf = 0
        max_nk_2tf = 0
        max_nk_2f = 0
        
        for k in range(1, a + 1):
            for v in range(1, a + 1):
                if v * k <= N: 
                    for m in range(1, a + 1):
                        if v * m <= N and k + m <= a:
                            for n in range(1, N + 1):
                                if 2 * math.floor((n - 1) / v) + 1 <= m:
                                    nk = n * k
                                    if nk > max_nk_3uf:
                                        max_nk_3uf = nk

    # ----------------------- 2TF ----------------------------------
        for k in range(1, a + 1):
            for v in range(1, a + 1):
                if v * k <= N: 
                    for m in range(1, a + 1):
                        if k + m <= a:
                            for n in range(1, N + 1):
                                if n + v * m <= N and 2 * math.floor((n - 1) / v) + 1 <= m:
                                    nk = n * k
                                    if nk > max_nk_2tf:
                                        max_nk_2tf = nk

    # ----------------------- 2F ----------------------------------
        for k in range(1, a + 1):
            for v in range(1, a + 1):
                if v * k <= N: 
                    for m in range(1, a + 1):
                        if k + m <= a and 2 * v * m <= N:
                            for n in range(1, N + 1):
                                if 2 * n <= N and 2 * math.floor((n - 1) / v) + 1 <= m:
                                    nk = n * k
                                    if nk > max_nk_2f:
                                        max_nk_2f = nk
        
        a_values.append(a)
        max_nk_3uf_list.append(max_nk_3uf)
        max_nk_2tf_list.append(max_nk_2tf)
        max_nk_2f_list.append(max_nk_2f)

    
                                    
    done_time = time.time()
    print(f'N={N} done')
    print(f"実行時間: {done_time - start:.4f} 秒")

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

                            