NodeIndexes = {}
class Node {
  constructor(role, variable, text) {
    this.variable = variable;
    this.text = text;
    this.role = role;
    this.nodes = {};
    NodeIndexes[variable] = this;
  }

  addNode(node){
    this.nodes[node.role] = node
  }

  html(index){
    var content = "";
    var roleText = "";
    if(this.role == 'top'){
      roleText = '';
    } else {
      roleText = this.role + ' ';
    }
    content +=  `&nbsp`.repeat(index) + `${roleText}(${this.variable} / <a style="background-color:red" href="#">${this.text}</a>)`;
    for(var role in this.nodes){
      var node = this.nodes[role];
      content += `<br/>` + node.html(index + 4)
    }
    return content;
  }
}

var topNode = new Node("top", "t", "tăng tốc");
topNode.addNode(new Node(":ARG0", "t0", "tuyến metro số 1"));

function writeAMR(node){
  console.log(node);
  var html = node.html(0);
  $("#amr2").html(html)
}

writeAMR(topNode);

top["node"] =
$('#command').keypress(function (e) {
  if (e.which == 13) {
    var command = $("#command").val();
    var { groups: { variable, text } } = /(?<variable>.*) :ARG0 (?<text>.*)/.exec(command)
    console.log(variable);
    console.log(text);
  }
});

function openNewWidow(url, top, left, width, height) {
    var features = "location=1, status=1, scrollbars=1, width=" + width + ", height=" + height + ", top=" + top + ", left=" + left;
    window.open(url, "kad", features);
    window.close();
}

$('#help').click(function(){
  openNewWidow('help.html', 0, 0, 500, 600)
})

$('#guide').click(function(){
  openNewWidow('guide.html', 0, 0, 500, 600)
})