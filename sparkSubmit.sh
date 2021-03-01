spark2-submit wordcount.py --master yarn \
                --driver-memory 25G \
                --deploy-mode cluster \
                --conf spark.dynamicAllocation.maxExecutors=20 \
                --conf spark.executor.memory=8G \
                --conf spark.executor.cores=5 \
                --conf spark.rdd.compress=true \
                --conf spark.shuffle.spill=true \
                --conf spark.shuffle.spill.compress=true \
                --conf spark.io.compression.codec=snappy \
                --conf spark.driver.maxResultSize=128G \
                --conf spark.core.connection.ack.wait.timeout=1000 \
                --conf spark.network.timeout=800 \
                --conf spark.rpc.message.maxSize=50 \
                --conf spark.debug.maxToStringFields=100 \
                --conf spark.sql.files.maxPartitionBytes=282627547 \
                --conf parquet.block.size=282627547 \
                --conf parquet.compression=SNAPPY \
#--jars spark-avro_2.11-2.4.3.jar \
#               --py-files ~userName/wordcount.py \


