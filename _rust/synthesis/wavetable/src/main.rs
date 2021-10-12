use std::fs::File;
use std::io::BufReader;
use rodio::{Decoder, OutputStream, source::Source};


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

fn main() {
    let (_stream, stream_handle) = OutputStream::try_default().unwrap();

    // let file = BufReader::new(File::open("gaussians.wav").unwrap());

    // let source = Decoder::new(file).unwrap();

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


    // stream_handle.play_raw(source.convert_samples());

    // std::thread::sleep(std::time::Duration::from_secs(5));
}
