import zstandard
import re
import time


def process_chunk(chunk):
    # Define the regular expression for matching Amazon links
    amazon_regex = re.compile(
        r"https?://(?:www\.)?(?:amzn|amazon)\.[a-z]{2,3}(?:\.[a-z]{2})?/[^ \t]*")

    # Open the output file for appending
    with open("amazon_links.txt", "a", encoding="utf-8") as output_file:
        # Decode the chunk from bytes to string
        chunk_str = chunk.decode('utf-8', errors='ignore')
        # Split the chunk into lines
        lines = chunk_str.splitlines()

        # Iterate over the lines and search for Amazon links
        for line in lines:
            output_file.write(line + "\n")
            # try:
            #     # Find the index of the first "body" match
            #     body_start = line.lower().index("body")
            # except ValueError:
            #     continue

            # # Get the substring that comes after the first "body" match
            # body_substring = line[body_start + 4:]

            # if re.search(amazon_regex, body_substring):
            #     # Write the line to the output file
            #     output_file.write(line + "\n")


# Set the path to your ZST file
zst_file_path = "C:\\Users\\jones\\Desktop\\RC_2022-12.zst"

# Start the timer
start_time = time.time()

# Create a decompression stream

with open(zst_file_path, "rb") as zst_file:
    dctx = zstandard.ZstdDecompressor(max_window_size=2147483648)
    stream_reader = dctx.stream_reader(zst_file)

    # Decompress the file in chunks
    chunk_size = 1024 * 1024  # 1 MB
    total_bad_lines = 0
    while True:
        try:
            chunk = stream_reader.read(chunk_size)
        except zstandard.ZstdError as e:
            # Write the error message to the log file and continue to the next chunk
            with open("bad_lines.log", "a") as log_file:
                log_file.write(f"Error reading chunk: {e}\n")
            continue

        if not chunk:
            print("End of file")
            break

        # Process the decompressed chunk and update the bad lines counter
        process_chunk(chunk)

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
