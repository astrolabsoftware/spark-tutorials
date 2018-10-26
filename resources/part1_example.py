from pyspark.sql import SparkSession

# (1) Initialise the Spark Session
spark = SparkSession\
    .builder\
    .getOrCreate()

# Uncomment to decrease verbosity
# logger = spark.sparkContext._jvm.org.apache.log4j
# logger.LogManager.getLogger("org").setLevel(logger.Level.WARN)

# (2) Generate fake data on the driver
mylist = [
    ["Julien", 67],
    ["Ιουλιανός", 32],
    ["Юлиан", 89],
    ["尤利安", 40]
]

# (3) Distribute it over the network
rdd = spark.sparkContext.parallelize(mylist)

# (4) Return the mean of ages:
meanage = rdd.map(lambda x: x[1]).mean()
print("Mean age is {}".format(meanage))

# (5) Return person whose age is above 60
belowthreshold = rdd\
    .filter(lambda x: x[1] < 60)\
    .map(lambda x: x[0])\
    .collect()
print("{} are below 60".format(belowthreshold))

# (6) Go from RDD to DataFrame
df = rdd.toDF(["Name", "Age"])
df.show()
df.printSchema()
