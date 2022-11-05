var i = 0;
function move() {
  if (i == 0) {
    i = 1;
    var elem = document.getElementById("myBar");
    var width = 1;
    var id = setInterval(frame, 10);
    function frame() {
      if (width >= 100) {
        clearInterval(id);
        i = 0;
      } else {
        width++;
        elem.style.width = width + "%";
      }
    }
  }
}

function showDiv() {
  var x = document.getElementById("myProgress")
  if (x.style.display === "none") {
    x.style.display = "block";
  }else {
    x.style.display = "none";
  }
}