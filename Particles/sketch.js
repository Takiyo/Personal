let particles = [];
let windSpeed = 0;
let windDirection = 0; // 0 = none, -1 = left, 1 = right.


function setup() {
createCanvas(windowWidth, windowHeight);
background (0, 0, 30);
}

function draw() {

textSize(64);
fill(255, 255, 255);
textAlign(CENTER);
var stuff = "Click to toggle wind direction. Middle click to disable wind.";
text(stuff, 900, 200);

for (let i = 0; i < 20; i++){
  let p = new Particle();
  particles.push(p);
}

  for (let i = particles.length-1; i >= 0; i--){
    particles[i].show();


    //// Wind accelerates to a point, then stays blowing.

      if (windDirection == 1){
        if (windSpeed < 5){
          windSpeed += 0.0001;
          }
      }
      else if (windDirection == -1)
      {
        if (windSpeed > -5){
        windSpeed -= 0.0001;
        }
      }



    particles[i].update(windSpeed);

    if (particles[i].finished()){
      particles.splice(i, 1);
    }
  }
}

function mousePressed(){
  if (mouseButton == LEFT){
    if (windDirection == 0 || windDirection == -1){
      windDirection = 1;
    }
    else{
      windDirection = -1;
    }
  }

  if (mouseButton == CENTER){
    windSpeed = 0;
    windDirection = 0;
  }

  return false;
}

class Particle{
  constructor(){
  this.x = mouseX;
  this.y =  mouseY;
  this.vx = random(-2, 2);
  this.vy = random(-4, 0);
  this.alpha = 255;
  }

  finished(){
    return this.alpha < 0;
  }

  //animation
  update(windSpeed){
    this.vx += windSpeed;
    this.x += this.vx;
    this.y += this.vy;
    this.alpha -=2;
  }

  //circle stuff
  show(){
    var randColor1 = setRand(0, 255);
    var randColor2 = setRand(0, 200);
    var randColor3 = setRand(0, 255);

    noStroke();
    // fill(255, this.alpha);
    fill(randColor1,randColor2,randColor3, this.alpha);
    ellipse(this.x, this.y, 7);
  }
}

function setRand(lower, upper){
  return random(lower, upper);
}
