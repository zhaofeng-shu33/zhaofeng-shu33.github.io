# Using SSE and AVX to accelerate the program
2020/04/10

Today I compare the program speeding for three cases: normal code, with SSE and with AVX.

## Normal code
```C
// speed_test.c
const int NUM = 1000000;
static float X[NUM], Y[NUM], Z[NUM];
void dig_hole() {
    for(int j = 0; j < 1000; j++) {
        for(int i = 0; i < NUM; i++) {
            Z[i] = X[i] + Y[i];
        }
    }
}
int main() {
    for(int i = 0; i < NUM; i++) {
        X[i] = i * 1.2;
        Y[i] = i * 1.8;
    }
    dig_hole();
}
```
Compiling with `g++ speed_test.c -o speed_test`(g++ version 4.8.5) and run with Intel Xeon Processor E5-2620 v4:
```
time ./speed_test.c
```
## SSE code
```C
// speed_test_simd.c
#include <immintrin.h>
const int NUM = 1000000;
static float X[NUM], Y[NUM], Z[NUM];
void dig_hole() {
    __m128 a,b,c;
    for(int j = 0; j < 1000; j++) {
        for(int i = 0; i < NUM; i += 4) {
            a = _mm_load_ps(&X[i]);
            b = _mm_load_ps(&Y[i]);
            c = _mm_add_ps(a, b);
            _mm_store_ps(&Z[i], c);
        }
    }
}
int main() {
    for(int i = 0; i < NUM; i++) {
        X[i] = i * 1.2;
        Y[i] = i * 1.8;
    }
    dig_hole();
}
```
## AVX code
```C
// speed_test_avx.c
#include <immintrin.h>
const int NUM = 1000000;
static float X[NUM], Y[NUM], Z[NUM];
void dig_hole() {
    __m256 a,b,c;
    for(int j = 0; j < 1000; j++) {
        for(int i = 0; i < NUM; i += 8) {
            a = _mm256_load_ps(&X[i]);
            b = _mm256_load_ps(&Y[i]);
            c = _mm256_add_ps(a, b);
            _mm256_store_ps(&Z[i], c);
        }
    }
}
int main() {
    for(int i = 0; i < NUM; i++) {
        X[i] = i * 1.2;
        Y[i] = i * 1.8;
    }
    dig_hole();
}
```
Comping with `g++ --mavx2 speed_test_avx.c -o speed_test_avx`.

## Result
### Debug mode:
| case   | real     | user     | sys      |
|--------|----------|----------|----------|
| normal | 0m3.907s | 0m3.890s | 0m0.015s |
| sse    | 0m2.083s | 0m2.072s | 0m0.011s |
| avx    | 0m1.397s | 0m1.384s | 0m0.012s |
### Release mode (`-O2`):
| case   | real     | user     | sys      |
|--------|----------|----------|----------|
| normal | 0m0.887s | 0m0.875s | 0m0.011s |
| sse    | 0m0.590s | 0m0.578s | 0m0.012s |
| avx    | 0m0.594s | 0m0.578s | 0m0.016s |

## Analysis
Under Debug mode, codes are translated literally. SSE can speed up the program since it processes 
4 float numbers at each inner loop. AVX can process 8 float numbers (32Bit * 8 = 256, 1 Float is 32Bit=4Byte long).

Under Release mode, the speed is not so much since the compiler has many good optimizations for normal operations as well. Especially, SSE and AVX are of almost the same performance.	
