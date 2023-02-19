import re
import time

# set the paths for the input and output files
input_file_path = "C:\\Users\\jones\\Desktop\\RC.txt"
output_file_path = "output345.txt"

# Start the timer
start_time = time.time()

match_count = 0

# compile a regular expression to match Amazon links
amazon_link_regex = re.compile(
    r"https?://(?:www\.)?(?:amzn|amazon)\.[a-z]{2,3}(?:\.[a-z]{2})?/[^ \t]*")

# open the input and output files
with open(input_file_path, "r") as input_file, open(output_file_path, "w") as output_file:
    # iterate over each line in the input file
    for line in input_file:
        # search for Amazon links in the line
        matches = amazon_link_regex.findall(line)
        for match in matches:
            match_count += 1
            print(match_count, match)
            # write the entire line to the output file for each link
            output_file.write(line)


# stop the timer and calculate the elapsed time
elapsed_time = time.time() - start_time
elapsed_hours = elapsed_time // 3600
elapsed_minutes = (elapsed_time % 3600) // 60
elapsed_seconds = elapsed_time % 60


# print out the elapsed time

print("Elapsed time: {:.0f} hours {:.0f} minutes {:.2f} seconds".format(
    elapsed_hours, elapsed_minutes, elapsed_seconds))

print("Elapsed time: {:.2f} seconds".format(elapsed_time))
