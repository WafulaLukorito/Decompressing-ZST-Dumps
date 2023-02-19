import zstandard
import re
import time


def process_chunk(chunk):
    # Define the regular expression for matching Amazon links
    amazon_regex = re.compile(
        r"https?://(?:www\.)?(?:amzn|amazon)\.[a-z]{2,3}(?:\.[a-z]{2})?/[^ \t]*")

    # Open the output file for appending
    with open("amazon_links.txt", "a") as output_file:
        # Decode the chunk from bytes to string
        chunk_str = chunk.decode()

        # Split the chunk into lines
        lines = chunk_str.splitlines()

        # Iterate over the lines and search for Amazon links
        for line in lines:
            if re.search(amazon_regex, line):
                # Write the line to the output file
                output_file.write(line + "\n")


# Set the path to your ZST file
zst_file_path = "C:\\Users\\jones\\Desktop\\RC.zst"

# Start the timer
start_time = time.time()

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


# stop the timer and calculate the elapsed time
elapsed_time = time.time() - start_time
elapsed_hours = elapsed_time // 3600
elapsed_minutes = (elapsed_time % 3600) // 60
elapsed_seconds = elapsed_time % 60


# print out the elapsed time

print("Elapsed time: {:.0f} hours {:.0f} minutes {:.2f} seconds".format(
    elapsed_hours, elapsed_minutes, elapsed_seconds))
