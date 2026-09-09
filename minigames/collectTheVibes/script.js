//Move the catcher with the left and right arrow keys to catch the falling objects. 

/* VARIABLES */
let catcher, fallingObject;
let score = 0;
let backgroundImg;
let catcherImg;
let fallingObjectImg = {};
let fallingObjectstate = "banana";

/* PRELOAD LOADS FILES */
function preload(){
  backgroundImg = loadImage("assets/nature_2.png");
  fallingObjectImg.banana = loadImage("assets/Banana.png");
  fallingObjectImg.mango = loadImage("assets/Mango.png");
  catcherImg = loadImage("assets/Basket.png");
}

/* SETUP RUNS ONCE */
function setup() {
  createCanvas(400,400);
//resize images
  backgroundImg.resize(0,400);
  fallingObjectImg.banana.resize(64,0);
  fallingObjectImg.mango.resize(64,0);
  
  //Create catcher 
  catcher = new Sprite(catcherImg, 200,360,110,30,"k");
  catcher.color = color(95,158,160);
  
  //Create falling object
  fallingObject = new Sprite(fallingObjectImg[fallingObjectstate],100,0,54);
  fallingObject.color = color(0,128,128);
  fallingObject.vel.y = 2;
  fallingObject.rotationLock = true;
}

/* DRAW LOOP REPEATS */
function draw() {
  background("#229df2");
  //Draw background image
  image(backgroundImg, 0 , 0);
  
  // Draw directions to screen
  fill(0);
  textSize(12);
  text("Move the \nbasket with the \nleft and right \narrow keys to \ncatch the\n bananas \nand mangoes.", width-100, 20);

//if falling object reaches bottom, move to random position at top and decrease score
  if (fallingObject.y >= height) {
    fallingObject.y = 0;
    fallingObject.x = random(width);
    fallingObject.vel.y = random(2, 5);
    score -= 1;
    
//randomizer variable uses javascript concepts known as objects and keys. fallingObjectImg is an object and mango and banana are the keys,,, its kind of like an array? but its elements (the keys) arent called based on numerical indexes.
    let randomizer = Object.keys(fallingObjectImg);
    fallingObjectstate = random(randomizer);
    fallingObject.img = fallingObjectImg[fallingObjectstate];
  }
  //Move catcher
  if(kb.pressing("left")) {
    catcher.vel.x = -3;
  } else if (kb.pressing("right")) {
    catcher.vel.x = 3;
  } else {
    catcher.vel.x = 0;
  }
  //Stop catcher at edge of screen 
  if (catcher.x < 50) {
    catcher.x = 50;
  } else if (catcher.x > 350) {
    catcher.x = 350;
  }
  //if fallingObject collides with catcher, move back to random position at top and increase score
  if (fallingObject.collides(catcher)) {
    fallingObject.y = 0;
    fallingObject.x = random(width);
    fallingObject.vel.y = random(2, 5);
    fallingObject.direction = "down";
    score += 1;

    let randomizer = Object.keys(fallingObjectImg);
    fallingObjectstate = random(randomizer);
    fallingObject.img = fallingObjectImg[fallingObjectstate];
  }
  textSize (20);
  fill ("white");
  text("Score: "+ score, 10, 30);
  allSprites.debug = mouse.pressing();
  
  if (score < 0) {
    catcher.pos.y = (-200);
    fallingObject.pos.x = (-2000);
    fallingObject.collider = "n";
    clear();
    background("#229df2");
    textSize(30);
    text("You Lose!", width /2 -70, height /2);
    textSize(20);
    text("Press run to play again.", width /2 - 110, height /2 + 25);
  }

}