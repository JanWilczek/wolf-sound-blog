import numpy as np
import scipy.signal as sig
import soundfile as sf


def apply_fade(signal):
    """Apply a fade-in and a fade-out to the 1-dimensional signal"""
    # Use a half-cosine window
    window = sig.hann(8192)
    # Use just the half of it
    fade_length = window.shape[0] // 2
    # Fade-in
    signal[:fade_length] *= window[:fade_length]
    # Fade-out
    signal[-fade_length:] *= window[fade_length:]
    # Return the modified signal
    return signal

    """"""

def second_order_allpass_filter(break_frequency, BW, fs):
    """
    Returns b, a: numerator and denominator coefficients
    of the second-order allpass filter respectively

    Refer to scipy.signal.lfilter for the explanation
    of b and a arrays.

    The coefficients come from the transfer function of
    the allpass (Equation 2 in the article).

    Parameters
    ----------
    break_frequency : number
        break frequency of the allpass in Hz
    BW : number
        bandwidth of the allpass in Hz
    fs : number
        sampling rate in hz

    Returns
    -------
    b, a : array_like
        numerator and denominator coefficients of
        the second-order allpass filter respectively
    """
    tan = np.tan(np.pi * BW / fs)
    c = (tan - 1) / (tan + 1)
    d = - np.cos(2 * np.pi * break_frequency / fs)
    
    b = [-c, d * (1 - c), 1]
    a = [1, d * (1 - c), -c]
    
    return b, a


def bandstop_bandpass_filter(input_signal, Q, center_frequency, fs, bandpass=False):
    """Filter the given input signal

    Parameters
    ----------
    input_signal : array_like
        1-dimensional audio signal
    Q : float
        the Q-factor of the filter
    center_frequency : array_like
        the center frequency of the filter in Hz
        for each sample of the input
    fs : number
        sampling rate in Hz
    bandpass : bool, optional
        perform bandpass filtering if True, 
        bandstop filtering otherwise, by default False

    Returns
    -------
    array_like
        filtered input_signal according to the parameters
    """
    # For storing the allpass output
    allpass_filtered = np.zeros_like(input_signal)
    
    # Initialize filter's buffers
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    
    # Process the input signal with the allpass
    for i in range(input_signal.shape[0]):
        # Calculate the bandwidth from Q and center frequency
        BW = center_frequency[i] / Q
        
        # Get the allpass coefficients
        b, a = second_order_allpass_filter(center_frequency[i], BW, fs)
        
        x = input_signal[i]
        
        # Actual allpass filtering:
        # difference equation of the second-order allpass
        y = b[0] * x + b[1] * x1 +  b[2] * x2 - a[1] * y1 - a[2] * y2
        
        # Update the filter's buffers
        y2 = y1
        y1 = y
        x2 = x1
        x1 = x
        
        # Assign the resulting sample to the output array
        allpass_filtered[i] = y
    
    # Should we bandstop- or bandpass-filter?
    sign = -1 if bandpass else 1
    
    # Final summation and scaling (to avoid clipping)
    output = 0.5 * (input_signal + sign * allpass_filtered)

    return output


def main():
    """
    Sample application of bandpass and bandstop
    filters: filter sweep.
    """
    # Parameters
    fs = 44100
    length_seconds = 6
    length_samples = fs * length_seconds
    Q = 3

    # We have a separate center frequency for each sample
    center_frequency = np.geomspace(100, 16000, length_samples)

    # The input signal
    noise = np.random.default_rng().uniform(-1, 1, (length_samples,))
    
    # Actual filtering
    bandstop_filtered_noise = bandstop_bandpass_filter(noise, Q, center_frequency, fs)
    bandpass_filtered_noise = bandstop_bandpass_filter(noise, Q, center_frequency, fs, 
                                                                        bandpass=True)
    
    # Make the audio files not too loud
    amplitude = 0.5
    bandstop_filtered_noise *= amplitude
    bandpass_filtered_noise *= amplitude
    
    # Apply the fade-in and the fade-out to avoid clicks
    bandstop_filtered_noise = apply_fade(bandstop_filtered_noise)
    bandpass_filtered_noise = apply_fade(bandpass_filtered_noise)
    
    # Write the output audio file
    sf.write('bandstop_filtered_noise.flac', bandstop_filtered_noise, fs)
    sf.write('bandpass_filtered_noise.flac', bandpass_filtered_noise, fs)


if __name__=='__main__':
    main()
