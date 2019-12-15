'''
(축약)영역을 칠하는 함수를 구현하시오.
'''

def paint(img, x,y, color):
    '''
    칠할 영역을 모두 고른 후 맨 마지막에 한꺼번에 칠하기로 정함.
    사실 나오는 족족 칠해버리는게 메모리 측면에서도 유리한듯.
    단, 한꺼번에 칠하는 경우, 칠할 목록을 가지고 있으므로, 디버깅과 테스트에 유리.
    적당히 중간중간 flush하는 방식도 가능할듯.
    '''
    assert 0<=x<len(img) and 0<=y<len(img[0])
    pixels_to_color = []
    current_color = img[x][y]

    queue = [(x,y)]
    while queue:
        pos = queue.pop(0)
        x,y = pos
        queue.extend(list(get_neighbors_to_color(img, x, y, current_color, pixels_to_color)))
        pixels_to_color.append((x,y))
    do_color(img, pixels_to_color, color)

def get_neighbors_to_color(img, x, y, current_color, pixels_to_color):
    # rule1: (x,y)의 상하좌우는 img 범위
    # rule2: 상하좌우는 pixels_to_color내에 없는 것중에만 고름.
    candidates = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
    result = []
    for x0, y0 in candidates:
        if not (0<=x0<len(img) and 0<=y0<len(img[0]) ):
            continue
        if (x0, y0) in pixels_to_color:
            continue
        if img[x0][y0] != current_color:
            continue
        yield x0, y0

def do_color(img, pixels_to_color, color):
    for x,y in pixels_to_color:
        img[x][y] = color

sample_img = [
        [0,1,2,1,2,1,0],
        [0,1,2,2,2,1,0],
        [0,1,2,2,1,1,2],
        [0,1,2,1,1,2,2],
        [0,1,2,2,1,0,0],
        [0,1,2,2,2,1,0],
]

color = 5

from pprint import pprint as print
print(sample_img)
paint(sample_img, 0, 2, color)
print(sample_img)
