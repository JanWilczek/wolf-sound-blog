use core::time::Duration;
use rodio::{OutputStream, source::Source};


struct WavetableOscillator {
    channels: u16,
    sample_rate: u32,
    frequency: f32,
    wave_table: Vec<f32>,
    index: f32,
    index_increment: f32,
}

impl WavetableOscillator {
    fn set_frequency(&mut self, frequency: f32) {
        self.frequency = frequency;
        self.index_increment = self.frequency * self.wave_table.len() as f32 / self.sample_rate as f32;
    }

    fn get_sample(&mut self) -> f32 {
        let sample = self.lerp();
        self.index += self.index_increment;
        self.index %= self.wave_table.len() as f32;
        return sample;
    }

    fn lerp(&self) -> f32 {
        let truncated_index = self.index as usize;
        let next_index = (truncated_index + 1) % self.wave_table.len();
        
        let next_index_weight = self.index - truncated_index as f32;
        let truncated_index_weight = 1.0 - next_index_weight;

        return truncated_index_weight * self.wave_table[truncated_index] + next_index_weight * self.wave_table[next_index];
    }
} 

impl Source for WavetableOscillator {
    fn channels(&self) -> u16 {
        return self.channels;
    }

    fn sample_rate(&self) -> u32 {
        return self.sample_rate;
    }   

    fn current_frame_len(&self) -> Option<usize> {
        return None;
    }

    fn total_duration(&self) -> Option<Duration> {
        return None;
    }
}

impl Iterator for WavetableOscillator {
    type Item = f32;
    
    fn next(&mut self) -> Option<Self::Item> {
        return Some(self.get_sample());
    }
}

fn main() {
    let (_stream, stream_handle) = OutputStream::try_default().unwrap();

    let wave_table_size = 64;
    let mut wave_table: Vec<f32> = Vec::with_capacity(wave_table_size);

    for n in (1..wave_table_size).rev() {
        wave_table.push((2.0 * std::f32::consts::PI * n as f32 / wave_table_size as f32).sin());
    }

    let mut osc = WavetableOscillator {
        channels: 1,
        sample_rate: 44100,
        frequency: 0.0,
        wave_table: wave_table,
        index: 0.0,
        index_increment: 0.0,
    };

    osc.set_frequency(440.0);

    let _result = stream_handle.play_raw(osc.convert_samples());

    std::thread::sleep(std::time::Duration::from_secs(5));
}
