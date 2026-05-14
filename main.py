print('hello world')

# ============================================================
# 仙人掌排序与收获 — 单轮排序优化版
# 仅做 行→列 一轮排序，省去冗余的第二轮遍历
# ============================================================
def get_world_size():
def get_pos_x():
def get_pos_y():
def move():

def move_to(x, y):
    """移动到指定坐标，利用地图环绕特性走最短路径"""
    size = get_world_size()
    cx = get_pos_x()
    cy = get_pos_y()

    dx = (x - cx) % size
    if dx > size // 2:
        for _ in range(size - dx):
            move(West)
    elif dx > 0:
        for _ in range(dx):
            move(East)

    dy = (y - cy) % size
    if dy > size // 2:
        for _ in range(size - dy):
            move(South)
    elif dy > 0:
        for _ in range(dy):
            move(North)

def sort_one_row(row):
    """对第 row 行升序排列"""
    size = get_world_size()

    move_to(0, row)
    values = []
    cnt = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(size):
        v = measure()
        values.append(v)
        cnt[v] = cnt[v] + 1
        if i < size - 1:
            move(East)

    target = []
    for v in range(10):
        for _ in range(cnt[v]):
            target.append(v)

    move_to(0, row)
    for i in range(size):
        if values[i] == target[i]:
            if i < size - 1:
                move(East)
            continue

        j = i + 1
        while j < size and values[j] != target[i]:
            j = j + 1

        move_to(j, row)
        for k in range(j, i, -1):
            swap(West)
            move(West)
            values[k], values[k-1] = values[k-1], values[k]

        if i < size - 1:
            move(East)

def sort_one_col(col):
    """对第 col 列升序排列"""
    size = get_world_size()

    move_to(col, 0)
    values = []
    cnt = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(size):
        v = measure()
        values.append(v)
        cnt[v] = cnt[v] + 1
        if i < size - 1:
            move(North)

    target = []
    for v in range(10):
        for _ in range(cnt[v]):
            target.append(v)

    move_to(col, 0)
    for i in range(size):
        if values[i] == target[i]:
            if i < size - 1:
                move(North)
            continue

        j = i + 1
        while j < size and values[j] != target[i]:
            j = j + 1

        move_to(col, j)
        for k in range(j, i, -1):
            swap(South)
            move(South)
            values[k], values[k-1] = values[k-1], values[k]

        if i < size - 1:
            move(North)

def sort_all():
    """单轮排序：先逐行升序，再逐列升序"""
    size = get_world_size()
    for y in range(size):
        sort_one_row(y)
    for x in range(size):
        sort_one_col(x)

def cactus_harvest():
    """主流程：种植 → 单轮排序 → 连锁收获"""
    size = get_world_size()

    for x in range(size):
        for y in range(size):
            plant(Entities.Cactus)
            move(North)
        move(East)

    sort_all()

    move_to(0, 0)
    harvest()

while True:
    cactus_harvest()