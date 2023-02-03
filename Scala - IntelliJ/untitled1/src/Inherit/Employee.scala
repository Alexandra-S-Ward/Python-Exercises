package Inherit

class Employee(name:String,age: Int, company:String) extends User{
  def this(){
    this(age)
  }
}

object Demo2{
  def main(args: Array[String]){
    var employee : Employee = new Employee("Alexandra", 26, "ITC")
    print(employee.age)
  }
}