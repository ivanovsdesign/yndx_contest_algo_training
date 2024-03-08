#vasya_tree, vasya_range = list(map(int, input().split()))
#masha_tree, masha_range = list(map(int, input().split()))

#vp = '0 7'
#mp = '12 5'

#vp = '2 3'
#mp = '10 3'

#vp = '-1 12'
#mp = '8 17'

#vp = '0 0'
#mp = '0 0'

#vasya_tree, vasya_range = list(map(int, input().split()))
#masha_tree, masha_range = list(map(int, input().split()))

#vasya_tree, vasya_range = list(map(int, vp.split()))
#masha_tree, masha_range = list(map(int, mp.split()))

# checking location

def count_painted_trees(vasya_tree, vasya_range, masha_tree, masha_range):
    if vasya_range == 0 and masha_range == 0:
        return 0

    if vasya_range == 0:
        return masha_range * 2 + 1
    if masha_range == 0:
        return vasya_range * 2 + 1

    vasya_left, vasya_right = vasya_tree - vasya_range, vasya_tree + vasya_range
    masha_left, masha_right = masha_tree - masha_range, masha_tree + masha_range

    overlap_left = max(vasya_left, masha_left)
    overlap_right = min(vasya_right, masha_right)

    overlap_range = max(0, overlap_right - overlap_left + 1)

    vasya_full_range = vasya_range * 2 + 1
    masha_full_range = masha_range * 2 + 1

    total_range = vasya_full_range + masha_full_range - overlap_range

    return total_range

vasya_tree, vasya_range = map(int, input().split())
masha_tree, masha_range = map(int, input().split())

print(count_painted_trees(vasya_tree, vasya_range, masha_tree, masha_range))
