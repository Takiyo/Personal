// Global
var randColor1;
var randColor2;
var randColor3;
var randWeight;


function setup() {
createCanvas(1500,1500);
}

function draw() {
background(0);
noFill();

randColor1 = setRand(0, 255);
randColor2 = setRand(0, 255);
randColor3 = setRand(0, 255);
randWeight = setRandDigit();

stroke(randColor1, randColor2, randColor3);
strokeWeight(randWeight);

//drawCircle(300, 300, 1);
drawQuad(138, 131, 186, 120, 169, 163, 130, 176);
}

function drawCircle(x,y,d){
  ellipse(x, y ,d);
  if (d <= 700){
    drawCircle(x+2, y+2.5, d*1.1);
  }
}

function drawQuad(x1,y1,x2,y2,x3,y3,x4,y4){
  quad(x1 + setRandDigit(), y1 + setRandDigit(), x2 + setRandDigit(),
  y2 + setRandDigit(), x3 + setRandDigit(), y3 + setRandDigit(),
  x4 + setRandDigit(), y4 + setRandDigit());
  if (x1 <= width){
    drawQuad(x1 + setRandDigit()+3, y1 + setRandDigit()+5, x2 + setRandDigit()+5,
    y2 + setRandDigit()+1, x3 + setRandDigit()+1, y3 + setRandDigit()+1,
    x4 + setRandDigit()+1, y4 + setRandDigit()+1);
  }
}

function setRand(lower, upper){
  return random(lower, upper);
}

function setRandDigit(){
  return random(1, 10);
}
