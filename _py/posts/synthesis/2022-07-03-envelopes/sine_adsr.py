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


def generate_sine_enveloped(f, fs):
    length_seconds = 3
    length_samples = length_seconds * fs
    t = np.arange(0, length_samples) / fs
    sine = np.sin(2 * np.pi * f * t)

    attack = 0.15
    decay = 0.05
    sustain = 0.5
    release = 0.4

    attack_length_samples = int(attack * length_samples)
    decay_length_samples = int(decay * length_samples)
    release_length_samples = int(release * length_samples)

    attack = np.exp(np.linspace(np.log(1e-3), 0, attack_length_samples, endpoint=True))
    decay = np.exp(np.linspace(0, np.log(sustain), decay_length_samples, endpoint=True))
    release = np.exp(np.linspace(np.log(sustain), np.log(1e-3), release_length_samples, endpoint=True))

    envelope = sustain * np.ones_like(sine)

    envelope[:attack_length_samples] = attack
    envelope[attack_length_samples:(attack_length_samples + decay_length_samples)] = decay
    envelope[-release_length_samples:] = release

    sine_enveloped = sine * envelope

    return sine_enveloped, envelope


def main():
    wav_path.mkdir(exist_ok=True, parents=True)
    fs = 22050

    sine_enveloped, envelope = generate_sine_enveloped(220, fs)
    sine_enveloped_plot, envelope = generate_sine_enveloped(20, fs)

    plt.figure(figsize=(8,4))
    plt.plot(sine_enveloped_plot, grey, linewidth=1)
    plt.plot(envelope, color, linewidth=3)
    plt.plot(-envelope, color, linewidth=3)
    a = plt.gca()
    a.spines['top'].set_visible(False)
    a.spines['right'].set_visible(False)
    a.set_yticks([-1, -0.5, 0, 0.5, 1])
    plt.xticks([])
    plt.ylabel('amplitude')
    plt.xlabel('time')
    output_path = images_path / 'sine_adsr.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    subprocess.run(['cwebp', '-q', '65', '-resize', '800', '0', output_path, '-o', output_path.with_suffix('.webp')])
    
    amplitude = 0.5
    signal_to_store = amplitude * sine_enveloped

    sf.write(wav_path / 'sine_adsr.flac', signal_to_store, fs)


if __name__ == "__main__":
    main()        
