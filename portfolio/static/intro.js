var app = document.getElementById('introtxt');

var typewriter = new Typewriter(app, {
  cursor: "_",
  delay: 50,
});

typewriter.typeString('Hello!')
    .pauseFor(500)
    .typeString(' My name is Mason Fisher')
    .pauseFor(500)
    .typeString('<br />I\'m a backend web developer')
    .pauseFor(500)
    .start();
