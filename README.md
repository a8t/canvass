# Canvass coding challenge

Both of these solutions are written in Python 2. I worked on them on and off for about four hours, including ample break time. Specific instructions and discussions follow. The code is also annotated, since both programs are quite brief.

### Challenge 1: Even digits

To run:

    python even_digits.py

This challenge was simpler. I created an empty list, looped through relevant numbers to check if they fit the criteria, and added them to the list (as strings) if so. At the end I joined the list on a comma as requested.

The criteria requested was that every digit in the number should be even. At first I wondered if some bit fiddling would be a concise solution, but in the end I decided that readability is much more important than a cute line of code. I checked each digit by dividing by 10 and taking mod 2, which works because the integer number type in Python truncates rather than converting to float.

While the problem asks for numbers from 1000–3000 where each digit is even, I knew that the program wouldn't have to check many of those numbers. I limited the range to ignore the 1XXXs and the 29XXs. I think that's important because even if the algorithm is clever internally, you don't want to catch yourself doing extra work in the bigger picture. The developer has the ability to pre-filter data.

### Challenge 2: Even digits

To run:

    python csv_sort.py [path_to_input_csv]

For example:

    python csv_sort.py ./random_data.csv

or

    python csv_sort.py ./large_data.csv

I've done very similar CSV parsing work before, so I was a familiar (though a bit rusty) with the CSV package in Python. I self-criticize that the solution is hard-coded to these particular CSV files, specifically the column headings. And I also noticed that the range of values for the Device_ID is very limited, which could be a source of optimization that my solution did not consider. That said, I do feel that the code is concisely but clearly structured and commented well enough that I could submit this for code review at work.

On my machine, the 3 million line CSV took 90 seconds to parse and sort. I feel that this is reasonable. However, if the file were large enough to not fit in memory (3 billion lines, by my estimation?) then the algorithm would have to be reconsidered completely. I found some references to 'external sorting algorithms', sorting chunks in memory and merging on disk, but I felt that would be overkill to implement :)
