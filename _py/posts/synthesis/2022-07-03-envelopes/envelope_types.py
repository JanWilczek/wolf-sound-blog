import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from matplotlib import rc


images_path = Path('/home/jawi/Projects/WolfSound/Page/assets/img/posts/synthesis/2022-07-03-envelopes/')
rc('font',**{'family':'sans-serif','sans-serif':['Verdana']})
plt.rcParams.update({'font.size': 20})
color = '#Ef7600'
grey = '#7c7c7c'

class Segment:
    def __init__(self, name, length, left_value, right_value):
        self.name = name
        self.length = length
        self.left_value = left_value
        self.right_value = right_value


def plot_envelope(envelope, name):
    x = 0
    
    plt.figure()
    for segment in envelope:
        next_x = x + segment.length
        plt.plot([x, next_x], [segment.left_value, segment.right_value], color, linewidth=3)
        plt.vlines(x, 0, 1.3, colors=grey, linestyles='dashed')
        plt.vlines(next_x, 0, 1.3, colors=grey, linestyles='dashed')
        plt.text(x + segment.length / 2, 1.1, segment.name, horizontalalignment='center')
        x = next_x
    plt.ylim([0, 1.3])
    plt.ylabel('amplitude')
    plt.xlabel('time')
    plt.xticks([])
    plt.yticks([])
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.savefig(images_path / f'{name}.png', dpi=300, bbox_inches='tight')


def main():
    images_path.mkdir(exist_ok=True, parents=True)
    
    attack = Segment('Attack', 0.2, 0, 1)
    decay = Segment('Decay', 0.2, 1, 0)
    ad_envelope = [attack, decay]
    plot_envelope(ad_envelope, 'AD')

if __name__=='__main__':
    main()
