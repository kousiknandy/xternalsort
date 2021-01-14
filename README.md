# xternalsort

External memory sorting in Python. The idea is to sort a very large file
that obviously does not fit the memory of a single machine, using an
external memory algorithm.

Algorithm is to take 1 bite at a time which you can chew (sort) and write
the temporary result into a file. So at the end we end up with a number (k)
of smaller files each individually sorted. Afterwards we do a k_way merge,
leading to complete sorting of the original file.

Suppose original file is M and machine's memory holding capacity is m. Then
each round we read m objects from the file, sort and flush. We'll have
roughly k = O(M/m) files. So option 1 is to read O(m/k) from each file,
take advantage that they're order, and do a k-way merge afterwards.

Licensed GNU GPL v3