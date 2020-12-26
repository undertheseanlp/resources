$("#search").click(function(){
  var queryString = $("#searchString").val()
  search(queryString)
})

async function searchAPI(queryString){
  const response = await fetch("/search", {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({"query": queryString})
  });
  return response.json()

}

class UI {
    static init(n=10){

    }

    static displaySentence(domId, content){
        $("#input-train-s1384").html($("#input-train-s321").text())
        $("#input-train-s1384").trigger("keyup")
        setTimeout(function(){
            $("#article-input-train-s1384 g.sentnum text").text("abc")
        }, 10)

    }

    static createSentence(domId, content){
        var dom = `
<article class="entry-content" class="article" id="article-input-${domId}">
<div id="vis-${domId}" tabs="yes" style="display:none"></div>
<textarea id="input-${domId}" rows="10" cols="80"
style="margin-top:0; display:none"></textarea>
<!-- no need to show the intermediate data representation -->
<textarea id="parsed-${domId}" style="display:none; margin: 0"></textarea>
<!--<p>Log and validator output:</p>-->
<!--<textarea id="log-${domId}" rows="10" cols="80" style="margin-top:0"
disabled="disabled"></textarea>-->
<!-- this div just initializes the pre-built visualization above. -->
<div class="conllu-parse" tabs="yes"
 data-visid="vis-${domId}" data-inputid="input-${domId}" data-parsedid="parsed-${domId}"
 data-logid="log-${domId}">
${content}
</div>
</article>
`
        $(".articles").append(dom);
    }

    static removeSentences(){
        $(".articles").html("")
    }
}
class Sentence {
  constructor(domId, sentId, content) {
    this.domId = "#" + domId;
    this.articleDom = "#article-" + domId;
    this.sentId = sentId
    this.sentIdDom = this.articleDom + " g.sentnum text"
    this.content = content
  }

  hide(){
    $(this.articleDom).hide()
  }

  updateSentIdDom(){
    $(this.sentIdDom).html(this.sentId)
  }

  show(){
    var content = this.content.replace("sent_id =", "sentence-label")
    console.log('this.dom', this.domId);
    $(this.domId).html(content)
    $(this.domId).trigger("keyup")
    setTimeout(this.updateSentIdDom.bind(this), 100)
  }
}

function search(queryString){
  console.log("search")
  UI.removeSentences()
  searchAPI(queryString).then(function(data){
    console.log('data:', data)
    for(var sent of data["sents"]){
        console.log(sent)
        domId = "input-" + sent["id"]
        console.log("domId", domId)
        content = sent["content"] + "\n"
        content = this.content.replace("sent_id =", "sentence-label")
        UI.createSentence(sent["id"], content)
        sentence = new Sentence(domId, sent["id"], content)
        sentence.show()
    }
  })
}


UI.init()

search("CCONJ")

setTimeout(function(){
    UI.displaySentence("hihi", "haha")
}, 2000)