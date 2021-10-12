use std::fs::File;
use std::io::BufReader;
use rodio::{Decoder, OutputStream, source::Source};

fn main() {
    let (_stream, stream_handle) = OutputStream::try_default().unwrap();

    let file = BufReader::new(File::open("gaussians.wav").unwrap());

    let source = Decoder::new(file).unwrap();

    stream_handle.play_raw(source.convert_samples());

    std::thread::sleep(std::time::Duration::from_secs(5));
}
