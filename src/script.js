function fact() {
    document.getElementById("wrong-button").style.display = "none";
    document.getElementById("true").innerHTML = "Correct";
}

function wrong() {
    document.getElementById("fact-button").style.display = "none";
    document.getElementById("true").innerHTML = "Incorrect"
}