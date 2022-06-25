import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import subprocess
import soundfile as sf
from functools import partial
from matplotlib import animation, rc


images_path = Path('/home/jawi/Projects/WolfSound/Page/assets/img/posts/synthesis/2022-06-26-sine-saw-square-triangle-basic-waveforms-in-synthesis/')
stem_params = {'linefmt': 'C0-', 'markerfmt': 'C0o', 'basefmt': 'k'}
rc('font',**{'family':'sans-serif','sans-serif':['Verdana']})
plt.rcParams.update({'font.size': 20})
color = '#Ef7600'


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


def plot_signal_impl(waveform):
    fs = 44100
    # f = 0.06 * fs
    f = 0.01 * fs
    samples_count = 400

    t = np.arange(0, samples_count) / fs

    signal = waveform(2 * np.pi * f * t)
    
    plt.figure(figsize=(12,6))
    plt.plot(signal, color)
    plt.yticks([-1, 0, 1])
    plt.xticks([])
    plt.xlim([0, samples_count])
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    # ax.spines['left'].set_visible(False)


def plot_signal(waveform, waveform_name: str):
    plot_signal_impl(waveform)
    output_path = images_path / f'{waveform_name}_signal.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight', transparent=True)
    
    subprocess.run(['cwebp', '-q', '65', '-resize', '800', '0', output_path, '-o', output_path.with_suffix('.webp')])


def plot_spectrum_impl(waveform):
    fs = 44100
    # f = 0.06 * fs
    f = 0.03 * fs
    time_seconds = 1

    t = np.arange(0, int(fs * time_seconds)) / fs
    harmonics_count = int(np.floor((fs / 2) / f))

    signal = waveform(2 * np.pi * f * t, harmonics_count=harmonics_count)
    signal = fade_in_out(signal)

    spectrum = np.abs(np.fft.rfft(signal))
    harmonics_indices = spectrum > 70
    harmonics_indices[0] = False # ignore the DC component
    harmonics = np.arange(0, spectrum.shape[0])[harmonics_indices]
    f0 = harmonics[0]
    multiplicities_of_fundamental = np.arange(f0, harmonics[-1] + f0, f0)
    harmonics_names = [r'$\mathregular{f_0}$'] + [str(n) + r'$\mathregular{f_0}$' for n in range(2, multiplicities_of_fundamental.shape[0] + 1)]

    plt.figure(figsize=(12,6))
    markerline, stemlines, baseline = plt.stem(harmonics, spectrum[harmonics_indices], **stem_params)
    color = '#Ef7600'
    plt.setp(markerline, 'color', color)
    plt.setp(stemlines, 'color', color)
    plt.setp(baseline, visible=False)
    plt.yticks([])
    plt.xticks(multiplicities_of_fundamental, harmonics_names)
    plt.xlim([0, spectrum.shape[0]])
    plt.hlines(0, 0, spectrum.shape[0], colors='k')
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    # ax.spines['left'].set_visible(False)


def plot_spectrum(waveform, waveform_name: str):
    plot_spectrum_impl(waveform)
    output_path = images_path / f'{waveform_name}_harmonics.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight', transparent=True)
    
    subprocess.run(['cwebp', '-q', '65', '-resize', '800', '0', output_path, '-o', output_path.with_suffix('.webp')])


def generate_waveform(waveform, waveform_name):
    fs = 44100
    f = 220
    duration_seconds = 2
    harmonics_count = int(np.floor((fs / 2) / f))
    samples_count = int(duration_seconds * fs)
    samples = np.arange(0, samples_count)
    signal = waveform(2 * np.pi * f * samples / fs, harmonics_count=harmonics_count)
    signal = fade_in_out(signal)
    signal *= 0.2
    wavs_path = Path('/home/jawi/Projects/WolfSound/Page/assets/wav/posts/synthesis/2022-06-26-sine-saw-square-triangle-basic-waveforms-in-synthesis')
    output_path = wavs_path / f'{waveform_name}_example.flac'
    sf.write(output_path, signal, fs)


def ideal_square(phase):
    return np.sign(np.sin(phase))


def square(phase, harmonics_count=13):
    harmonics_count = harmonics_count // 2
    waveform = np.zeros_like(phase)
    for k in range(1, harmonics_count + 1):
        waveform += 4 / np.pi * (2 * k - 1) ** -1 * np.sin((2 * k - 1) * phase)
    return waveform


def ideal_sawtooth_ramp_up(phase):
    return ((phase % (2 * np.pi)) / np.pi) - 1


def sawtooth_ramp_up(phase, harmonics_count=26):
    waveform = np.zeros_like(phase)
    for k in range(1, harmonics_count + 1):
        waveform += 2 / np.pi * (-1) ** k * k ** -1 * np.sin(k * phase)
    return waveform


def ideal_triangle(phase):
    # return (2 * (phase % np.pi) / np.pi - 1) * np.sign(np.sin(phase))
    return 2 * np.abs(2 * (phase/(2 * np.pi) - np.floor(phase / (2 * np.pi) + 0.5))) - 1


def triangle(phase, harmonics_count=13):
    waveform = np.zeros_like(phase)
    for k in range(1, harmonics_count + 1):
        waveform += 8 / (np.pi ** 2) * (-1) ** k * (2 * k - 1) ** -2 * np.sin((2 * k - 1) * phase)
    return waveform


def pulse(phase, duty_cycle=0.2, harmonics_count=14):
    waveform = (2 * duty_cycle - 1) * np.ones_like(phase)
    for k in range(1, harmonics_count + 1):
        waveform += 4 / (k * np.pi) * np.sin(np.pi * k * duty_cycle) * np.cos(k * phase - np.pi * k * duty_cycle)
    # waveform = duty_cycle * np.ones_like(phase)
    # for k in range(1, harmonics_count + 1):
    #     waveform += 2 / (k * np.pi) * np.sin(np.pi * k * duty_cycle) * np.cos(k * phase - np.pi * k * duty_cycle)
    return waveform


def generate_pulse_video():
    fs = 44100
    # f = 0.06 * fs
    f = 0.01 * fs
    samples_count = 400

    t = np.arange(0, samples_count) / fs
    t_spectrum = np.arange(0, int(fs * 1)) / fs

    duty_cycle = 0.1

    signal = pulse(2 * np.pi * f * t, duty_cycle=duty_cycle, harmonics_count=1000)
    harmonics_count = int(np.floor((fs / 2) / f)) - 1
    signal_for_spectrum = pulse(2 * np.pi * f * t_spectrum, duty_cycle=duty_cycle, harmonics_count=harmonics_count)
    signal_for_spectrum = fade_in_out(signal_for_spectrum)

    spectrum = np.abs(np.fft.rfft(signal_for_spectrum))
    harmonics_indices = spectrum > 80
    harmonics_indices[0] = False # ignore the DC component
    harmonics = np.arange(0, spectrum.shape[0])[harmonics_indices]
    
    fig, ax = plt.subplots(2, 1)
    ax[0].plot(signal, color)
    ax[0].set_yticks([-1, 0, 1])
    ax[0].set_xticks([])
    ax[0].set_xlim([0, samples_count])
    ax[0].spines['top'].set_visible(False)
    ax[0].spines['right'].set_visible(False)
    ax[0].spines['bottom'].set_visible(False)
    ax[0].set_xlabel('Time')

    markerline, stemlines, baseline = ax[1].stem(harmonics, spectrum[harmonics_indices], **stem_params)
    plt.setp(markerline, 'color', color)
    plt.setp(stemlines, 'color', color)
    plt.setp(baseline, visible=False)
    ax[1].set_yticks([])
    ax[1].set_xticks([])
    ax[1].set_xlim([0, spectrum.shape[0]])
    ax[1].hlines(0, 0, spectrum.shape[0], colors='k')
    ax[1].spines['top'].set_visible(False)
    ax[1].spines['right'].set_visible(False)
    ax[1].spines['bottom'].set_visible(False)
    ax[1].set_xlabel('Frequency')
    plt.savefig(images_path / 'pulse_video0.png')

    frames_count = 500

    def update(i):
        progress = i / frames_count
        duty_cycle = 2 * progress if progress < 0.5 else (1 - 2 * progress) + 1

        signal = pulse(2 * np.pi * f * t, duty_cycle=duty_cycle, harmonics_count=1000)
        signal_for_spectrum = pulse(2 * np.pi * f * t_spectrum, duty_cycle=duty_cycle, harmonics_count=harmonics_count)
        signal_for_spectrum = fade_in_out(signal_for_spectrum)

        spectrum = np.abs(np.fft.rfft(signal_for_spectrum))
        harmonics_indices = spectrum > 80
        harmonics_indices[0] = False # ignore the DC component
        harmonics = np.arange(0, spectrum.shape[0])[harmonics_indices]
        
        ax[0].cla()
        ax[1].cla()
        lines = ax[0].plot(signal, color)
        ax[0].set_yticks([-1, 0, 1])
        ax[0].set_xticks([])
        ax[0].set_xlim([0, samples_count])
        ax[0].spines['top'].set_visible(False)
        ax[0].spines['right'].set_visible(False)
        ax[0].spines['bottom'].set_visible(False)
        ax[0].set_xlabel('Time')

        markerline, stemlines, baseline = ax[1].stem(harmonics, spectrum[harmonics_indices], **stem_params)
        plt.setp(markerline, 'color', color)
        plt.setp(stemlines, 'color', color)
        plt.setp(baseline, visible=False)
        ax[1].set_yticks([])
        ax[1].set_xticks([])
        ax[1].set_xlim([0, spectrum.shape[0]])
        ax[1].hlines(0, 0, spectrum.shape[0], colors='k')
        ax[1].spines['top'].set_visible(False)
        ax[1].spines['right'].set_visible(False)
        ax[1].spines['bottom'].set_visible(False)
        ax[1].set_xlabel('Frequency')

        return markerline, stemlines, baseline

    animation1 = animation.FuncAnimation(fig, update, frames=np.arange(0, frames_count), interval=8000, blit=True, repeat=False)
    FFwriter = animation.FFMpegWriter(fps=8)
    animation1.save(images_path / 'duty_cycle_visualization.mp4', writer=FFwriter)
    animation1.save(images_path / 'duty_cycle_visualization.gif', writer='imagemagick', fps=8)


def main():
    waveforms = [lambda x, harmonics_count: np.sin(x), square, sawtooth_ramp_up, triangle, partial(pulse, duty_cycle=0.2)]
    ideal_waveforms = [np.sin, ideal_square, ideal_sawtooth_ramp_up, ideal_triangle, partial(pulse, duty_cycle=0.2, harmonics_count=1000)]
    waveform_names = ['sine', 'square', 'sawtooth', 'triangle', 'pulse']

    # for waveform, waveform_name in zip(ideal_waveforms, waveform_names):
        # plot_signal(waveform, waveform_name)
    # for waveform, waveform_name in zip(waveforms, waveform_names):
        # plot_spectrum(waveform, waveform_name)
        # generate_waveform(waveform, waveform_name)

    # generate_pulse_video()


if __name__ == '__main__':
    main()
