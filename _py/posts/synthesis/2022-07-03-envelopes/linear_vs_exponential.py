import soundfile as sf
import scipy.signal as sig
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from matplotlib import rc
import subprocess


images_path = Path('/home/jawi/Projects/WolfSound/Page/assets/img/posts/synthesis/2022-07-03-envelopes/')
wav_path = Path('/home/jawi/Projects/WolfSound/Page/assets/wav/posts/synthesis/2022-07-03-envelopes/')
rc('font',**{'family':'sans-serif','sans-serif':['Verdana']})
plt.rcParams.update({'font.size': 20})
color = '#Ef7600'
grey = '#7c7c7c'

def main():
    wav_path.mkdir(exist_ok=True, parents=True)
    fs = 22050
    f = 220
    t = np.arange(0, 5 * fs) / fs
    sine = np.sin(2 * np.pi * f * t)
    window_length = 4096 * 2
    hann_window = sig.hann(window_length)
    sine[-window_length // 2:] *= hann_window[window_length // 2:]
    linear_envelope = t / np.amax(t)
    exponential_envelope = np.exp(np.linspace(np.log(1e-3), 0, t.shape[0], endpoint=True))

    fig, ax = plt.subplots(1, 2, sharey=True, figsize=(8,4))
    ax[0].plot(linear_envelope, color, linewidth=3)
    ax[1].plot(exponential_envelope, color, linewidth=3)
    for a in ax:
        a.set_xticks([0, linear_envelope.shape[0] - 1], ['start', 'end'])
        a.spines['top'].set_visible(False)
        a.spines['right'].set_visible(False)
        a.set_yticks([0, 0.5, 1])
    output_path = images_path / 'linear_vs_exponential.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    subprocess.run(['cwebp', '-q', '65', '-resize', '800', '0', output_path, '-o', output_path.with_suffix('.webp')])
    
    amplitude = 0.5
    sine_linear = sine * linear_envelope * amplitude
    sine_exponential = sine * exponential_envelope * amplitude

    sf.write(wav_path / 'linear.flac', sine_linear, fs)
    sf.write(wav_path / 'exponential.flac', sine_exponential, fs)


if __name__ == "__main__":
    main()        
