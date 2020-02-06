let img;

async function preload() {
  let promiseData;
  const response = await fetch('a1.bin.npz');
  if (response.ok) {
    // console.log(response.arrayBuffer());
    img = await response.arrayBuffer();
    // console.log(promiseData);
    // promiseData.then(data => {
    //   img = data
    //   console.log(img);
    // });
  }
}

function setup() {
  createCanvas(160, 160);
  background(255);
}

function draw() {
  frameRate(1);
  // let img1 = createImage(160, 160);
  // img1.loadPixels();
  for (let i = 0; i < 160; i++) {
    for (let j = 0; j < 160; j++) {
      console.log(img);
      // img1.set(i, j, color(img.slice(j + i * 160)));
    }
  }
  // img1.updatePixels();
  // image(img1);
}
