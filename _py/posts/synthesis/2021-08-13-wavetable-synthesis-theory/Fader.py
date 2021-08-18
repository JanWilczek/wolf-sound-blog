import numpy as np


class Fader:
    """Apply fade in and/or fade out to the given signals.

    Applies a half-cosine window to make the signal smoothly rise to its amplitude.

    Parameters
    ----------
    fade_in_length: int
        length of the fade-in window

    fade_out_length: int
        length of the fade-out window
    """

    def __init__(self, fade_in_length=1000, fade_out_length=1000):
        self.fade_in_length = fade_in_length
        self.fade_out_length = fade_out_length

    def fade_in(self, signal):
        """Apply fade-in to the first self.fade_in_length samples of the signal.

        Parameters
        ----------
        signal : (M,N) ndarray
            signal to apply the fade-in to along the first axis on each of the N channels

        Returns
        -------
        (M,N) ndarray
            a copy of the signal with the applied fade-in
        """
        fade_in_envelope = (1 - np.cos(np.linspace(0, np.pi, self.fade_in_length))) * 0.5
        if signal.ndim == 2:
            fade_in_envelope = fade_in_envelope[:, np.newaxis]

        output = np.copy(signal)

        output[:self.fade_in_length, ...] = np.multiply(signal[:self.fade_in_length, ...], fade_in_envelope)

        return output

    def fade_out(self, signal):
        """Apply fade-out to the last self.fade_out_length samples of the signal.

        Parameters
        ----------
        signal : (M,N) ndarray
            signal to apply the fade-out to along the first axis on each of the N channels

        Returns
        -------
        (M,N) ndarray
            a copy of the signal with the applied fade-out
        """
        fade_out_envelope = (1 - np.cos(np.linspace(np.pi, 0, self.fade_out_length))) * 0.5
        if signal.ndim == 2:
            fade_out_envelope = fade_out_envelope[:, np.newaxis]

        output = np.copy(signal)

        output[-self.fade_out_length:, ...] = np.multiply(signal[-self.fade_out_length:, ...], fade_out_envelope)

        return output

    def fade_in_out(self, signal):
        """Apply both, fade_in and fade_out."""
        return self.fade_out(self.fade_in(signal))


def fade_in_out(get_signal_array_function):
    """
    A decorator for a get_signal_array() method. 
    Works as fader.fade_in_out(signal.get_signal_array()) with default Fader parameters.
    """
    def wrapper(*args, **kwargs):
        fader = Fader()
        return fader.fade_in_out(get_signal_array_function(*args, **kwargs))
    return wrapper
