import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from matplotlib import rc
import soundfile as sf
import subprocess


images_path = Path('/home/jawi/Projects/WolfSound/Page/assets/img/posts/synthesis/2022-07-03-envelopes/')
wav_path = Path('/home/jawi/Projects/WolfSound/Page/assets/wav/posts/synthesis/2022-07-03-envelopes/')
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
    def __init__(self, name, segments, key_on=0, key_off=None):
        self.name = name
        self.segments = segments
        self.key_on = key_on
        self.key_off = key_off


def plot_envelope(envelope):
    x = 0
    ylim = [0, 1.5]
    arrow_height = 0.2
    vlines_height = 1.3
    arrow_y =  ylim[1] - 0.1
    arrow_kwargs = { "width": 0.03, "color": grey, "zorder": 2, "length_includes_head": True}
    arrow_text_y = arrow_y + 0.05
    output_path = images_path / f'{envelope.name}.png'

    plt.figure(figsize=(9,4))
    for segment in envelope.segments:
        next_x = x + segment.length
        plt.plot([x, next_x], [segment.left_value, segment.right_value], color, linewidth=3)
        plt.vlines(x, ylim[0], vlines_height, colors=grey, linestyles='dashed')
        plt.vlines(next_x, ylim[0], vlines_height, colors=grey, linestyles='dashed')
        plt.text(x + segment.length / 2, 1.05, segment.name, horizontalalignment='center')
        x = next_x
    plt.ylim(ylim)
    plt.ylabel('value')
    plt.xlabel('time')
    plt.xticks([])
    plt.yticks([])
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    if envelope.key_on is not None:
        plt.arrow(envelope.key_on, arrow_y, 0, - arrow_height, **arrow_kwargs)
        plt.text(envelope.key_on, arrow_text_y, 'key on', horizontalalignment='center', color=grey)
    if envelope.key_off is not None:
        plt.arrow(envelope.key_off, arrow_y - arrow_height, 0, arrow_height, **arrow_kwargs)
        plt.text(envelope.key_off, arrow_text_y, 'key off', horizontalalignment='center', color=grey)
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    subprocess.run(['cwebp', '-q', '65', '-resize', '800', '0', output_path, '-o', output_path.with_suffix('.webp')])


def envelope_sound_example(envelope):
    fs = 22050
    f = 220
    length_seconds = 5
    length_samples = length_seconds * fs
    t = np.arange(0, length_samples) / fs
    sine = np.sin(2 * np.pi * f * t)

    total_length = np.sum([s.length for s in envelope.segments])
    e = np.ones_like(sine)

    n = 0
    for i, segment in enumerate(envelope.segments):
        segment_length_samples = int(segment.length * length_samples / total_length) if i < len(envelope.segments) - 1 else e.shape[0] - n
        next_n = n + segment_length_samples
        if segment.left_value == segment.right_value:
            e[n:next_n] *= segment.left_value
        else:
            e[n:next_n] *= np.exp(np.linspace(np.log(np.maximum(segment.left_value, 0.0001)), np.log(np.maximum(segment.right_value, 0.0001)), segment_length_samples, endpoint=True))
        n = next_n

    sine_enveloped = sine * e

    amplitude = 0.5
    signal_to_store = amplitude * sine_enveloped

    sf.write(wav_path / f'{envelope.name.lower()}_example.flac', signal_to_store, fs)


def main():
    images_path.mkdir(exist_ok=True, parents=True)
    
    attack = Segment('Attack', 0.2, 0, 1)
    decay = Segment('Decay', 0.2, 1, 0)
    decay_adsr = Segment('Decay', 0.2, 1, 0.6)
    sustain = Segment('Sustain', 0.4, 0.6, 0.6)
    release = Segment('Release', 0.3, 0.6, 0)
    
    ad_envelope = Envelope('AD', [attack, decay])

    ar_sustain = Segment('Sustain', 0.4, 1, 1)
    ar_release = Segment('Release', 0.2, 1, 0)
    ar_envelope = Envelope('AR', [attack, ar_sustain, ar_release], key_off=0.6)

    adr_decay = Segment('Decay', 0.15, 1, 0.4)
    adr_release = Segment('Release', 0.3, 0.4, 0)
    adr_envelope = Envelope('ADR', [attack, adr_decay, adr_release], key_off=0.35)

    ads_sustain = Segment('Sustain', 0.4, 0.4, 0.4)
    ads_release = Segment('', 0.02, 0.4, 0)
    ads_envelope = Envelope('ADS', [attack, adr_decay, ads_sustain, ads_release], key_off=0.75)

    adsd_release = Segment('', 0.1, 0.4, 0)
    adsd_envelope = Envelope('ADSD', [attack, adr_decay, ads_sustain, adsd_release], key_off=0.75)

    adsr_envelope = Envelope('ADSR', [attack, decay_adsr, sustain, release], key_off=0.8)

    hold = Segment('Hold', 0.15, 1, 1)
    ahdsr_envelope = Envelope('AHDSR', [attack, hold, decay_adsr, sustain, release], key_off=0.95)

    decay1 = Segment('Decay1', 0.2, 1, 0.65)
    decay2 = Segment('Decay2', 0.4, 0.65, 0.5)
    release_adbdr = Segment('Release', 0.2, 0.5, 0)
    adbdr_envelope = Envelope('ADBDR', [attack, decay1, decay2, release_adbdr], key_off=0.8)

    for envelope in [ad_envelope, ar_envelope, adr_envelope, ads_envelope, adsd_envelope, adsr_envelope, ahdsr_envelope, adbdr_envelope]:
        plot_envelope(envelope)
        envelope_sound_example(envelope)
        
    

if __name__=='__main__':
    main()
