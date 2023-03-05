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

        # Initialize the counter for bad lines
        bad_lines = 0

        # Iterate over the lines and search for Amazon links
        for line in lines:
            body_start = line.lower().index("body")

            # Get the substring that comes after the first "body" match
            body_substring = line[body_start + 4:]

            if re.search(amazon_regex, body_substring):
                # Write the line to the output file
                output_file.write(line + "\n")

        return bad_lines


# Set the path to your ZST file
zst_file_path = "C:\\Users\\jones\\Desktop\\RC.zst"

# Start the timer
start_time = time.time()

# Create a decompression stream
with open(zst_file_path, "rb") as zst_file:
    dctx = zstandard.ZstdDecompressor(max_window_size=2147483648)  # 2 GB
    stream_reader = dctx.stream_reader(zst_file)

    # Decompress the file in chunks
    chunk_size = 1024 * 1024  # 1 MB
    total_bad_lines = 0
    chunk = stream_reader.read(chunk_size)

    if not chunk:
        print("End of file")

        # Process the decompressed chunk and update the bad lines counter
        total_bad_lines += process_chunk(chunk)

    # Print the total number of bad lines
    print(f"Total bad lines: {total_bad_lines}")

# Stop the timer and calculate the elapsed time
elapsed_time = time.time() - start_time
elapsed_hours = elapsed_time // 3600
elapsed_minutes = (elapsed_time % 3600) // 60
elapsed_seconds = elapsed_time % 60

# Print out the elapsed time
print("Elapsed time: {:.0f} hours {:.0f} minutes {:.2f} seconds".format(
    elapsed_hours, elapsed_minutes, elapsed_seconds))
