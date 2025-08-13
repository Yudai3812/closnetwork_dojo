import math
import matplotlib.pyplot as plt
import time
import numpy as np

# N != 3 mod 6 の場合, 3UF >= 2TFの可能性あり
N_values = np.arange(50, 100, 1)

process_time = []
max_capacity = []
min_capacity = []
avg_capacity = []

for N in N_values:
    start = time.time()
    a_values = []
    max_nk_3uf_list = []
    max_nk_2tf_list = []
    max_nk_2f_list = []
    # ----------------------- 3UF ----------------------------------
    for a in range(math.floor(0.5 * N), math.floor(2.3 * N + 1), math.floor(2 * N / 60)):
        max_nk_3uf = 0
        max_nk_2tf = 0
        max_nk_2f = 0
        
        for n in range(1, N + 1):
            for k in range(1, a + 1):
                nk = n * k
                if nk <= max_nk_3uf:
                    continue  # 最大値更新の可能性がないならスキップ
                for v in range(1, a + 1):
                    if v * k > N:
                        break
                    for m in range(1, a + 1):
                        # if v * m > N or k + m > a:
                        if v * m > N or 2*k + m > a:
                            break
                        if 2 * math.floor((n - 1) / v) + 1 <= m:
                            if nk > max_nk_3uf:
                                max_nk_3uf = nk

    # ----------------------- 2TF ----------------------------------
        for n in range(1, N + 1):
            for k in range(1, a + 1):
                nk = n * k
                if nk <= max_nk_2tf:
                    continue  # 今のmaxより小さいならスキップ

                for v in range(1, a + 1):
                    if v * k > N:
                        break

                    for m in range(1, a + 1):
                        if k + m > a:
                            break
                        if n + v * m > N:
                            break
                        if 2 * math.floor((n - 1) / v) + 1 <= m:
                            if nk > max_nk_2tf:
                                max_nk_2tf = nk
    
    # ----------------------- 2F ----------------------------------
        for n in range(1, N // 2 + 1):  # nに対して 2*n <= N を考慮
            for k in range(1, a + 1):
                nk = n * k
                if nk <= max_nk_2f:
                    continue  # すでにmax超えないならスキップ

                for v in range(1, a + 1):
                    if v * k > N:
                        break  # v*k > Nなら以降もアウト

                    for m in range(1, a + 1):
                        if k + m > a:
                            break  # k+m>aならアウト
                        if 2 * v * m > N:
                            break  # 2vm > Nならアウト
                        if 2 * math.floor((n - 1) / v) + 1 <= m:
                            if nk > max_nk_2f:
                                max_nk_2f = nk
        
        a_values.append(a)
        max_nk_3uf_list.append(max_nk_3uf)
        max_nk_2tf_list.append(max_nk_2tf)
        max_nk_2f_list.append(max_nk_2f)

    
    a_values = np.array(a_values) 
    max_nk_2tf_list = np.array(max_nk_2tf_list)
    max_nk_3uf_list = np.array(max_nk_3uf_list)
    max_nk_2f_list = np.array(max_nk_2f_list)

    # ratio = max_nk_2tf_list / max_nk_3uf_list
    ratio = max_nk_2tf_list / max_nk_2f_list
    max_capacity.append(np.max(ratio))
    min_capacity.append(np.min(ratio))
    avg_capacity.append(np.mean(ratio))

    end = time.time()
    print(f'N={N}, 実行時間: {end - start:.4f} 秒')
    process_time.append(end - start)

plt.figure(figsize=(8,6))
plt.plot(N_values, max_capacity, marker='o')
plt.plot(N_values, min_capacity, marker='o')
plt.plot(N_values, avg_capacity, marker='o')
plt.xlabel('N', fontsize=16)
plt.ylabel('Relative capacity (2TF / 2F)', fontsize=16)
plt.legend(['Max', 'Min', 'Avg'], fontsize=14)
# plt.title('Max, Min, Avg of Relative capacity (2TF / 2F)')
plt.grid(True)
plt.tight_layout()
plt.show()


                            