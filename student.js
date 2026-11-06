let students = [
    { name: "Anu", marks: 80 },
    { name: "Priya", marks: 90 },
    { name: "Sam", marks: 70 }
];
for (let i = 0; i < students.length; i++) {
    console.log(students[i].name);
}
let total = 0;
for (let i = 0; i < students.length; i++) {
    total = total + students[i].marks;
}
let average = total / students.length;
console.log("Average Marks:", average);