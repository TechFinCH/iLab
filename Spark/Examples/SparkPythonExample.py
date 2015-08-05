from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("My App")
sc = SparkContext(conf = conf)

lines = sc.textFile("README.md")
print lines.count()
print lines.first()

pythonLines = lines.filter(lambda line: "Python" in line)
print pythonLines.count()
print pythonLines.first()
