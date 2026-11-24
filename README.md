This is the script and function library for the TOROS data reduction pipeline. It was adapted by Oelkers et al. 2026 to reduce TOROS images of the globular cluster 47 Tuc. Most of the scripts should be able to run by setting up appropriate directories in the configuration file and then running main.py.

For the C code to compile properly, you will need the cfitsio library and c math library installed as well as a c compiler, I typically use gcc. You will compile to code as normal i.e:

gcc oisdifference.c -L/usr/local/lib/ -I/usr/local/include/ -lcfitsio -lm

and to run you will simply run the .out file: ./a.out

Please contact me at ryan.oelkers@utrgv.edu if you have any questions about the code or if you find a bug.
