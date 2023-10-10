from pysparkling import Context, RDD
from preloaded import data

def my_sum_func(x,y):
  return int(x) + int(y)

def main():
  sc = Context()
  rdd = sc.parallelize(data).map(lambda x: tuple(x))
  
  solution = (
    rdd
    .map(lambda x: [x[1], x[3]])
    .reduceByKey(my_sum_func)
    .filter(lambda x: x[1] == 'Belize')
    .collect()
  )
  
  return solution
