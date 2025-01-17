import zstandard
from tqdm import tqdm

def decompress_zstd(input_file, output_file):
    with open(input_file, 'rb') as compressed_file:
        decompressor = zstandard.ZstdDecompressor()
        with decompressor.stream_reader(compressed_file) as reader:
            with open(output_file, 'wb') as decompressed_file:
                decompressed_file.write(reader.read())
def main():
    input_file = '/Users/daichij.watanabe/Desktop/GuessTheEval/LichessDataDumps/lichess_db_standard_rated_2014-07.pgn.zst'
    output_file = '/Users/daichij.watanabe/Desktop/GuessTheEval/LichessDataDumps/lichess_rated_2014-07.pgn'

    decompress_zstd(input_file, output_file)
    print("Decompression completed.")

if __name__ == "__main__":
    main()