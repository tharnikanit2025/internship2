let word = "javascript";
let count = 0;
for (let i = 0; i < word.length; i++) {
    let ch = word[i].toLowerCase();
    if (
        ch === "a" ||
        ch === "e" ||
        ch === "i" ||
        ch === "o" ||
        ch === "u"
    ) {
        count++;
    }
}
console.log("Number of vowels:", count);