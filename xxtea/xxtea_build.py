from cffi import FFI
import sys
from os.path import join, dirname

__PATH = dirname(__file__)
__SOURCES = [join(__PATH, 'xxtea.c')]

ffi = FFI()
ffi.set_source('xxtea._xxtea', source='#include <xxtea.h>', sources=__SOURCES, include_dirs=[__PATH])
ffi.cdef('''
    void * xxtea_encrypt(const void * data, size_t len, const void * key, size_t * out_len);
    void * xxtea_decrypt(const void * data, size_t len, const void * key, size_t * out_len);
    void free(void * ptr);
''')
# lib = ffi.verify('#include <xxtea.h>', sources = __SOURCES, include_dirs=[__PATH])

if __name__ == "__main__":
    ffi.compile()