# mongodb_elasticsearch_jieba

ubuntu 14.04 使用elasticsearch+jieba+ mongodb 搜索
==================================================


1.安装elasticsearch（注意elasticsearch的版本）
--------------------------------------------
 参考链接 ：https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-elasticsearch-on-ubuntu-14-04
 http://www.vpsee.com/2014/05/install-and-play-with-elasticsearch/
 版本选为2.3.4
 '''
Download and install the Public Signing Key:

wget -qO - https://packages.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
Save the repository definition to /etc/apt/sources.list.d/elasticsearch-2.x.list:

echo "deb https://packages.elastic.co/elasticsearch/2.3/debian stable main" | sudo tee -a /etc/apt/sources.list.d/elasticsearch-2.3.list
Warning
Use the echo method described above to add the Elasticsearch repository. Do not use add-apt-repository as it will add a deb-src entry as well, but we do not provide a source package. If you have added the deb-src entry, you will see an error like the following:

Unable to find expected entry 'main/source/Sources' in Release file (Wrong sources.list entry or malformed file)
Just delete the deb-src entry from the /etc/apt/sources.list file and the installation should work as expected.

Run apt-get update and the repository is ready for use. You can install it with:

sudo apt-get update && sudo apt-get install elasticsearch
'''
2.jieba分词插件 https://github.com/huaban/elasticsearch-analysis-jieba 
----------------------------------

3.mongodb开启副本集 本机mongodb已经装好了（port 27017） 目录在\www\data
----------------------------------
1. 停止mongodb service mongodb stop
2. 开启副本集  mongod --port 27017 --dbpath "\www\data" --replSet rs0
3. 重新开一个终端  输入mongo 进入mongodb shell,输入 rs.initiate() 来初始化 副本集

4.利用mongo-connector 来同步Mongo内的数据到 elasticsearch
---------------------------------------------------------
1. pip install mongo-connector
2. mongo-connector -m localhost:27017 -t localhost:9200 -d elastic2_doc_manager 同步~

5.搜索https://github.com/elastic/elasticsearch-py
------------------------------------------------------
https://elasticsearch-py.readthedocs.io/en/master/api.html#elasticsearch.Elasticsearch.search
http://es.xiaoleilu.com/
1. pip install elasticsearch
2. 查询
1. sss
2. xxx







            
