## Standalone sentement analysis using Map Reduce. 

/TODO Create a Makefile

Config based on [Apache's instructions](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/SingleCluster.html).

Tested on an Ubuntu VM on VirtualBox on a Macbook Pro. VM created 
based on instructions in the [handbook](http://cyberaide.org/papers/vonLaszewski-bigdata.pdf).

If you already have a VM setup with hadoop, use with the following commands to run 
the mapreduce job on a single node in pseudo mode. First, in the same directory 
where the scripts in this directory are, download the data:
```
mkdir data
curl -s http://www.cs.cornell.edu/people/pabo/movie-review-data/review_polarity.tar.gz | tar -xz -C data
```
Format the hdfs namenode:
```
hdfs namenode -format
```
Start the Hadoop daemons and run (config setting follow in the install instructions, 
path relative to the hadoop directory. May need to chmod +x first or prefix with `bash`):
```
sbin/start-dfs.sh
./runall.sh
```

### VM Setup

Install Curl and Java:
```
sudo apt-get install curl
sudo apt install openjdk-8-jre-headless
```

Python 3.6.2 and six (using pynev):
```
git clone git://github.com/yyuu/pyenv.git .pyenv
```
Add the following to .bashrc:
```
export PYENV_ROOT=$HOME/.pyenv
export PATH=$PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH
```

Then run the following:
```
source .bashrc
pyenv install 3.6.2
pyenv global 3.6.2
python -m ensurepip
pip install --upgrade pip
pip install six
```

Install Hadoop 2.9.0:
```
cd /usr/local
sudo -i
curl -s http://mirrors.ocf.berkeley.edu/apache/hadoop/common/hadoop-2.9.0/hadoop-2.9.0.tar.gz | tar xvz
cp hadoop-2.9.0 hadoop
chown -R hduser:hadoop hadoop
```
For pseudo-distributed operation, modify the following files:

/usr/local/hadoop/etc/hadoop/core-site.xml:
```
<configuration>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://localhost:9000</value>
    </property>
</configuration>
```

/usr/local/hadoop/etc/hadoop/hdfs-site.xml:
```
<configuration>
    <property>
        <name>dfs.replication</name>
        <value>1</value>
    </property>
</configuration>
```





