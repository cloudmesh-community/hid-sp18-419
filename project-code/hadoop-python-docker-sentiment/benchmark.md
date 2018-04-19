# Running time for sentiment analysis hadoop version 2.9.0


| #worker | rounds | mbp     | centos  | ubuntu | Echo(c) | Pi |
|---------|--------|---------|---------|--------|---------|----|
| pseudo  | 1      | 99m25s  | 83m34s  | 43m24s | 59m13s  |    |
|         | 2      | 100m33s | 83m43s  | 42m6s  | 42m51s  |    |
|         | 3      | 97m44s  | 83m47s  | 44m21s | 33m33s  |    |
| 1       | 1      | 102m22s | 83m9s   | 44m30s | 42m41s  |    |
|         | 2      | 106m12s | 83m28s  | 43m53s |         |    |
|         | 3      | 105m8s  | 83m55s  | 43m42s |         |    |
| 2       | 1      | 106m43s | 84m46s  | 41m2s  |         |    |
|         | 2      | 110m20s | 85m4s   | 41m5s  |         |    |
|         | 3      | 109m27s | 84m49s  | 41m37s |         |    |
| 3       | 1      |         | 87m10s  | 41m51s | 22m24s  |    |
|         | 2      |         | 86m48s  | 42m29s |         |    |
|         | 3      |         | 86m47s  | 42m21s |         |    |
| 4       | 1      |         | 87m30s  | 43m39s | 18m52s  |    |
|         | 2      |         | 88m15s  | 43m34s | 17m46s  |    |
|         | 3      |         | 88m2s   | 44m11s | 17m49s  |    |
| 5       | 1      |         | 88m59s  | 48m19s | 18m2s   |    |
|         | 2      |         |         | 47m50s | 18m2s   |    |
|         | 3      |         |         | 45m41s | 18m2s   |    |
| 6       | 1      |         | 93m15s  | 60m19s | 21m25s  |    |
|         | 2      |         |         | 60m33s |         |    |
|         | 3      |         |         | 58m23s |         |    |
| 7       | 1      |         | 95m44s  | 98m29s |         |    |
|         | 2      |         |         |        |         |    |
|         | 3      |         |         |        |         |    |
| 8       | 1      |         | 128m21s |        |         |    |
| max #w  |        | 2       | 6(78)   |        |         |    |


# Information about the machine:


## Min's mbp

* MacBook Pro (Retina, 13-inch, Early 2015) 
* 2.7 GHz Intel Core i5
* 2 Core
* 8G memory
* macOS High Sierra 10.13.3

## Min's centos

* Acer Aspire 4830
* Intel(R) Core(TM) i5-2430M CPU @2.40GHz
* 2 Core
* 16G memory
* centOS 

## Min's Ubuntu VirtualBox

### Host machine info

* Asus Desktop
* Intel(R) Core(TM) i5-4690K CPU @3.50GHz
* 4 Cores
* 16G memory
* windows7

### VirutualBox allocation

* 11G base memory
* 2 base Core




