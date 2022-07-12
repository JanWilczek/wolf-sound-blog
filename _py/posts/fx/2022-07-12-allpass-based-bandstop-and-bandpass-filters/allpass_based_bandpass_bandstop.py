import numpy as np
import scipy.signal as sig
import soundfile as sf
import matplotlib.pyplot as plt
import librosa
import librosa.display
from pathlib import Path
import subprocess
from matplotlib import rc


wav_output_dir = Path('assets', 'wav', 'posts', 'fx', \
        '2022-07-12-allpass-based-bandstop-and-bandpass-filters')

img_output_dir = Path('assets', 'img', 'posts', 'fx', \
        '2022-07-12-allpass-based-bandstop-and-bandpass-filters')

rc('font',**{'family':'sans-serif','sans-serif':['Verdana']})
plt.rcParams.update({'font.size': 14})
color = '#Ef7600'
grey = '#7c7c7c'


def plot_spectrogram(signal, fs, name):
    stft = librosa.stft(signal)
    spectrogram = np.abs(stft)
    spectrogram_db = librosa.amplitude_to_db(spectrogram, ref=np.max)
    
    plt.figure(figsize=(10,4))
    img = librosa.display.specshow(spectrogram_db, y_axis='log', x_axis='time', sr=fs, cmap='inferno')
    plt.xlabel('Time [s]')
    plt.ylabel('Frequency [Hz]')
    plt.yticks([63, 125, 250, 500, 1000, 2000, 4000, 8000, 16000], ['63', '125', '250', '500', '1k', '2k', '4k', '8k', '16k'])
    plt.colorbar(img, format="%+2.f dBFS")
    output_path = img_output_dir / f'{name}.png'
    plt.savefig(output_path, bbox_inches='tight', dpi=300)
    subprocess.run(['cwebp', '-q', '65', '-resize', '800', '0', output_path, '-o', output_path.with_suffix('.webp')])
    

def second_order_allpass_filter(break_frequency, BW, fs):
    tan = np.tan(np.pi * BW / fs)
    c = (tan - 1) / (tan + 1)
    d = - np.cos(2 * np.pi * break_frequency / fs)
    
    b = [-c, d * (1 - c), 1]
    a = [1, d * (1 - c), -c]
    
    return b, a


def plot_amplitude_response(w, h, name):
    h_abs = np.abs(h)
    h_normalized = h_abs / np.amax(h_abs)
    h_db = 20 * np.log10(np.maximum(h_normalized, 1e-6))
    plt.figure(figsize=(6,3))
    plt.semilogx(w, h_db, color, linewidth=3)
    plt.xticks([63, 125, 250, 500, 1000, 2000, 4000, 8000, 16000], ['63', '125', '250', '500', '1k', '2k', '4k', '8k', '16k'])
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Magnitude [dB]')
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.xlim([50, 20000])
    plt.ylim([-25, 1])
    output_path = img_output_dir / f'{name}.png'
    plt.savefig(output_path, bbox_inches='tight', dpi=300)
    subprocess.run(['cwebp', '-q', '65', '-resize', '800', '0', output_path, '-o', output_path.with_suffix('.webp')])


def bandstop_bandpass_filter(input_signal, Q, center_frequency, fs, bandpass=False):
    allpass_filtered = np.zeros_like(input_signal)
    
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    
    for i in range(input_signal.shape[0]):
        BW = Q * center_frequency[i]
        
        b, a = second_order_allpass_filter(center_frequency[i], BW, fs)
        
        x = input_signal[i]
        
        y = b[0] * x + b[1] * x1 +  b[2] * x2 - a[1] * y1 - a[2] * y2
        
        y2 = y1
        y1 = y
        x2 = x1
        x1 = x
        
        allpass_filtered[i] = y
    
    sign = -1 if bandpass else 1
    
    output = 0.5 * (input_signal + sign * allpass_filtered)

    return output


def main():
    wav_output_dir.mkdir(exist_ok=True, parents=True)
    img_output_dir.mkdir(exist_ok=True, parents=True)
    
    fs = 44100
    length_seconds = 6
    length_samples = fs * length_seconds
    Q = 0.3
    center_frequency = np.geomspace(100, 16000, length_samples)
    noise = np.random.default_rng().uniform(-1, 1, (length_samples,))
    
    bandstop_filtered_noise = bandstop_bandpass_filter(noise, Q, center_frequency, fs)
    bandpass_filtered_noise = bandstop_bandpass_filter(noise, Q, center_frequency, fs, bandpass=True)
    
    amplitude = 0.5
    bandstop_filtered_noise *= amplitude
    bandpass_filtered_noise *= amplitude
    
    bandstop_filtered_noise = apply_fade(bandstop_filtered_noise)
    bandpass_filtered_noise = apply_fade(bandpass_filtered_noise)
    
    plot_spectrogram(bandstop_filtered_noise, fs, 'bandstop_example')
    plot_spectrogram(bandpass_filtered_noise, fs, 'bandpass_example')
    
    plot_center_frequency = 250
    plot_BW = Q * plot_center_frequency
    b, a = second_order_allpass_filter(plot_center_frequency, plot_BW, fs)
    w, h = sig.freqz(b, a, fs=fs, worN=2048)
    
    h_bandstop = 0.5 * (1 + h)
    h_bandpass = 0.5 * (1 - h)
    
    plot_amplitude_response(w, h_bandstop, 'bandstop_amplitude_response')
    plot_amplitude_response(w, h_bandpass, 'bandpass_amplitude_response')
    
    sf.write(wav_output_dir / 'bandstop_filtered_noise.flac', bandstop_filtered_noise, fs)
    sf.write(wav_output_dir / 'bandpass_filtered_noise.flac', bandpass_filtered_noise, fs)
    

def apply_fade(signal):
    window = sig.hann(8192)
    fade_length = window.shape[0] // 2
    signal[:fade_length] *= window[:fade_length]
    signal[-fade_length:] *= window[fade_length:]
    return signal


if __name__=='__main__':
    main()
