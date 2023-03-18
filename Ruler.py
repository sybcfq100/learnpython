def draw_line(tick_length, tick_label=''):
    line = '-'*tick_length
    if tick_label:
        line += f' {tick_label}'
    print(line)

def draw_interval(center_length):
    """ Draw tick interval based upon a central tick length. """
    if center_length > 0:                   # 当长度为0时，停止
        draw_interval(center_length - 1)    # 画上线
        draw_line(center_length)            # 画中心线
        draw_interval(center_length - 1)    # 画下线


def draw_ruler(num_inches, major_length):
    draw_line(major_length, '0')            # 画0线
    for j in range(1, 1+num_inches) :
        draw_interval(major_length - 1)     # 画间隔线
        draw_line(major_length, str(j))     # 画 j 英尺，并标记


# draw_line(4, '2')
# draw_interval(3)
draw_ruler(2, 2)
