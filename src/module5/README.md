# Python Files and Exceptions

### Most common Python file modes you can use with open()

"r" → Read (default). Opens file for reading. Error if file does not exist.


"w" → Write. Creates a new file or overwrites an existing one.


"a" → Append. Opens file for writing, but data is added at the end (file not erased).


"x" → Create. Creates a new file; error if file already exists.


Variations with b and +:
**"rb" / "wb" / "ab" → Read/Write/Append in binary mode (e.g., images, PDFs).


"r+" → Read and write (file must exist).


"w+" → Write and read (overwrites file or creates new).


"a+" → Append and read (creates file if it doesn’t exist).


**"rb+" / "wb+" / "ab+" → Binary versions of the above.