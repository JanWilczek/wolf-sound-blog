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


class Envelope:
    def __init__(self, name, segments, key_on=None, key_off=None):
        self.name = name
        self.segments = segments
        self.key_on = key_one
        self.key_off = key_off


def plot_envelope(envelope, name):
    x = 0
    
    plt.figure(figsize=(9,4))
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
    decay_adsr = Segment('Decay', 0.2, 1, 0.6)
    sustain = Segment('Sustain', 0.4, 0.6, 0.6)
    release = Segment('Release', 0.3, 0.6, 0)
    
    ad_envelope = [attack, decay]
    plot_envelope(ad_envelope, 'AD')

    ar_sustain = Segment('Sustain', 0.4, 1, 1)
    ar_release = Segment('Release', 0.2, 1, 0)
    ar_envelope = [attack, ar_sustain, ar_release]
    plot_envelope(ar_envelope, 'AR')

    adr_decay = Segment('Decay', 0.15, 1, 0.4)
    adr_release = Segment('Release', 0.3, 0.4, 0)
    adr_envelope = [attack, adr_decay, adr_release]
    plot_envelope(adr_envelope, 'ADR')

    ads_sustain = Segment('Sustain', 0.4, 0.4, 0.4)
    ads_release = Segment('', 0.02, 0.4, 0)
    ads_envelope = [attack, adr_decay, ads_sustain, ads_release]
    plot_envelope(ads_envelope, 'ADS')

    adsd_release = Segment('', 0.1, 0.4, 0)
    adsd_envelope = [attack, adr_decay, ads_sustain, adsd_release]
    plot_envelope(adsd_envelope, 'ADSD')

    adsr_envelope = [attack, decay_adsr, sustain, release]
    plot_envelope(adsr_envelope, 'ADSR')

    hold = Segment('Hold', 0.15, 1, 1)
    ahdsr_envelope = [attack, hold, decay_adsr, sustain, release]
    plot_envelope(ahdsr_envelope, 'AHDSR')

    decay1 = Segment('Decay1', 0.2, 1, 0.7)
    decay2 = Segment('Decay2', 0.4, 0.7, 0.5)
    release_adbdr = Segment('Release', 0.2, 0.5, 0)
    adbdr_envelope = [attack, decay1, decay2, release_adbdr]
    plot_envelope(adbdr_envelope, 'ADBDR')
    

if __name__=='__main__':
    main()
