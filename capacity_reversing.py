import math
import matplotlib.pyplot as plt
import time
import numpy as np

# N != 3 mod 6 の場合, 3UF >= 2TFの可能性あり
N_values = np.arange(57, 87, 1)
reversing_ratios = []  # 割合を保存

process_time = []
for N in N_values:
    start = time.time()
    a_values = []
    max_nk_3uf_list = []
    max_nk_2tf_list = []
    max_nk_2f_list = []
    # ----------------------- 3UF ----------------------------------
    for a in range(2, math.floor(2.3 * N + 1), math.floor(2 * N / 60)):
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
    
        
        a_values.append(a)
        max_nk_3uf_list.append(max_nk_3uf)
        max_nk_2tf_list.append(max_nk_2tf)
        
        
    a_values = np.array(a_values) 
    max_nk_2tf_list = np.array(max_nk_2tf_list)
    max_nk_3uf_list = np.array(max_nk_3uf_list)

    # 比率の計算と保存
    ratio = max_nk_2tf_list / max_nk_3uf_list
         
    reversing_ratio = np.sum(ratio < 1) / len(ratio)
    # print(f"{len(ratio)}, {np.sum(ratio < 1)}")
    reversing_ratios.append(reversing_ratio)

    end = time.time()
    print(f'N={N} 実行時間: {end - start:.4f} 秒')
    process_time.append(end - start)

# === 割合のプロット ===
plt.figure(figsize=(8,6))
plt.plot(N_values, reversing_ratios, marker='o')
plt.xlabel('N', fontsize=16)
plt.ylabel('Proportion of capacity reversing (2TF < 3UF)', fontsize=16)
# plt.title('Proportion of capacity reversing (2TF < 3UF)')
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.grid(True)
plt.tight_layout()
plt.show()

                            