import numpy as np
from pathlib import Path
from scipy.io import wavfile


def fade_in_out(signal, fade_length=1000):
    fade_in_envelope = (1 - np.cos(np.linspace(0, np.pi, fade_length))) * 0.5
    fade_out_envelope = np.flip(fade_in_envelope)
    
    if signal.ndim == 2:
        fade_in_envelope = fade_in_envelope[:, np.newaxis]
        fade_out_envelope = fade_out_envelope[:, np.newaxis]

    signal[:fade_length, ...] = np.multiply(signal[:fade_length, ...], fade_in_envelope)
    signal[-fade_length:, ...] = np.multiply(signal[-fade_length:, ...], fade_out_envelope)

    return signal

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

class WavetableOscillator:
    def __init__(self, wavetable, sampling_rate, interpolator):
        self.wavetable = wavetable
        self.sampling_rate = sampling_rate
        self.interpolator = interpolator
        self.wavetable_index = 0.0
        self.__frequency = 0

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

def synthesize(wave_table, frequency, duration_seconds, sampling_rate, gain=-20):
    osc = WavetableOscillator(wave_table, sampling_rate, LinearInterpolator())
    osc.frequency = frequency
    samples = osc.fill(np.zeros((duration_seconds * sampling_rate,), dtype=np.float32))
    amplitude = 10 ** (gain / 20)
    samples *= amplitude
    samples = fade_in_out(samples)
    return samples

def synthesize_with_instantaneous_frequency(wave_table, instantaneous_frequency, duration_seconds, sampling_rate, gain=-20):
    osc = WavetableOscillator(wave_table, sampling_rate, LinearInterpolator())
    buffer = np.zeros((duration_seconds * sampling_rate,), dtype=np.float32)
    for i in range(len(buffer)):
        osc.frequency = instantaneous_frequency[i]
        osc.fill(buffer, i, i+1)
    amplitude = 10 ** (gain / 20)
    buffer *= amplitude
    buffer = fade_in_out(buffer)
    return buffer

def output_all(signal, name, sampling_rate, table):
    # Output
    output_dir = Path('assets', 'wav', 'posts', 'synthesis', '2021-08-27-wavetable-synthesis-python')
    output_dir.mkdir(parents=True, exist_ok=True)

    wavfile.write(output_dir / f'{name}_table.wav', sampling_rate, table)
    wavfile.write(output_dir / f'{name}.wav', sampling_rate, signal)

def generate_gaussians_table():
    def gaussian_mixture(x):
        return np.exp(-3*(x-1)**2) \
            - 0.4 * np.exp(-3*(x-2.3)**2) \
            + 0.8 * np.exp(-10*(x-3.3)**2) \
            - np.exp(-7*(x-4.5)**2) \
            + 0.3 * np.exp(-2 * (x-5)**2)

    gaussians_table = generate_wavetable(wavetable_size, gaussian_mixture)
    gaussians_table -= np.mean(gaussians_table)
    gaussians_table = fade_in_out(gaussians_table, 5)
    return gaussians_table

def main():
    sampling_rate = 44100
    wavetable_size = 64

    # Sine generation
    sine_table = generate_wavetable(wavetable_size, np.sin)
    sine = synthesize(sine_table, 440, 5, sampling_rate)
    output_all(sine, 'sine', sampling_rate, sine_table)

    # # Sawtooth generation
    def sawtooth(x):
        """Sawtooth with period 2 pi."""
        return (x + np.pi) / np.pi % 2 - 1

    sawtooth_table = generate_wavetable(wavetable_size, sawtooth)
    sawtooth_signal = synthesize(sawtooth_table, 440, 5, sampling_rate)
    output_all(sawtooth_signal, 'sawtooth', sampling_rate, sawtooth_table)

    sawtooth880 = synthesize(sawtooth_table, 880, 5, sampling_rate)
    output_all(sawtooth880, 'sawtooth880', sampling_rate, sawtooth_table)

    # Gaussian mixture generation
    gaussians_table = generate_gaussians_table()
    gaussians_waveform = synthesize(gaussians_table, 110, 5, sampling_rate)
    output_all(gaussians_waveform, 'gaussians', sampling_rate, gaussians_table)

    # Multi-cycle waveform generation
    square_table = generate_wavetable(wavetable_size, lambda x: np.sign(np.sin(x)))
    multi_cycle_table = np.concatenate((sine_table, square_table, sawtooth_table))
    multi_cycle = synthesize(multi_cycle_table, 330, 5, sampling_rate)
    output_all(multi_cycle, 'multi_cycle', sampling_rate, multi_cycle_table)

    # Continuous frequency control
    duration = 20
    min_frequency = 20
    max_frequency = 3000
    base = (max_frequency / min_frequency) ** (1 / (duration // 2 * sampling_rate))
    instantaneous_frequency_half = min_frequency * base ** np.arange(0, duration // 2 * sampling_rate, 1)
    instantaneous_frequency = np.concatenate((instantaneous_frequency_half, np.flip(instantaneous_frequency_half)))
    instantaneous_frequency += np.multiply(instantaneous_frequency, np.random.default_rng().uniform(-0.1, 0.1, size=instantaneous_frequency.shape))

    signal_with_varying_frequency = synthesize_with_instantaneous_frequency(gaussians_table, instantaneous_frequency, duration, sampling_rate)
    output_all(signal_with_varying_frequency, 'instantaneous_frequency', sampling_rate, gaussians_table)

if __name__=='__main__':
    main()
