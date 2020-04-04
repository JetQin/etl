# Genereate keypair

openssl genrsa -out jetqin.key 2048
openssl rsa -in ./config/jetqin.key -pubout > ./config/jetqin.pub

openssl req -new -key jetqin.key -out jetqin.csr -subj "/CN=jetqin/O=dev"\n

## Benchmark Test

`ab -c 10 -n 1000 -p bench.txt -T application/x-www-form-urlencoded http://127.0.0.1:5000/api/v1/auth/login`

```
This is ApacheBench, Version 2.3 <$Revision: 1843412 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient)
Completed 100 requests
Completed 200 requests
Completed 300 requests
Completed 400 requests
Completed 500 requests
Completed 600 requests
Completed 700 requests
Completed 800 requests
Completed 900 requests
Completed 1000 requests
Finished 1000 requests


Server Software:        Werkzeug/0.16.0
Server Hostname:        127.0.0.1
Server Port:            5000

Document Path:          /api/v1/auth/login
Document Length:        11 bytes

Concurrency Level:      10
Time taken for tests:   28.046 seconds
Complete requests:      1000
Failed requests:        0
Total transferred:      197000 bytes
Total body sent:        200000
HTML transferred:       11000 bytes
Requests per second:    35.66 [#/sec] (mean)
Time per request:       280.456 [ms] (mean)
Time per request:       28.046 [ms] (mean, across all concurrent requests)
Transfer rate:          6.86 [Kbytes/sec] received
                        6.96 kb/s sent
                        13.82 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.1      0       1
Processing:   246  277  15.0    280     370
Waiting:      245  276  14.8    279     370
Total:        246  278  15.0    280     370

Percentage of the requests served within a certain time (ms)
  50%    280
  66%    286
  75%    289
  80%    290
  90%    295
  95%    298
  98%    305
  99%    309
 100%    370 (longest request)

```
