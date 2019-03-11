# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import matplotlib

matplotlib.rc('font', family='NanumGothic')  # 한글 폰트 설정

# fig = plt.figure()
fig = plt.figure(figsize=(6, 6), dpi=100)  # 그림 사이즈, 해상도 설정

fig.suptitle('bold figure suptitle', fontsize=14, fontweight='bold')

ax = fig.add_subplot(111)
fig.subplots_adjust(top=0.85)
ax.set_title('axes title')

labx ='x 축의 레이블을 이렇게 표시'
laby = ' 와이 축 레이블 표시 방법을 이렇게 함.'

ax.set_xlabel( labx )
ax.set_ylabel( laby )

ax.text(3, 8, 'boxed italics text in data coords', style='italic',
        bbox={'facecolor':'red', 'alpha':0.5, 'pad':10})

ax.text(2, 6, r'an equation: $E_{i,j}=mc^2$', fontsize=15)


msg = 'colored 한글 입력 테스트 in axes coords'
# msg = 'colored 한글 in axes coords'

ax.text(0.95, 0.01, msg,
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='green', fontsize=15)


ax.plot([2], [1], 'o')
ax.annotate('annotate', xy=(2, 1), xytext=(3, 4),
            arrowprops=dict(facecolor='black', shrink=0.05))

ax.axis([0, 10, 0, 10])

plt.show()


