## Standalone sentement analysis using Map Reduce. 

Usage:
```
make - start and run
make start - formats the file system and initializes the daemons
make run - runs the mapreduce job
make clean
```
Assumes you have done the configuration below.

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
Create `hduser` in `hadoop` group:
```
su - hduser
ssh-keygen -t rsa -P ""
cat /home/hduser/.ssh/id_rsa.pub >> $HOME/.ssh/authorized_keys
ssh localhost
exit
```
The last step is so that localhost is added to /home/hduser/.ssh/known_hosts.

Add the following to .bashrc for hduser
```
# HADOOP SETINGS
# Set Hadoop-related environment variables
export HADOOP_HOME=/usr/local/hadoop

# Set JAVA_HOME (we will also configure JAVA_HOME directly for Hadoop later on)
#export JAVA_HOME=/usr/lib/jvm/java-6-sun
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64

# Some convenient aliases and functions for running Hadoop-related commands
unalias fs &> /dev/null
alias fs="hadoop fs"
unalias hls &> /dev/null
alias hls="fs -ls"

export PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin"
export PATH="$PATH:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/usr/local/hadoop/bin:."
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
cp -R hadoop-2.9.0 hadoop
chown -R hduser:hadoop hadoop
```
For pseudo-distributed operation, modify the following files:

/usr/local/hadoop/etc/hadoop/core-site.xml:
```
<configuration>
    <property>
        <name>hadoop.tmp.dir</name>
        <value>/app/hadoop/tmp</value>
        <description>A base for other temporary directories.</description>
    </property>
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
Change the line in /usr/local/hadoop/etc/hadoop/hadoop_env.sh to:
```
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
```
Make hadoop_env.sh executable:
```
chmod +x /usr/local/hadoop/etc/hadoop/hadoop-env.sh
```





