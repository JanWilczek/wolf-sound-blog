import librosa
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from scipy.special import jv
from pathlib import Path

from dspyplot import style
from dspyplot.audiofile import save_audio_file_with_normalization
from dspyplot.dft import magnitude_spectrum, dft_frequencies
from dspyplot.constants import img_output_path
from dspyplot.plot import (
    plot_spectrum_and_save,
    save,
    save_spectrum,
    PlotPeriodCommand,
    plot_signal_and_save,
)
from dspyplot.signals import apply_fade, generate_sine

AUDIO_OUTPUT_PATH = Path("assets/wav/posts/synthesis/2025-03-01-fm-synthesis")
IMG_OUTPUT_PATH = Path("assets/img/posts/synthesis/2025-03-01-fm-synthesis")

SAMPLE_RATE = 44100


def vibrato_example():
    carrier_amplitude = 1
    carrier_frequency = librosa.midi_to_hz(57)
    modulator_frequency = 6
    modulation_index = 2
    time = np.arange(0, 5, 1 / SAMPLE_RATE)

    plain_note = carrier_amplitude * np.sin(2 * np.pi * carrier_frequency * time)
    pm_modulated_note = generate_simple_pm(
        carrier_amplitude,
        carrier_frequency,
        modulation_index,
        modulator_frequency,
        time,
    )
    fm_modulated_note = generate_simple_fm(
        carrier_amplitude,
        carrier_frequency,
        modulation_index,
        modulator_frequency,
        SAMPLE_RATE,
        time,
    )

    plain_note = apply_fade(plain_note, 1000)
    pm_modulated_note = apply_fade(pm_modulated_note, 1000)
    fm_modulated_note = apply_fade(fm_modulated_note, 1000)

    save_audio_file_with_normalization(
        AUDIO_OUTPUT_PATH / f"plain_note_{carrier_frequency:.0f}Hz.flac",
        plain_note,
        SAMPLE_RATE,
    )
    save_audio_file_with_normalization(
        AUDIO_OUTPUT_PATH / f"pm_vibrato_note_{carrier_frequency:.0f}Hz.flac",
        pm_modulated_note,
        SAMPLE_RATE,
    )
    save_audio_file_with_normalization(
        AUDIO_OUTPUT_PATH / f"fm_vibrato_note_{carrier_frequency:.0f}Hz.flac",
        fm_modulated_note,
        SAMPLE_RATE,
    )


def generate_simple_fm(
    carrier_amplitude,
    carrier_frequency,
    modulation_index,
    modulator_frequency,
    sample_rate,
    time,
):
    frequency_over_time = (
        carrier_frequency
        + modulation_index
        * modulator_frequency
        * np.cos(2 * np.pi * modulator_frequency * time)
    )
    fm_modulated_note = carrier_amplitude * np.sin(
        2 * np.pi * np.cumsum(frequency_over_time) / sample_rate
    )
    return fm_modulated_note


def generate_simple_pm(
    carrier_amplitude, carrier_frequency, modulation_index, modulator_frequency, time
):
    pm_modulated_note = carrier_amplitude * np.sin(
        2 * np.pi * carrier_frequency * time
        + modulation_index * np.sin(2 * np.pi * modulator_frequency * time)
    )
    return pm_modulated_note


def fm_example_1():
    carrier_amplitude = 1
    carrier_frequency = librosa.midi_to_hz(57)
    modulator_frequency = carrier_frequency / 2
    modulation_index = 2
    time = np.arange(0, 5, 1 / SAMPLE_RATE)

    wrong_fm = carrier_amplitude * np.sin(
        2
        * np.pi
        * (
            carrier_frequency
            + modulation_index
            * modulator_frequency
            * np.cos(2 * np.pi * modulator_frequency * time)
        )
        * time
    )
    postprocess_and_save_audio_file(
        f"wrong_fm_{carrier_frequency:.0f}Hz.flac", wrong_fm
    )

    proper_fm = generate_simple_fm(
        carrier_amplitude,
        carrier_frequency,
        modulation_index,
        modulator_frequency,
        SAMPLE_RATE,
        time,
    )
    postprocess_and_save_audio_file(
        f"proper_fm_{carrier_frequency:.0f}Hz.flac", proper_fm
    )


def postprocess_and_save_audio_file(file_name: str, signal, sample_rate=SAMPLE_RATE):
    save_audio_file_with_normalization(AUDIO_OUTPUT_PATH / file_name, signal, sample_rate)


def modulation_index_motivation():
    time = np.arange(0, 5, 1 / SAMPLE_RATE)
    basic_signal = generate_simple_fm(
        carrier_amplitude=1,
        carrier_frequency=200,
        modulation_index=2,
        modulator_frequency=400,
        time=time,
        sample_rate=SAMPLE_RATE,
    )
    octave_higher = generate_simple_fm(
        carrier_amplitude=1,
        carrier_frequency=400,
        modulation_index=2,
        modulator_frequency=800,
        time=time,
        sample_rate=SAMPLE_RATE,
    )
    octave_higher_half_index = generate_simple_fm(
        carrier_amplitude=1,
        carrier_frequency=400,
        modulation_index=1,
        modulator_frequency=800,
        time=time,
        sample_rate=SAMPLE_RATE,
    )

    basic_signal_name = "basic_signal"
    octave_higher_name = "octave_higher"
    octave_higher_half_index_name = "octave_higher_half_index"

    postprocess_and_save_audio_file(basic_signal_name, basic_signal)
    postprocess_and_save_audio_file(octave_higher_name, octave_higher)
    postprocess_and_save_audio_file(
        octave_higher_half_index_name, octave_higher_half_index
    )

    basic_signal_magnitude_spectrum = magnitude_spectrum(basic_signal)
    frequencies = dft_frequencies(basic_signal_magnitude_spectrum.shape[0], SAMPLE_RATE)
    plot_kwargs = dict(frequencies=frequencies, xlim=[0, 5000])
    plot_spectrum_and_save(
        basic_signal_magnitude_spectrum,
        IMG_OUTPUT_PATH / basic_signal_name,
        **plot_kwargs,
    )
    plot_spectrum_and_save(
        magnitude_spectrum(octave_higher),
        IMG_OUTPUT_PATH / octave_higher_name,
        **plot_kwargs,
    )
    plot_spectrum_and_save(
        magnitude_spectrum(octave_higher_half_index),
        IMG_OUTPUT_PATH / octave_higher_half_index_name,
        **plot_kwargs,
    )


def simple_fm_spectrum():
    time = np.arange(0, 5, 1 / SAMPLE_RATE)
    carrier_frequency = 1000
    modulator_frequency = 300
    time_domain_signal = generate_simple_fm(
        carrier_amplitude=1,
        carrier_frequency=carrier_frequency,
        modulation_index=1,
        modulator_frequency=modulator_frequency,
        time=time,
        sample_rate=SAMPLE_RATE,
    )
    m = magnitude_spectrum(time_domain_signal)
    frequencies = dft_frequencies(m.shape[0], SAMPLE_RATE)

    xticks = [carrier_frequency + i * modulator_frequency for i in range(-3, 4)]
    xtick_labels = [
        f'$f_C {"+" if i > 0 else "-"} {abs(i) if abs(i) != 1 else ""}f_M$'
        for i in range(-3, 4)
    ]
    xtick_labels[3] = "$f_C$"
    plot_spectrum_and_save(
        m,
        IMG_OUTPUT_PATH / "simple_fm",
        frequencies,
        xlim=[0, 2000],
        xticks=xticks,
        xtick_labels=xtick_labels,
    )


def timbre_control_example():
    pass


def fm_vs_pm_modulation():
    # Plot "standard FM" spectrum for c : m = 1 : 2 and I = pi
    # Plot original FM for the same parameters at the same sampling rate
    # If the above are not different decrease the sampling rate
    carrier_frequency = 200
    modulator_frequency = 400
    modulation_index = np.pi
    for sample_rate in [22050, 96000]:
        time = np.arange(0, 5, 1 / sample_rate)
        standard_fm = generate_simple_fm(
            1,
            carrier_frequency,
            modulation_index,
            modulator_frequency,
            sample_rate,
            time,
        )
        pm = generate_simple_pm(
            1, carrier_frequency, modulation_index, modulator_frequency, time
        )

        pm_file_name = f"pm_fs_{sample_rate}"
        fm_file_name = f"fm_fs_{sample_rate}"

        postprocess_and_save_audio_file(pm_file_name, pm, sample_rate)
        postprocess_and_save_audio_file(
            fm_file_name, standard_fm, sample_rate
        )

        standard_fm_spectrum = magnitude_spectrum(standard_fm)
        pm_spectrum = magnitude_spectrum(pm)
        frequencies = dft_frequencies(standard_fm_spectrum.shape[0], sample_rate)

        plt.figure(figsize=(12, 6))
        plt.plot(frequencies, standard_fm_spectrum, style.color)
        plt.plot(frequencies, pm_spectrum, style.complementary_color_1, linestyle="--")
        xlim = [frequencies[0], 5000]
        plt.xlim(xlim)
        plt.xlabel("frequency [Hz]")
        plt.hlines(0, xlim[0], xlim[1], colors="k")
        plt.yticks([])
        plt.ylabel("magnitude")
        ax = plt.gca()
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["bottom"].set_visible(False)
        plt.legend(["frequency modulation", "phase modulation"])
        save_spectrum(IMG_OUTPUT_PATH / f"fm_vs_pm_modulation_fs_{sample_rate}")
        plt.close()


def fm_vs_pm_modulation_2():
    carrier_frequency = 600
    modulator_frequency = 50
    modulation_index = 10
    sample_rate = SAMPLE_RATE
    LENGTH_SECONDS = 0.2
    time = np.arange(0, LENGTH_SECONDS, 1 / sample_rate)

    carrier = generate_sine(carrier_frequency, LENGTH_SECONDS, sample_rate, 0)
    modulator = generate_sine(modulator_frequency, LENGTH_SECONDS, sample_rate, 0)

    standard_fm = generate_simple_fm(
        1,
        carrier_frequency,
        modulation_index,
        modulator_frequency,
        sample_rate,
        time,
    )
    pm = generate_simple_pm(
        1, carrier_frequency, modulation_index, modulator_frequency, time
    )

    pm_file_name = f"pm_fs_2_{sample_rate}"
    fm_file_name = f"fm_fs_2_{sample_rate}"

    plot_signal_and_save(pm, IMG_OUTPUT_PATH / pm_file_name)
    plot_signal_and_save(standard_fm, IMG_OUTPUT_PATH / fm_file_name)

    # Plot carrier, modulator, FM, and PM on a single plot
    signals = [carrier, modulator, standard_fm, pm]
    signal_ylabels = ["carrier", "modulator", "FM", "PM"]
    signal_styles = [dict(color=style.color, linestyle="-") for _ in signals]
    yticks = []

    plt.figure(figsize=(12, 6))
    for i, (signal, ylabel, signal_style) in enumerate(zip(signals, signal_ylabels, signal_styles)):
        plt.subplot(4, 1, i+1)
        plt.plot(signal, **signal_style)
        samples_count = signal.shape[0]
        xlim = [0, samples_count]
        plt.xlim(xlim)
        plt.xticks([])
        plt.yticks(yticks)
        plt.ylabel(ylabel)
    plt.xlabel("time")

    ax = plt.gca()
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_visible(False)

    save(IMG_OUTPUT_PATH / "carrier_modulator_fm_pm", "_signal")


def harmonic_and_inharmonic_spectra_example():
    for c, m, pitch in [
        (1, 2, 200),
        (2, 1, 200),
        (10, 9, 200),
        (np.sqrt(2), 1, 200),
        (1000, 637, 200),
    ]:
        signal = generate_simple_pm_with_ratio(c=c, m=m, pitch=pitch)
        formatted_c = f"{c:.0f}" if isinstance(c, int) else f"{c:.2f}"
        file_name = f"c_{formatted_c}_m_{m}_f0_{pitch}.flac"
        postprocess_and_save_audio_file(file_name, signal)
        spectrum = magnitude_spectrum(signal)
        frequencies = dft_frequencies(spectrum.shape[0], SAMPLE_RATE)
        xlim = [0, 2500]
        if c == 10 and m == 9:
            xlim[1] = 10000
        plot_spectrum_and_save(
            spectrum, IMG_OUTPUT_PATH / file_name, frequencies, xlim=xlim
        )


def generate_simple_pm_with_ratio(
    c: int, m: float, pitch: float, modulation_index=np.pi
):
    carrier_amplitude = 1
    time = np.arange(0, 5, 1 / SAMPLE_RATE)
    return generate_simple_pm(
        carrier_amplitude, pitch * c, modulation_index, pitch * m, time
    )


def eliminating_every_nth_partial_example():
    pitch = 1000
    for c, m, pitch in [
        (5, 1, pitch),
        (5, 2, pitch),
        (5, 3, pitch),
        (5, 4, pitch),
        (5, 5, pitch),
    ]:
        signal = generate_simple_pm_with_ratio(
            c=c, m=m, pitch=pitch, modulation_index=2
        )
        file_name = f"c_{c}_m_{m}_f0_{pitch}"
        postprocess_and_save_audio_file(file_name, signal)
        spectrum = magnitude_spectrum(signal)
        frequencies = dft_frequencies(spectrum.shape[0], SAMPLE_RATE)
        plot_spectrum_and_save(
            spectrum, IMG_OUTPUT_PATH / file_name, frequencies, xlim=[0, 10000]
        )


def apply_adsr_envelope(
    signal,
    attack_time: float,
    decay_time: float,
    sustain_level: float,
    release_time: float,
    sample_rate=SAMPLE_RATE,
):
    attack_length_samples = int(attack_time * sample_rate)
    decay_length_samples = int(decay_time * sample_rate)
    release_length_samples = int(release_time * sample_rate)
    assert (
        attack_length_samples + decay_length_samples + release_length_samples
        <= signal.shape[0]
    )
    sustain_start = attack_length_samples + decay_length_samples
    alpha = 5
    attack_curve = np.exp(
        np.linspace(np.log(1e-3), 0, attack_length_samples, endpoint=True)
    )
    # plot_signal_and_save(attack_curve, IMG_OUTPUT_PATH / 'attack_curve')
    decay_curve = sustain_level + (1 - sustain_level) * np.exp(
        -np.arange(decay_length_samples) * alpha / decay_length_samples
    )
    # plot_signal_and_save(decay_curve, IMG_OUTPUT_PATH / 'decay_curve')
    release_curve = sustain_level * np.exp(
        -np.arange(release_length_samples) * alpha / release_length_samples
    )
    # plot_signal_and_save(release_curve, IMG_OUTPUT_PATH / 'release_curve')
    signal[:attack_length_samples] *= attack_curve
    signal[attack_length_samples:sustain_start] *= decay_curve
    signal[sustain_start:-release_length_samples] *= sustain_level
    signal[-release_length_samples:] = release_curve
    return signal


def cool_sounds():
    for c, m, pitch, modulation_index in [(1, 0.99, 200, np.pi)]:
        signal = generate_simple_pm_with_ratio(
            c=c, m=m, pitch=pitch, modulation_index=modulation_index
        )
        file_name = f"c_{c}_m_{m}_f0_{pitch}_I_{modulation_index}.flac"
        postprocess_and_save_audio_file(file_name, signal)
    brass_like_sound = 0.5 * generate_simple_pm_with_ratio(1, 1, 440, 5)
    postprocess_and_save_audio_file("brass_like", brass_like_sound)

    sample_rate = 44100
    time = np.arange(0, 2, 1 / sample_rate)
    brass_like_sound = 0.5 * np.sin(
        2 * np.pi * 440 * time + 5 * np.sin(2 * np.pi * 440 * time)
    )
    save_audio_file_with_normalization(
        AUDIO_OUTPUT_PATH / "brass_like_sound.mp3", brass_like_sound, sample_rate
    )

    electric_piano = apply_adsr_envelope(
        generate_simple_pm_with_ratio(1, 3, 220, 5),
        attack_time=0.01,
        decay_time=0.2,
        sustain_level=0.7,
        release_time=0.3,
    )
    plot_signal_and_save(electric_piano, IMG_OUTPUT_PATH / "electric_piano")
    postprocess_and_save_audio_file("electric_piano", electric_piano)


def spectrum_brightness_example():
    for modulation_index in [1, 2, 3, 4, 5]:
        c = 5
        m = 1
        pitch = 200
        signal = generate_simple_pm_with_ratio(
            c=c, m=m, pitch=pitch, modulation_index=modulation_index
        )
        file_name = f"c_{c}_m_{m}_f0_{pitch:.0f}_I_{modulation_index}"
        postprocess_and_save_audio_file(file_name, signal)
        spectrum = magnitude_spectrum(signal)
        frequencies = dft_frequencies(spectrum.shape[0], SAMPLE_RATE)
        spectrum_bandwidth = 2 * m * pitch * (modulation_index + 1)
        carrier_frequency = c * pitch
        lower_spectrum_boundary = carrier_frequency - spectrum_bandwidth // 2
        upper_spectrum_boundary = carrier_frequency + spectrum_bandwidth // 2

        spectrum_height = np.max(np.abs(spectrum))
        extra_command = PlotPeriodCommand(
            lower_spectrum_boundary,
            spectrum_bandwidth,
            arrows_y=spectrum_height * 1.05,
            label_text=f"{spectrum_bandwidth:.0f}" + r"$\text{ Hz}$",
            head_width=spectrum_height * 0.01,
            head_length=spectrum_height * 0.003,
        )

        plot_spectrum_and_save(
            spectrum,
            IMG_OUTPUT_PATH / file_name,
            frequencies,
            xlim=[0, 10000],
            extra_command=extra_command,
        )


def plot_bessel_functions():
    xlim = [-10, 10]
    x = np.arange(*xlim, 0.1)
    legend = []

    plt.figure()
    for order, color in enumerate(style.color_palette[:4]):
        bessel_function_first_kind = jv(order, x)
        plt.plot(x, bessel_function_first_kind, color)
        legend.append(f"$J_{order}(I)$")
    plt.hlines(0, *xlim, "k")
    plt.xlim(xlim)
    plt.ylim([-1, 1.1])
    plt.xlabel("$I$")
    plt.legend(legend, loc="lower right")
    ax = plt.gca()
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    save(IMG_OUTPUT_PATH / "bessel_functions_first_kind")


def plot_partials_amplitudes_in_3d():
    modulation_index = np.arange(0, 20, 0.1)
    base_level = -1
    ylim = [0, 20]

    ax = plt.figure(figsize=(12, 8)).add_subplot(projection="3d")
    for partial_id in reversed(range(*ylim)):
        partial_amplitude = jv(partial_id, modulation_index)
        vertices = [
            (modulation_index[i], partial_id, partial_amplitude[i])
            for i in range(len(modulation_index))
        ]
        vertices += [
            (modulation_index.max(), partial_id, base_level),
            (modulation_index.min(), partial_id, base_level),
        ]
        ax.add_collection3d(
            Poly3DCollection([vertices], color="white", edgecolor=style.color)
        )
        ax.plot(
            modulation_index,
            partial_id * np.ones_like(modulation_index),
            partial_amplitude,
            color=style.color,
            zorder=-1,
        )
    ax.view_init(azim=245, elev=25, roll=0)
    ax.set_box_aspect((12, 10, 6), zoom=1)
    ax.set_xlabel("modulation index $I$", labelpad=20)
    ax.set_ylabel("partial index $k$", labelpad=15)
    ax.set_zlim([base_level, 1.1])
    ax.set_xlim([modulation_index.min(), modulation_index.max()])
    ax.set_ylim(*ylim)
    ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax.set_xticks(np.arange(modulation_index.min(), modulation_index.max(), 5))
    ax.set_zticks([-1, 0, 1])
    ax.set_yticks(np.arange(ylim[0], ylim[1], 5))
    # to avoid the axes labels being cut off
    plt.tight_layout()
    save(IMG_OUTPUT_PATH / "partials_amplitudes_in_3d")


def plot_partials_amplitudes_in_3d_for_specific_modulation_index():
    modulation_index = np.arange(0, 20, 0.1)
    base_level = -1
    ylim = np.asarray([0, 20])

    ax = plt.figure(figsize=(12, 8)).add_subplot(projection="3d")
    for partial_id in reversed(range(*ylim)):
        partial_amplitude = jv(partial_id, modulation_index)
        vertices = [
            (modulation_index[i], partial_id, partial_amplitude[i])
            for i in range(len(modulation_index))
        ]
        vertices += [
            (modulation_index.max(), partial_id, base_level),
            (modulation_index.min(), partial_id, base_level),
        ]
        ax.add_collection3d(
            Poly3DCollection([vertices], color=(0, 0, 0, 0), edgecolor=style.color)
        )
        ax.plot(
            modulation_index,
            partial_id * np.ones_like(modulation_index),
            partial_amplitude,
            color=style.color,
            zorder=-1,
        )
    ax.view_init(azim=245, elev=25, roll=0)
    ax.set_box_aspect((12, 10, 6), zoom=1)
    ax.set_xlabel("modulation index $I$", labelpad=20)
    ax.set_ylabel("partial index $k$", labelpad=15)
    ax.set_zlim([base_level, 1.1])
    ax.set_xlim([modulation_index.min(), modulation_index.max()])
    ax.set_ylim(*ylim)
    ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax.set_xticks(np.arange(modulation_index.min(), modulation_index.max(), 5))
    ax.set_zticks([-1, 0, 1])
    ax.set_yticks(np.arange(ylim[0], ylim[1], 5))
    # to avoid the axes labels being cut off
    plt.tight_layout()

    # Plot particular cross-section of the plot
    modulation_index_value = 10
    cross_section_vertices = [
        (modulation_index_value, partial_id, jv(partial_id, modulation_index_value))
        for partial_id in ylim
    ]
    cross_section_vertices += [
        (modulation_index_value, ylim.max(), base_level),
        (modulation_index_value, ylim.min(), base_level),
    ]
    ax.add_collection3d(
        Poly3DCollection(
            [cross_section_vertices], color=style.complementary_color_1, edgecolor="red"
        )
    )

    save(IMG_OUTPUT_PATH / "partials_amplitudes_in_3d_for_specific_modulation_index")


def main():
    cool_sounds()
    plot_partials_amplitudes_in_3d_for_specific_modulation_index()
    plot_partials_amplitudes_in_3d()
    plot_bessel_functions()
    spectrum_brightness_example()
    eliminating_every_nth_partial_example()
    vibrato_example()
    fm_example_1()
    modulation_index_motivation()
    simple_fm_spectrum()
    timbre_control_example()
    fm_vs_pm_modulation()
    fm_vs_pm_modulation_2()
    harmonic_and_inharmonic_spectra_example()


if __name__ == "__main__":
    main()
