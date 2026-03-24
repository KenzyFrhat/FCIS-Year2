const canvas = document.getElementById("emojiCanvas");
const ctx = canvas.getContext("2d");
// face
ctx.beginPath();
ctx.arc(150, 150, 100, 0, Math.PI * 2);
ctx.fillStyle = "red";
ctx.fill();
ctx.stroke();


// eyes
ctx.beginPath();
ctx.arc(110, 120, 10, 0, Math.PI * 2);
ctx.fillStyle = "black";
ctx.fill();

ctx.beginPath();
ctx.arc(190, 120, 10, 0, Math.PI * 2);
ctx.fillStyle = "black";
ctx.fill();

// mouth
ctx.beginPath();
ctx.arc(150, 210, 50, 0, Math.PI, true); // smile 
ctx.stroke();

// eyebrows
ctx.beginPath();
ctx.moveTo(90, 100);
ctx.lineTo(130, 110);
ctx.stroke();

ctx.beginPath();
ctx.moveTo(170, 110);
ctx.lineTo(210, 100);
ctx.stroke();

