
import zstandard
import os
import sys
dctx = zstandard.ZstdDecompressor(max_window_size=2147483648)


# input_path = sys.argv[1]
# output_path = sys.argv[2]

input_path = "C:\\Users\\jones\\Desktop\\RC.zst"
output_path = "C:\\Users\\jones\\Desktop\\RC.txt"

with open(input_path, 'rb') as ifh, open(output_path, 'wb') as ofh:
    dctx.copy_stream(ifh, ofh, read_size=8192, write_size=16384)
