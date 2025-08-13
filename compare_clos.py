import math
import matplotlib.pyplot as plt
import time
import numpy as np

# N != 3 mod 6 の場合, 3UF >= 2TFの可能性あり
# N_values = [32, 64, 128, 256]
N_values = [33, 63, 123, 255]

plt.figure(figsize=(8,6))
process_time = []
for N in N_values:
    start = time.time()
    a_values = []
    max_nk_3uf_list = []
    max_nk_2tf_list = []
    max_nk_2f_list = []
    # ----------------------- 3UF ----------------------------------
    for a in range(2, math.floor(3 * N + 1), math.floor(2 * N / 20)):
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

    

    # a vs max(nk) for each N
    # plt.figure(figsize=(8,6))
    # plt.plot(a_values, max_nk_3uf_list, label="3UF", marker='o')
    # plt.plot(a_values, max_nk_2tf_list, label="2TF", marker='x')
    # plt.plot(a_values, max_nk_2f_list, label="2F", marker='x')
    # plt.xlabel('a')
    # plt.ylabel('Max n*k')
    # plt.title(f'Max n*k vs a (N={N})')
    # plt.legend()
    # plt.grid(True)
    # plt.show()
    
    a_values = np.array(a_values) 
    max_nk_2tf_list = np.array(max_nk_2tf_list)
    max_nk_3uf_list = np.array(max_nk_3uf_list)
    max_nk_2f_list = np.array(max_nk_2f_list)

    # 3UF vs 2TF
    # plt.plot(a_values/N, max_nk_2tf_list / max_nk_3uf_list, label=f"N={N}", marker='o') 
    # 2F vs 2TF
    plt.plot(a_values/N, max_nk_2tf_list / max_nk_2f_list, label=f"N={N}", marker='o') 

    end = time.time()
    print(f'N={N}, 実行時間: {end - start:.4f} 秒')
    process_time.append(end - start)

# a/N (relative no of available switches) vs relative capacity(f_P/f_U)
plt.axhline(y=1, color='black', linestyle='--') 
plt.axvline(x=1.65, color='red', linestyle='--')

# 3UF vs 2TF
# plt.axvline(x=1.95, color='red', linestyle='--')
# plt.xlabel('Relative number of available switches, a/N', fontsize=16)
# plt.ylabel('Relative capacity: 2TF/3UF', fontsize=16)
# # plt.title(f'Relative capacity: 2TF/3UF vs a/N')
# plt.xlim(right=3)
# plt.ylim(bottom=0.7, top=1.5)
# plt.xticks(fontsize=14)
# plt.yticks(fontsize=14)
# plt.legend(fontsize=14)
# plt.grid(True)
# plt.tight_layout()
# plt.show()

# 2F vs 2TF
plt.xlabel('Relative number of available switches, a/N', fontsize=16)
plt.ylabel('Relative capacity: 2TF/2F', fontsize=16)
# plt.title(f'Relative capacity: 2TF/2F vs a/N')
plt.xlim(right=2.3)
plt.ylim(bottom=0.8, top=1.5)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.legend(fontsize=14)
plt.grid(True)
plt.tight_layout()
plt.show()

# plt.figure(figsize=(8,6))
# plt.plot(N_values, process_time, marker='o')
# plt.xlabel('N')
# plt.ylabel('Processing time')
# plt.title('Processing time with N')
# plt.grid(True)
# plt.show()

                            