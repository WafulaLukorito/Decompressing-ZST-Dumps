import zstandard

# Set the path to your ZST file
zst_file_path = "C:\\Users\\jones\\Desktop\\RC.zst"

# Create a decompression stream
with open(zst_file_path, "rb") as zst_file:
    dctx = zstandard.ZstdDecompressor()
    stream_reader = dctx.stream_reader(zst_file)

    # Decompress the file in chunks
    chunk_size = 2**27  # 128 MiB
    while True:
        chunk = stream_reader.read(chunk_size)
        if not chunk:
            break

        # Process the decompressed chunk
        process_chunk(chunk)


def process_chunk(chunk):
    # Do something with the decompressed chunk
    pass
