object Main {
  // Currying
  def add(x:Int) = (y:Int) => x+y;
  def addMore (x:Int) (y:Int) (z:Int) = x + y + z;

  def main(args: Array[String]): Unit = {
    val num1 = 30;
    val num2 = 20;
    val num3 = 55;
    val sum = addMore(55)_;
    println(add(num1)(num2))
    println(sum(num3)(num2))

    /*
          Set Functions and tests
     */

    var mySet : Set[Int] = Set(1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 10)
    var mySet2 : Set[Int] = Set(22,33,44,55)
    println(mySet)
    mySet = mySet+13 // Returns a new set because sets are immutable
    println(mySet)
    println(mySet(839490387)) // Check if val in set
    println(mySet.head)
    println(mySet.isEmpty)
    println(mySet.tail)
    println(mySet ++ mySet2) // Union or mySet.++(mySet2)
    println(mySet.intersect(mySet2)) // Intersection (or mySet.&())

    /*
          Map Functions and tests
     */

    val myMap : Map[Int,String] = Map(822 -> "Rupali", 833 -> "Eworitse")
    println(myMap)
    println(myMap.keys)
    println(myMap.values)
    println(myMap(822)) // Get key

    myMap.keys.foreach{ key =>
      println("Key " + key)
      println("Value " + myMap(key))
    }
    println(myMap.contains(822))

    /*
          Tuple Functions and tests
     */
    val myTuple = (1,2,"Hello",false)
    val myTuple2 = new Tuple3(1,2, "Tuple")
    val myTuple3 = new Tuple3(1,5,("Tuple inside of", "A tuple"))
    println(myTuple2._2) // Print third char
    myTuple.productIterator.foreach{
      i => println(i)
    }
    println(myTuple3._3._2) // Printing a tuple into a tuple
    println(1 -> 3 -> 4 -> 5 -> 6) // x -> y = (x,y) -> z = ((x,y),z)

    /*

          Options (Some or None)

     */
    val lst = List(1,2,3)
    println(lst.find(_ > 3000))
    println(myMap.get(3))

    /*
          Map / Filter
     */
    println(lst.map(_ * 2)) // println(lst.map(x => x * 2))
    println(myMap.mapValues(x => x + 3)) // deprecated
    val joinedList = List(List(1,3,5,7),List(2,4,6,8)).flatten

    // Filter
    println(joinedList.filter(x => x % 2 == 0))

    // Reduce
    println(joinedList.reduceLeft(_ + _ ))

    // Fold -> Element as start value
    println(joinedList.foldRight(100)(_+_))

    // Scan
    println(joinedList.scanLeft(100)(_ + _))
  }
}