

function setup() {

  gui = getElement("gui")
  canvas = getElement("canvas")

  // скуф
  c = createCanvas(1040, 300);
  c.parent(canvas)
  
  var dflt = 100;
  background(255 - dflt);
  sl1 = createSlider(0,255,dflt);
  sl1.size('100px');
  sl1.parent(gui)
  

  t1 = createP(dflt);
  t1.parent(gui)
  t1.id('t')


}

function draw() {

	var n1 = 255 - sl1.value()
	t1.html(n1)
	background(n1);
}

