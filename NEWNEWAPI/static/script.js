function getRandomCars() {
    fetch('/random_car')
    .then(r => r.json())
    .then(data => {
        document.getElementById('random-result').innerText =
            "🚗 " + data["car brand"] + " " + data["model"] + " (" + data["color"] + ") - " + data["price"];
        document.getElementById('random-result').style.display = "block";
    });
}

function getRandomColor() {
    fetch('/random_color')
    .then(r => r.json())
    .then(data => {
        document.getElementById('random-result').innerText =
            "🎨 " + data["name"] + " (" + data["number"] + ")";
        document.getElementById('random-result').style.display = "block";
    });
}

function getTip() {
    fetch('/tip')
    .then(r => r.json())
    .then(data => {
        document.getElementById('random-result').innerText = "💡 " + data["tip"];
        document.getElementById('random-result').style.display = "block";
    });
}

function calculate() {
    let n1 = document.getElementById('num1').value;
    let n2 = document.getElementById('num2').value;
    fetch('/calculate?num1=' + n1 + '&num2=' + n2)
    .then(r => r.json())
    .then(data => {
        document.getElementById('calc-result').innerText =
            "➕ " + data.num1 + " + " + data.num2 + " = " + data.result;
        document.getElementById('calc-result').style.display = "block";
    });
}
function calculate2() {
    let n3 = parseFloat(document.getElementById('num3').value);
    let n4 = parseFloat(document.getElementById('num4').value);

    fetch(`/subtract?num3=${n3}&num4=${n4}`)
    .then(r => r.json())
    .then(data => {
        document.getElementById('calc-result2').innerText =
            "➖ " + data.num3 + " - " + data.num4 + " = " + data.result;
        document.getElementById('calc-result2').style.display = "block";
    });
}
function calculateMultiply() {
    let n5 = document.getElementById('num5').value;
    let n6 = document.getElementById('num6').value;

    fetch(`/multiply?num5=${n5}&num6=${n6}`)
        .then(r => r.json())
        .then(data => {
            document.getElementById('calc-mul').innerText =
                `✖️ ${data.num5} × ${data.num6} = ${data.result}`;
        });
}

function calculateDivide() {
    let n7 = document.getElementById('num7').value;
    let n8 = document.getElementById('num8').value;

    fetch(`/divide?num7=${n7}&num8=${n8}`)
        .then(r => r.json())
        .then(data => {
            if (data.error) {
                document.getElementById('calc-div').innerText = "⚠️ " + data.error;
            } else {
                document.getElementById('calc-div').innerText =
                    `➗ ${data.num7} ÷ ${data.num8} = ${data.result}`;
            }
        });
}
function getGreeting() {
    let name = document.getElementById('name').value;
    let age = document.getElementById('age').value;
    fetch('/greet?name=' + name + '&age=' + age)
    .then(r => r.json())
    .then(data => {
        document.getElementById('greet-result').innerText = data.greeting;
        document.getElementById('greet-result').style.display = "block";
    });
}
