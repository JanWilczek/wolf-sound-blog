import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import subprocess


def fade_in_out(signal, fade_length=100):
    """
    Apply a half-cosine window to first and 
    last fade_length samples of signal.
    """
    fade_in_envelope = (1 - np.cos(np.linspace(0, np.pi, fade_length))) * 0.5
    fade_out_envelope = np.flip(fade_in_envelope)

    # Handle 2-channel audio
    if signal.ndim == 2:
        fade_in_envelope = fade_in_envelope[:, np.newaxis]
        fade_out_envelope = fade_out_envelope[:, np.newaxis]

    # Apply fade-in
    signal[:fade_length, ...] = np.multiply(
        signal[:fade_length, ...], fade_in_envelope)

    # Apply fade-out
    signal[-fade_length:, ...] = np.multiply(
        signal[-fade_length:, ...], fade_out_envelope)

    return signal


def main():
    plt.rcParams.update({'font.size': 18})
    stem_params = {'linefmt': 'C0-', 'markerfmt': 'C0o', 'basefmt': 'k'}
    
    fs = 2000
    f = 120
    time_seconds = 2
    images_path = Path('/home/jawi/Projects/WolfSound/Page/assets/img/posts/synthesis/2022-06-26-sine-saw-square-triangle-basic-waveforms-in-synthesis/')

    t = np.arange(0, int(fs * time_seconds)) / fs

    signal = np.sin(2 * np.pi * f * t)

    plot_samples_count = 40
    
    plt.figure(figsize=(12,6))
    markerline, stemlines, baseline = plt.stem(signal[:plot_samples_count], **stem_params)
    color = '#Ef7600'
    plt.setp(markerline, 'color', color)
    plt.setp(stemlines, 'color', color)
    plt.yticks([-1, 0, 1])
    plt.xticks([])
    plt.xlim([0, plot_samples_count])
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    # ax.spines['left'].set_visible(False)
    output_path = images_path / 'sine_signal.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight', transparent=True)
    
    subprocess.run(['cwebp', '-q', '65', '-resize', '800', '0', output_path, '-o', output_path.with_suffix('.webp')])

    signal = fade_in_out(signal)

    spectrum = np.abs(np.fft.rfft(signal))
    harmonics_indices = spectrum > 100
    harmonics = np.arange(0, spectrum.shape[0])[harmonics_indices]
    harmonics_names = ['f0'] + [f'{n}f0' for n in range(2, harmonics.shape[0] + 1)]

    plt.figure(figsize=(12,6))
    markerline, stemlines, baseline = plt.stem(harmonics, spectrum[harmonics_indices], **stem_params)
    color = '#Ef7600'
    plt.setp(markerline, 'color', color)
    plt.setp(stemlines, 'color', color)
    plt.setp(baseline, visible=False)
    plt.yticks([])
    plt.xticks(harmonics, harmonics_names)
    plt.xlim([0, spectrum.shape[0]])
    plt.hlines(0, 0, spectrum.shape[0], colors='k')
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    # ax.spines['left'].set_visible(False)
    output_path = images_path / 'sine_harmonics.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight', transparent=True)
    
    subprocess.run(['cwebp', '-q', '65', '-resize', '800', '0', output_path, '-o', output_path.with_suffix('.webp')])


if __name__ == '__main__':
    main()
