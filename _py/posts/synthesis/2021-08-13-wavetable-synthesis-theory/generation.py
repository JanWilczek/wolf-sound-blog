import numpy as np
from pathlib import Path
from scipy.io import wavfile
from Fader import Fader
from plot import stem, magnitude_spectrum, plot, setup_pyplot_for_latex


class Oscillator():
    def __init__(self):
        self.__frequency = 0
    
    @property
    def frequency(self):
        return self.__frequency

    @frequency.setter
    def frequency(self, value):
        self.__frequency = value

    def fill(self, audio_block, from_index, to_index):
        pass

class LinearInterpolator():
    def __call__(self, values, index):
        low = int(index)
        high = int(np.ceil(index))
        if low == high:
            return values[low]
        return (index - low) * values[high % values.shape[0]] + (high - index) * values[low]

class ZeroOrderInterpolator():
    def __call__(self, values, index):
        return values[int(index)]

class WavetableOscillator(Oscillator):
    def __init__(self, wavetable, sampling_rate, interpolator):
        self.wavetable = wavetable
        self.sampling_rate = sampling_rate
        self.interpolator = interpolator
        self.wavetable_index = 0.0

    def fill(self, audio_block, from_index=0, to_index=-1):
        for i in range(from_index, to_index % audio_block.shape[0]):
            audio_block[i] = self.interpolator(self.wavetable, self.wavetable_index)
            self.wavetable_index = (self.wavetable_index + self.wavetable_increment) % self.wavetable.shape[0]
        return audio_block

    @property
    def frequency(self):
        return self.__frequency

    @frequency.setter
    def frequency(self, value):
        self.__frequency = value
        self.wavetable_increment = self.wavetable.shape[0] * self.frequency / self.sampling_rate

def generate_wavetable(length, f):
    """Period of f is assumed to be 2 pi."""
    wavetable = np.zeros((length,), dtype=np.float32)
    for i in range(length):
        wavetable[i] = f(2 * np.pi * i / length)
    return wavetable

def synthesize(wave_table, frequency, duration_seconds, sampling_rate):
    osc = WavetableOscillator(wave_table, sampling_rate, LinearInterpolator())
    osc.frequency = frequency
    samples = osc.fill(np.zeros((duration_seconds * sampling_rate,), dtype=np.float32))
    gain = -10
    amplitude = 10 ** (gain / 20)
    samples *= amplitude
    return samples

def output_all(signal_no_fade, name, fs, table):
    fader = Fader(fs//4, fs//4)
    signal = fader.fade_in_out(signal_no_fade)

    # Output
    output_dir = Path('assets', 'wav', 'posts', 'synthesis', '2021-08-13-wavetable-synthesis-theory')
    output_dir.mkdir(parents=True, exist_ok=True)

    wavfile.write(output_dir / f'{name}.wav', fs, signal)

    img_output_dir = Path('assets', 'img', 'posts', 'synthesis', '2021-08-13-wavetable-synthesis-theory')
    n = np.arange(table.shape[0])
    stem(n, table, f'{name}_wave_table', img_output_dir, xlabel='Index', ylabel='Amplitude')

    signal_1s = fader.fade_in_out(signal_no_fade[:fs])
    S = magnitude_spectrum(signal_1s, normalize_spectrum=True)
    f = np.fft.rfftfreq(signal_1s.shape[0], 1/fs)
    ylim = [-60, 0]
    plot(f, S, f'{name}_spectrum', img_output_dir, color='C1', xlabel='Frequency [Hz]', ylabel='Magnitude [dB]', ylim=ylim)

def main():
    setup_pyplot_for_latex()
    fs = 44100

    # Sine generation
    sine_table = generate_wavetable(64, np.sin)
    sine_no_fade = synthesize(sine_table, 440, 5, fs)
    output_all(sine_no_fade, 'sine', fs, sine_table)

    # Sawtooth generation
    sawtooth_table = generate_wavetable(64, lambda x: (x + np.pi) / np.pi % 2 - 1)
    sawtooth_no_fade = synthesize(sawtooth_table, 440, 5, fs)
    output_all(sawtooth_no_fade, 'sawtooth', fs, sawtooth_table)

    sawtooth880_no_fade = synthesize(sawtooth_table, 880, 5, fs)
    output_all(sawtooth880_no_fade, 'sawtooth880', fs, sawtooth_table)
    

if __name__=='__main__':
    main()
