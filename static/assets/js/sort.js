
let spanElement = document.getElementById('qual');

// Get the text content of the span
let spanContent = spanElement.textContent;


let stringWithoutQuotesAndBrackets = spanContent.replace(/["({}):\[\]]/g, '');
let result2 = stringWithoutQuotesAndBrackets.replace(/value/g, '');

spanElement.textContent = result2;

