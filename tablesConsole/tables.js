//datos primitivos en un array
 console.table(["apples", "oranges", "bananas"]);

function Person(firstName, lastName) {
    this.firstName = firstName;
    this.lastName = lastName;
  }
  
  var me = new Person("John", "Smith");
 //objetos
  console.table(me);
//array de arrays
var people = [["John", "Smith",["axel","toni"]], ["Jane", "Doe"], ["Emily", "Jones"]]
console.table(people);

//array de objetos
var john = new Person("John", "Smith");
var jane = new Person("Jane", "Doe");
var emily = new Person("Emily", "Jones");

console.table([john, jane, emily]);

//objeto con propiedades de un objeto
var family = {};

family.mother = new Person("Jane", "Smith");
family.father = new Person("John", "Smith");
family.daughter = new Person("Emily", "Smith");

console.table(family);

//array de objetos mostrando solo el parametro firstname
var john = new Person("John", "Smith");
var jane = new Person("Jane", "Doe");
var emily = new Person("Emily", "Jones");

console.table([john, jane, emily], ["firstName"]);