def double_sums(fs1, fs2, ss1, ss2):
    print(sum([x+y for x in range(fs1, fs2+1) for y in range(ss1, ss2+1)]))


double_sums(1, 3, 1, 2)
