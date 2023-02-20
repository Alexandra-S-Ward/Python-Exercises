import pyspark
from pyspark.sql import SparkSession
import random


##################################################
#                                                #
#              RDD Functions!                    #
#                                                #
##################################################

spark = SparkSession.builder.appName("SparkByExamplesTest").getOrCreate()
sc = spark.sparkContext 
sc.setLogLevel("ERROR")
rand_arr = [i+1 * random.randint(13,300) for i in range(30)]

rdd = sc.parallelize(rand_arr)

print(f"# Partitions: {rdd.getNumPartitions()}.") # Number of partitions.
print(f"First Element: {rdd.first()}.") # First Element

# Empty RDD?
empty_rdd = sc.emptyRDD()
empty_rdd2 = _rdd = sc.parallelize([])

text_file_rdd = sc.textFile("./data/ceo_r3000.csv")
split_rdd = text_file_rdd.map(lambda line: (line.split(",")[0],line.split(",")[1]))
print(f"# Partitions: {text_file_rdd.getNumPartitions()}.") # Number of partitions.
print(f"First Element: {text_file_rdd.first()}.") # First Element
print(f"# Partitions: {split_rdd.getNumPartitions()}.") # Number of partitions.
print(f"First Element: {split_rdd.first()}.") # First Element

# Repartition is an expensive operation on IO. 
partitioned_text_rdd = text_file_rdd.repartition(4)
print(f"# Partitions: {partitioned_text_rdd.getNumPartitions()}.") # Number of partitions.


##################################################
#                                                #
#              Transform Functions!              #
#                                                #
##################################################

# flatMap, map, reduceByKey, sortByKey, filter

lorem_ipsum_rdd = sc.textFile("./data/lorem_ipsum.txt")
li_rdd2 = lorem_ipsum_rdd.flatMap(lambda x: x.split(" ")) # Get words
li_rdd3 = li_rdd2.map(lambda x: (x,1))
li_rdd4 = li_rdd3.reduceByKey(lambda x,y : x+y)
print()
print()
li_filter_rdd = li_rdd4.filter(lambda x: 'a' in x[1])


##################################################
#                                                #
#              Action    Functions!              #
#                                                #
##################################################

# Count
print(f"Count: {li_filter_rdd.count()}")

#First
first_record = li_filter_rdd.first()
print(f"First Record: {str(first_record[0]},{str(first_record[1]}")
#Max and Min
max_record = li_filter_rdd.max()
min_record = li_filter_rdd.min()
print(f"max: {str(max_record)} - min: {str(min_record)}")

total_words = li_rdd4.reduce(lambda x,y: (x[0]+y[0],x[1]))
print(str(total_words))

##################################################
#                                                #
#              Actions!                          #
#                                                #
##################################################

# RDD Actions (non pyspark. Pyspark is less efficiently laid out)
# aggregate() -> Aggregates elements of each partition then returns the results
# treeAggregate() -> Similar to aggregate but uses a multi-level tree pattern*
# fold() -> Aggeegates elements of each partition and returns results -> Difference between aggregate?
# Reduce() -> Reduces elements using a binary operator
# treeReduce() -> Reduces elements in a multi-level tree pattern. Similar to reduce()
# collect() -> Return the dataset as an array
# count, countapprox, countApproxDistinct -> Counts element, approximate count depending on timeout execution time and distinct elements in dataset
# countByValue, countByValueApprox -> Returns a map of k,v. k = value, v = # of occurences
# first() -> return the first element.
# top(n) -> return the top n elements
# max, min -> returns the minimum and maximum
# take -> returns the first num elements of a dataset.
# takeOrdered -> return first num nums of ordered dataset
# takeSample -> Returns a subset of the dataset. DO NOT USE THIS for bigger datasets.

